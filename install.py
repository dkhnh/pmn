import os
import platform

if __name__ == "__main__":
	crdir = os.getcwd()

	if platform.system() == "Windows":
		open(os.path.join(crdir, "pmn.bat"), "w").write("@ECHO OFF\nSET currentpath=%~dp0\npython %currentpath%/pmn_gp/rcp.py %*")
	elif platform.system() == "Linux":
		open(os.path.join(crdir, "pmn"), "w").write("#!/bin/bash\n\nBASEDIR=$(dirname $0)\npython3 $BASEDIR/pmn_gp/rcp.py $*")
	else:
		print("No support")