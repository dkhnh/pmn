import os
import json
import shutil
import platform

OI = {
	"packages-folder-name": "packages",
	"erm-folder-name": ".erm",
	"class-path-file-name": ".class-path",
	"jar-path-file-name": ".jar-path",
	"main-class-file-name": "App",
	"default-file-contents":
	{
		"app": "class App {\n\tpublic static void main(String[] args) {\n\t\t\n\t}\n}",
		"clwpkg": "package !package;\n\npublic class !class {\n\t\n}",
		"clnpkg": "class !class {\n\tpublic static void main(String[] args) {\n\t\t\n\t}\n}"
	},
	"intimate":
	{
		"status": { "s": "SUCCESS", "e": "ERROR", "w": "WARNING" },
		"action": { "a": "ADD", "r": "REMOVE", "c": "CREATE", "d": "DELETE" },
		"pattern": { "cp": "class-path", "rp": "jar-path", "fd": "folder", "fl": "file", "pk": "package", "cl": "class", "pp": "package-path", "dr": "directory" },
		"detail":
		{
			"cwr": "This command is wrong",
			"cpe": "Class-path exists",
			"rpe": "Jar-path exists",
			"pke": "Package exists",
			"cle": "Class exists",
			"dre": "Directory exists",
			"fle": "File exists",
			"scpj": "Successfully created the project",
			"scpk": "Successfully created the package",
			"sccl": "Successfully created the class",
			"sdpk": "Successfully deleted the package",
			"sdcl": "Successfully deleted the class",
			"sacp": "Successfully added the class-path",
			"sarp": "Successfully added the jar-path",
			"srcp": "Successfully removed the class-path",
			"srrp": "Successfully removed the jar-path",
			"sbcp": "Successfully build the class-path",
			"sppk": "Successfully compiled the packages",
			"spcl": "Successfully compiled the classes",
			"nsdr": "No such directory",
			"nsfl": "No such file",
			"nscp": "No such class-path",
			"nsrp": "No such jar-path",
			"nspk": "No such package",
			"nscl": "No such class",
			"nspkfd": "No such packages folder",
			"nscpfl": "No such class-path file",
			"nsrpfl": "No such jar-path file",
			"cncdr": "Could not create directory",
			"cncfl": "Could not create file",
			"cncdr": "Could not delete directory",
			"cndfl": "Could not detele file",
			"scipk": "Special characters in package name",
			"scicl": "Special characters in class name"
		}
	},
	"helps":
	{
		"new project":
		{
			"argument": "<PROJECT_NAME> [<DIRECTORY>]",
			"description": "Create new project."
		},

		"new package":
		{
			"argument": "<PACKAGE_NAME>",
			"description": "Create new package."
		},

		"new class":
		{
			"argument": "<CLASS_NAME> [<PACKAGE_NAME> | <DIRECTORY>]",
			"description": "Create new class."
		},

		"delete package":
		{
			"argument": "<PACKAGE_NAME>",
			"description": "Delete package."
		},

		"delete class":
		{
			"argument": "<CLASS_NAME> [<PACKAGE_NAME> | <DIRECTORY>]",
			"description": "Delete class."
		},

		"add class-path":
		{
			"argument": "<PATH>",
			"description": "Add class-path."
		},

		"add jar-path":
		{
			"argument": "<PATH>",
			"description": "Add jar-path."
		},

		"remove class-path":
		{
			"argument": "<PATH>",
			"description": "Remove class-path."
		},

		"remove jar-path":
		{
			"argument": "<PATH>",
			"description": "Remove jar-path."
		},

		"show class-path":
		{
			"description": "Shows class-path"
		},

		"show jar-path":
		{
			"description": "Shows jar-path."
		},

		"show package":
		{
			"description": "Shows package list."
		},

		"show class":
		{
			"argument": "<PACKAGE_NAME>",
			"description": "Shows class list in package."
		},

		"build class-path":
		{
			"description": "Build class-path from jar-path."
		},

		"compile package":
		{
			"argument": "[<PACKAGE_NAME>]",
			"description": "Compile a package or all package."
		},

		"compile class":
		{
			"argument": "<CLASS_NAME> [<PACKAGE_NAME> | <DIRECTORY>]",
			"description": "Compile class."
		},

		"run":
		{
			"argument": "[<CLASS_NAME> [<PACKAGE_NAME> | <DIRECTORY>]]",
			"description": "Compile all packages, main class then execute main class. If the argument exists only compile and execute the requested class."
		},

		"help":
		{
			"argument": "[<KEYWORD_SEARCH>]",
			"description": "Shows all commands. if a parameter exists showing only the related commands."
		}
	}
}

# is

def is_right_package_name(name):
	chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
			 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
			 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
			 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "_", "."]
	for c in name:
		if not c in chars:
			return False

	return True

def is_right_class_name(name):
	chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
			 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
			 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
			 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "_"]
	for c in name:
		if not c in chars:
			return False

	return True

def is_package(package_name):
	return package_name in os.listdir("./" + OI["packages-folder-name"]) and os.path.isdir("./" + OI["packages-folder-name"] + "/" + package_name)

def is_class(class_name, package_name):
	return class_name + ".java" in os.listdir("./" + OI["packages-folder-name"] + "/" + package_name) and os.path.isfile("./" + OI["packages-folder-name"] + "/" + package_name + "/" + class_name + ".java")

# get

def get_packages_folder_name():
	return OI["packages-folder-name"]

def get_erm_folder_name():
	return OI["erm-folder-name"]

def get_class_path_file_name():
	return OI["class-path-file-name"]

def get_jar_path_file_name():
	return OI["jar-path-file-name"]

def get_main_class_file_name():
	return OI["main-class-file-name"]

def get_packages_folder_path():
	return "./" + OI["packages-folder-name"] + "/"

def get_erm_folder_path():
	return "./" + OI["erm-folder-name"] + "/"

def get_class_path_file_path():
	return "./" + OI["class-path-file-name"] + "/"

def get_jar_path_file_path():
	return "./" + OI["jar-path-file-name"] + "/"

def get_main_class_file_path():
	return "./" + OI["main-class-file-name"] + "/"

def get_default_file_content(key):
	return OI["default-file-contents"][key]

def get_helps():
	return OI["helps"]

def get_help(key):
	return OI["helps"][key]

def get_packages():
	return [package_name for package_name in os.listdir("./" + OI["packages-folder-name"]) if os.path.isdir("./" + OI["packages-folder-name"] + "/" + package_name) and is_right_package_name(package_name)]

def get_classes(package_name):
	return [class_name for class_name in os.listdir("./" + OI["packages-folder-name"] + "/" + package_name) if os.path.isfile("./" + OI["packages-folder-name"] + "/" + package_name + "/" + class_name) and class_name.endswith(".java") and is_right_class_name(class_name[:-5])]

def get_package_path(package_name):
	return "./" + OI["packages-folder-name"] + "/" + package_name + "/"

def get_package_class_path(class_name, package_name):
	return "./" + OI["packages-folder-name"] + "/" + package_name + "/" + class_name + ".java"

def get_class_path():
	return open("./" + OI["class-path-file-name"], "r").read()

def get_jar_path():
	return open("./" + OI["jar-path-file-name"], "r").read()

# create

def create_package(package_name):
	try:
		os.mkdir("./" + OI["packages-folder-name"] + "/" + package_name)
	except:
		return False

	return True

def create_class(class_name, package_name):
	try:
		open("./" + OI["packages-folder-name"] + "/" + package_name + "/" + class_name + ".java", "w").write(OI["default-file-contents"]["clwpkg"].replace("!package", package_name).replace("!class", class_name))
	except:
		return False

	return True

def create_class_file(class_name, path):
	try:
		open(path + class_name + ".java", "w").write(OI["default-file-contents"]["clnpkg"].replace("!class", class_name))
	except:
		return False

	return True

# delete

def delete_package(package_name):
	try:
		shutil.rmtree("./" + OI["packages-folder-name"] + "/" + package_name)
	except:
		return False

	return True

def delete_class(class_name, package_name):
	try:
		os.remove("./" + OI["packages-folder-name"] + "/" + package_name + "/" + class_name + ".java")
	except:
		return False

	return True

def delete_class_file(class_name, path):
	try:
		os.remove(path + class_name + ".java")
	except:
		return False

	return True

# add

def add_class_path(path):
	class_path = open("./" + OI["class-path-file-name"], "r").read()

	if path in class_path.split(":"):
		return False

	open("./" + OI["class-path-file-name"], "w").write(class_path + ":" + path)

	return True

def add_jar_path(path):
	jar_path = open("./" + OI["jar-path-file-name"], "r").read()

	if path in jar_path.split(":"):
		return False

	open("./" + OI["jar-path-file-name"], "w").write(jar_path + ":" + path)

	return True

# remove

def remove_class_path(path):
	class_paths = open("./" + OI["class-path-file-name"], "r").read().split(":")

	if not path in class_paths:
		return False

	class_paths.remove(path)

	open("./" + OI["class-path-file-name"], "w").write(':'.join(class_paths))

	return True

def remove_jar_path(path):
	jar_paths = open("./" + OI["jar-path-file-name"], "r").read().split(":")

	if not path in jar_paths:
		return False

	jar_paths.remove(path)

	open("./" + OI["jar-path-file-name"], "w").write(':'.join(jar_paths))

	return True

# exists

def packages_folder_exists():
	return os.path.exists("./" + OI["packages-folder-name"]) and os.path.isdir("./" + OI["packages-folder-name"])

def class_path_file_exists():
	return os.path.exists("./" + OI["class-path-file-name"]) and os.path.isfile("./" + OI["class-path-file-name"])

def jar_path_file_exists():
	return os.path.exists("./" + OI["jar-path-file-name"]) and os.path.isfile("./" + OI["jar-path-file-name"])

# echo

def inti(status, action, pattern, content, detail = ""):
	print("{:11}{:8}{:14}{}".format(
		"[" + OI["intimate"]["status"][status] + "]",
		OI["intimate"]["action"][action],
		OI["intimate"]["pattern"][pattern],
		content))

	if detail != "":
		print(OI["intimate"]["detail"][detail])

def deta(detail):
	print(OI["intimate"]["detail"][detail])

def show_help(help_key):
	if "argument" in OI["helps"][help_key]:
		print("{:19}{}".format(help_key, OI["helps"][help_key]["argument"]))
		print("{:19}{}".format("", OI["helps"][help_key]["description"]))
	else:
		print("{:19}{}".format(help_key, OI["helps"][help_key]["description"]))

def show(*content):
	print(*content)

# spt

def is_file(path):
	return os.path.isfile(path)

def is_dir(path):
	return os.path.isdir(path)

def join_path(f_path, s_path):
	return os.path.join(f_path, s_path)

def path_exists(path):
	return os.path.exists(path)

def path_format(path):
	if path == "":
		return "./"

	if path[0] != "." and path[0] == "/":
		path = "." + path
	elif path[0] != "." and path[0] != "/":
		path = "./" + path
	elif len(path) > 1 and path[0] == "." and path[1] != "/":
		path = "./" + path

	if path[-1] != "/":
		path += "/"

	return path

def create_folder(path):
	try:
		os.mkdir(path)
	except:
		return False

	return True

def create_file(path, content = ""):
	try:
		file = open(path, "w")
		file.write(content)
		file.close()
	except:
		return False

	return True

def delete_file(path):
	try:
		os.remove(path)
	except:
		return False

	return True

def delete_folder(path):
	try:
		shutil.rmtree(path)
	except:
		return False

	return True

def com_option_0(com, opt_name, defaut_value = False):
	if not "-" + opt_name in com:
		return { opt_name: defaut_value }

	if com.count("-" + opt_name) > 1:
		return;

	com.remove("-" + opt_name)

	if not opt_name in com:
		return { opt_name: True }


def com_option_1(com, opt_name, defaut_value = ""):
	if not "-" + opt_name in com:
		return {  opt_name: defaut_value }

	if com.count("-" + opt_name) > 1:
		return;

	value = ""
	try:
		i = com.index("-" + opt_name)
		value = com[i + 1]
	except:
		return;

	com.pop(i + 1)
	com.pop(i)

	return { opt_name: value }

# windows

def is_windows_platform():
	return platform.system()

def hidden_file(path):
	os.system("attrib +h " + path)

# java

def jexecutable(cp, file_names):
	if cp == "":
		os.system("java " + file_names)
	else:
		os.system("java -cp " + cp + " " + file_names)

def jcompile(cp, file_names, directory = ""):
	if directory == "":
		if cp == "":
			os.system("javac " + file_names)
		else:
			os.system("javac -cp " + cp + " " + file_names)
	else:
		if cp == "":
			os.system("javac -d " + directory + " " + file_names)
		else:
			os.system("javac -d " + directory + " -cp " + cp + " " + file_names)
