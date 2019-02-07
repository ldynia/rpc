#!/usr/local/bin/python

from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from jsonrpc import JSONRPCResponseManager, dispatcher


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["add"] = lambda a, b: a + b
    dispatcher["echo"] = lambda value: value

    response = JSONRPCResponseManager.handle( request.data, dispatcher)

    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    print("Press CTRL+C to end ..")
    run_simple('0.0.0.0', 80, application)
