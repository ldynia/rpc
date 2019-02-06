#!/usr/local/bin/python

from xmlrpc.server import SimpleXMLRPCServer


def is_even(n):
    return n % 2 == 0


server = SimpleXMLRPCServer(("0.0.0.0", 80))
print("Listening on port 80...")

server.register_function(is_even, "is_even")

print("Press CTRL+C to end ..")
server.serve_forever()
