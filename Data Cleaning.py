import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\PC\Desktop\Estudio\Analisis de Datos\Proyectos\Festival Purchase Behavior Analysis\festival_dataset_dirty.csv")

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

# I'm selecting columns of type 'object' (text) or 'category' to analyze unique values in those columns.
text_columns = df.select_dtypes(include=['object', 'category']).columns

# Displaying unique values for each text column
# With it, we can see the unique values in each text column, which helps us understand the dataset better
# And detect typos or inconsistencies in the data.
for col in text_columns:
    print(f"\nUnique values of '{col}':")
    print(df[col].unique())



# --- Gender column ---
# Null values management

# Count the number of unique values in each column
# Used to understand the dataset better
print(df['gender'].value_counts(dropna=False))
print("\n")

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



# # --- Typos cleaning ---
df["was_present"] = df["was_present"].replace({"Yess": "Yes"})
df["payment_method"] = df["payment_method"].replace({"cash ": "Cash"})
df["favourite_genre"] = df["favourite_genre"].replace("hiphop", "Hip-Hop")
df["recommend_to_friend"] = df["recommend_to_friend"].replace({"nO": "No"})

# Strips leading and trailing whitespace from all string columns
for col in df.columns:
    if df[col].dtype == 'object':
      # It will convert to string, then strip whitespace
        df[col] = df[col].str.strip()
      # It will replace multiple spaces with a single space
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)

# Type conversion
# With it, we ensure that the data types are appropriate for analysis and optimize memory usage
df = df.astype({
    'ticket_id': 'category',
    'ticket_type': 'category',
    'ticket_price': 'int',
    'was_present': 'bool',
    'attendee_id': 'category',
    'age': 'int',
    'gender': 'category',
    'origin_city': 'category',
    'transport_used': 'category',
    'group_size': 'int',
    'food_expense': 'float',
    'drink_expense': 'float',
    'merch_expense': 'float',
    'payment_method': 'category',
    'favourite_genre': 'category',
    'stages_visited': 'int',
    'top_artist_seen': 'category',
    'hours_spent': 'float',
    'satisfaction_score': 'int',
    'security_rating': 'int',
    'cleanliness_rating': 'int',
    'recommend_to_friend': 'bool'
})

# Conversión de fechas
df['purchase_date'] = pd.to_datetime(df['purchase_date'])
df['attendance_date'] = pd.to_datetime(df['attendance_date'])

# Conversión de hora
df['entry_time'] = pd.to_datetime(df['entry_time'], format='%H:%M:%S').dt.time

# # Overwrite the original dataset with the new values
# # Index=False will ensure that the index is not written to the file
# # This is important because the index is not needed in the final dataset
# df.to_csv(r"C:\Users\PC\Desktop\Estudio\Analisis de Datos\Proyectos\Festival Purchase Behavior Analysis\festival_dataset_clean.csv", index=False)

print(df.dtypes)