# This program is an implementation of De Moivre's theorem
# De Moivre's theorem:
# r(cos θ + i sin θ)^n = r^n (cos nθ + i sin nθ)

import cmath

def de_moivres_theorem(r, theta, n):
    # Convert polar coordinates to rectangular coordinates
    z = cmath.rect(r, theta)
    # Apply De Moivre's theorem
    result = z ** n
    return result

def main():
    r = float(input("Enter the modulus (r): "))
    theta = float(input("Enter the argument (θ) in radians: "))
    n = int(input("Enter the exponent (n): "))
    result = de_moivres_theorem(r, theta, n)
    print("The result of the complex number calculation is:", result)

if __name__ == "__main__":
    main()