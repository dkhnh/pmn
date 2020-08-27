from cre import *

# class-path

def class_path_pfm(path):
	if not class_path_file_exists():
		deta("nscpfl")
		return

	path = path_format(path)

	if not add_class_path(path):
		inti("e", "a", "cp", path, "cpe")
		return

	inti("s", "a", "cp", path)

	deta("sacp")

def class_path_itr(argv):
	if len(argv) != 1:
		deta("cwr")
		return

	class_path_pfm(argv[0])

# jar-path

def jar_path_pfm(path):
	if not jar_path_file_exists():
		deta("nscpfl")
		return

	path = path_format(path)

	if not add_jar_path(path):
		inti("e", "a", "rp", path, "rpe")
		return

	inti("s", "a", "rp", path)

	deta("sarp")

def jar_path_itr(argv):
	if len(argv) != 1:
		deta("cwr")
		return

	jar_path_pfm(argv[0])

# _itr

def _itr(argv):
	if len(argv) == 0:
		deta("cwr")
	elif argv[0] == "class-path":
		argv.pop(0)
		class_path_itr(argv)
	elif argv[0] == "jar-path":
		argv.pop(0)
		jar_path_itr(argv)
	else:
		deta("cwr")