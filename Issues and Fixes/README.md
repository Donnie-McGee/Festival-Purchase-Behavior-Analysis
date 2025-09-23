# Issues and Fixes

Here I will share the major obstacles, inconvenients, razoning, progresses and fixes I faced while developing my first data analysis project. Some points have been organically explained in a different section (links will be provided, in order to avoid repetition across sections), while some deserve their space here, since they needed a deeper thought and coding process.

## [Shapening my data base](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/tree/main/2.-%20Data%20Sharpening)

I generated the raw dataset with AI in order to have the opportunity to work with a music festival data base. Thanks to AI, I could have the information I wanted to work with, but during the [Data Survey](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/blob/main/1.-%20Data%20Survey/Data%20Survey.ipynb) I realised most of my fields presented unrealistic distributions, reason for which I decided to sharpen the dataset into a more chaotic and vivid representation of what a music festival would be.

For most of the fields I used customized or random linear distributions, but for one specific field *"age*", I decided to use a normal distribution.

## [Normal distribution in *"age"*](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/blob/main/Issues%20and%20Fixes/Issues%20and%20Fixes.ipynb)

The main difference between this field and others lies in the number of unique values it contains. While fields like *"gender"* (3 values), *"stages_visited"* (5), or even *"satisfaction_score"* (10) have a limited number of categories, *"age"* ranges from 18 to 59 (meaning 41 distinct values).

To simulate a realistic age distribution, I considered two approaches:

1. Manually define the proportion for each of the 41 possible values: a tedious and error-prone approach that doesn't scale well.
2. Use a statistical model to automate the process in a scalable way: scalable and flexible.

Since festival attendees are likely to follow a normal distribution centered around young adults, I opted for the second option.

Initially, I generated a normal distribution with a mean of 30 and a standard deviation of 7, clipping the values between 18 and 59. However, this introduced a new problem:  

- All values below 18 were forced to the lower bound, creating an artificial spike at *18*. As a result, *18* became the mode, surpassing the expected peak around the mean (*30*). This flaw in the statistical model broke the realistic approch I first intended.

To address this, I applied a **right-skewed distribution**. This approach reduced the number of values generated below 18 (therefore, fewer were clipped) and allowed the distribution to retain its central tendency near 30 without inflating the frequency of the lower bound. Since the upper limit (59) was farther from the mean, it was less affected by clipping, and the overall distribution improved significantly.

## [Normalized tables](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/blob/main/Issues%20and%20Fixes/Discurted%20normalized%20tables.ipynb)

During the [Data Modelling](https://github.com/Donnie-McGee/Festival-Purchase-Behavior-Analysis/tree/main/4.-%20Data%20Modelling) phase I come up with the idea of normalizing dimention tables to make the whole proccess more efficient, but, eventually, I realized the balance between how much proccessing time it will save and how complex SQL queries will become was not worth it. For that reason I took a step back and erased it from the project, but kept it in this section, just to keep track of how I got to make it.