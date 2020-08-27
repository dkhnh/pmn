from cre import *
 
# project

def project_pfm(project_name, path = "./"):
	path = path_format(path)

	if not path_exists(path):
		inti("e", "c", "fd", path + project_name, "nsdr")
		return

	if path_exists(path + project_name):
		inti("e", "c", "fd", path + project_name, "dre")
		return

	if not create_folder(path + project_name):
		inti("e", "c", "fd", path + project_name, "cncdr")
		return

	inti("s", "c", "fd", path + project_name)

	if not create_folder(path + project_name + "/jar"):
		inti("e", "c", "fd", path + project_name + "/jar", "cncdr")
		return

	inti("s", "c", "fd", path + project_name + "/jar")

	if not create_folder(path + project_name + "/" + get_packages_folder_name()):
		inti("e", "c", "fd", path + project_name + "/" + get_packages_folder_name(), "cncdr")
		return

	inti("s", "c", "fd", path + project_name + "/" + get_packages_folder_name())

	if not create_folder(path + project_name + "/" + get_erm_folder_name()):
		inti("e", "c", "fd", path + project_name + "/" + get_erm_folder_name(), "cncdr")
		return

	inti("s", "c", "fd", path + project_name + "/" + get_erm_folder_name())

	if not create_file(path + project_name + "/" + get_main_class_file_name() + ".java", get_default_file_content("app")):
		inti("e", "c", "fl", path + project_name + "/" + get_main_class_file_name() + ".java", "cncfl")
		return

	inti("s", "c", "fl", path + project_name + "/" + get_main_class_file_name() + ".java")

	if not create_file(path + project_name + "/" + get_class_path_file_name(), get_erm_folder_path() + ":" + get_erm_folder_path() + get_packages_folder_name() + "/"):
		inti("e", "c", "fl", path + project_name + "/" + get_class_path_class_file_name(), "cncfl")
		return

	inti("s", "c", "fl", path + project_name + "/" + get_class_path_file_name())

	if not create_file(path + project_name + "/" + get_jar_path_file_name(), "./jar/"):
		inti("e", "c", "fl", path + project_name + "/" + get_jar_path_file_name(), "cncfl")
		return

	inti("s", "c", "fl", path + project_name + "/" + get_jar_path_file_name())

	deta("scpj")

def project_itr(argv):
	if len(argv) == 1:
		project_pfm(argv[0])
	elif len(argv) == 2:
		project_pfm(argv[0], argv[1])
	else:
		deta("cwr")

# package

def package_pfm(package_name):
	if not packages_folder_exists():
		deta("nspkfd")
		return

	if not is_right_package_name(package_name):
		deta("scipk")
		return

	if is_package(package_name):
		deta("pke")
		return

	if not create_package(package_name):
		inti("e", "c", "fd", get_packages_folder_path() + package_name, "cncdr")
		return

	inti("s", "c", "fd", get_packages_folder_path() + package_name)

	deta("scpk")

def package_itr(argv):
	if len(argv) != 1:
		deta("cwr")
		return

	package_pfm(argv[0])

# class

def class_pfm(class_name, package_name):
	if not packages_folder_exists():
		deta("nspkfd")
		return

	if not is_right_class_name(class_name):
		deta("scicl")
		return

	if not is_package(package_name):
		path = path_format(package_name)
		if not path_exists(path):
			deta("nsdr")
			return

		if path_exists(path + class_name + ".java"):
			deta("fle")
			return

		if not create_class_file(class_name, path):
			inti("e", "c", "fl", path + class_name + ".java", "cncfl")
			return

		inti("s", "c", "fl", path + class_name + ".java")

		deta("sccl")
		return

	if is_class(class_name, package_name):
		deta("cle")
		return

	if not create_class(class_name, package_name):
		inti("e", "c", "fl", get_packages_folder_path() + package_name + "/" + class_name + ".java", "cncfl")
		return

	inti("s", "c", "fl", get_packages_folder_path() + package_name + "/" + class_name + ".java")

	deta("sccl")

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
	elif argv[0] == "project":
		argv.pop(0)
		project_itr(argv)
	elif argv[0] == "package":
		argv.pop(0)
		package_itr(argv)
	elif argv[0] == "class":
		argv.pop(0)
		class_itr(argv)
	else:
		deta("cwr")