from cre import *

def buil_class_path():
	class_path = get_class_path()

	if is_windows_platform():
		class_path = class_path.replace(":", ";")

	return class_path

def compile_packages(cp):
	for package_name in get_packages():
		file_names = ""

		for class_name in get_classes(package_name):
			file_names += get_package_path(package_name) + class_name + " "

		if file_names == "":
			continue

		jcompile(cp, file_names, "./" + get_erm_folder_name() + "/" + get_packages_folder_name())

def run(cp, main_class_file_name, path = "./"):
	jcompile(cp, path + main_class_file_name + ".java", "./" + get_erm_folder_name())
	jexecutable(cp, main_class_file_name)

# _pfm

def not_default_pfm(main_class_file_name, path):
	if not class_path_file_exists():
		deta("nscpfl")
		return

	if not jar_path_file_exists():
		deta("nscpfl")
		return

	path = path_format(path)

	if not path_exists(path):
		deta("nsdr")
		return

	cp = buil_class_path()
	run(cp, main_class_file_name, path)


def _pfm():
	if not class_path_file_exists():
		deta("nscpfl")
		return

	if not jar_path_file_exists():
		deta("nscpfl")
		return

	if not packages_folder_exists():
		deta("nspkfd")
		return

	cp = buil_class_path()
		
	compile_packages(cp)
	run(cp, get_main_class_file_name())

# _itr

def _itr(argv):
	if len(argv) == 0:
		_pfm()
	elif len(argv) == 1:
		not_default_pfm(argv[0], "./")
	elif len(argv) == 2:
		not_default_pfm(argv[0], argv[1])
	else:
		deta("cwr")