# Ansys HFSS Simulation Setup & Reproduction Guide

This guide walks through reproducing and inspecting the 5 GHz Inset-Fed Microstrip Patch Antenna model in **Ansys Electronics Desktop (HFSS)**.

---

## 1. Opening the Model

1. Launch **Ansys Electronics Desktop** (version 2018.2 or newer).
2. Go to **File** $\rightarrow$ **Open...**
3. Select `models/5ghz_inset_patch.aedt` (or `final capstone project/5ghz.aedt`).
4. In the Project Manager tree, expand `Patch_5GHz_Perfect` $\rightarrow$ `InsetPatch (DrivenModal)`.

---

## 2. Geometry Setup & Variables

The 3D model is fully parameterized. You can inspect or modify the parameters by clicking **HFSS** $\rightarrow$ **Design Properties**:

| Variable Name | Value | Description |
| :--- | :--- | :--- |
| `h_s` | `1.6mm` | Substrate height / thickness |
| `h_m` | `0.035mm` | Copper metallization thickness ($1\text{ oz}$ standard) |
| `w_p` | `18.2574mm` | Patch width |
| `l_p` | `13.6629mm` | Patch resonant length |
| `w_f` | `3.059mm` | $50\ \Omega$ microstrip feedline width |
| `y_0` | `4.6689mm` | Inset notch depth (tuned for minimum reflection) |
| `g` | `0.5mm` | Inset gap spacing between patch and feed |
| `w_s` | `w_p + 6*h_s` | Substrate width ($27.8574\text{ mm}$) |
| `l_s` | `l_p + 6*h_s` | Substrate length ($23.2629\text{ mm}$) |

---

## 3. Boundary Conditions & Excitations

### Radiation Boundary (`Rad1`)
* **Geometry:** Rectangular air enclosure (`AirBox`) surrounding the antenna structure with $\ge \lambda_0 / 4$ clearance in radiating directions.
* **Type:** `Radiation` boundary assigned to outer faces of `AirBox`.

### Excitation Port (`PortSheet`)
* **Geometry:** 2D rectangle (`w_f` $\times$ `h_s`) placed at the substrate edge between the feedline strip and the ground plane.
* **Type:** `Lumped Port` with a characteristic reference impedance of $50\ \Omega$.
* **Integration Line:** Defined vertically from the Ground plane edge $(Z = -h_s)$ pointing towards the feedline $(Z = 0)$.

---

## 4. Analysis & Adaptive Mesh Setup

* **Solution Type:** `DrivenModal`
* **Adaptive Solution Frequency:** $5.0\text{ GHz}$
* **Maximum Number of Passes:** 20
* **Maximum Delta S:** `0.01` ($1\%$)
* **Refinement per pass:** $30\%$

### Frequency Sweep Configuration
* **Sweep Name:** `Sweep`
* **Type:** `Interpolating`
* **Frequency Range:** $4.0\text{ GHz}$ to $6.0\text{ GHz}$
* **Step Size:** $0.01\text{ GHz}$ ($10\text{ MHz}$, 201 solution points)

---

## 5. Optimetrics Parametric Sweep

To find the optimal inset feed depth $y_0$:
1. Check **Optimetrics** $\rightarrow$ `ParametricSetup1`.
2. Variable swept: `y_0` from $3.5\text{ mm}$ to $6.0\text{ mm}$ with a step of $0.5\text{ mm}$.
3. Observe the input impedance and $S_{11}$ curve shifting across sweeps. The optimum resonance occurs at $y_0 = 4.6689\text{ mm}$.

---

## 6. Accessing Results & Plots

Under the **Results** branch in the Project Manager tree:
1. **S11**: Rectangular plot displaying $\text{dB}(S(1,1))$ vs Frequency.
2. **VSWR**: Rectangular plot displaying $\text{VSWR}(1)$ vs Frequency.
3. **Smith Chart**: Complex reflection coefficient showing impedance locus centered at $(1.0, 0)$.
4. **Gain 3D**: 3D polar radiation plot showing total realized gain.
5. **Gain E-H planes**: 2D Cartesian/Polar cuts for $\phi = 0^\circ$ (E-plane) and $\phi = 90^\circ$ (H-plane).
