# Data Preparation

## Data Survey

Prior to preparation, I dived in the dataset to get familiar with it using Pandas. With this first approach I got useful information:

- The presence of null values in columns *'ticket_type'* and *'gender'* (140 each), which will need special attention.
- Columns *'gender'*, *'was_present'* and _'recommended_to_friend'_ may contain hidden null values or inconsistent labels, which requires an in depth inspection.
- Some columns seem to be 100% structurally clean, like 'ticket_type', 'ticket_price' and 'attendance_date'. Still, they have to be checked out.
- 'attendee_id' and 'ticket_id' have fewer unique values than rows in the dataset, which could indicate duplicates or shared IDs across records. This requires closer examination.

Once studied this first approach, I proceed to inspect, clean and optimise the columns 'gender', 'was_present' and 'recommended_to_friend':

### Column 'gender':
