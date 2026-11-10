from scipy.stats import norm 
from scipy.integrate import quad 

ϕ = norm()

value, error = quad(ϕ.pdf, -2, 2) # assings the integral of ϕ(z)dz with upper 2 and lower -2 
print(value, error) 