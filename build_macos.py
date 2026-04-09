"""
build_macos.py
--------------
Monkey-patches os.symlink and os.makedirs to handle pre-existing
paths during PyInstaller's COLLECT and BUNDLE steps on macOS.
"""
import os
import sys

# Patch os.symlink
_orig_symlink = os.symlink
def _safe_symlink(src, dst, *args, **kwargs):
    try:
        _orig_symlink(src, dst, *args, **kwargs)
    except (FileExistsError, OSError):
        pass
os.symlink = _safe_symlink

# Patch os.makedirs
_orig_makedirs = os.makedirs
def _safe_makedirs(path, *args, **kwargs):
    # If a file exists at this path, remove it first then create the dir
    if os.path.isfile(path):
        os.remove(path)
    try:
        _orig_makedirs(path, *args, **kwargs)
    except FileExistsError:
        pass
os.makedirs = _safe_makedirs

print("os.symlink and os.makedirs patched")

from PyInstaller.__main__ import run
sys.argv = ['pyinstaller', 'powdr_native.spec']
run()
