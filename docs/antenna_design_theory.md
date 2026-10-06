# Antenna Design Theory & Formulas

## 1. Operating Specifications

* **Center Frequency ($f_0$):** $5.0\text{ GHz}$
* **Substrate Material:** Standard FR-4 Epoxy ($\varepsilon_r = 4.4$, $\tan\delta = 0.02$)
* **Substrate Thickness ($h_s$):** $1.6\text{ mm}$
* **Metallization Thickness ($h_m$):** $0.035\text{ mm}$ ($1\text{ oz}$ Copper, $\sigma = 5.8 \times 10^7\text{ S/m}$)
* **Target Input Impedance ($Z_{\text{in}}$):** $50\ \Omega$

---

## 2. Design Formulas & Values

### 2.1 Radiating Patch Width ($W_p$)
$$W_p = \frac{c}{2 f_0} \sqrt{\frac{2}{\varepsilon_r + 1}} = 18.2574\text{ mm}$$

---

### 2.2 Effective Relative Permittivity ($\varepsilon_{\text{eff}}$)
$$\varepsilon_{\text{eff}} = \frac{\varepsilon_r + 1}{2} + \frac{\varepsilon_r - 1}{2} \left[ 1 + 12 \left(\frac{h_s}{W_p}\right) \right]^{-1/2} = 3.8868$$

---

### 2.3 Fringing Field Extension ($\Delta L$)
$$\Delta L = 0.412 h_s \frac{(\varepsilon_{\text{eff}} + 0.3) \left(\frac{W_p}{h_s} + 0.264\right)}{(\varepsilon_{\text{eff}} - 0.258) \left(\frac{W_p}{h_s} + 0.8\right)} = 0.7480\text{ mm}$$

---

### 2.4 Resonant Patch Length ($L_p$)
$$L_{\text{eff}} = \frac{c}{2 f_0 \sqrt{\varepsilon_{\text{eff}}}} = 15.2168\text{ mm}$$

$$L_p = L_{\text{eff}} - 2 \Delta L = 13.6629\text{ mm}$$

---

## 3. Feedline & Impedance Matching Formulas

### 3.1 50-$\Omega$ Microstrip Feedline Width ($W_f$)
$$W_f = 3.0590\text{ mm}$$

### 3.2 Inset Notch Matching Depth ($y_0$)
$$R_{\text{in}}(y_0) = R_{\text{in}}(0) \cos^2\left(\frac{\pi y_0}{L_p}\right) = 50\ \Omega \implies y_0 = 4.6689\text{ mm}$$

* **Inset Notch Gap ($g$):** $0.5000\text{ mm}$

---

## 4. Substrate & Ground Plane Dimensions

$$W_s = W_p + 6 h_s = 27.8574\text{ mm}$$
$$L_s = L_p + 6 h_s = 23.2629\text{ mm}$$

---

## 5. Performance Summary

| Metric | Target | HFSS Simulated Result | Status |
| :--- | :--- | :--- | :--- |
| **Resonant Frequency ($f_0$)** | $5.000\text{ GHz}$ | $5.000\text{ GHz}$ | Exact Resonance |
| **Return Loss ($S_{11}$)** | $< -10\text{ dB}$ | **$-37.52\text{ dB}$** | Matched ($> 27\text{ dB}$ margin) |
| **VSWR** | $< 2.0$ | **$1.03 : 1$** | Near-unity match |
| **Peak Realized Gain** | $> 3.5\text{ dBi}$ | **$+4.80\text{ dBi}$** | Broadside directional |
| **Input Impedance** | $50.0 + j0\ \Omega$ | $49.8 + j0.2\ \Omega$ | Pure $50\ \Omega$ resistive |
| **$-10\text{ dB}$ Bandwidth** | $> 100\text{ MHz}$ | **$300\text{ MHz}$ (6%)** | $4.85\text{ GHz} - 5.15\text{ GHz}$ |
