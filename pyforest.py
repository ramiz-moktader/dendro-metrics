import streamlit as st
import pandas as pd

def calculate_biomass(data, height_col, dbh_col, wd_col):
    # Calculate aboveground biomass (AGB)
    agb = 0.0673 * (data[height_col] * data[dbh_col] ** 2 * data[wd_col]) ** 0.976
    
    # Calculate belowground biomass (BGB)
    bgb = agb * 0.15
    
    # Calculate total biomass
    total_biomass = agb + bgb
    
    # Add biomass columns to the DataFrame
    data['AGB'] = agb
    data['BGB'] = bgb
    data["Total Biomass"] = total_biomass
    
    return data

def main():
    st.title('Biomass Calculator')

    # Upload file
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

    if uploaded_file is not None:
        data = pd.read_excel(uploaded_file)
        st.write("## Data Preview")
        st.write(data.head())

        # Select columns
        height_col = st.selectbox("Select height column", options=data.columns)
        dbh_col = st.selectbox("Select DBH column", options=data.columns)
        wd_col = st.selectbox("Select wood density column", options=data.columns)

        # Calculate biomass
        if st.button("Calculate Biomass"):
            data = calculate_biomass(data, height_col, dbh_col, wd_col)
            st.write("## Updated Data with Biomass Calculations")
            st.write(data[[height_col, dbh_col, wd_col, 'AGB', 'BGB', 'Total Biomass']])

if __name__ == "__main__":
    main()
