# Data Modelling

In this part of the project, I transition from a single cleaned dataset to a structured and optimized model that facilitates analysis in SQL and Power BI.

## Objectives

- Create new calculated columns that will add value to the analysis.
- Split the cleaned dataset into several smaller, focused tables.
- Design a star schema to ensure clarity, performance, and scalability in the analytical tools.

### Create new columns

- *"total_expense"*: A combination of all 3 expenses (for food, drink and merch) columns. This means all expenses within the festival, not including the ticket price.
- *"mean_rating"*: The aritmetical mean of all 3 expenses column, useful for advanced calculations and to extract insights.
- *"is_multiday"*: Boolean column that segmentates attendees whether their ticket is multiday or not.
- *"age_group"*: Bin column that segmentates attendees in age ranges.
- *"satisfaction_level"*, *"cleanliness_rating_level"* and *"security_rating_level"*: Bin column that segmentates the related column into levels of *"Low"*, *"Medium"* and *"High"* scores.
- *"group_size"*: Bin column that segmentates the atteendees into *"Individual"*, *"Couple"* and *"Group"*.

### Spliting into smaller tables

Code detailed and explained in (Data Modelling.ipynb) [AÑADIR ENLACE A NOTEBOOK].

A key step is to normalize the string columns. For it, I created dimention tables that will contain strings and relate these columns with their corresponding corresponding column in the main tables. This way I'm optimising computing time and scalability.

### Star schema

