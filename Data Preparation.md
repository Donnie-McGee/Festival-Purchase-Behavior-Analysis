# Data Preparation

## Data Survey

Prior to preparation, I dived in the dataset to get familiar with it using Pandas. With this first approach I got useful information:

- The presence of null values in columns _'ticket_type'_ and _'gender'_ (140 each), which will need special attention.
- Columns _'gender'_, _'was_present'_ and _'recommended_to_friend'_ may contain hidden null values or inconsistent labels, which requires an in depth inspection.
- Some columns seem to be 100% structurally clean, like _'ticket_type'_, _'ticket_price'_ and _'attendance_date'_. Still, they have to be checked out.
- _'attendee_id'_ and _'ticket_id'_ have fewer unique values than rows in the dataset, which could indicate duplicates or shared IDs across records. This requires closer examination.

Once studied this first approach, I proceed to inspect, clean and optimise the columns _'gender'_, _'was_present'_ and _'recommended_to_friend'_:

### _Column 'gender'_:

Since the dataset counts 140 null values for _"gender"_ (this represent less than a 1%), I decided to proportionally assign them to "Male", "Female" and "Other" (all 3 non-null values found during the survey). With such a small percentage and the proportions being so similar (see Step 1, further down) I assume there is no reason to believe that the missing values are systematic (e.g., more frequent in a specific group).

To clean _"gender"_ these steps were taken:

  1. Normalize the distribution: Doing so, I have a proper understanding of each value's the percentage. This will help me later to randomly distribute the null values among the 3 possibilities we have for _"gender"_.
  2. Locate the null values in the dataset.
  3. Replace them: In this step I'll change each null-value to one of the possible values following the proportion calculated in Step 1 and the locations from Step 2. This will provide consistency in the metrics.
  4. Change the column's type to category: Doing so, I'm saving resources and time during the analysis, since this practice will encode the values ("Male" as 1, "Female" as 2, "Other" as 3, for example) preparing the dataset for later. 
  5. Overwrite dataset: Otherwise, the changes would only occur during the Python script is running. The data base must be updated.

### _Column "ticket_type"_:

This column follows the same pattern as _"gender"_: 140 null values and 3 possible values with similar probabilities, so the steps taken will be the same.

### _Column "was_present"_:

Had a typo easy to clean: _"Yess" -> "Yes"_

### _Column "payment_method"_:

Had a typo easy to clean: _"cash " -> "Cash"_

### _Column "favourite_genre"_:

Had a typo easy to clean: _"hiphop" -> "Hip-Hop"_

### _Column "recommend_to_friend"_:

Had a typo easy to clean: _"nO" -> "No"_

### _Clean columns_:

All other columns are clean: they contain no null values, no typos and all the values they have are logical and consistent.

### Data Type convertion:

Once the cleaning process is finished, I've converted the columns to specific type:

1. Category: All the string values will be assigned this type ("ticket_id", "origin_city"...)
2. Int: Integers ("age", "ticket_price", "satisfaction_score"...) 
3. Float: Decimal numbers ("food_expense", "drink_expense", "merch_expense")
4. Bool: Those that contain dicotomical values ("was_present", "recommend_to_friend")
5. Datetime: All values related to time ("purchase_date", "attendance_date")

This ensures each column will be processed according to the information it contains.