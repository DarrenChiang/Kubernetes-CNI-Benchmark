FROM alpine:3.7

COPY /app /app

RUN apk --update --no-cache add bash iperf3 curl openssh-client \
    python \
    py-pip \
  && pip install iperf3 \
  && chmod +x /app/server.py

ENTRYPOINT ["/app/server.py"]
