from cre import *

# package

def package_pfm(package_name):
	if not packages_folder_exists():
		deta("nspkfd")
		return

	if not is_package(package_name):
		deta("nspk")
		return

	if not delete_package(package_name):
		inti("e", "d", "fd", get_packages_folder_path() + package_name, "cndfd")
		return

	inti("s", "d", "fd", get_packages_folder_path() + package_name)

	deta("sdpk")

def package_irt(argv):
	if len(argv) != 1:
		deta("cwr")
		return

	package_pfm(argv[0])

# class

def class_pfm(class_name, package_name):
	if not packages_folder_exists():
		deta("nspkfd")
		return

	if not is_package(package_name):
		path = path_format(package_name)
		if not path_exists(path):
			deta("nsdr")
			return

		if not path_exists(path + class_name + ".java"):
			deta("nsfl")
			return

		if not delete_class_file(class_name, path):
			inti("e", "d", "fl", path + class_name + ".java", "cndfl")
			return

		inti("s", "d", "fl", path + class_name + ".java")

		deta("sdcl")
		return

	if not is_class(class_name, package_name):
		deta("nscl")
		return

	if not delete_class(class_name, package_name):
		inti("e", "d", "fl", get_packages_folder_path() + package_name + "/" + class_name + ".java", "cndfl")
		return

	inti("s", "d", "fl", get_packages_folder_path() + package_name + "/" + class_name + ".java")

	deta("sdcl")

def class_itr(argv):
	if len(argv) == 1:
		class_pfm(argv[0], "./")
	elif len(argv) == 2:
		class_pfm(argv[0], argv[1])
	else:
		deta("cwr")
		return
	
# _itr

def _itr(argv):
	if len(argv) == 0:
		deta("cwr")
	elif argv[0] == "package":
		argv.pop(0)
		package_irt(argv)
	elif argv[0] == "class":
		argv.pop(0)
		class_itr(argv)
	else:
		deta("cwr")