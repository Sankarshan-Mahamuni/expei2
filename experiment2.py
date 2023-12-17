#experiment 2

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

st.title('EXPERIMENT haha haha haha 2')
st.header('Determine dissociation constant Ka of Weak acid (Acetic acid) using pH-meter.')
st.header('Prior Concepts:')
st.write('Concentration of H+ and OH-, pH, pOH, pKa, pKb. Concept of strong and weak acids and bases, Buffers: acidic and basic, dissociation constant (Ka)')
st.header('New Concept:')
st.subheader('Proposition 1: pH metric Titration')
st.write('Study of pH-metric titration of weak acid against strong base using pH-meter without use of any indicators.')

# Display image 1
img_path_1 = "exp2_1.png"
img_1 = Image.open(img_path_1)
st.image(img_1, use_column_width=True)

st.subheader('Proposition 2:')
st.write('Nature of graph depends on the fact that')
st.write('i) Acetic acid being weak acid feebly dissociates and hence up to the stage of complete neutralization pH of system increases very mildly due to formation of buffer CH3COONa + CH3COOH.')

# Display image 2
img_path_2 = "exp2_2.png"
img_2 = Image.open(img_path_2)
st.image(img_2, use_column_width=True)

st.subheader('Proposition 3:')
st.write('Determination of dissociation constant Ka of weak acid (acetic acid) using Henderson’s equation.')

# Display image 3
img_path_3 = "exp2_3.png"
img_3 = Image.open(img_path_3)
st.image(img_3, use_column_width=True)

st.header('Learning Objective:')
st.subheader('Intellectual skills:')
st.write('a) To understand the pH-metry an electro analytical technique to study pH-metric titration.')
st.write('b) To understand theory behind titration between strong base Vs weak acid')
st.write('c) To understand Henderson’s equation and its use in determining Ka i.e. dissociation constant of weak acid.')
st.subheader('Apparatus :')
st.write('pH meter, pH meter electrode, burette, pipette, beaker etc.')
st.subheader('Chemicals')
st.write('Sodium hydroxide, Acetic acid, buffer solution.')
st.subheader('Procedure')


def calculate_ka(pH_at_endpoint):
    # Assuming the initial concentration of weak acid is 0.1 M (adjust as needed)
    initial_concentration_acid = 0.1

    # Calculate dissociation constant (Ka)
    ka = 10 ** (np.array(pH_at_endpoint, dtype=float) - np.log10(initial_concentration_acid))
    return ka

def main():
    st.title("Dissociation Constant (Ka) Determination for Weak Acid (e.g., Acetic Acid)")

    # User input for the number of observations
    num_observations = st.number_input("Enter the number of observations:", min_value=1, step=1)

    # Create an observation table
    observations = {"Sr No": [], "Volume of NaOH added": [], "pH": []}

    # Populate the observation table with user input
    for i in range(1, num_observations + 1):
        observations["Sr No"].append(i)
        volume_naoh = st.number_input(f"{i}. Volume of NaOH added (ml):", min_value=0.0, step=0.1)
        ph_value = st.number_input(f"{i}. pH:", min_value=0.0, step=0.1)
        observations["Volume of NaOH added"].append(volume_naoh)
        observations["pH"].append(ph_value)

   # Calculate Ka using the provided function
       ka_values = calculate_ka(observations["pH"])

# Ensure ka_values is a NumPy array with float dtype
       ka_values = np.asarray(ka_values, dtype=float)

# Display calculated Ka values
      formatted_ka_values = [f"{value:.4f}" for value in ka_values]
      st.write("Calculated Ka values:", formatted_ka_values)


    # Create a DataFrame from the observation table
    df_observations = pd.DataFrame(observations)

    # Display the observation table
    st.dataframe(df_observations)

    # Plot pH vs. Volume graph
    plt.figure(figsize=(8, 6))
    plt.plot(df_observations["Volume of NaOH added"], df_observations["pH"], marker='o')
    plt.title("pH vs. Volume of NaOH Added")
    plt.xlabel("Volume of NaOH added (ml)")
    plt.ylabel("pH")
    st.pyplot(plt)
    st.write('pH = -log(Ka)')

if __name__ == "__main__":
    main()

