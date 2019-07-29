#!/usr/bin/env python

import sys
import os
import iperf3
from time import sleep

def get_server_info():
	return {'hostname': sys.argv[1]}

def wait_for_server(server):
	while (os.system("ping -c 1 " + server['hostname']) != 0):
		sleep(1)

def test_iperf3(server, protocol, print_info):
	client = iperf3.Client()
	client.server_hostname = server['hostname']
	client.protocol = protocol
	test = client.run()
	if print_info:
		print(test)
	return test

if __name__ == '__main__':
	server = get_server_info()
	f = open('results.txt', 'w+')

	for i in range(10):
		wait_for_server(server)
		f.write(str(test_iperf3(server, 'tcp', True)) + '\n')
		f.write(str(test_iperf3(server, 'udp', True)) + '\n')

	f.close()

	while True:
		sleep(1)
