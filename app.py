#!/usr/bin/python

from __future__ import print_function
import sys
import os
import hashlib
from termcolor import colored
from shutil import copyfile

OUTPUT_DIR = 'output'

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

with open(sys.argv[-1]) as f:
	if not os.path.exists(OUTPUT_DIR):
		os.mkdir(OUTPUT_DIR)

	for line in f:
		prefix, filepath = line.rstrip("\n").rstrip("\r").split("\t")
		
		if len(filepath)  < 2:
			continue
		
		tidied_path = os.path.normpath(filepath.replace('\\','/').replace('Q:','/Volumes/Shared$/',1))
		print(colored(tidied_path, 'green' if os.path.exists(tidied_path) else 'red'), end='')
		if os.path.isfile(tidied_path):
			print("\t->\t", end="")
			hash = md5(tidied_path)
			output_path = OUTPUT_DIR + "/" + prefix + "-" + hash + ".pdf"
			print(output_path)
			copyfile(tidied_path, output_path)
		else:
			print()
		
		#sys.exit(0)