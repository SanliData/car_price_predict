import streamlit as st
import pandas as pd

def main():
    # Title
    st.title("CarPricePred")

    #Header
    st.header("Arabanizin tahmini fiyati")

    #sub header
    st.subheader("Arabanizin değerini öğrenin")

    # Description
    st.write("This is a simple Streamlit app to demonstrate how to display a sample dataset.")

    # Load sample dataset
    df = load_data()

    # Display the dataset
    st.write("CarPricePred")
    st.write(df)

def load_data():
    # Sample dataset (can be replaced with your own dataset)
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 30, 35, 40, 45],
        'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    main()
