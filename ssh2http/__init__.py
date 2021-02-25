from pwn import *
from sanic import Sanic
from sanic.request import Request
from sanic.response import json

DEFAULT_PORT = 1337
__version__ = "0.1.0"


def usage(name=sys.argv[0]):
    return f"""
    {name} <entry-in-ssh-config> <port: optional, defaults to 1337>
    """


class HelpException(BaseException):
    def __init__(self, msg=usage()):
        self.msg = msg

    def __str__(self):
        return self.msg

    def exit(self, status_code=os.EX_SOFTWARE, out=sys.stderr):
        print(str(self), file=out)
        sys.exit(status_code)


def get_args(default_port=DEFAULT_PORT):
    args = sys.argv

    if len(args) < 2:
        raise HelpException()
    if len(args) == 2:
        args += [default_port]

    return args


def app(io: ssh):
    sanic = Sanic(name=__name__)

    @sanic.route("/", methods=["POST"])
    async def handler(request: Request):
        log.info("called / with %s", request.body)
        payload = request.json
        command = payload.get("command", "")
        timeout = payload.get("timeout", 30)
        try:
            timeout = int(timeout)
        except Exception:
            timeout = 30

        cmd = io.run(command)
        try:
            response = cmd.recvall(timeout=timeout)
        except Exception as err:
            return json(
                {
                    "response": "could not finish the request, ran into a timeout!",
                    "error": str(err),
                },
                status=500,
            )

        return json({"response": response.decode("utf-8")})

    return sanic


def main(prog, name, port=DEFAULT_PORT):
    log.info("Welcome to %s, version %s", prog, __version__)
    io = ssh(host=name, ssh_agent=True)
    sanic = app(io)
    sanic.run(host="0.0.0.0", port=port)
