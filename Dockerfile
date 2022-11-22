FROM alpine

RUN apk add -q --progress --update --no-cache ffmpeg python py-pip
RUN pip install --upgrade pip
RUN pip install youtube_dl

COPY ./youtube-dl.conf /etc/youtube-dl.conf

WORKDIR /hedgebot

ENTRYPOINT ["youtube-dl"]