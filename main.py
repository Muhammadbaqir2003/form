import streamlit as st

st.title("Appointment Request")
name = st.text_input(" Name: ")
Email = st.text_input("Email: ")
Contact = st.text_input("Phone No.: ")
age = st.text_input("Age: ")
gender = st.selectbox("Gender: ", ("Male", "Female"))
Visit = st.selectbox("Is this your first visit here?  ", ("Yes", "No"))
Date = st.text_input("Appointment date: ")
Time = st.selectbox("Time: ", ("9:00 am", "10:00 am", "11:00 am",))
Reason = st.text_input("Please describe the reason for this visit")
# Submit button
submit_button = st.button("Submit")

# Process form submission
if submit_button:
    # Process the form submission here...

    # Show success message
    st.success("Your request has been submitted!")



















