#!/bin/bash

kubectl apply -f bench_config.yaml #starting config
kubectl apply -f benchmark.yaml #starting service
kubectl apply -f server/pod.yaml #starting server pod
sleep 5
kubectl apply -f client/pod.yaml #starting client pod
kubectl exec client /app/client.py #executing benchmarking test
