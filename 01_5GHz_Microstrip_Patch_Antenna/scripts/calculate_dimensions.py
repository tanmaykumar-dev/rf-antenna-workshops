import math

# Specifications
f0 = 5.0e9       # Frequency: 5 GHz
er = 4.4         # Substrate: FR-4
h = 1.6e-3       # Substrate thickness: 1.6 mm
c = 3e8          # Speed of light (m/s)

# 1. Patch Width (W)
W = (c / (2 * f0)) * math.sqrt(2 / (er + 1))

# 2. Effective Permittivity (eps_eff)
eps_eff = (er + 1) / 2 + ((er - 1) / 2) * (1 / math.sqrt(1 + 12 * (h / W)))

# 3. Length extension due to fringing fields (Delta L)
num = (eps_eff + 0.3) * (W / h + 0.264)
den = (eps_eff - 0.258) * (W / h + 0.8)
delta_L = 0.412 * h * (num / den)

# 4. Resonant Patch Length (L)
L_eff = c / (2 * f0 * math.sqrt(eps_eff))
L = L_eff - 2 * delta_L

# 5. 50 Ohm Feedline width
Wf = 3.059e-3

# 6. Inset feed depth (y0) & notch gap (g)
# Parametrically swept and optimized in HFSS for 50 Ohm match
y0 = 4.6689e-3
g = 0.5e-3

# 7. Substrate dimensions
Ws = W + 6 * h
Ls = L + 6 * h

print("=== 5 GHz Microstrip Patch Antenna Dimensions ===")
print(f"Patch Width (W)       : {W * 1e3:.4f} mm")
print(f"Patch Length (L)      : {L * 1e3:.4f} mm")
print(f"Effective eps_r       : {eps_eff:.4f}")
print(f"Delta L               : {delta_L * 1e3:.4f} mm")
print(f"50 Ohm Feed Width (Wf): {Wf * 1e3:.4f} mm")
print(f"Inset Depth (y0)      : {y0 * 1e3:.4f} mm")
print(f"Inset Gap (g)         : {g * 1e3:.4f} mm")
print(f"Substrate Width (Ws)  : {Ws * 1e3:.4f} mm")
print(f"Substrate Length (Ls) : {Ls * 1e3:.4f} mm")
