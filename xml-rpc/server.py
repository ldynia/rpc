#!/usr/local/bin/python

import time
import subprocess

from xmlrpc.server import SimpleXMLRPCServer


def is_even(n):
    return n % 2 == 0


def spike_cpu(duration_seconds):
    subprocess.run(["dd", "if=/dev/zero", "of=/dev/null"])
    time.sleep(duration_seconds)
    return duration_seconds


server = SimpleXMLRPCServer(("0.0.0.0", 80))
print("Listening on port 80...")

server.register_function(is_even, "is_even")
server.register_function(spike_cpu, "spike_cpu")

print("Press CTRL+C to end ..")
server.serve_forever()
