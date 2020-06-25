#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
import time
import threading
import sys


class ToyServerInstance(ThreadingHTTPServer):
    def __init__(self, docroot, port):
        super().__init__(
            ("localhost", port),
            lambda *args: SimpleHTTPRequestHandler(*args, directory=docroot),
        )


def main(argv):
    threads = []
    servers = []
    for port in [8001, 8002, 8003]:
        port_docroot = os.path.join(os.path.dirname(__file__), "docroot", str(port))
        server = ToyServerInstance(port_docroot, port)
        servers.append(server)
        thread = threading.Thread(target=server.serve_forever)
        thread.start()
        threads.append(thread)
        print(f"started server for '{port_docroot}' on port {port}")

    try:
        time.sleep(0.0)
    except KeyboardInterrupt:
        for server in servers:
            server.shutdown()
        for thread in threads:
            thread.join()


if __name__ == "__main__":
    main(sys.argv)
