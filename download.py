#!/usr/bin/env python
# encoding=utf8  
# -*- coding: utf8  -*-

# DOWNLOAD CO2 AND CLIMATE CHANGE DATASETS
#
# Some more details here
#
#
#
import os
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from pprint import pprint

# REQUESTS
import requests
import urllib2

DOWNLOAD_DIR = "/Volumes/roam/datasets/climate/"

print "Downlaoding climate data to", DOWNLOAD_DIR
try:
	os.makedirs(DOWNLOAD_DIR)
except:
	print "download dir exists. great"

# https://www.netl.doe.gov/research/coal/carbon-storage/natcarb-atlas/data-download
netl_doe_gov = ["https://edx.netl.doe.gov/dataset/natcarb-alldata-v1502/resource_download/f7b936b3-b250-47e4-8475-e1c8474d9e22",
"https://edx.netl.doe.gov/dataset/natcarb-coal-v1502/resource_download/60d80fc7-ecd6-4912-a086-4d8dccf74b1a",
"https://edx.netl.doe.gov/dataset/natcarb-oilgas-v1502/resource_download/747f671d-b599-4eb6-9da9-83c3eceb593d",
"https://edx.netl.doe.gov/dataset/natcarb-saline-v1502/resource_download/4189ccbd-f88e-4e7d-a505-bc99fe4924c4",
"https://edx.netl.doe.gov/dataset/natcarb-sources-v1502/resource_download/76df1e7d-ffc0-4ab6-8806-9003239f8be6"]


# http://data.okfn.org/data/core/co2-ppm#data
data_okfn_org = ["https://raw.githubusercontent.com/datasets/co2-ppm/master/data/co2-mm-mlo.csv",
"https://raw.githubusercontent.com/datasets/co2-ppm/master/data/co2-annmean-mlo.csv",
"https://raw.githubusercontent.com/datasets/co2-ppm/master/data/co2-gr-mlo.csv",
"https://raw.githubusercontent.com/datasets/co2-ppm/master/data/co2-mm-gl.csv",
"https://raw.githubusercontent.com/datasets/co2-ppm/master/data/co2-annmean-gl.csv",
"https://raw.githubusercontent.com/datasets/co2-ppm/master/data/co2-gr-gl.csv"]


def download_file(url):
	local_filename = url.split('/')[-1]

	with open(DOWNLOAD_DIR+local_filename, 'wb') as f:
		print "Downloading %s" % local_filename
		response = requests.get(url, stream=True)
		total_length = response.headers.get('content-length')

		if total_length is None: # no content length header
			f.write(response.content)
		else:
			dl = 0
			total_length = int(total_length)
		for data in response.iter_content(chunk_size=4096):
			dl += len(data)
			f.write(data)
			done = int(50 * dl / total_length)
			sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
			sys.stdout.flush()
	return local_filename



download_file("https://edx.netl.doe.gov/dataset/natcarb-alldata-v1502/resource_download/f7b936b3-b250-47e4-8475-e1c8474d9e22")


# cd /path/to/download/location;wget -rpk www.epa.gov
