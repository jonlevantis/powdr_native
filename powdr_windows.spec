# powdr_windows.spec
# PyInstaller spec for packaging powdR GUI on Windows
#
# Usage (in the powdr_native folder, on a Windows machine or CI):
#   pip install pyinstaller PyQt6 pandas numpy scipy matplotlib
#   pyinstaller powdr_windows.spec
#
# Output: dist\powdR\powdR.exe

from PyInstaller.utils.hooks import collect_data_files, collect_all

block_cipher = None

qt_datas, qt_binaries, qt_hiddenimports = collect_all("PyQt6")

a = Analysis(
    ["app_qt.py"],
    pathex=["."],
    binaries=qt_binaries,
    datas=[
        ("afps.py",          "."),
        ("fitting.py",       "."),
        ("preprocessing.py", "."),
        ("plotting.py",      "."),
        *qt_datas,
        *collect_data_files("matplotlib"),
        *collect_data_files("scipy"),
        *collect_data_files("pandas"),
    ],
    hiddenimports=[
        *qt_hiddenimports,
        "PyQt6.QtWidgets",
        "PyQt6.QtCore",
        "PyQt6.QtGui",
        "matplotlib.backends.backend_qtagg",
        "matplotlib.backends.backend_agg",
        "scipy.optimize",
        "scipy.optimize._nnls",
        "scipy.interpolate",
        "scipy.linalg.cython_blas",
        "scipy.linalg.cython_lapack",
        "pandas",
        "numpy",
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=["tkinter", "streamlit"],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="powdR",
    debug=False,
    strip=False,
    upx=True,
    console=False,       # set True to see debug output in a terminal
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,           # path to a .ico file if you have one
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="powdR",
)
