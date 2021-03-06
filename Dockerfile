FROM python:3.6.7-alpine3.8

WORKDIR /app

RUN addgroup -g 1000 app && adduser -u 1000 -HD -G app app && \
    chown app:app /app && apk add --update --no-cache postgresql-dev && \
    apk add --no-cache --virtual .build-deps gcc libc-dev musl-dev \
    linux-headers

COPY --chown=app:app ["requirenments.txt", "/app"]

RUN pip3 install --no-cache-dir -r requirenments.txt

COPY --chown=app:app [".", "/app"]

RUN apk del --purge .build-deps

USER app

ENTRYPOINT ["uwsgi", "--uid", "app", "--gid", "app", \
    "--chdir", "/app"]
