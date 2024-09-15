# SpaceX Falcon 9 First Stage Landing Prediction

## Overview

This project aims to predict the successful landing of Falcon 9 first stages and identify factors influencing successful landings. By analyzing historical data from SpaceX, including launch details and outcomes, the project utilizes machine learning techniques to develop predictive models. Insights gained from exploratory data analysis (EDA) and interactive visualizations provide valuable information for stakeholders in the space exploration industry.

## Contents

### 1_Data_Collection_API.ipynb
- Notebook for collecting data from SpaceX's API.
- Includes code to make API requests, parse the responses, and save the data into a structured format for further analysis.
- Extracts information such as launch dates, success outcomes, and payload details.

### 2_Data_Collection_Web_Scraped.ipynb
- Notebook for web scraping launch data from Wikipedia.
- Demonstrates how to extract launch details from Wikipedia pages, clean the data, and store it in a usable format.
- Scrapes information such as launch sites, rocket versions, and mission outcomes.

### 3_Data_Wrangling.ipynb
- Notebook for exploratory data analysis using SQL queries.
- Explores the dataset stored in a SQL database, retrieves relevant information, and performs aggregate calculations.
- Analyzes launch success rates, payload masses, and other key metrics using SQL queries.

### 4_Exploratory_Data_Analysis_Using_SQL.ipynb
- Notebook for exploratory data analysis using SQL queries.
- Explores the dataset stored in a SQL database, retrieves relevant information, and performs aggregate calculations.
- Analyzes launch success rates, payload masses, and other key metrics using SQL queries.

### 5_Exploratory_Data_Analysis_with_Visualization.ipynb
- Notebook for exploratory data analysis with visualizations.
- Includes charts and graphs to visualize relationships between variables, identify patterns, and uncover insights in the data.
- Explores correlations between flight numbers, orbit types, and landing success rates.

### 6_Interactive_Visual_Analytics_with_Folium.ipynb
- Notebook for creating interactive visualizations using Folium.
- Demonstrates how to plot SpaceX launch sites on maps, add markers, clusters, and other interactive features.
- Visualizes launch site locations, mission outcomes, and proximities.

### 7_Interactive_Dashboard_with_Dash (folder)
- Folder containing files for building an interactive dashboard with Plotly Dash.\
[View Separate Repo of Dash App](https://github.com/rjacaac211/SpaceX-Falcon-9-Dash-App)\
[View Dash Web App](https://spacex-falcon-9-dash-app.onrender.com/)

### 8_Falcon9_First_Stage_Landing_Prediction.ipynb
- Notebook for predictive analysis and building classification models.
- Covers data preprocessing, model training, evaluation, and selection of the best-performing algorithm for predicting Falcon 9 landing outcomes.

### SpaceX Falcon9 Landing Prediction.pdf
- Explores data collection through SpaceX API and Wikipedia web scraping, followed by thorough data wrangling to prepare for analysis.
- Highlights insights from EDA, including correlations between flight numbers, orbit types, payload mass, and landing success rates, with key findings on the influence of launch site locations.
- Discusses the development of interactive visualizations using Folium and Plotly Dash, providing dynamic insights into launch success rates, payloads, and booster performance.
- Presents predictive modeling using a Decision Tree Classifier, achieving 88.9% accuracy in predicting Falcon 9 landing outcomes, offering valuable insights for future launches.

### data
- This folder contains all the data used/created during the project. 

## Summary

This project explores SpaceX's Falcon 9 first stage landing predictions by leveraging data collection techniques, exploratory data analysis, interactive visualizations, and predictive modeling. It provides valuable insights for stakeholders in the space exploration industry, aiding in decision-making processes related to launch planning and operations.
