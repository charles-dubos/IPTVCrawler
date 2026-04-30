FROM    python:3-alpine
LABEL   maintainer="Papa Dub's" \
        version="26.04" \
        description="Crawler IPTV maison"

ENV     APP_PATH="/iptv_crawler"
ENV     PYTHONUNBUFFERED=1

WORKDIR $APP_PATH

ADD     iptv_crawler.py requirements.txt .

RUN     pip install -r requirements.txt

CMD     ["python", "./iptv_crawler.py" ]
