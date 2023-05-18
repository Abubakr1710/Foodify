import streamlit as st
import numpy as np
import pandas as pd
import io
st.cache(allow_output_mutation=True)

st.sidebar.image("logo.jpg")
menu = ["Home", "Log in / Sign Up", "Delivery" ,"Personal Information", "Statistics","How it works?", "Contact"]
choice = st.sidebar.selectbox("Revolutionize meal planning, minimize waste.",menu)

if choice == "Home":
    st.markdown("<h1 style='text-align: center;'>Introduction</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Foodify is a cutting-edge web and mobile application that helps you plan your weekly meals while minimizing food waste. By leveraging state-of-the-art technologies such as Machine Learning and Deep Learning, Foodify recommends over 100 dishes from different nations for you to enjoy. But that's not all - with Foodify's delivery option, you can have your weekly meals planned and delivered straight to your door, without having to worry about a thing! Whether you are a busy professional looking to streamline your meal planning process, or simply want to try out new and exciting dishes from around the world, Foodify has you covered. With a user-friendly interface and powerful back-end algorithms, Foodify takes the guesswork out of meal planning and makes it easy and fun to discover new recipes and cuisines. Give Foodify a try today and experience the future of meal planning!</h5>", unsafe_allow_html=True)


elif choice == "Log in / Sign Up":
    logsign = ["Log in", "Sign up"]
    choose = st.selectbox("PLease choose Log in or sign up inorder to get access to your acount", logsign)
    if choose == "Log in":
        form = st.form("my_form")
        form.text_input("Email")
        form.text_input("Username")
        form.text_input("Password")

        # Now add a submit button to the form:
        form.form_submit_button("Submit")
    
    else:
        form = st.form("my_form")
        form.text_input("First Name")
        form.text_input("Last Name")
        form.text_input("Age")
        form.text_input("Gender")
        form.text_input("Email")
        form.text_input("Create Password")

        # Now add a submit button to the form:
        form.form_submit_button("Submit")

elif choice == "Delivery":
    st.markdown("<h1 style='text-align: center;'>Delivery</h1>", unsafe_allow_html=True)

    form = st.form("my_form")
    form.text_input("City")
    form.text_input("Street")
    form.text_input("Apartment number")
    form.text_input("Home number")
    form.form_submit_button("Submit")

    df = pd.DataFrame(
    np.random.randn(1, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.map(df)

elif choice == "Personal Information":
    st.markdown("<h1 style='text-align: center;'>Personal Informations</h1>", unsafe_allow_html=True)
    famset = ['Solo', 'Family']
    fam = st.selectbox('Solo / Family?', famset)
    if fam == 'Solo':
        allergy = st.radio(
        "Do you have allergic simptoms for specific products?",
        ('Yes', 'No'))

        form = st.form("my_form")
        form.multiselect(
        'Please specify products that you have Allergy. Also you can specify products that you will not use.',
        ['Meat', 'Milk', 'Egg', 'Strawberry', 'Fish', 'Onion', 'Apple', 'Orange', 'PineApple'],
        ['Egg', 'Strawberry'])
        form.form_submit_button("Submit")

        st.markdown("<h4 style='text-align: center;'>National Foods</h4>", unsafe_allow_html=True)
        form = st.form("country")
        form.multiselect(
        'Please choose countries that you want to taste their food',
        ['United Kingdom', 'France', 'Spain', 'Germany', 'Poland', 'Italy', 'Russia', 'Turkey', 'Iran', 'Saudi Arabia', 'Uzbekistan', 'China', 'Thailand', 'Malaysia', 'Brazil', 'Argentina'],
        ['Uzbekistan', 'Poland'])
        form.form_submit_button("Submit")
    
    else:
        allergy = st.radio(
        "Does someone have allergic simptoms for specific products?",
        ('Yes', 'No'))

        form = st.form("my_form")
        form.multiselect(
        'Please specify products that you have Allergy. Also you can specify products that you will not use.',
        ['Meat', 'Milk', 'Egg', 'Strawberry', 'Fish', 'Onion', 'Apple', 'Orange', 'PineApple'],
        ['Egg', 'Strawberry'])
        form.form_submit_button("Submit")

        st.markdown("<h4 style='text-align: center;'>National Foods</h4>", unsafe_allow_html=True)
        form = st.form("country")
        form.multiselect(
        'Please choose countries that you want to taste their food',
        ['United Kingdom', 'France', 'Spain', 'Germany', 'Poland', 'Italy', 'Russia', 'Turkey', 'Iran', 'Saudi Arabia', 'Uzbekistan', 'China', 'Thailand', 'Malaysia', 'Brazil', 'Argentina'],
        ['Uzbekistan', 'Poland'])
        form.form_submit_button("Submit")

        form = st.form("Family set")
        form.text_input("How many people you want try")
        form.form_submit_button("Submit")

elif choice == 'Statistics':
    st.markdown("<h1 style='text-align: center;'>Statistics</h1>", unsafe_allow_html=True)

elif choice == 'How it works?':
    st.markdown("<h1 style='text-align: center;'>How it works?</h1>", unsafe_allow_html=True)
    video_file = open('works.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown("<h1 style='text-align: center;'>If you have any questions, Do not hesitate to contact.</h1>", unsafe_allow_html=True)

elif choice == 'Contact':
    st.markdown("<h1 style='text-align: center;'>Contact</h1>", unsafe_allow_html=True)
    form = st.form("contact")
    form.text_input("Leave your message")
    form.text_input("Contact number")
    form.text_input("Email")
    form.radio(
        "How we need to contact",
        ('Phone number', 'Email'))
    form.form_submit_button("Submit")