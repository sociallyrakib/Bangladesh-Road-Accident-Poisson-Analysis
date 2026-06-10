import math
#Poisson Distribution - Bangladesh Daily Road Accidents
# Source: Bangladesh Passenger Welfare Association, 2025
# Total accidents in 2025: 6,729 → daily average = 6729/365 ≈ 18

lam=18

def poisson(k, lam):
    return (math.e ** -lam * lam ** k) / math.factorial(k)
    
print("=== Bangladesh Daily Road Accident - Poisson Analysis ===")
print("Data Source: Bangladesh Passenger Welfare Association (2025)")
print("Average accidents per day (lambda):", lam)
print()

for k in range (0,31):
    p=poisson(k,lam)
    print(f"p(exactly {k:2d} accidents)= {p:.4f}")
