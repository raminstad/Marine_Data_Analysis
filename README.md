# Marine Data Analysis
![1_0_GIF_2](https://user-images.githubusercontent.com/79353291/156057373-1ae765a9-5001-4959-a441-90d9ada27f58.GIF)

# Group Members
* Ramin Estadabadi
* Yiuxuan Huang
* Zane Hallauer

# Datasets that will be utilized
[Link for downloading the data](https://rda.ucar.edu/datasets/ds539.5/index.html#!description)

[The file for datasets](https://github.com/raminstad/Marine_Data_Analysis/tree/main/acre_marine_data)

# Potential Packages
* Pandas
* Seaborn
* Matplotlyb
* Numpy
* Folium

# Data Cleaning
[The notebook for data cleaning](https://github.com/raminstad/Marine_Data_Analysis/blob/main/data_pipeline.ipynb)
* If you checked the link above for the file for the datasets, you can see we have 81 different excel files
* Some of the excel files have only one sheet and some have up to 5 sheets
## Objectives Of Data Cleaning
* Make pandas dataframe of each excel sheet
* Add all of the dataframes into a list, so we can start cleaning by having track of all of the dataframes 
* The columns that were present in most of the dataframes are: Year,Month,Day,Barometer,Thermometer,Longitude, and Latitude
* Each dataframe had different names for these columns, for example Barometer was: barmoter, BAROMETER, Barometer., and many other versions
* We cleaned the names so all of the columns that we are keeping have the same name
* After fixing the spellings, we then make sure our values for each dataframe have the same units
* We then merged all of the dataframes into one final datframe and only kept the columns that were mentioned earlier

[Final Dataframe](https://github.com/raminstad/Marine_Data_Analysis/blob/main/final_df.csv)

# Exploratory Data Analysis

[The notebook for EDA](https://github.com/raminstad/Marine_Data_Analysis/blob/main/EDA.ipynb)
* The main focus of our analysis is to see how the Barometer and Thermometer have changed over the years from 1800-1900
* Changes Of Mean And Standard Deviation For Thermometer And Barometer Over The Years
* Seperating Latitude and Longitude into bins and see where did we have the most changes
* Visualizing The data on Folium map 
### Thermometer Map
 
 <img width="2033" alt="temp" src="https://user-images.githubusercontent.com/79353291/156082022-2ebb27fc-91f4-4afc-8c73-8c3c87a7b2e2.png">
 
 ### Barometer Map
 
 <img width="2048" alt="pressure" src="https://user-images.githubusercontent.com/79353291/156082076-2e917f90-7b0d-4de5-9ec7-9e805a2ac0c2.png">


