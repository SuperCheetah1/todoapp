import json
import random
import pandas as pd
import streamlit as st

dbfile = "Parking_Lot_Log"

def reserve_spot(name, date, license_plate, choice, spot_number, code):
    d = {
        "Name": name,
        "Date": date.strftime("%Y/%m/%d"),
        "License Plate": license_plate,
        "Choice": choice,
        "Spot Number": spot_number,
        "Code": code
    }
    with open(dbfile, "a") as f:
        json.dump(d, f)
        f.write("\n")

#def verify_info(name, license_plate) :
    
def to_prevent_security_breach() :       
    security_x=random.randint(0,100000)
    security_y=random.randint(0,100000)
    security_z=random.randint(0,100000)

    security_total = security_x + security_y + security_z

    return security_total
def load_data():
    return pd.read_json(dbfile, lines=True)

    
number = to_prevent_security_breach()

st.write("# Parking Lot")
st.write("Enter your spot")

name = st.text_input("Name")
date = st.date_input("Date of Reservation")
license_plate = st.text_input("License Plate")
choice = st.selectbox("Reserve", ("reserve", "free"))
spot_number = st.selectbox("Spot Number", ('1','2','3','4','5','6','7','8','9','10'))
if st.button("Add Reservation"):
    if name == "" or license_plate == "" :
        st.write("You have to fill out all boxes to submit your request.")
    else :
        reserve_spot(name, date, license_plate, choice, spot_number, number)
        st.write("Your number is {0}. Please remember this number to free your spot.".format(number))

df = load_data()
#verify_info()


if len(df) > 0 :
    st.write("## Mark it done")
    st.write("Work in progress.")
    done_task = st.selectbox("Names", df["Name"].values)

    if st.button("Done!"):
        pass


