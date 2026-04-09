# powdR Native GUI

A native desktop app for XRPD quantitative analysis (afps/fps),
implementing Butler & Hillier 2021. Built with PyQt6.

---

## Getting builds

### Option A — GitHub Actions (recommended, no Windows machine needed)

Every push to `main` automatically builds both a `.app` (Mac) and `.exe` (Windows).

1. Push this folder to a GitHub repository
2. Go to **Actions** tab → select the latest **Build powdR** run
3. Scroll to **Artifacts** at the bottom → download `powdR-mac` or `powdR-windows`

You can also trigger a build manually: Actions → Build powdR → Run workflow.

### Option B — Build locally on macOS

```bash
pip install PyQt6 pandas numpy scipy matplotlib pyinstaller
python app_qt.py          # test first
pyinstaller powdr_native.spec
# output: dist/powdR.app
```

**First launch (Gatekeeper):** right-click → Open → Open, or:
```bash
xattr -cr dist/powdR.app
```

### Option C — Build locally on Windows

```bash
pip install PyQt6 pandas numpy scipy matplotlib pyinstaller
python app_qt.py          # test first
pyinstaller powdr_windows.spec
# output: dist\powdR\powdR.exe
```

---

## Setting up the GitHub repo (first time)

```bash
cd powdr_native
git init
git add .
git commit -m "Initial commit"
# Create a new repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/powdr.git
git push -u origin main
```

That's it — the Actions workflow fires automatically on push.

---

## File structure

```
powdr_native/
├── app_qt.py              # Main GUI application
├── afps.py                # afps() analysis core
├── fitting.py             # Numerical fitting routines
├── preprocessing.py       # Data harmonisation & alignment
├── plotting.py            # Plot utilities
├── powdr_native.spec      # PyInstaller spec — macOS
├── powdr_windows.spec     # PyInstaller spec — Windows
└── .github/
    └── workflows/
        └── build.yml      # GitHub Actions CI build
```

---

## Input file formats

**Reference patterns CSV** — first column 2θ, rest are phase IDs:
```
tth,   COR,  CAL
5.01,  624,  662
5.04,  679,  664
```

**Phases CSV:**
```
phase_id, phase_name, rir
COR,      Corundum,   1.00
CAL,      Calcite,    2.51
```

**Sample CSV:**
```
tth,    counts
5.013,  638
5.039,  653
```
