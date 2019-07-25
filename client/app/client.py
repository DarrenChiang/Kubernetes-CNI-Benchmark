#!/usr/bin/env python

import sys
import iperf3
from time import sleep

ip = sys.argv[1]

client = iperf3.Client()
client.server_hostname = ip
results = []

for i in range(5):
	results.append(client.run())
	sleep(1)

print(results)
