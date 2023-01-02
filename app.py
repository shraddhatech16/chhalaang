
# import time  # to simulate a real time data, time loop
# import numpy as np  # np mean, np random
# import pandas as pd  # read csv, df manipulation
# # import plotly.express as px  # interactive charts
# import streamlit as st  # 🎈 data web app development
# st.title("""Loan prediction System""")
# df= pd.read_csv("survey.csv")
# # df['status']
# # df=csv_reader['status']
# st.line_chart(df)
# st.set_page_config(
#     page_title="Real-Time Data Science Dashboard",
#     page_icon="✅",
#     layout="wide",
# )

# # read csv from a github repo
# dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

# # read csv from a URL
# @st.experimental_memo
# def get_data() -> pd.DataFrame:
#     return pd.read_csv(dataset_url)

# df = get_data()

# # dashboard title
# st.title("Real-Time / Live Data Science Dashboard")

# # top-level filters
# job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

# # creating a single-element container
# placeholder = st.empty()

# # dataframe filter
# df = df[df["job"] == job_filter]

# # near real-time / live feed simulation
# for seconds in range(200):

#     df["age_new"] = df["age"] * np.random.choice(range(1, 5))
#     df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

#     # creating KPIs
#     avg_age = np.mean(df["age_new"])

#     count_married = int(
#         df[(df["marital"] == "married")]["marital"].count()
#         + np.random.choice(range(1, 30))
#     )

#     balance = np.mean(df["balance_new"])

#     with placeholder.container():

#         # create three columns
#         kpi1, kpi2, kpi3 = st.columns(3)

#         # fill in those three columns with respective metrics or KPIs
#         kpi1.metric(
#             label="Age ⏳",
#             value=round(avg_age),
#             delta=round(avg_age) - 10,
#         )
        
#         kpi2.metric(
#             label="Married Count 💍",
#             value=int(count_married),
#             delta=-10 + count_married,
#         )
        
#         kpi3.metric(
#             label="A/C Balance ＄",
#             value=f"$ {round(balance,2)} ",
#             delta=-round(balance / count_married) * 100,
#         )

#         # create two columns for charts
#         fig_col1, fig_col2 = st.columns(2)
#         with fig_col1:
#             st.markdown("### First Chart")
#             fig = px.density_heatmap(
#                 data_frame=df, y="age_new", x="marital"
#             )
#             st.write(fig)
            
#         with fig_col2:
#             st.markdown("### Second Chart")
#             fig2 = px.histogram(data_frame=df, x="age_new")
#             st.write(fig2)

#         st.markdown("### Detailed Data View")
#         st.dataframe(df)
#         time.sleep(1)
from pathlib import WindowsPath
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# # Basic Page Configurations to to make GUI a little better
st.set_page_config(page_title="Loan Prediction",
                   page_icon=":bar_chart:",
                   layout="wide")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style> """, unsafe_allow_html=True)


# adding dark theme to the plt plots to match overall GUI
plt.style.use("dark_background")

# Adding Header
st.header("Loan prediction")

# Adding Side bar along with width and height field for some plots

st.sidebar.write(
    "Use These sliders to change height and width of 2nd and last plots")
width = st.sidebar.slider("Width", min_value=6, max_value=20, value=10)
height = st.sidebar.slider("Height", min_value=1, max_value=10, value=3)


# Loading data and removing null values
data = pd.read_csv("./survey.csv")
data = data.dropna()  # dropping null values


# # 1 Some Basic information about data like total number of entries
c0, c1, c2, c3 = st.columns(4)  # creating 4 containers for metrics
c0.metric("Satisfied users", len(data))
c1.metric("Edlevel", len(data['EdLevel'].unique()))
c2.metric("Employment", len(data['Employment'].unique()))
c3.metric("Status", len(data['Status'].unique()))

# # 2 Checkbox to show dataset
if st.checkbox("Show Data"):
    st.write(data)


# # 3 Total data data distribution according to Platform or Genre accornding to the selection
op = st.selectbox("Select one of the following", ["Platform", "Genre"])
st.subheader(op + " wise data distribution")
st.bar_chart(data[op].value_counts(), height=400, use_container_width=True)


# # 4  Videogames Sales Data by years
# figsize is used to change the width and height of plots
fig, ax = plt.subplots(figsize=(width, height))
st.subheader("Salesdata by Year")
op1 = st.multiselect(
    "Select Sales Category", ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"], default="Global_Sales")
group1 = data.groupby('Year').sum()  # Grouping the data by Years
ax.plot(group1[op1], label=op1)
ax.set_xlabel("Years")
ax.set_ylabel("Sales in Million")
ax.legend()
st.pyplot(fig)


# # 5 PieCharts of various SalesData record
left, right = st.columns(2)  # creating 2 container/columns for Piecharts

# # 5.1 PieChart of Salesdata by region
left.subheader("SalesData by Region")
lst = []
plt.figure(2)  # assigning figure number to plot for using in later
for i in data.columns[6:-1]:
    # Calculting total sales data of region and appending it into list
    lst.append(sum(data[i]))

mylabels = data.columns[6:-1]
plt.pie(lst, labels=mylabels, autopct='%1.1f%%')
plt.legend()
plt.tight_layout()
left.pyplot(plt.figure(2))

# # 5.2 Piechart of Salesdata by Genre
right.subheader("Salesdata by Genre")
plt.figure(3)
group1 = data.groupby('Genre').sum()  # Grouping data by Genre
mlabels = data["Genre"].unique()
plt.pie(group1["Global_Sales"], labels=mlabels, autopct='%1.1f%%')
plt.legend()
plt.tight_layout()
right.pyplot(plt.figure(3))

# # 6 Genre wise Average Sales
st.subheader("Genre wise average Sales")
cols = list(data.columns[6:])
op3 = st.multiselect(
    "Select Region ", data.columns[6:], default=cols)
# Grouping data by Genre by using method of mean
result = data.groupby(['Genre']).mean()
st.bar_chart(result[op3], height=350, use_container_width=True)


# # 7 Top 10 Stats in Tables
st.subheader("Loan prediction")
left, right = st.columns(2)

# 7.1 Top 10 Games by Platform
platform = sorted(data['Platform'].unique())
p = left.selectbox("Select platform", platform)
left.subheader("Yes/No ")
# Making new dataframe with Platform equal to required platform
df = data.query("Platform == @p")
# Sorting the dataframe in decending order on GlobalSales
df = df.sort_values(by=['Global_Sales'], ascending=False)
df = df.iloc[:10]
df = df[['Name', 'Global_Sales']]
left.table(df)

# 7.2 Top 10 Games by Genre
genre = sorted(data['Genre'].unique())
g = right.selectbox("Select genre", genre, index=6)
right.subheader("Top 10 Highest Grossing Games by genre")
# making new dataframe with Genre equal to required genre
df01 = data.query("Genre == @g")
# sorting in decending order on GLobalSales
df01 = df01.sort_values(by=['Global_Sales'], ascending=False)
df01 = df01.iloc[:10]
df01 = df01[['Name', 'Global_Sales']]
right.table(df01)

# # 8 Comparing Sales Data of 2 PUblishers
st.subheader("Comparing Salesdata of two Publishers")
publisher = sorted(data['Publisher'].unique())
left, right = st.columns(2)
# selecting two publishers
c1 = left.selectbox("Select 1st Publisher", publisher, index=21)
c2 = right.selectbox("Select 2nd Publisher", publisher, index=359)

# creating dataframes of 2 selected publishers
df1 = data.query("Publisher == @c1")
df2 = data.query("Publisher == @c2")

# Grouping the data by years
group1 = df1.groupby("Year").sum()
group2 = df2.groupby("Year").sum()

# Now Plotting
fig, ax = plt.subplots(figsize=(width, height))

ax.bar(group1.index-0.2, group1['Global_Sales'], 0.4, label=c1, color="Red")
ax.bar(group2.index+0.2, group2['Global_Sales'],
       0.4, label=c2, color="orange")
ax.set_xlabel("Year")
ax.set_ylabel("Total Global Sales")
ax.legend()

st.pyplot(fig)


# # Adding My credentials in sidebar
st.sidebar.write("Made by team 15")