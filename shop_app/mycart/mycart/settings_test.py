from .settings import *

SECRET_KEY = "django-insecure-y$knt!95tg78oycw3+p)^_cjgd$$%(jl*wttb92iaezoms6xi@"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0", "shop_api"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # type: ignore
    },
}
