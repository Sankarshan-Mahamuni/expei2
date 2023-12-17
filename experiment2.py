#experiment 2

import streamlit as st
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

st.title('EXPERIMENT haha haha haha 2')
st.header('Determine dissociation constant Ka of Weak acid (Acetic acid) using pH-meter.')
st.header('Prior Concepts:')
st.write('Concentration of H+ and OH-, pH, pOH, pKa, pKb. Concept of strong andweak acids and bases, Buffers: acidic and basic, dissociation constant (Ka)')
st.header('New Concept:')
st.subheader('Proposition 1: pH metric Titration')
st.write('Study of pH-metric titration of weak acid against strong base using pH-meter without use of any indicators.')

# Option 1: Provide the path to the image file
#image_path = r"C:\Users\Arpita\OneDrive\Pictures\Screenshots\Screenshot 2023-11-19 202426.png"
#st.image(image_path,use_column_width=True)
import streamlit as st
from PIL import Image

# Open an image file
img_path = "exp2_1.png"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)

st.subheader('Proposition 2:')
st.write('Nature of graph depends on the fact that')
st.write('i) Acetic acid being weak acid feebly dissociates and hence up to the stage of complete neutralization pH of system increases very mildly due to formation of buffer CH3COONa + CH3COOH.')


    # Option 1: Provide the path to the image file
#image_path =r"C:\Users\Arpita\OneDrive\Pictures\Screenshots\Screenshot 2023-11-19 203238.png"
#st.image(image_path, use_column_width=True)
import streamlit as st
from PIL import Image

# Open an image file
img_path = "exp2_2.png"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)

st.subheader('Proposition 3:')
st.write('Determination of dissociation constant Ka of weak acid (acetic acid) using Henderson’s equation.')


    # Option 1: Provide the path to the image file
#image_path = r"C:\Users\Arpita\OneDrive\Pictures\Screenshots\Screenshot 2023-11-19 204820.png"
#st.image(image_path, use_column_width=True)
import streamlit as st
from PIL import Image

# Open an image file
img_path = "exp2_3.png"
img = Image.open(img_path)

# Display the image using Streamlit
st.image(img,  use_column_width=True)

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
    ka = 10 ** (np.array(pH_at_endpoint) - np.log10(initial_concentration_acid))
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

    # Now you can use the ka_values as needed
    st.write("Calculated Ka values:", ka_values)


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


    # Calculate dissociation constant (Ka) based on user input
    #end_point_index = st.number_input("Enter the observation index at the end point of titration:", min_value=1, step=1)
    #pH_at_end_point = df_observations.at[end_point_index - 1, "pH"] if "pH" in df_observations.columns else None
    #st.write('pH = -log(Ka)')

    # Display the result
    #st.header("Result:")
    #st.write("1. End Point of Titration:", df_observations.at[end_point_index - 1, "Volume of NaOH added"], "ml")
    #st.write("2. pH at End Point:", pH_at_end_point)
    #if pH_at_end_point is not None:
        #dissociation_constant = calculate_ka(pH_at_end_point)
        #st.write("3. Dissociation Constant of Weak Acid (Ka):", dissociation_constant)

if __name__ == "__main__":
    main()
