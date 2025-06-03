# Data Sharpening

## Why?

The dataset used in this project was generated with the help of AI. Although this provides structure and consistency, it also means the data lacks the chaotic imperfections and variability that real-world datasets often have.

In order to simulate realistic behavior and enrich the analysis, I introduced controlled modifications to some key columns. These changes were designed to make the data more dynamic to what one would expect in a real festival.

This way, the depths of the insights will be richer and will also make the project more enjoyable and meaningful to work with.

## Column *"satisfaction_score"*

Originally, the unique values in *"satisfaction_score"* were limited to [5, 6, 7, 9], which doesn’t reflect the range of real attendee experiences. In reality, ratings tend to vary more widely (from 1 to 10) depending on each person’s expectations, mood, and outcomes during the festival. 

To make the project follow a more realistic distribution, I designed a custom probability model and used it to randomly assign values across the dataset.