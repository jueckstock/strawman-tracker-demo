# Strawman Tracker Demo
Mock-up example of a hypothesized cross-site tracker scheme that propagates via navigation URL manipulation, without any third-party storage or redirection tricks employed.

## Requirements

* Python 3 (uses only standard library, no `venv` or `pip` steps needed)
* TCP ports 8001, 8002, and 8003 unbound

## Running

`$ python3 server.py`

(`^C` cleanly terminates the server)

## Testing

After starting the server, navigate a web browser to [localhost:8001](http://localhost:8001/index.html) and click the provided link[s].
To monitor the "tracking," open the developer's console and/or localStorage views.
