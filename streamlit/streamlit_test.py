import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
import json
from user_query import print_state
import subprocess

# Define functions to be executed based on clicked areas


def function_area1():
    st.write("You clicked on Area 1")
    # Perform actions for Area 1 click


def function_area2():
    st.write("You clicked on Area 2")
    # Perform actions for Area 2 click


def function_area3():
    st.write("You clicked on Area 3")
    # Perform actions for Area 3 click

def in_range_x_y(x, y, leftx, rightx, topy, bottomy):
    if x < leftx:
        return False
    if x > rightx:
        return False
    if y > topy:
        return False
    if y < bottomy:
        return False
    return True

def write_x_y(x, y):
    st.write(x, y)

def your_function(x, y):
    # Your Python logic based on the clicked coordinates
    # Replace this with your actual functionality
    try:
        # Call the "query.py" program and capture its output
        #result = subprocess.check_output(["python3", "user_query.py"], universal_newlines=True)
        result = print_state("Alaska", 2001)
        #result = result.replace('\n', '<br>')
        print(result)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

    return f"Clicked at ({x}, {y})"

def main():
    # Streamlit app starts here
    st.set_page_config(
        page_title="United States Death Statistics \n 1999-2017",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # create columns 
    col1, col2, col3 = st.columns([.2,.6,.2])
    # years slider 
    years_range = col1.select_slider('Select a year:', options=[i for i in range(1999, 2018)])
    display_values_range = col1.slider('Select result range', value=[0,10],
        min_value=0, max_value=10)

    with col2:
        # Display the image
        image = 'map.png'  # Replace 'your_image.jpg' with the path to your image file
        #st.image(image, use_column_width=True)

        # Capture mouse clicks on the image
        value = streamlit_image_coordinates(image, width=700, height=500,
             key='local')

        # get x y cords
        x = value['x']
        y = value['y']

        result = your_function(x, y)
    with col3:
        st.write('Output')
        st.write(x, y)


if __name__ == '__main__':
    main()