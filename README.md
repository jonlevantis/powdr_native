# powdR GUI

A native desktop application for quantitative mineralogy from X-ray powder diffraction (XRPD) data, implementing the automated full pattern summation (afps) method of Butler & Hillier (2021).

Built with PyQt6. Available for macOS and Windows.

---

## Download

1. Go to the [**Actions**](../../actions) tab
2. Click the latest **Build powdR** run
3. Scroll to the bottom of the page — under **Artifacts**, download:
   - `powdR-mac` → macOS (Apple Silicon)
   - `powdR-windows` → Windows (64-bit)
4. Unzip the downloaded file and follow the installation steps below

---

## Installation

### macOS

Because powdR is not distributed through the Mac App Store, macOS will block it from opening by default. You only need to do this once.

**Step 1 — Remove the quarantine flag**

Open Terminal and run:
```bash
xattr -cr ~/Downloads/powdR.app
```
If you moved the app somewhere else, replace `~/Downloads/powdR.app` with the actual path.

**Step 2 — Open the app**

Double-click `powdR.app`. If macOS still shows a warning:
- Right-click (or Control-click) `powdR.app`
- Select **Open** from the menu
- Click **Open** in the dialog that appears

You will only need to do this the first time. After that, double-clicking works normally.

**If you see "powdR is damaged and can't be opened"**

This is a Gatekeeper message caused by the quarantine flag not being fully cleared. Run the following in Terminal:
```bash
sudo xattr -rd com.apple.quarantine ~/Downloads/powdR.app
```
Enter your Mac password when prompted, then try opening the app again.

---

### Windows

1. Unzip `powdR-windows.zip`
2. Open the `powdR` folder
3. Double-click `powdR.exe`

**If Windows Defender SmartScreen shows a warning:**
- Click **More info**
- Click **Run anyway**

This warning appears because the app is not code-signed. It is safe to proceed.

---

## Usage

### Input files

The app requires three CSV files. Example files are provided in the `example_inputs/` folder in this repository.

**Reference patterns CSV** — first column is 2θ, remaining columns are phase IDs:
```
tth,   COR,  CAL,  QUA
5.01,  624,  662,  300
5.04,  679,  664,  310
```

**Phases CSV** — phase IDs, names, and Reference Intensity Ratios:
```
phase_id, phase_name, rir
COR,      Corundum,   1.00
CAL,      Calcite,    2.51
QUA,      Quartz,     3.40
```

RIR values can be found at the [RRUFF database](https://rruff.geo.arizona.edu/).

**Sample CSV(s)** — one file per sample, two columns:
```
tth,    counts
5.013,  638
5.039,  653
```

### Running an analysis

1. Upload your reference patterns CSV, phases CSV, and sample CSV(s) using the Browse buttons in the left panel
2. Set your internal standard phase ID (e.g. `COR` for corundum)
3. Adjust algorithm settings if needed — defaults work for most cases
4. Click **▶ Run Analysis**
5. Results appear as tabs — one per sample, plus a batch summary
6. Use **Export summary CSV** to save all results, or **Save plot as PNG** for individual fit plots

---

## Algorithm settings

| Setting | Default | Description |
|---|---|---|
| Std concentration | 0 (sum to 100%) | Known wt-% of internal standard; 0 = phases normalised to 100% |
| Solver | BFGS | Optimisation algorithm |
| Objective | Rwp | Goodness-of-fit metric to minimise |
| Max alignment | 0.2° | Maximum 2θ shift allowed for sample alignment |
| LOD | 0.5 wt-% | Phases below this limit of detection are removed |
| 2θ range | 5–70° | Fitting range |

---

## Reference

Butler, B.M., Hillier, S. (2021) powdR: An R package for quantitative mineralogy using full pattern summation of X-ray powder diffraction data. *Computers and Geosciences*, 147, 104662. https://doi.org/10.1016/j.cageo.2020.104662

---

## For developers

### Building from source

```bash
pip install PyQt6 pandas numpy scipy matplotlib pyinstaller
python app_qt.py        # test before building
pyinstaller powdr_native.spec   # macOS → dist/powdR.app
pyinstaller powdr_windows.spec  # Windows → dist/powdR/powdR.exe
```

### Automated builds

Every push to `main` triggers a GitHub Actions workflow that builds both platforms automatically. Artifacts are retained for 30 days. To trigger a build manually: Actions → Build powdR → Run workflow.

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
├── example_inputs/        # Files for example analysis
└── .github/
    └── workflows/
        └── build.yml      # GitHub Actions CI build
```
