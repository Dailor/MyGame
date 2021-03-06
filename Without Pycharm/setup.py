from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


PROGRAM_NAME = "Game"
VERSION = "1.0"
MAIN_SCRIPT_NAME = "main.py"

setup(  name = PROGRAM_NAME,
        version = VERSION, 
        options={"build_exe": {"packages":["pygame"],
        		 'include_files':[
            						os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            						os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')]}},              
        executables = [Executable(MAIN_SCRIPT_NAME)])