# Data Modelling

In this part of the project, I transition from a single cleaned dataset to a structured and optimized star model that facilitates analysis in SQL and Power BI.

## Objectives

- Create new calculated columns that will add value to the analysis.
- Split the cleaned dataset into fact and dim tables.

### Create new columns

In order to make it easier in the incoming steps, I decided to create these columns:

- *"total_expense"*: A combination of all 3 expenses (food, drink and merch) columns. This means all expenses within the festival, not including the ticket price.
- *"mean_rating"*: The aritmetical mean of all 3 expenses column, useful for advanced calculations and to extract insights.
- *"is_multiday"*: Boolean column that segmentates attendees whether their ticket is multiday or not.
- *"age_group"*: Bin column that segmentates attendees in age ranges.
- *"satisfaction_level"*, *"cleanliness_level"* and *"security_level"*: Bin column that segmentates the related column into levels of *"Low"*, *"Medium"* and *"High"* scores.
- *"group_type"*: Bin column that segmentates the atteendees into *"Individual"*, *"Couple"* and *"Group"*.

The code for it can be checked [here](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/blob/develop/4.-%20Data%20Modelling/1.-%20New%20columns.ipynb).

### Spliting into smaller tables

This step is divided in 2 sub-steps:

1. Defining fact and dim tables' structure. This sub-step can be checked [here](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/blob/develop/4.-%20Data%20Modelling/2.-%20Dim%20tables.ipynb).
2. Dividing the *"final_festival_dataset"* file into smaller tables, saving each new table individually.

### Star schema

