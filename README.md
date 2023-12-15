# Food Truck Exploration Project

## Project Overview

The Food Truck Exploration Project is a comprehensive data analysis and visualization project focused on enhancing the experience of exploring food trucks in Indiana. Utilizing open-source map APIs, the project gathers, cleans, and analyzes data on local food trucks, providing insightful visualizations and a well-planned foodie exploration schedule for the weekend.

## Features

**Data Collection:** Utilizes Google Map API and Yelp API to collect data on local food trucks in Indiana.
**Data Cleaning and Organization:** Cleans and organizes the collected data into a usable format.
**Data Analysis:** Performs detailed data analysis to draw conclusions about the food truck scene in Indiana.
**Weekend Planning:** Provides a detailed two-day weekend plan for exploring various food trucks, complete with timings, locations, cuisine types, travel time, and distance.
**Visualization:** Offers data visualizations and a mapped route for the planned foodie tour.

## File Descriptions

**Script.py:** Python script for data collection from Google Maps and Yelp APIs.
**Food_Trucks_Exploration.ipynb:** Jupyter Notebook for data cleaning, analysis, and visualization.
**food_trucks.csv:** Collected raw data on food trucks.
**Cleaned_food_trucks.csv:** Cleaned and processed data.
**weekend_food_plan.csv:** Finalized weekend plan for food truck exploration.
**requirements.txt:** List of Python packages required for the project.

## Installation

To set up the project environment, follow these steps:

### Clone the repository:
```bash
git clone [URL of the FoodX GitHub repository]
```

### Install the required packages:
```
pip install -r requirements.txt
```

### Running the Notebook

Run the script:

```bash
python script.py
```

Then Run the Jupyter notebook:

```bash
jupyter notebook FoodX_Exploration.ipynb
```

## API Keys Setup
The project requires API keys for Google Maps and Yelp. Follow these steps to set up your API keys:

1. Create a file named APIKEY.env in the root directory of the project.
2. Obtain your Google Maps and Yelp API keys
3. Add your API keys to the APIKEY.env file:
```
GOOGLE_API_KEY='Your_Google_Maps_API_Key'
YELP_API_KEY='Your_Yelp_API_Key'
```

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.
