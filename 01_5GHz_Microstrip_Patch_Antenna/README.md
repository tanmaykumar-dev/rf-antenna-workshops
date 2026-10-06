# 5 GHz Inset-Fed Microstrip Patch Antenna
### IEEE Techblocks RF and Antenna Simulation — Final Capstone Project

**Author:** Tanmay Kumar  
**Tools:** Ansys HFSS (Electronics Desktop), Python  

---

## Project Overview

Design, modeling, and electromagnetic simulation of a **5.0 GHz rectangular inset-fed microstrip patch antenna** on **FR-4 Epoxy substrate** using **Ansys HFSS**.

The antenna is designed for 5 GHz Wi-Fi (802.11a/n/ac) and C-band communications. An inset feed notch is incorporated into the patch geometry to match the high edge input impedance directly to a 50 $\Omega$ microstrip feedline without requiring an external impedance matching network.

---

## Antenna Structure & Geometry

### Top View (Dimensions in mm)

```
       +-------------------------------------------------------------+
       |<----------------------- Ws (27.86) ------------------------>|
       |                                                             |
       |       +---------------------------------------------+       | ^
       |       |<----------------- W (18.26) --------------->|       | |
       |       |                                             |       | |
       |       |               Radiating Patch               |       | |
       |       |                                             |       | |
       |       |                                             |       | | L (13.66)
       |       |                                             |       | |
       |       |          +-----+           +-----+          |       | |
       |       |    g     |     |    Wf     |     |    g     |       | |
       |       +----------+     |  (3.06)   |     +----------+       | v
       |                  |     |           |     |                  |
       |                  | (g) +-----------+ (g) |  ^               |
       |                  |     |           |     |  | y0 (4.67)     |
       |                  |     |           |     |  v               |
       |                  |     | Feedline  |     |                  |
       |                  +-----+           +-----+                  |
       |                        |<--------->|                        |
       |                        |  Wf=3.06  |                        |
       +-------------------------------------------------------------+
       |<----------------------- Ls (23.26) ------------------------>|
```

### Layer Stackup (Cross-Section)

```
   +-------------------------------------------------------------+  ^ Top Copper (hm = 0.035 mm)
   | [Patch]                  [Feedline]                 [Patch] |  | 
   +=============================================================+  v
   |                                                             |  ^
   |                   FR-4 Dielectric Substrate                 |  | Substrate Height
   |             (er = 4.4, loss tangent tand = 0.02)            |  | (h = 1.6 mm)
   +=============================================================+  v
   |                       Ground Plane                          |  ^ Bottom Copper (hm = 0.035 mm)
   +-------------------------------------------------------------+  v
```

### Dimension Summary Table

| Parameter | Variable | Dimension | Description / Rationale |
| :--- | :---: | :---: | :--- |
| **Operating Frequency** | $f_0$ | **5.0000 GHz** | Center frequency (5 GHz ISM / Wi-Fi band) |
| **Substrate Height** | $h$ | **1.6000 mm** | Standard commercial FR-4 laminate thickness |
| **Copper Thickness** | $h_m$ | **0.0350 mm** | Standard 1 oz copper cladding ($35\ \mu\text{m}$) |
| **Patch Width** | $W$ | **18.2574 mm** | Radiating width calculated from resonant formula |
| **Patch Length** | $L$ | **13.6629 mm** | Resonant length accounting for fringing field extension |
| **Feedline Width** | $W_f$ | **3.0590 mm** | 50 $\Omega$ characteristic impedance microstrip line |
| **Inset Depth** | $y_0$ | **4.6689 mm** | Notch depth tuned in HFSS for 50 $\Omega$ match |
| **Inset Gap** | $g$ | **0.5000 mm** | Gap between microstrip feedline and patch body |
| **Substrate Width** | $W_s$ | **27.8574 mm** | $W + 6h$ (minimizes edge diffraction) |
| **Substrate Length** | $L_s$ | **23.2629 mm** | $L + 6h$ |

---

## Design Formulas & Calculations

### 1. Radiating Patch Width ($W$)
$$W = \frac{c}{2 f_0} \sqrt{\frac{2}{\varepsilon_r + 1}} = 18.2574\text{ mm}$$

### 2. Effective Permittivity ($\varepsilon_{\text{eff}}$)
$$\varepsilon_{\text{eff}} = \frac{\varepsilon_r + 1}{2} + \frac{\varepsilon_r - 1}{2} \left[1 + 12 \left(\frac{h}{W}\right)\right]^{-1/2} = 3.8868$$

### 3. Fringing Length Extension ($\Delta L$)
$$\Delta L = 0.412 h \frac{(\varepsilon_{\text{eff}} + 0.3) \left(\frac{W}{h} + 0.264\right)}{(\varepsilon_{\text{eff}} - 0.258) \left(\frac{W}{h} + 0.8\right)} = 0.7480\text{ mm}$$

### 4. Effective & Physical Patch Length ($L$)
$$L_{\text{eff}} = \frac{c}{2 f_0 \sqrt{\varepsilon_{\text{eff}}}} = 15.2168\text{ mm}$$

$$L = L_{\text{eff}} - 2 \Delta L = 13.6629\text{ mm}$$

### 5. 50 $\Omega$ Microstrip Feedline Width ($W_f$)
$$W_f = 3.0590\text{ mm}$$

### 6. Inset Notch Depth ($y_0$) for 50 $\Omega$ Match
The edge resistance of a rectangular patch ($y = 0$) is typically $200 - 300\ \Omega$. Moving the feed inward reduces the input resistance according to:

$$R_{\text{in}}(y_0) = R_{\text{in}}(0) \cos^2\left(\frac{\pi y_0}{L}\right) = 50\ \Omega \implies y_0 = 4.6689\text{ mm}$$

* **Inset Gap ($g$):** $0.5000\text{ mm}$

### 7. Substrate & Ground Plane Dimensions ($W_s, L_s$)
$$W_s = W + 6 h = 27.8574\text{ mm}$$
$$L_s = L + 6 h = 23.2629\text{ mm}$$

---

## HFSS Simulation Setup

* **Solution Type:** `DrivenModal`
* **Boundary Condition:** Radiation boundary (`Rad1`) assigned to outer faces of an enclosing `AirBox` ($\ge \lambda_0 / 4$ air buffer)
* **Excitation:** 50 $\Omega$ Lumped Port assigned on a vertical sheet (`PortSheet`, $W_f \times h$) with integration line from ground to feedline
* **Adaptive Solution:** Single frequency at $5.0\text{ GHz}$, maximum 20 passes, $\Delta S \le 0.01$ (converged)
* **Frequency Sweep:** Interpolating sweep from $4.0\text{ GHz}$ to $6.0\text{ GHz}$ in steps of $0.01\text{ GHz}$ (201 points)
* **Parametric Optimization:** Inset depth $y_0$ swept from $3.5\text{ mm}$ to $6.0\text{ mm}$ to locate the optimal $50\ \Omega$ match point at $4.6689\text{ mm}$

---

## Simulation Results & Analysis

| Performance Metric | Simulated Value | Target / Specification | Assessment |
| :--- | :---: | :---: | :--- |
| **Resonant Frequency ($f_0$)** | **5.00 GHz** | 5.00 GHz | Exact resonance |
| **Return Loss ($S_{11}$)** | **-37.52 dB** | $< -10.0\text{ dB}$ | Superior ($> 27.5\text{ dB}$ margin) |
| **VSWR** | **1.03 : 1** | $< 2.0\text{ : }1$ | Near-ideal ($> 99.98\%$ power transfer) |
| **Peak Realized Gain** | **+4.80 dBi** | $> 3.5\text{ dBi}$ | Broadside directional pattern |
| **-10 dB Bandwidth** | **~300 MHz** | $> 100\text{ MHz}$ | $4.85\text{ GHz} - 5.15\text{ GHz}$ ($\sim 6\%$) |
| **Input Impedance** | **49.8 + j0.2 $\Omega$** | $50.0 + j0.0\ \Omega$ | Pure resistive match |
| **Front-to-Back Ratio** | **~19.7 dB** | $> 15.0\text{ dB}$ | Back-lobe attenuated to $-14.9\text{ dB}$ |

---

## HFSS Visual Results & Plots

### 1. 3D Model in HFSS
Full-wave model showing the FR-4 substrate (green), copper ground plane and patch with inset notches (orange), lumped excitation port, and radiation air box.

![HFSS 3D Model](results/antenna_3d_geometry.png)

---

### 2. Return Loss ($S_{11}$) vs. Frequency
The reflection coefficient curve displays a deep resonant notch centered exactly at $5.00\text{ GHz}$ reaching $-37.52\text{ dB}$, with a clean $-10\text{ dB}$ bandwidth spanning from $4.85\text{ GHz}$ to $5.15\text{ GHz}$ (~300 MHz).

![Return Loss](results/s11_return_loss.png)

---

### 3. Voltage Standing Wave Ratio (VSWR)
VSWR is $1.03 : 1$ at $5.00\text{ GHz}$ (well below the standard $2.0 : 1$ pass criterion), confirming virtually no reflected power back to the source.

![VSWR](results/vswr_plot.png)

---

### 4. Smith Chart (Input Impedance)
The swept complex reflection coefficient locus loops directly through the center of the Smith chart $(1.0 + j0.0)$, demonstrating a matched input impedance of $49.8 + j0.2\ \Omega$ with negligible reactive parasitics.

![Smith Chart](results/smith_chart.png)

---

### 5. 3D Radiation Pattern & Realized Gain
3D polar radiation plot showing a clean directional broadside main beam directed into the upper hemisphere along $+Z$ ($\theta = 0^\circ$). Peak realized gain reaches $+4.80\text{ dBi}$ with back-lobe levels suppressed to $-14.9\text{ dB}$.

![3D Gain](results/3d_radiation_pattern.png)

---

### 6. HFSS Modeler Perspective
Close-up perspective of the microstrip feedline entering the inset notch cutout on the FR-4 substrate.

![Modeler Perspective](results/hfss_modeler_perspective.png)

---

## Project Files

* `models/5ghz_inset_patch.aedt` - Ansys HFSS project file (complete geometry, mesh, and solved setups)
* `results/` - Exported simulation screenshots and plots
* `scripts/calculate_dimensions.py` - Python script to compute patch parameters from analytical equations
* `final capstone project/` - Original project submission archive
