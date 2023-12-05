import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
import json

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

# Streamlit app starts here
st.title('Clickable Image App')

# Display the image
image = 'map.jpg'  # Replace 'your_image.jpg' with the path to your image file
#st.image(image, use_column_width=True)

# Capture mouse clicks on the image
value = streamlit_image_coordinates(image, width=800)

# get x y cords
x = value['x']
y = value['y']

write_x_y(x, y)

if in_range_x_y(x, y, 140,180,140,180):
    function_area1()

