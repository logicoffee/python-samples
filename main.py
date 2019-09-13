import responder
from lib.helper import add_header
from controllers.foo import Foo, Hello, Hellos

api = responder.API()

api.add_route(None, add_header, before_request=True)
api.add_route('/foo/{id:int}', Foo)
api.add_route('/hello/{name:str}', Hello)
api.add_route('/hello', Hellos)


@api.route('/healthcheck')
def healthcheck(req, resp):
    resp.text = 'I am healthy.'


if __name__ == '__main__':
    api.run()
