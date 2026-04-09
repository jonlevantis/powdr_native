"""
build_macos.py — patches os.symlink then runs PyInstaller (COLLECT only, no BUNDLE)
"""
import os, sys

_orig_symlink = os.symlink
def _safe_symlink(src, dst, *args, **kwargs):
    try:
        _orig_symlink(src, dst, *args, **kwargs)
    except (FileExistsError, OSError):
        pass
os.symlink = _safe_symlink

from PyInstaller.__main__ import run
sys.argv = ['pyinstaller', 'powdr_native.spec']
run()
