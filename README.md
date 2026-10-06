# RF & Antenna Simulation Workshops
### IEEE Techblocks — Antenna Design & Simulation Projects

**Author:** Tanmay Kumar  
**Tools:** Ansys HFSS (Electronics Desktop), Python  

This repository contains my antenna design and electromagnetic simulation projects from the **IEEE Techblocks RF and Antenna Simulation Workshop**.

Each project is organized in its own folder with simulation models, design calculations, and results.

---

## Workshop Projects

| # | Project Name | Operating Frequency | Substrate | Key Results | Folder |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **01** | **5 GHz Inset-Fed Microstrip Patch Antenna** (Capstone) | 5.0 GHz | FR-4 ($\varepsilon_r = 4.4$, $h = 1.6\text{ mm}$) | $S_{11} = -37.52\text{ dB}$, $\text{VSWR} = 1.03$, Gain $= 4.8\text{ dBi}$ | [View Project](./01_5GHz_Microstrip_Patch_Antenna/) |

*(More workshop projects will be added here)*

---

## Featured Project: 5 GHz Inset-Fed Patch Antenna (Capstone)

Full design, 3D modeling, and EM simulation of a 5 GHz rectangular patch antenna with 50-ohm inset feed for Wi-Fi / C-band applications.

* **Resonant Frequency:** 5.00 GHz
* **Return Loss ($S_{11}$):** -37.52 dB
* **VSWR:** 1.03 : 1
* **Peak Realized Gain:** 4.80 dBi
* **-10 dB Bandwidth:** ~300 MHz (4.85 GHz – 5.15 GHz)
* **Input Impedance:** ~50 $\Omega$ matched

For complete design formulas, geometry specifications, and simulation plots, see:  
👉 **[01_5GHz_Microstrip_Patch_Antenna/README.md](./01_5GHz_Microstrip_Patch_Antenna/)**

---

## Repository Structure

```
rf-antenna-workshops/
├── .gitignore
├── README.md                                  # Repository overview
│
└── 01_5GHz_Microstrip_Patch_Antenna/          # Capstone Project
    ├── README.md                              # Detailed design formulas & plots
    ├── models/
    │   └── 5ghz_inset_patch.aedt              # HFSS simulation project
    ├── results/                               # Simulation plots (S11, VSWR, Smith Chart, 3D Gain)
    ├── scripts/
    │   └── calculate_dimensions.py            # Python calculation script
    └── final capstone project/                # Original workshop files
```
