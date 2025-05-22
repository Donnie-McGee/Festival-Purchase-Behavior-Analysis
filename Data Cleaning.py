import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\PC\Desktop\Estudio\Analisis de Datos\Proyectos\Festival Purchase Behavior Analysis\festival_dataset_dirty_from_uploaded_v2.csv")

# This part of the code provides an overview of the dataset, spaced, so each function is easier to read.

print(df.shape)
print("\n")
print(df.head())
print("\n")
print(df.info())
print("\n")
print(df.describe())
print("\n")
print(df.isnull().sum())
print("\n")
print(df.duplicated().sum())
print("\n")
print(df.nunique())
print("\n")
print(df.columns)
print("\n")

# --- Gender column ---
# Null values management

# Count the number of unique values in each column
# Used to understand the dataset better
print(df['gender'].value_counts(dropna=False))

# gender_dist will store the normalized distribution
gender_dist = df["gender"].value_counts(normalize=True)

# mask will be used to locate the null values in the dataset
mask = df["gender"].isnull()

# Adds all the null
n_nulls = mask.sum()

# Fill the null values with random choices based on the distribution
# This will ensure that the null values are filled in a way that reflects the original distribution
df.loc[mask, "gender"] = np.random.choice(
    gender_dist.index,
    size=n_nulls,
    p=gender_dist.values
)

# Check if there are any null values left in the dataset
print(df['gender'].value_counts(dropna=False))

# Changes the data type to category, which is more efficient for categorical data
df["gender"] = df["gender"].astype("category")
print(df["gender"].dtype)

# Overwrite the original dataset with the new values
# Index=False will ensure that the index is not written to the file
# This is important because the index is not needed in the final dataset
df.to_csv(r"C:\Users\PC\Desktop\Estudio\Analisis de Datos\Proyectos\Festival Purchase Behavior Analysis\festival_dataset_dirty_from_uploaded_v2.csv", index=False)



# --- Ticket Type column ---
# Same steps to clean "ticket_type" column as we followed for "gender" column
# Visualization of counts of each ticket type has been dropped for a more readable code
print(df["ticket_type"].value_counts(dropna=False))

type_dist = df["ticket_type"].value_counts(normalize=True)
mask = df["ticket_type"].isnull()
n_nulls = mask.sum()
df.loc[mask, "ticket_type"] = np.random.choice(
    type_dist.index,
    size = n_nulls,
    p=type_dist.values
)
df["ticket_type"] = df["ticket_type"].astype("category")
df.to_csv(r"C:\Users\PC\Desktop\Estudio\Analisis de Datos\Proyectos\Festival Purchase Behavior Analysis\festival_dataset_dirty_from_uploaded_v2.csv", index=False)


