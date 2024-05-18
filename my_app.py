import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd

athletes = pd.read_csv('athlete_events.csv')
region = pd.read_csv('noc_regions.csv')
a_df = athletes.merge(region, how='left', on='NOC')


def main():
    st.write(""" # Olympic Data Analysis""")
    
   
    selected_year = st.sidebar.selectbox('Select a year', sorted(a_df['Year'].unique()))#front end code
    col1, col2 = st.columns(2)  
    col3, col4 = st.columns(2)  
    
    with col1:
     st.write(f"Top 5 countries in {selected_year}")
     top_5_countries = a_df[a_df['Year'] == selected_year]['Team'].value_counts().head(5)
     fig, ax = plt.subplots(figsize=(8, 6)) #for front end
     sns.barplot(x=top_5_countries.index, y=top_5_countries, palette='Set1', ax=ax)
     plt.xticks(rotation=45)
     plt.xlabel('Country')
     plt.ylabel('Number of Medals')
     plt.title(f'Top 5 Countries by Medals in {selected_year}')
     st.pyplot(fig)#for front end




    
    with col3:
        st.write(f'Gold Medalists Dashboard - above 60')
        gold_medals = a_df[(a_df['Medal'] == 'Gold') & (a_df['Age'] > 60)]
        sporting_events = gold_medals['Sport']
        fig, ax = plt.subplots(figsize=(8, 6))  
        ax.plot(sporting_events)
        plt.xticks(rotation=45)
        plt.xlabel('Athlete')
        plt.ylabel('Sporting Event')
        st.pyplot(fig)

   
    with col2:
        st.write(f"Gender Distribution in {selected_year}")
        gender = a_df[a_df['Year'] == selected_year]['Sex'].value_counts()
        fig, ax = plt.subplots(figsize=(8, 6))
        plt.title("Gender Distribution")
        plt.pie(gender, labels=gender.index)
        st.pyplot(fig)
    
    with col4:
     st.write("Summer vs Winter")
     selected_gender = st.slider("Select Gender", 0, 1, 0, format="%d")

    summer_filtered = a_df[(a_df['Season'] == 'Summer') & (a_df['Sex'] == ['M', 'F'][selected_gender])]
    winter_filtered= a_df[(a_df['Season'] == 'Winter') & (a_df['Sex'] == ['M', 'F'][selected_gender])]

    summer_counts = summer_filtered.groupby('Year').size()
    winter_counts = winter_filtered.groupby('Year').size()

    fig, ax = plt.subplots(figsize=(6, 4)) 

    plt.plot(summer_counts.index, summer_counts.values, color='b', label='Summer')
    plt.plot(winter_counts.index, winter_counts.values, color='r', label='Winter')
    plt.title('Summer vs Winter Olympic Participation by Athletes')
    plt.xlabel('Year')
    plt.ylabel('Number of Athletes')
    plt.xticks(rotation=45)  
    plt.legend()
    st.pyplot(fig)

   
if __name__ == "__main__":
    main()

