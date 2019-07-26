FROM alpine:3.7

COPY /app /app

RUN apk --no-cache add bash iperf3 curl openssh-client \
    python \
    py-pip \
  && pip install iperf3 \
  && chmod +x /app/client.py

ENTRYPOINT ["/bin/sh"]
