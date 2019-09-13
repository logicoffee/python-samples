from responder import API
from sqlalchemy.orm.exc import NoResultFound
from lib.helper import validate_body, handle_no_result


api = API()


class Foo:
    @handle_no_result
    def on_get(self, req, resp, *, id):
        if id < 2:
            raise NoResultFound
        else:
            resp.media = {
                'status': 'ok',
                'foo': {
                    'id': id,
                },
            }


class Hello:
    @validate_body('hello.yml', 'HelloResponse')
    async def on_get(self, req, resp, *, name):
        resp.media = {
            'name': name,
            'greeting': 'hello'
        }


class Hellos:
    @validate_body('hello.yml', 'HelloResponse', 'HelloRequest')
    async def on_post(self, req, resp):
        media = await req.media()
        print(media)
        resp.media = {
            'name': media['name'],
            'greeting': 'good morning'
        }
