FROM alpine:3.7

COPY /app /app

RUN apk --no-cache add iperf3 \
    python \
    py-pip \
  && pip install iperf3 \
  && chmod +x /app/server.py

ENTRYPOINT ["/bin/sh"]
