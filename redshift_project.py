def recession_velocity(distance, H0=70):
    return H0 * distance

print("Astroparticle Mini Project")

distance = float(input("Enter galaxy distance (Mpc): "))
velocity = recession_velocity(distance)

print(f"Recession velocity: {velocity} km/s")
