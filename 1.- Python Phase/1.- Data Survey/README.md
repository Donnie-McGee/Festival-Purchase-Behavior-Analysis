# Data Survey

Prior to preparation, I dived into the dataset to get familiar with it using Pandas. This initial exploration revealed useful insights:

- The presence of null values in columns *"ticket_type"* and *"gender"* (140 and 280, respectively), which will need special attention.
- Columns *"payment_method"*, *"favourite_genre"* and *"recommend_to_friend"* contain typos, which requires an in-depth inspection.
- Despite null values, some columns seem to be 100% structurally clean, like *"ticket_type"*, *"ticket_price"* and *"attendance_date"*. Still, they have to be checked out.
- *"attendee_id"* and *"ticket_id"* have fewer unique values than rows in the dataset, which could indicate duplicates or shared IDs across records. This requires closer examination.
- Unconsistent *"ticket_price"* across the data base.

After this initial exploration, I proceeded to the [Data Sharpening](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/tree/main/1.-%20Python%20Phase/2.-%20Data%20Sharpening).