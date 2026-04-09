"""
build_macos.py
--------------
Monkey-patches os.symlink to ignore FileExistsError,
then runs PyInstaller programmatically.
"""
import os
import sys

_original_symlink = os.symlink

def _safe_symlink(src, dst, *args, **kwargs):
    try:
        _original_symlink(src, dst, *args, **kwargs)
    except FileExistsError:
        pass

os.symlink = _safe_symlink
print("os.symlink patched to ignore FileExistsError")

from PyInstaller.__main__ import run
sys.argv = ['pyinstaller', 'powdr_native.spec']
run()
