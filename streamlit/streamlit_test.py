import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
import json
import subprocess
import pandas as pd

# local 
from find_cords import build_state_with_cords
from user_query import print_state, print_state2

# global vars
global_state = "Ohio"


def your_function(x, y):
    # Your Python logic based on the clicked coordinates
    # Replace this with your actual functionality
    try:
        # Call the "query.py" program and capture its output
        # result = subprocess.check_output(["python3", "user_query.py"], universal_newlines=True)
        result = print_state("Alaska", 2001)
        # result = result.replace('\n', '<br>')
        print(result)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

    return f"Clicked at ({x}, {y})"

def call_state(x, y, year):
    global global_state
    states_with_cords = build_state_with_cords()
    for st, cord_tup in states_with_cords.items():
        p1, p2 = cord_tup
        if x >= p1[0] and x <= p2[0]:
            if y >= p1[1] and y <= p2[1]:
                state = st
                global_state = st
        else:
            state = global_state

    try:
        result = print_state2(state, year)
        #result_and_coordinates = f"Clicked at ({x}, {y})\n" + result
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


def main():
    # Streamlit app starts here
    st.set_page_config(
        page_title="United States Death Statistics \n 1999-2017",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # header of the page
    st.header("United States Death Statistics \n 1999-2017")

    # create columns
    col1, col2 = st.columns([.75, .25])
    
    # sidebar things
    st.sidebar.title("Settings")
    # years slider
    year = st.sidebar.select_slider('Select a year:', options=[
                                    i for i in range(1999, 2018)])
    display_values_range = st.sidebar.slider('Select result range', value=[0, 10],
                                    min_value=0, max_value=10)
        
    with col1:
        # Display the image
        image = 'map.png'  # Replace 'your_image.jpg' with the path to your image file
        # st.image(image, use_column_width=True)

        # Capture mouse clicks on the image
        value = streamlit_image_coordinates(image, width=800,
                                            key='local')

        # get x y cords
        x = value['x']
        y = value['y']

        result, result_dict = call_state(x, y, year)
        df = pd.DataFrame.from_dict(result_dict, orient='index')
        st.bar_chart(df)

    with col2:
        st.write('Output')
        st.write(x, y)
        for r in result:
            st.write(r)
        


if __name__ == '__main__':
    main()
