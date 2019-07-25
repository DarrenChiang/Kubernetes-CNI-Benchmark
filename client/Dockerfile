FROM alpine:3.7

COPY /app /app

RUN apk --update --no-cache add bash iperf3 curl openssh-client \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/* \
  && pip install iperf3

#ENTRYPOINT ["/app/client.py"]
