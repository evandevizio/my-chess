import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("mychess.py", base=base)]

setup(
    name="My Chess",
    version="0.7",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ['images/']}},
    executables=executables
)
