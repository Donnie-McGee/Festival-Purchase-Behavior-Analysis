# Data Preparation

## Data Survey

Prior to preparation, I dived in the dataset to get familiar with it using Pandas. With this first approach I got useful information:

- The presence of null values in columns _'ticket_type'_ and _'gender'_ (140 each), which will need special attention.
- Columns _'gender'_, _'was_present'_ and _'recommended_to_friend'_ may contain hidden null values or inconsistent labels, which requires an in depth inspection.
- Some columns seem to be 100% structurally clean, like _'ticket_type'_, _'ticket_price'_ and _'attendance_date'_. Still, they have to be checked out.
- _'attendee_id'_ and _'ticket_id'_ have fewer unique values than rows in the dataset, which could indicate duplicates or shared IDs across records. This requires closer examination.

Once studied this first approach, I proceed to inspect, clean and optimise the columns _'gender'_, _'was_present'_ and _'recommended_to_friend'_:

### Column 'gender':
