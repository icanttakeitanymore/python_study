#!/usr/bin/env python3
import os
def run(a):
	os.chdir(a)
	from http.server import HTTPServer, CGIHTTPRequestHandler
	server_address = ("", 8000)
	httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
	httpd.serve_forever()
dir = '/home/boris/git'
run(dir)
