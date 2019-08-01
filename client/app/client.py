#!/usr/bin/env python

import sys
import os
import iperf3
from time import sleep

def get_server_info():
	return {'hostname': os.environ['hostname']}

def wait_for_server(server):
	while (os.system("ping -c 1 " + server['hostname']) != 0):
		sleep(0.5)

def test_iperf3(server, protocol, print_info):
	client = iperf3.Client()
	client.server_hostname = server['hostname']
	client.protocol = protocol
	client.duration = int(os.environ['test_duration'])
	test = client.run()
	if print_info:
		print(test)
	return test

if __name__ == '__main__':
	server = get_server_info()
	f = open('results.txt', 'a')
	wait_for_server(server)

	for i in range(10):
		f.write(str(test_iperf3(server, 'tcp', True)) + '\n')
		sleep(5)
		#f.write(str(test_iperf3(server, 'udp', True)) + '\n')
		#sleep(5)

	f.close()

	while True:
		sleep(1)
