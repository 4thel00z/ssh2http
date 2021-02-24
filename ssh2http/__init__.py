from pwn import *
import sys
import os


def usage(name=sys.argv[0]):

    return f"""
    {name} <entry-in-ssh-config> <port: optional, defaults to 1337>
    """


class HelpException:
    def __init__(self, msg=usage()):
        self.msg = msg

    def __str__(self):
        return self.msg

    def exit(self, status_code=os.EX_SOFTWARE, out=sys.stderr):
        print(str(self), file=out)
        sys.exit(status_code)


def get_args(default_port=1337):

    args = sys.argv

    if len(args) < 2:
        raise HelpException()
    if len(args) == 2:
        args += [1337]

    return args
