#!/usr/bin/env python

import sys
import iperf3

server = iperf3.Server()

while True:
	server.run()
