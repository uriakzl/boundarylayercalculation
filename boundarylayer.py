#simple code to solve for boundary layer 
#no inputs, keep it as simple as possible

#mew is the viscosity of water in SI units
mew = 0.001 # viscosity of water in Pa.s (SI units)

#rho is the density of water in SI units
rho = 1000 # density of water in kg/m^3 (SI units)

#u is the liquid velocity
u = 1.0 # velocity of water in m/s (SI units)

#dH is the hydraulic diameter
h = 0.00079375 #in meters
l = 0.03 #in meters
perimeter = 2*(l+h)
xarea = l * h
dH = (4 * xarea)/perimeter

#calculate reynolds number, ensure it is below 2000 to ensure laminar flow
Re = (rho * u * dH) / mew 
print(f"Reynolds number: {Re:.2f}")
if Re > 2000:
    print("Reynolds number is above 2000, flow is not laminar.")

#calculate Schmidt number
#diffusivity of cobalt in water
D_cobalt = 0.72 * 10**-9 # diffusivity in m^2/s

#diffusivity of nickel in water
D_nickel = 0.69 * 10**-9 # diffusivity in m^2/s

Sc_cobalt = mew / (rho * D_cobalt) # Schmidt number for cobalt
Sc_nickel = mew / (rho * D_nickel) # Schmidt number for nickel

#solving for boundary layer thickness
# Sh = 1.85 * (Re**(1/3)) * (Sc_cobalt**(1/3)) # Sherwood number for cobalt
L = 0.1 #in meters length of the channel
boundary_l_t_cobalt = dH/(1.85 * ((Re*Sc_cobalt *dH/L)**(1/3))) 
boundary_l_t_nickel = dH/(1.85 * ((Re*Sc_nickel *dH/L)**(1/3)))

print(f"Boundary layer thickness for cobalt: {boundary_l_t_cobalt:.9f} m")
print(f"Boundary layer thickness for nickel: {boundary_l_t_nickel:.9f} m")
# Note: The above code assumes that the user has a basic understanding of fluid dynamics and the relevant equations.



