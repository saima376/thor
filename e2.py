import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def harmonic_oscillator_kinetic_energy(mass, velocity):
    # Kinetic energy calculation
    kinetic_energy = 0.5 * mass * velocity ** 2
    return kinetic_energy

def harmonic_oscillator_potential_energy(k_constant, displacement):
    # Potential energy calculation
    potential_energy = 0.5 * k_constant * displacement ** 2
    return potential_energy

def main():
    st.title('Harmonic Oscillator Energy Calculator and Visualization')

    # Input parameters
    mass = st.number_input('Mass (kg)', min_value=0.1, value=1.0, step=0.1)
    k_constant = st.number_input('Spring Constant (N/m)', min_value=0.1, value=10.0, step=1.0)
    amplitude = st.number_input('Amplitude (m)', min_value=0.1, value=1.0, step=0.1)
    max_time = st.number_input('Max Time (s)', min_value=0.1, value=10.0, step=1.0)

    # Generate time values
    time_values = np.linspace(0, max_time, 1000)

    # Harmonic oscillator equations
    angular_frequency = np.sqrt(k_constant / mass)
    displacement = amplitude * np.cos(angular_frequency * time_values)
    velocity = -amplitude * angular_frequency * np.sin(angular_frequency * time_values)

    # Calculate kinetic energy
    kinetic_energy_values = harmonic_oscillator_kinetic_energy(mass, velocity)

    # Calculate potential energy
    potential_energy_values = harmonic_oscillator_potential_energy(k_constant, displacement)

    # Plot kinetic energy and potential energy
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time_values, kinetic_energy_values, label='Kinetic Energy (J)')
    ax.plot(time_values, potential_energy_values, label='Potential Energy (J)')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Energy (J)')
    ax.set_title('Harmonic Oscillator Energy')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Calculate and display final kinetic energy and potential energy
    final_kinetic_energy = kinetic_energy_values[-1]
    final_potential_energy = potential_energy_values[-1]

    st.write(f'Final Kinetic Energy: {final_kinetic_energy:.2f} J')
    st.write(f'Final Potential Energy: {final_potential_energy:.2f} J')

if __name__ == "__main__":
    main()
