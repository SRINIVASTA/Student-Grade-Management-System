import streamlit as st
import subprocess
import pandas as pd
from io import StringIO

st.set_page_config(layout="centered")
st.title("📊 C-Engine Student Dashboard")
st.write("This app runs compiled C code natively on the server and displays the processed data.")

if st.button("Fetch and Process Data via C", type="primary"):
    with st.spinner("Compiling and executing C backend..."):
        try:
            # 1. Compile the C code into a Linux binary
            subprocess.run(["gcc", "project.c", "-o", "backend"], check=True)
            
            # 2. Run the binary and capture stdout
            result = subprocess.run(["./backend"], capture_output=True, text=True, check=True)
            
            # 3. Read the CSV output from C directly into Pandas
            csv_data = StringIO(result.stdout)
            df = pd.read_csv(csv_data)
            
            # 4. Display results in Streamlit UI
            st.success("Data processed successfully by C logic!")
            st.dataframe(df, use_container_width=True)
            
            # Show a metric generated from data
            highest_avg = df["Average"].max()
            st.metric(label="Highest Class Average", value=f"{highest_avg}%")
            
        except subprocess.CalledProcessError as e:
            st.error(f"Execution failed. Error: {e}")
