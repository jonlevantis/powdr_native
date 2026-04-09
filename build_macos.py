"""
build_macos.py
--------------
Wrapper that monkey-patches os.symlink to ignore FileExistsError,
then runs PyInstaller programmatically. This ensures the patch is
active during the entire build, not just before it starts.
"""
import os
import sys

# Monkey-patch os.symlink BEFORE importing PyInstaller
_original_symlink = os.symlink

def _safe_symlink(src, dst, *args, **kwargs):
    try:
        _original_symlink(src, dst, *args, **kwargs)
    except FileExistsError:
        pass

os.symlink = _safe_symlink
print("os.symlink patched to ignore FileExistsError")

# Now run PyInstaller with the spec file
from PyInstaller.__main__ import run
sys.argv = ['pyinstaller', 'powdr_native.spec']
run()
