import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def harmonic_oscillator_acceleration(mass, k_constant, amplitude, time):
    # Harmonic oscillator equation for acceleration
    angular_frequency = np.sqrt(k_constant / mass)
    acceleration = -amplitude * (angular_frequency ** 2) * np.cos(angular_frequency * time)

    return acceleration

def main():
    st.title('Harmonic Oscillator Acceleration Calculator and Visualization')

    # Input parameters
    mass = st.number_input('Mass (kg)', min_value=0.1, value=1.0, step=0.1)
    k_constant = st.number_input('Spring Constant (N/m)', min_value=0.1, value=10.0, step=1.0)
    amplitude = st.number_input('Amplitude (m)', min_value=0.1, value=1.0, step=0.1)
    max_time = st.number_input('Max Time (s)', min_value=0.1, value=10.0, step=1.0)

    # Generate time values
    time_values = np.linspace(0, max_time, 1000)

    # Calculate acceleration for each time value
    acceleration_values = harmonic_oscillator_acceleration(mass, k_constant, amplitude, time_values)

    # Display calculated acceleration
    st.write(f'Calculated Acceleration: {acceleration_values[0]:.2f} m/s^2')

    # Plot acceleration
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time_values, acceleration_values, label='Acceleration (m/s^2)')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Acceleration (m/s^2)')
    ax.set_title('Harmonic Oscillator Acceleration')
    ax.grid(True)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
