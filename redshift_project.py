import numpy as np
import matplotlib.pyplot as plt

# Hubble constant (km/s/Mpc)
H0 = 70

def hubble_velocity(distance):
    return H0 * distance

def main():
    # Generate distances
    distances = np.linspace(0, 500, 100)
    velocities = hubble_velocity(distances)

    # Plot
    plt.figure()
    plt.plot(distances, velocities)
    plt.xlabel("Distance (Mpc)")
    plt.ylabel("Velocity (km/s)")
    plt.title("Hubble's Law: Cosmic Expansion")
    plt.grid()

    plt.show()

if __name__ == "__main__":
    main()
