import sys , lib 
from lib import * 
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-k",'--key',action="store",help="input key",default=False)
parser.add_option("-d","--decoder",action="store",help="input to decode",default=False)
parser.add_option("-e","--encoder",action="store",help="input to encode",default=False)

(options,argv) = parser.parse_args()

if options.key == False :
	print "No key input"
	raise SystemExit(1)
key = options.key

if options.decoder != False :
	crpty = options.decoder 
	print de_en_coder(key,crpty,False)
elif options.encoder != False:
	encode = options.encoder
	print de_en_coder(key,encode,True)
else:
	print "You should input something to decode or encode,"
	print "run 'python main.py -h' can get information."
	raise SystemExit(1)

