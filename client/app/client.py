#!/usr/bin/env python

import sys
import iperf3
from time import sleep

def get_server_info() {
	server = {}
	return server
}

def test_iperf3(server, protocol, print_info) {
	client = iperf3.Client()
	client.server_hostname = server['hostname']
	client.protocol = protocol
	test = client.run()
	if print_info:
		print(test)
	return test
}

if __name__ == '__main__':
	server = get_server_info()
	results = []

	while True:
		results.append(('tcp', test_iperf3(server, 'tcp', true))
		results.append(('udp', test_iperf3(server, 'udp', true))
		sleep(3)