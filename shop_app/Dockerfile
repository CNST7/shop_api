FROM python:3.10.9-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /:/shop_app/mycart

RUN mkdir -p /shop_app/mycart/staticfiles
RUN pip install --upgrade pip
COPY ./requirements.txt /shop_app/requirements.txt
RUN pip install -r /shop_app/requirements.txt --no-cache-dir

COPY ./mycart /shop_app/mycart
COPY ./shop_domain /shop_app/shop_domain

EXPOSE 8000
WORKDIR /shop_app/mycart

# remove --reload on production
CMD python manage.py collectstatic --no-input && \
    python manage.py makemigrations --no-input && \
    python manage.py wait_for_db && \ 
    python manage.py migrate --no-input && \ 
    python -m gunicorn mycart.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --reload