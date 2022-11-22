FROM alpine

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN apk add -q --progress --update --no-cache ffmpeg python3 py-pip 
RUN pip install discord.py==1.7.3 youtube-dl pynacl

WORKDIR /Hedgebot
COPY . .

CMD ["python3", "wrapper.py"]