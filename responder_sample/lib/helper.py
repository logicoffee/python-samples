from functools import wraps
from sqlalchemy.orm.exc import NoResultFound
from pathlib import Path
from yaml import safe_load
from jsonschema import validate, ValidationError


def add_header(req, resp):
    resp.headers['myheader'] = 'lorem-ipsum'


def handle_no_result(f):
    @wraps(f)
    def wrapped_function(self, req, resp, *args, **kwargs):
        try:
            f(self, req, resp, *args, **kwargs)
        except NoResultFound:
            resp.status_code = 404
            resp.media = {
                'status': 'error',
                'message': 'not found',
            }
    return wrapped_function


def load_swag(swagger_file):
    filepath = Path(__file__).resolve().parents[1] / 'swagger' / swagger_file
    with open(filepath) as f:
        specs = safe_load(f)
    return specs


def validate_body(swagger_file, response_def, request_def=None):
    def decorator(f):
        specs = load_swag(swagger_file)['definitions']
        @wraps(f)
        async def wrapped_function(self, req, resp, *args, **kwargs):
            if request_def:
                request_schema = specs[request_def]
                try:
                    media = await req.media()
                    print(media)
                    validate(media, request_schema)
                except ValidationError:
                    resp.status_code = 400
                    resp.media = {
                        'status': 'error',
                        'message': 'invalid request body'
                    }
                    return

            await f(self, req, resp, *args, **kwargs)

            response_schema = specs[response_def]
            try:
                validate(resp.media, response_schema)
            except ValidationError:
                resp.status_code = 500
                resp.media = {
                    'status': 'error',
                    'message': 'internal server error'
                }

        return wrapped_function

    return decorator
