#!/usr/local/bin/python

import signal
import signal
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://rpc-server:80/") as proxy:
    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))
    #print("CPU spike run for: %s seconds" % str(proxy.spike_cpu(3)))

print("Press CTRL+C to end ..")
signal.pause()
