import sys , lib 
from lib import * 
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-k",'--key',action="store",help="input key",default=False)
parser.add_option("-f",'--file',action="store_true",help="input keyfile",default=False)
parser.add_option("-d","--decoder",action="store",help="input a string to decode, eg. -d 'ToDecode' ",default=False)
parser.add_option("-e","--encoder",action="store",help="input a string to encode, eg. --encoder='ToEncode' ",default=False)
parser.add_option("-o","--output",action="store",help="input a path to store result, eg. -o 'result.txt' ",default=False)
parser.add_option("-i","--input",action="store_true",help="input a path for loading to decode or encode,eg. -i -d 'file.txt' ",default=False)

(options,argv) = parser.parse_args()

def readfile(filename) :
	content = ""
	with open(filename) as f :
		content += f.read()
	return content

if options.key == False :
	print "No key input"
	print "run 'python main.py -h' can get information."
	raise SystemExit(1)

key = (options.file) and readfile(options.key) or options.key

if options.decoder != False :
	content , state = (options.input) and readfile(options.decoder) or options.decoder , False
elif options.encoder != False:
	content , state  = (options.input) and readfile(options.encoder) or options.encoder , True
else:
	print "You should input something to decode or encode,"
	print "run 'python main.py -h' can get information."
	raise SystemExit(1)

result = de_en_coder(key,content,state)

if options.output == False :
	print result
else :
	with open(options.output,'w') as output:
		output.write(result)
