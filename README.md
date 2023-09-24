# Wrangle OpenStreetMap Data
August 28, 2019  
Preston Hall

## Overview

This is my project submission for the Udacity Data Analyst Nanodegree program, titled "Wrangle OpenStreetMap Data." The project involves the process of data wrangling, which encompasses data collection, cleaning, and analysis. Through this project, I have gained valuable skills such as assessing data quality, parsing and gathering data from XML files, programmatically cleaning and processing large datasets, and using SQL for data storage and querying.

## Map Area

The map area I chose for this project is Beaverton, Oregon, United States. As I currently reside in this area, I was particularly interested in exploring and contributing to its improvement on OpenStreetMap.org.

To make the dataset more manageable for analysis, I used the sample.py script to generate a smaller sample of the data.

## Understanding the Data

Before diving into data cleaning and analysis, I began by understanding the structure and content of the dataset:

- The mapparser.py script helped create a dictionary with different elements and their occurrences within the dataset.
- I examined the types of tags present in the data, including "lower," "lower_colon," "other," and "problemchars."

## Problems Encountered in the Map

During the auditing phase using the audit.py script, I identified several issues with the data, including:

- Abbreviated street types and directions.
- Inconsistent zip code formats.
- Incorrect zip codes for the area.
- Phone numbers in various formats.

## Data Cleaning

In the data cleaning phase, I addressed the identified issues programmatically using the data.py script. This process involved cleaning and converting the data from XML to CSV format. By transforming the data from a document format to a tabular format, it became easier to work with and analyze.

## Importing to Database

To facilitate further analysis, I imported the cleaned CSV files into a SQL database using the createdb.py script. The resulting database, osm.db, consists of five tables: nodes, nodes_tags, ways, ways_tags, and ways_nodes.

## Inspecting Cities

To focus my analysis within the city of Beaverton, I checked if other cities were included in the dataset. I ran SQL queries to identify and remove entries that were not related to Beaverton.

## Data Overview

Here is an overview of the file sizes and some key statistics:

- Beaverton.osm: 85.3 MB
- osm.db: 47.1 MB
- nodes.csv: 33.7 MB
- nodes_tags.csv: 521 KB
- ways.csv: 9.7 MB
- ways_nodes.csv: 7 MB
- ways_tags.csv: 2.9 MB

Number of nodes: 352,195
Number of ways: 43,527
Number of unique users: 245

## Key Findings

- Top 10 contributing users and their contributions.
- Identification of users appearing only once (having 1 post).
- Analysis of religious places, including the most prominent religions.
- Analysis of Christian denominations.
- Identification of the most popular cuisines in the area.

## Conclusion

This project provided valuable experience in handling and cleaning real-world data. While the dataset is generally complete, valid, and accurate, it highlighted the importance of consistency in data quality. The skills acquired through this project are essential for working with large and potentially messy datasets, making it a valuable addition to the Udacity Data Analyst Nanodegree program.

