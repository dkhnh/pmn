import sys
from cre import deta
import nef
import dlf
import rnf
import adf
import rmf
import swf
import blf
import cpf
import hlf

if __name__ == "__main__":
	sys.argv.pop(0)
	if len(sys.argv) == 0:
		deta("cwr")
	elif sys.argv[0] == "new":
		sys.argv.pop(0);
		nef._itr(sys.argv)
	elif sys.argv[0] == "delete":
		sys.argv.pop(0);
		dlf._itr(sys.argv)
	elif sys.argv[0] == "add":
		sys.argv.pop(0);
		adf._itr(sys.argv)
	elif sys.argv[0] == "remove":
		sys.argv.pop(0);
		rmf._itr(sys.argv)
	elif sys.argv[0] == "show":
		sys.argv.pop(0);
		swf._itr(sys.argv)
	elif sys.argv[0] == "build":
		sys.argv.pop(0);
		blf._itr(sys.argv)
	elif sys.argv[0] == "compile":
		sys.argv.pop(0);
		cpf._itr(sys.argv)
	elif sys.argv[0] == "run":
		sys.argv.pop(0);
		rnf._itr(sys.argv)
	elif sys.argv[0] == "help":
		sys.argv.pop(0);
		hlf._itr(sys.argv)
	else:
		deta("cwr")