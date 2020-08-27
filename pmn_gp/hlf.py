from cre import *
 
# _pfm

def not_default_pfm(request):
	for help_key in get_helps().keys():
		if help_key.find(request) != -1:
			show_help(help_key)
			show()

def _pfm():
	for help_key in get_helps().keys():
		show_help(help_key)
		show()

# _itr

def _itr(argv):
	if len(argv) == 0:
		_pfm()
	elif len(argv) == 1:
		not_default_pfm(argv[0])
	else:
		deta("cwr")