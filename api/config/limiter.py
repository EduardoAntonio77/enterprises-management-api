from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per minute"]
)

def init_limiter(app):
    limiter.init_app(app)
