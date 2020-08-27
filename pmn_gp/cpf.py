from cre import *

def buil_class_path():
	class_path = get_class_path()

	if is_windows_platform():
		class_path = class_path.replace(":", ";")

	return class_path

def package_pfm(package_name):
	if not class_path_file_exists():
		deta("nscpfl")
		return

	if not packages_folder_exists():
		deta("nspkfd")
		return

	if not is_package(package_name):
		deta("nspk")
		return

	cp = buil_class_path()

	file_names = ""

	for class_name in get_classes(package_name):
		file_names += get_package_path(package_name) + class_name + " "

	if file_names == "":
		return

	jcompile(cp, file_names, "./" + get_erm_folder_name() + "/" + get_packages_folder_name())

	deta("sppk")

def packages_pfm():
	if not class_path_file_exists():
		deta("nscpfl")
		return
	
	if not packages_folder_exists():
		deta("nspkfd")
		return

	cp = buil_class_path()

	for package_name in get_packages():
		file_names = ""

		for class_name in get_classes(package_name):
			file_names += get_package_path(package_name) + class_name + " "

		if file_names == "":
			continue

		jcompile(cp, file_names, "./" + get_erm_folder_name() + "/" + get_packages_folder_name())

	deta("sppk")

def package_itr(argv):
	if len(argv) == 0:
		packages_pfm()
	elif len(argv) == 1:
		package_pfm(argv[0])
	else:
		deta("cwr")

# class

def class_pfm(class_name, package_name):
	if not class_path_file_exists():
		deta("nscpfl")
		return
	
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

		cp = buil_class_path()

		jcompile(cp, path + class_name + ".java", get_erm_folder_path())

		deta("spcl")
		return

	if not is_class(class_name, package_name):
		deta("nspk")
		return

	cp = buil_class_path()

	jcompile(cp, get_package_path(package_name) + class_name + ".java", "./" + get_erm_folder_name() + "/" + get_packages_folder_name())

	deta("spcl")

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
		package_itr(argv)
	elif argv[0] == "class":
		argv.pop(0)
		class_itr(argv)
	else:
		deta("cwr")