#!/usr/bin/python3

from multiprocessing import Pool
import sys, requests, time

def request(line):
	time.sleep(0.5)
	user = line.strip()
	status = requests.get(f"https://github.com/{user}").status_code
	result = {"user": user, "data": status}
	if status == 404: print(user)
	return result

pool = Pool(processes=1)

try:
	lines = sys.stdin.readlines()
	results = pool.map(request, lines)
except KeyboardInterrupt:
	sys.exit()

for res in results:
	print(res)
