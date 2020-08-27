from cre import *

def class_path_pfm():
	if not class_path_file_exists():
		deta("nscpfl")
		return

	if not jar_path_file_exists():
		deta("nscpfl")
		return

	jar_path = get_jar_path().split(":")
	for path in jar_path:
		for file in os.listdir(path):
			if file.endswith(".jar"):
				add_class_path(path_format(join_path(path, file)))

	deta("sbcp")

def class_path_itr(argv):
	if len(argv) != 0:
		deta("cwr")
		return

	class_path_pfm()

def _itr(argv):
	if len(argv) == 0:
		deta("cwr")
	elif argv[0] == "class-path":
		argv.pop(0)
		class_path_itr(argv)
	else:
		deta("cwr")