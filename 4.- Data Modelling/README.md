# Data Modelling

In this part of the project, I transition from a single cleaned dataset to a structured and optimized model that facilitates analysis in SQL and Power BI.

## Objectives

- Create new calculated columns that will add value to the analysis.
- Split the cleaned dataset into several smaller, focused tables.
- Design a star schema to ensure clarity, performance, and scalability in the analytical tools.

### Create new columns

In order to make it easier in the incoming steps, I decided to create these columns:

- *"total_expense"*: A combination of all 3 expenses (for food, drink and merch) columns. This means all expenses within the festival, not including the ticket price.
- *"mean_rating"*: The aritmetical mean of all 3 expenses column, useful for advanced calculations and to extract insights.
- *"is_multiday"*: Boolean column that segmentates attendees whether their ticket is multiday or not.
- *"age_group"*: Bin column that segmentates attendees in age ranges.
- *"satisfaction_level"*, *"cleanliness_rating_level"* and *"security_rating_level"*: Bin column that segmentates the related column into levels of *"Low"*, *"Medium"* and *"High"* scores.
- *"group_size"*: Bin column that segmentates the atteendees into *"Individual"*, *"Couple"* and *"Group"*.

The code for it can be checked [here](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/blob/develop/4.-%20Data%20Modelling/1-%20Adding%20new%20columns/New%20columns.ipynb).

### Spliting into smaller tables

This step is divided in 2 sub-steps:

1. Creating dimention tables to optimise proccessing time and improve organisation and scalability. This sub-step can be checked [here](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/blob/develop/4.-%20Data%20Modelling/2-%20Creating%20dim%20tables/Dim%20tables.ipynb)
2. Dividing the *"final_festival_dataset"* csv file into smaller tables, each containing self-related information.

A key step is to normalize the string columns. For it, I created dimention tables that will contain strings and relate these columns with their corresponding corresponding column in the main tables. This way I'm optimising computing time and scalability.

### Star schema

