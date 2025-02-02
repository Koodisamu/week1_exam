import pandas as pd

# Creating a dataframe from the csv. file
df = pd.read_csv('productdata.csv')

# Checking for missing values
# print(df.isnull().sum())

# Cleaning data
# Removing duplicate product ID's, keeping the first one
df = df.drop_duplicates(subset='Product ID', keep='first')
# Setting the index to Product ID
df = df.set_index('Product ID')
# Removing rows with all missing values
df = df.dropna(how='all')
# Removing the row with missing price value
df = df.dropna(subset=['Price'])
# Removing whitespace and special characters from the Category column
df['Category'] = df['Category'].str.replace('[^a-zA-Z0-9]', '', regex=True)

# Grouping the data by Category showing the mean price
df_category = df.groupby(['Category','Material'])['Price'].agg(AveragePrice ='mean')
df_category = df_category.reset_index()

# Printing the result
print(f"Result: \n{df_category}")
