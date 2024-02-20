import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def harmonic_oscillator_velocity(mass, k_constant, amplitude, time):
    # Harmonic oscillator equation for velocity
    angular_frequency = np.sqrt(k_constant / mass)
    velocity = -amplitude * angular_frequency * np.sin(angular_frequency * time)
    st.write(' angular_frequency',np.sqrt(k_constant / mass))
    return velocity

def main():
    st.title('Harmonic Oscillator Velocity Calculator')

    # Input parameters
    mass = st.number_input('Mass (kg)', min_value=0.1, value=1.0, step=0.1)
    k_constant = st.number_input('Spring Constant (N/m)', min_value=0.1, value=10.0, step=1.0)
    amplitude = st.number_input('Amplitude (m)', min_value=0.1, value=1.0, step=0.1)
    max_time = st.number_input('Max Time (s)', min_value=0.1, value=10.0, step=1.0)
    angular_frequency = np.sqrt(k_constant / mass)

    # Generate time values
    time_values = np.linspace(0, max_time, 1000)

    # Calculate velocity for each time value
    st.write('velocity', -amplitude * angular_frequency * np.sin(angular_frequency * max_time))
    velocity_values = harmonic_oscillator_velocity(mass, k_constant, amplitude, time_values)

    # Plot velocity
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time_values, velocity_values, label='Velocity (m/s)')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Velocity (m/s)')
    ax.set_title('Harmonic Oscillator Velocity')
    ax.grid(True)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
