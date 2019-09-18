from responder import API

from controllers.team import app

# flask と responder が共存するパターン・共存しないパターンを集めた

api = API()


def hello(req, resp):
    resp.text = "hello"


# flask のパスが responder のパスよりも深い場合は共存できる
api.mount("/teams", app)
api.add_route("/", hello)


# responder のほうが深い場合(同じ場合も含む)は flask のパスしか機能しない

# 例1
api.mount("/", app)
api.mount("/hello", hello)


# 例2
api.mount("/teams", app)
api.add_route("/teams", hello)


# 例3
api.mount("/teams", app)
api.add_route("/teams/hello", hello)


# ただし mount に指定するパスには パラメーター を含めることができないため, 以下のは思ったとおりに動かない
api.mount("/teams/<name>", app)
api.add_route("/", hello)
