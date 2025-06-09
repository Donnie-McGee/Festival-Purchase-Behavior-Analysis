# Data Sharpening

## Why?

The dataset used in this project was generated with the help of AI. Although this provides structure and consistency, it also means the data lacks the chaotic imperfections and variability that real-world datasets often have. This can be seen in the [Data Survey section](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/blob/main/1.-%20Data%20Survey/Data%20Survey.ipynb).

In order to simulate realistic behavior and enrich the analysis, I introduced controlled modifications to some key columns. These changes were designed to make the data more dynamic to what one would expect in a real festival.

This way, the depths of the insights will be richer and will also make the project more enjoyable and meaningful to work with.

## Redefinying distributions

By default, an AI would generate a balanced dataset if not specified. In this case, all columns followed the same pattern: all possible values had almost the same proportion, what would lead to a very monotonous and unsatisfying analysis. Therefore, in this step of the project I used Python to change those distributions to what I think fits best to a real music festiva experience.

For some columns I introduced proportions manually and let Python randomly select which rows would change (this allowed me to make some columns follow a bimodal distribution), whereas, for one specific field (*"age"*) I used a normal distribution, to test my statistical coding knowledge.

### Customized distribution

By default, rating fields followed the same pattern, and non-rating fields had perfectly uniform distributions across categories. To bring the dataset closer to real-world behavior, I designed and applied custom distributions to various fields.

#### Rating fields 

Originally, the unique values in *"satisfaction_score"* were limited to [5, 6, 7, 9], which doesn't accurately reflect the range of real attendee experiences. In practice, ratings tend to vary more widely (from 1 to 10), influenced by each person's expectations, mood, and overall experience.

To better simulate this variability, I created custom probability distributions and randomly reassigned values across the dataset. The same approach was applied to *"security_rating"* and *"cleanliness_rating"*.

#### No rating fields

In reality, people tend to pay with cash or card more often than with the festival app; larger groups are more frequent than individuals; most attendees visit more than two stages. To reflect this natural imbalance, I manually adjusted the distributions of *"payment_method"*, *"group_size"*, and *"stages_visited"*.

### Column *"age"*

I applied a random normal distribution to this field, as it best simulates a realistic age spread.. I thought this would be the best fit for the column to behave realisticly. I clipped the values to ensure a minimum of 18 and a maximum of 59, meaning any outliers below or above those limits were automatically set to the nearest boundary.

### Adding variety in *"origin_city"*

I included *"Malaga"* as a new city in the dataset to diversify the geographic origin of attendees and make the data more representative of a real Spanish festival.

### Changing *"tickep_price"*

The original ticket prices were:

- 1-Day = 80  
- 3-Day = 150  
- VIP = 200  

These values didn’t reflect a realistic price gap between tickets, especially considering the added value of multi-day or VIP passes. I updated them as follows:

- 1-Day = 80  
- 3-Day = 210  
- VIP = 350  

This change makes the ticket hierarchy more believable and aligns better with real-world pricing logic.