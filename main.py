import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

def custom_plot(dots, x_axis_location, y_axis_location):
    fig, ax = plt.subplots()

    for dot in dots:
        x, y, radius = dot
        ax.scatter(x, y, s=radius*10)

    ax.axhline(y=y_axis_location, color='gray', linestyle='--')
    ax.axvline(x=x_axis_location, color='gray', linestyle='--')

    ax.spines['left'].set_position(('data', x_axis_location))
    ax.spines['bottom'].set_position(('data', y_axis_location))

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return buffer

st.title('Custom Plot')

dots = []
num_dots = st.slider('Number of Dots', min_value=1, max_value=15, value=1)

for i in range(num_dots):
    col1, col2, col3 = st.columns(3)
    with col1:
        x = st.number_input(f'X {i + 1}', value=0.0)
    with col2:
        y = st.number_input(f'Y {i + 1}', value=0.0)
    with col3:
        radius = st.number_input(f'Radius {i + 1}', value=10.0)
    dots.append((x, y, radius))

x_axis_location = st.slider('X Axis Location', min_value=-10.00, max_value=10.00, value=1.00)
y_axis_location = st.slider('Y Axis Location', min_value=-10.00, max_value=10.00, value=1.00)

buffer = custom_plot(dots, x_axis_location, y_axis_location)
st.image(buffer, use_column_width=True)
