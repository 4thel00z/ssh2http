# ssh2http

## Motivation

Imagine you want to multiplex/expose one ssh connection over a simple REST API.
Ideally you want to just pass the hostname and it does the lookup via the `ssh_agent`.

Something like this:

```
ssh2http <something-in-your-~/.ssh/config> <port-no>
```
