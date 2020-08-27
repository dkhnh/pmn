from cre import *

# class-path

def class_path_pfm():
	if not class_path_file_exists():
		deta("nscpfl")
		return

	show(get_class_path())

def class_path_itr(argv):
	if len(argv) != 0:
		deta("cwr")
		return

	class_path_pfm()

# jar-path

def jar_path_pfm():
	if not jar_path_file_exists():
		deta("nscpfl")
		return

	show(get_jar_path())

def jar_path_itr(argv):
	if len(argv) != 0:
		deta("cwr")
		return

	jar_path_pfm()


# package

def package_pfm():
	if not packages_folder_exists():
		deta("nspkfd")
		return

	for package_name in get_packages():
		show(package_name)

def package_itr(argv):
	if len(argv) != 0:
		deta("cwr")
		return

	package_pfm()

# class

def class_pfm(package_name):
	if not packages_folder_exists():
		deta("nspkfd")
		return

	if not is_package(package_name):
		deta("nspk")
		return

	for class_name in get_classes(package_name):
		show(class_name[:-5])


def class_itr(argv):
	if len(argv) != 1:
		deta("cwr")
		return

	class_pfm(argv[0])

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
	elif argv[0] == "package":
		argv.pop(0)
		package_itr(argv)
	elif argv[0] == "class":
		argv.pop(0)
		class_itr(argv)
	else:
		deta("cwr")