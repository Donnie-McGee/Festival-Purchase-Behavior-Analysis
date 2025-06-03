# Data Preparation

## Data Survey

Prior to preparation, I dived into the dataset to get familiar with it using Pandas. This initial exploration revealed useful insights:

- The presence of null values in columns *"ticket_type"* and *"gender"* (140 and 280, respectively), which will need special attention.
- Columns *"payment_method"*, *"favourite_genre"* and *"recommend_to_friend"* contain typos, which requires an in-depth inspection.
- Despite null values, some columns seem to be 100% structurally clean, like *"ticket_type"*, *"ticket_price"* and *"attendance_date"*. Still, they have to be checked out.
- *"attendee_id"* and *"ticket_id"* have fewer unique values than rows in the dataset, which could indicate duplicates or shared IDs across records. This requires closer examination.

After this initial exploration, I proceeded to handle the null values.

## Dropping Unnecessary Columns

To streamline the dataset and optimize processing time, I removed several columns that are not relevant to the analysis. This helps reduce noise and improve overall clarity. The dropped columns are:

- *"attendee_id"*
- *"entry_time"*
- *"origin_city"*
- *"purchase_date"*
- *"ticket_id"*
- *"top_artist_seen*
- *"transport_used"*
- *"was_present"*

## Null values management

### Column *"gender"*

Since the dataset counts 140 null values for *"gender"* (this represents less than 1%), I decided to proportionally assign them to *"Male"*, *"Female"* and *"Other"* (all 3 non-null values found during the survey). With such a small percentage and the proportions being so similar (see Step 1, further down), I assume there is no reason to believe that the missing values are systematic (e.g., more frequent in a specific group).

To clean *"gender"* these steps were taken:

1. Normalize the distribution: Doing so, I gain a proper understanding of each value's percentage. This helps later to randomly assign the null values among the 3 possibilities we have for *"gender"*.
2. Locate the null values in the dataset.
3. Replace them: In this step, I change each null value to one of the possible values following the proportion calculated in Step 1 and the locations from Step 2. This provides consistency in the metrics.
4. Change the column's type to category: This saves resources and time during analysis, as it encodes the values (e.g., *"Male"* as 1, *"Female"* as 2, *"Other"* as 3), preparing the dataset for later steps.
5. Overwrite dataset: Otherwise, the changes would only occur during the Python script's execution. The dataset must be updated.

### Column *"ticket_type"*

The distribution in this column is less balanced than in *"gender"*, but the same procedure was applied, since the number of null values represents only about 2% of the sample.

### Columns with minor typos

The following columns contained small, easily correctable errors:

- *"payment_method"*: "cash " → "Cash"
- *"favourite_genre"*: "hiphop" → "Hip-Hop"
- *"favourite_genre"*: "Regueton" → "Reggaeton"
- *"recommend_to_friend"*: "nO" → "No"

### Trimming Extra Spaces

As part of the data cleaning process, I removed leading and trailing spaces from all values across the dataset. Additionally, I replaced occurrences of multiple consecutive spaces with a single space to ensure consistency.

### Verifying Clean Columns

All remaining columns have been reviewed and are clean. They contain:

- No null values
- No typos
- Logical and consistent data throughout

## Data Type Conversion

Once the cleaning process is finished, I've converted the columns to specific types:

1. *Category*: All the string values are assigned this type (*"ticket_id"*, *"origin_city"*, etc.)
2. *Int*: Integers (*"age"*, *"ticket_price"*, *"satisfaction_score"*, etc.)
3. *Float*: Decimal numbers (*"food_expense"*, *"drink_expense"*, *"merch_expense"*)
4. *Bool*: Those that contain dichotomous values (*"was_present"*, *"recommend_to_friend"*)
5. *Datetime*: All values related to time (*"purchase_date"*, *"attendance_date"*)

This ensures each column is processed according to the information it contains.