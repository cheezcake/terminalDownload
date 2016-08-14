#!/usr/bin/env python

import base64
import sys

ESC = '\x1b'

BEL = '\x07'

ARGV = sys.argv

filenameParameterTemplate = "name=%s"

filesizeParameterTemplate = "size=%s"

fileTransferTemplate = "".join((ESC, "]1337;File=%s:", "%s", BEL))

if(__name__) == "__main__":
	if(len(ARGV) != 2):
		print "terminalDownload: iTerm terminal file downloader by cheez\n"
		
		print "Convenience utility for downloading files using iTerm via SSH wherever python is available\n"

		print "Usage: %s <file>\n" % ARGV[0]

		exit()

	try:
		fileName = ARGV[1]

		# open, read, close the file

		inputFile = open(fileName, "r")

		fileContents = inputFile.read()

		inputFile.close()

		# get the size of the file contents before base64 encoding

		fileSize = len(fileContents)

		# the file contents will now be overwritten by the encoded version

		fileContents = base64.b64encode(fileContents)

		filenameParameter = filenameParameterTemplate % base64.b64encode(fileName)

		filesizeParameter = filesizeParameterTemplate % fileSize

		fileTransferOptions = ";".join((filenameParameter, filesizeParameter))

		fileTransfer = fileTransferTemplate % (fileTransferOptions, fileContents)

		print fileTransfer

	except IOError, e:
		print "error opening file <%s>: does file exist? do we have permissions?\n\nso many questions... so little time...."

		exit(-1)

