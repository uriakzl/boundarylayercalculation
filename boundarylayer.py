# Simple boundary layer thickness calculator for cobalt and nickel
# Assumes laminar flow in a rectangular channel

# === Parameters ===
mu = 0.001               # Dynamic viscosity of water (Pa·s)
rho = 1000               # Density of water (kg/m³)

# Geometry
gasket_height_in = 1/32  # Gasket height (inches)
h = gasket_height_in * 0.0254   # Gasket height (m)
l = 0.03                        # Channel width (m)
L = 0.1                         # Channel length (m)

# Flow
flow_rate_ml_min = 10          # Flow rate (mL/min)

# Diffusivity values (m²/s)
D_cobalt = 0.72e-9
D_nickel = 0.69e-9

# === Calculations ===

# Convert flow rate to m³/s
flow_rate_m3_s = flow_rate_ml_min / 1e6 / 60

# Cross-sectional area (m²) and velocity (m/s)
cross_section_area = l * h
u = flow_rate_m3_s / cross_section_area

# Hydraulic diameter (m)
perimeter = 2 * (l + h)
dH = 4 * cross_section_area / perimeter

# Reynolds number (dimensionless)
Re = (rho * u * dH) / mu
print(f"Reynolds number: {Re:.2f}")
if Re > 2000:
    print("Reynolds number exceeds 2000, flow may not be laminar.")

# Schmidt numbers (dimensionless)
Sc_cobalt = mu / (rho * D_cobalt)
Sc_nickel = mu / (rho * D_nickel)

# Boundary layer thicknesses (m)
Sh_cobalt = 1.85 * ((Re * Sc_cobalt * dH / L) ** (1/3))
Sh_nickel = 1.85 * ((Re * Sc_nickel * dH / L) ** (1/3))

boundary_layer_cobalt = dH / Sh_cobalt
boundary_layer_nickel = dH / Sh_nickel

# === Output ===
print(f"Boundary layer thickness (Co²⁺): {boundary_layer_cobalt:.9f} m")
print(f"Boundary layer thickness (Ni²⁺): {boundary_layer_nickel:.9f} m")

# Percent of a reference thickness (1/64 inch = 0.0015875 m)
ref_thickness = 0.0015875
print(f"Co²⁺ layer as % of 1/64 inch: {boundary_layer_cobalt / ref_thickness * 100:.2f}%")
print(f"Ni²⁺ layer as % of 1/64 inch: {boundary_layer_nickel / ref_thickness * 100:.2f}%")

# Optional: print Schmidt numbers
print(f"Schmidt number (Co²⁺): {Sc_cobalt:.2f}")
print(f"Schmidt number (Ni²⁺): {Sc_nickel:.2f}")
