# app.py - Simple Web Interface for Edge-DRS
import streamlit as st
import numpy as np

# --- STEP 1: CREATE THE APP INTERFACE ---
st.title("Edge-DRS: Trajectory Predictor")
st.write("An open-source prototype to test ball-tracking logic using simple mathematics.")

# --- STEP 2: SETUP THE STUMPS BOUNDARY ---
stumps_x = 600
stumps_top_y = 150     # Top boundary of the bails
stumps_bottom_y = 450  # Ground level

# --- STEP 3: CREATING USER SLIDERS FOR DATA POINTS ---
st.write("### Adjust Ball Tracking Points (Y-Coordinates)")
st.write("Simulate how the ball travels forward on the X-axis and drops down on the Y-axis due to gravity.")

y1 = st.slider("Position 1 (X = 50)", 100, 500, 200)
y2 = st.slider("Position 2 (X = 150)", 100, 500, 220)
y3 = st.slider("Position 3 (X = 250)", 100, 500, 250)
y4 = st.slider("Position 4 (X = 350)", 100, 500, 290)

# Pack the sliders directly into our coordinates list
ball_coordinates = [(50, y1), (150, y2), (250, y3), (350, y4)]

# --- STEP 4: TRIGGER MATH AND DECISION ---
if st.button("Run Review Decision"):
    st.write("---")
    st.write("### Decision Engine Diagnostics")
    
    # Separate the coordinates for numpy
    x_points = np.array([pt[0] for pt in ball_coordinates])
    y_points = np.array([pt[1] for pt in ball_coordinates])
    
    # Calculate the 2nd-degree curve (y = ax^2 + bx + c)
    fit_coefficients = np.polyfit(x_points, y_points, 2)
    
    # Predict the Y height when the ball reaches the stumps (X = 600)
    predicted_y_impact = np.polyval(fit_coefficients, stumps_x)
    
    st.write(f"**Current Input Coordinates:** {ball_coordinates}")
    st.write(f"**Predicted Ball Height at Stumps:** {round(predicted_y_impact, 2)} pixels")
    
    # Check if the predicted height falls within the stumps top and bottom
    if predicted_y_impact >= stumps_top_y and predicted_y_impact <= stumps_bottom_y:
        st.error("FINAL VERDICT: OUT (HITTING STUMPS)")
    else:
        st.success("FINAL VERDICT: NOT OUT (MISSING STUMPS)")
