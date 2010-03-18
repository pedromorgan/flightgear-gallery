#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

url_base = "http://flightgear-gallery.googlecode.com/svn/trunk/v2.0"

image_path = "v2.0/thumbs/"

image_list = []
for img in os.listdir(image_path):
	if not img.startswith('.'):
		image_list.append( {'image': '%s/images/%s' % (url_base, img), 'thumb': '%s/thumbs/%s' % (url_base, img)} )
		#print img

json_str = json.dumps( {'gallery': image_list} )

json_file = open("./gallery.js", "w")
json_file.write( json_str )
json_file.close()
