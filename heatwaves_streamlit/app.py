# @Project:  Heatwaves Dashboard w/ Streamlit



import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Heat Waves Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    # df = pd.read_excel(
    #     io="datathon.xlsx",
    #     engine="openpyxl",
    #     sheet_name="Sheet1",
    #     skiprows=3,
    #     usecols="B:R",
    #     nrows=1000,
    # )
    df= pd.read_excel("datathon.xlsx")

    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the Country:",
    options=df["CountryName"].unique(),
    default="Afghanistan"
)


df_selection = df.query(
    "CountryName == @city"
)
df_selection=df_selection[["CountryName","Heatwaves_WMO","Heatwaves_Other"]]

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.

# ---- MAINPAGE ----
st.title(":bar_chart: Heat Waves Dashboard")
st.markdown("##")

st.dataframe(df_selection)



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
