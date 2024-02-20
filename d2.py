import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def harmonic_oscillator_displacement(mass, k_constant, amplitude, time):
    # Harmonic oscillator equation for displacement
    angular_frequency = np.sqrt(k_constant / mass)
    displacement = amplitude * np.cos(angular_frequency * time)
    st.write('angular_frequency',np.sqrt(k_constant / mass))
    return displacement
def main():
    st.title('Harmonic Oscillator Displacement Calculator')
    # Input parameters
    mass = st.number_input('Mass (kg)', min_value=0.1, value=1.0, step=0.1)
    k_constant = st.number_input('Spring Constant (N/m)', min_value=0.1, value=10.0, step=1.0)
    amplitude = st.number_input('Amplitude (m)', min_value=0.1, value=1.0, step=0.1)
    max_time = st.number_input('Max Time (s)', min_value=0.1, value=10.0, step=1.0)
    angular_frequency = np.sqrt(k_constant / mass)

    time_values = np.linspace(0, max_time, 1000)
    displacement = harmonic_oscillator_displacement(mass, k_constant, amplitude, time_values)
    st.write('displacement', amplitude * np.cos(angular_frequency * max_time))

    # Plotting displacement
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time_values, displacement, label='Displacement (m)')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Displacement (m)')
    ax.set_title('Harmonic Oscillator Displacement')
    ax.grid(True)
    st.pyplot(fig)


if __name__ == "__main__":
    main()
