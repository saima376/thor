import streamlit as st

import d2
import v2
import a2
import e2


def main():
    st.title("Physics App")
    st.write(
        "Welcome to the Amazing World Of PHYSICS.")

    st.header("HARMONIC OSCILLATOR")
    selected_topic = st.selectbox("Choose a topic", ["displacement", "velocity", "acceleration", "energy"])

    if selected_topic == "displacement":
        d2.main()
    elif selected_topic == "velocity":
        v2.main()
    elif selected_topic == "acceleration":
        a2.main()
    elif selected_topic == "energy":
        e2.main()

main()
if __name__ == "_main_":
    main()
