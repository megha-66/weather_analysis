import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from functools import lru_cache

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/blue-sky-with-shiny-clouds-background_1017-23279.jpg?w=360");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 



# Load weather data
weather_data = pd.read_csv(r"C:\Users\prach\Downloads\weather_analysis-main\weather_analysis-main\WeatherData.csv")



st.title("Weather Analysis Project")




# Display data usiing Streamlit 
st.write("Here is the weather data:")
st.write(weather_data)



# Create a selectbox for options
option = st.selectbox("Select an option", ("EXPLORATORY DATA ANALYSIS", "STATISTICAL DATA ANALYSIS", "DATA VISUALIZATION"))

# Show content based on the selected option
if option == "EXPLORATORY DATA ANALYSIS":

   st.write("            ")
   st.write("            ")
   st.write("            ")
   st.markdown("### EXPLORATORY DATA ANALYSIS")
   df=pd.read_csv(r"C:\Users\prach\Downloads\Weather Data.csv")
   st.write ("The first 10 rows of the data are as follows :")
   st.write(df.head(10))
   st.write("The shape of the data is :")
   st.write(df.shape)
   st.write("The indexes of the dataframe are :")
   m=df.index
   st.write(m)
   st.write("The names of each attribute is :")
   n=df.columns
   st.write(n)
   st.write ("Dataype of each column is :")
   o=df.dtypes
   st.write(o)
   p=df['Weather'].unique()
   st.write("A list of unique entries in the WEATHER column of dataframe are : ", p)
   q=df.info()
   st.write("Here is a basic information about the dataframe :")
   st.write(q)
   st.write("The number of non-null values in each column of the dataframe :")
   st.write(df.nunique())
   st.write("A count of all unique values in the Weather column of a dataframe:")
   st.write(df['Weather'].value_counts())
   st.write("A count of all Unique wind speed values in the dataframe :")
   st.write(df['Wind Speed_km/h'].unique())
   st.write("The number of null values in each column :")
   st.write(df.isnull().sum())

   
   
   
   
   st.write("            ")
   st.write("            ")
   st.write("            ")


elif option == "STATISTICAL DATA ANALYSIS":
    
    
   st.markdown("### STATISTICAL DATA ANALYSIS")
   df=pd.read_csv(r"C:\Users\prach\Downloads\Weather Data.csv")
   k=df[df.Weather == 'Clear']
   st.write("FINDING THE NUMBER OF TIMES, WHEN THE WEATHER IS EXACTLY CLEAR",k)
   a = df[df["Wind Speed_km/h"]==4]
   st.write("FINDING ALL INSTANCES WHEN WIND SPEED IS 4 kmph")
   st.write(a)
   mean= df.Visibility_km.mean()
   st.write("Thee MEAN of all the Visibilty values is (in km): ",mean)
   sd=df.Press_kPa.std()
   st.write("The STANDARD DEVIATION of all the Pressure values is (in kPa)",sd)
   var=df['Rel Hum_%'].var()
   st.write("The VARIANCE of Relative Humidity is :", var)
   snow=df[df['Weather']=='Snow']
   st.write("Finding all instances when the weather condition was snowy")
   st.write(snow)
   b=df[(df['Wind Speed_km/h']>24) & (df['Visibility_km']==25)]
   st.write('Finding all the instances when Wind speed is greater than 24 km/hr and Visibility is 25km' )
   st.write(b)
   
   e=df.groupby('Weather').min()
   st.write("Finding the MINIMUM value of each column against 'Weather condition' ")
   st.write(e)
   f=df.groupby('Weather').max()
   st.write('Finding the MAXIMUM of each column against weather condition')
   st.write(f)
   g=df[(df['Weather']=='Clear') & (df['Rel Hum_%']>50) | (df['Visibility_km']>40)]
   st.write("Finding all instances when 'Weather is Clear' and 'Relative Humidity is greater than 50%'or 'Visibility is above 40 km'")
   st.write(g)
   st.write("Finding all records, when the weather condition is FOGGY :")
   st.write(df['Weather']=='Fog')
   st.write("Finding all instances when Weather is 'CLEAR' or Visibility is greater than 40km")
   st.write(df[(df['Weather']=='Clear') | (df['Visibility_km']>40)])
   
   


elif option == "DATA VISUALIZATION":
    
   
# Load the data
  @st.cache_data
  def load_data():
    df = pd.read_csv(r'C:/Users/prach/Downloads/Weather Data.csv')
    return df

# Function to generate line plot
  @st.cache_data
  def generate_line_plot(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Date/Time'], df['Temp_C'], 'blue')
    ax.set_xlabel('Date and Time')
    ax.set_ylabel('Temperature')
    ax.set_title('Temperature Variation')
    ax.grid(True)
    ax.tick_params(axis='x', rotation=45, labelright=True)
    plt.tight_layout()
    return fig

# Function to generate histogram
  @st.cache_data
  def generate_histogram(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['Wind Speed_km/h'], bins=20)
    ax.set_xlabel('Wind Speed')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Wind Speed')
    return fig

# Function to generate pie chart
  @st.cache_data
  def generate_pie_chart(df):
    weather_counts = df['Weather'].value_counts()
    threshold = 120
    weather_counts_filtered = weather_counts[weather_counts >= threshold]
    total_count = weather_counts_filtered.sum()
    percentages = (weather_counts_filtered / total_count) * 100
    other_count = weather_counts[weather_counts < threshold].sum()
    percentages['Others'] = (other_count / total_count) * 100
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.pie(percentages, labels=percentages.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title('Weather Condition Distribution (with "Others")')
    return fig

# Function to generate box plot
  @st.cache_data
  def generate_box_plot(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    box_color = 'c'
    sns.boxplot(x=df['Weather'], y=df['Rel Hum_%'], color=box_color)
    ax.set_xlabel('Weather Condition')
    ax.set_ylabel('Relative Humidity')
    ax.set_title('Weather Condition vs Relative Humidity')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    return fig

# Function to generate scatter plot
  @st.cache_data
  def generate_scatter_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    marker_color = 'black'
    ax.scatter(df['Temp_C'], df['Visibility_km'], color=marker_color)
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Visibility')
    ax.set_title('Temperature vs Visibility')
    return fig

# Function to generate bar graph
  @st.cache_data
  def generate_bar_graph(df):
    attributes = ["Temp_C", "Wind Speed_km/h"]
    subset_data = df[attributes]
    fig, ax = plt.subplots()
    subset_data.plot(kind='bar', ax=ax)
    ax.set_title("Temperature and Wind Speed")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    return fig


  df = load_data()

  st.write('A line Plot of Temperature (in C) wrt Time')
  line_plot = generate_line_plot(df)
  st.pyplot(line_plot)

  st.write("-" * 60)
  st.write("A histogram plot for distribution of Wind Speed values :")
  histogram = generate_histogram(df)
  st.pyplot(histogram)
  
  st.write("-" * 50)
  st.write('A PI-Chart showing the WEATHER CONDITIONS distribution:')
  pie_chart = generate_pie_chart(df)
  st.pyplot(pie_chart)

  st.write("-" * 50)
  st.write("A Box Plot of Weather Condition vs Relative Humidity is as follows :")
  box_plot = generate_box_plot(df)
  st.pyplot(box_plot)

  st.write("-" * 50)
  st.write("A SCATTER PLOT of Temperature vs Visibility is as follows :")
  scatter_plot = generate_scatter_plot(df)
  st.pyplot(scatter_plot)

  st.write("-" * 50)
  st.write("A BAR graph of TEMPERATURE and WIND SPEED values :")
  bar_graph = generate_bar_graph(df)
  st.pyplot(bar_graph)
  
  
