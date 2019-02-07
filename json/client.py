#!/usr/local/bin/python

import json
import signal
import requests
from jsonrpcclient import request
from jsonrpcclient.clients.http_client import HTTPClient


def main():
    URL = "http://rpc-server:80/"
    HEADERS = {'content-type': 'application/json'}

    payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }

    payload2 = {
        "method": "add",
        "params": [2, 3],
        "jsonrpc": "2.0",
        "id": 0,
    }

    # 1st client
    client = HTTPClient(URL)

    # 2nd client
    response = client.send(payload2)
    # response = requests.post(URL, data=json.dumps(payload2), headers=HEADERS).json()

    # 3rd client
    # response = request(URL, "echo", value="Yoko")

    print('RPC Response', response.data)


if __name__ == "__main__":
    main()
    print("Press CTRL+C to end ..")
    signal.pause()
