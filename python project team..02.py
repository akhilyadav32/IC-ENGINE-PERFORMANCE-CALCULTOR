import math
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="IC Engine Performance Calculator",
    page_icon="⚙️",
    layout="centered"
)

# --- Functions ---
def brake_power(torque, rpm):
    bp = (2 * math.pi * torque * rpm) / (60 * 1000)
    return bp

def friction_power(ip, bp):
    fp = ip - bp
    return fp

def mechanical_efficiency(bp, ip):
    if ip == 0:
        return 0.0
    efficiency = (bp / ip) * 100
    return efficiency

# --- UI Layout ---
st.title("⚙️ IC Engine Performance Calculator")
st.write("Easily calculate engine performance metrics through an interactive web interface.")

# Sidebar Navigation Menu
menu = [
    "Calculate Brake Power",
    "Calculate Indicated Power",
    "Calculate Friction Power",
    "Calculate Mechanical Efficiency"
]
choice = st.sidebar.selectbox("Select Calculation", menu)

st.divider()

# --- Option 1: Brake Power ---
if choice == "Calculate Brake Power":
    st.subheader("Brake Power (BP) Calculation")
    
    torque = st.number_input("Enter Torque (N-m):", min_value=0.0, value=100.0, step=1.0)
    rpm = st.number_input("Enter Engine Speed (RPM):", min_value=0.0, value=3000.0, step=100.0)

    if st.button("Calculate BP", type="primary"):
        bp = brake_power(torque, rpm)
        st.success(f"*Brake Power =* {round(bp, 2)} kW")

# --- Option 2: Indicated Power ---
elif choice == "Calculate Indicated Power":
    st.subheader("Indicated Power (IP) Entry")
    
    ip = st.number_input("Enter Indicated Power (kW):", min_value=0.0, value=50.0, step=1.0)

    if st.button("Submit IP", type="primary"):
        st.success(f"*Indicated Power =* {round(ip, 2)} kW")

# --- Option 3: Friction Power ---
elif choice == "Calculate Friction Power":
    st.subheader("Friction Power (FP) Calculation")
    
    ip = st.number_input("Enter Indicated Power (kW):", min_value=0.0, value=50.0, step=1.0, key="fp_ip")
    bp = st.number_input("Enter Brake Power (kW):", min_value=0.0, value=40.0, step=1.0, key="fp_bp")

    if st.button("Calculate FP", type="primary"):
        if ip >= bp:
            fp = friction_power(ip, bp)
            st.success(f"*Friction Power =* {round(fp, 2)} kW")
        else:
            st.error("Error: Indicated Power must be greater than or equal to Brake Power.")

# --- Option 4: Mechanical Efficiency ---
elif choice == "Calculate Mechanical Efficiency":
    st.subheader("Mechanical Efficiency Calculation")
    
    ip = st.number_input("Enter Indicated Power (kW):", min_value=0.0, value=50.0, step=1.0, key="eff_ip")
    bp = st.number_input("Enter Brake Power (kW):", min_value=0.0, value=40.0, step=1.0, key="eff_bp")

    if st.button("Calculate Efficiency", type="primary"):
        if ip > 0 and bp >= 0 and bp <= ip:
            efficiency = mechanical_efficiency(bp, ip)
            st.success(f"*Mechanical Efficiency =* {round(efficiency, 2)} %")
        else:
            st.error("Error: Enter valid power values (IP > 0 and BP <= IP).")

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
