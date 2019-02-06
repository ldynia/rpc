#!/usr/local/bin/python

import signal
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://rpc-server/") as proxy:
    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))

print("Press CTRL+C to end ..")
signal.pause()
