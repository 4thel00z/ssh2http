# ssh2http

## Motivation

Imagine you want to multiplex/expose one ssh connection over a simple REST API.
Ideally you want to just pass the hostname and it does the lookup via the `ssh_agent`.

## Installation

```
python3 -m pip install ssh2http
```

## Usage

```
# server
python3 -m ssh2http <name-of-ssh-config-entry> <port - defaults to 1337>

# client
python3 -m ssh2http.client <url-to-ssh2http-server> <timeout-of-commands - defaults to 30 secs>
```
## License

This project is licensed under the GPL-3 license.
