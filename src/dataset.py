import pandas as pd

# Sample data: student names and their scores
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math": [85, 92, 78, 90, 88],
    "Science": [89, 94, 72, 91, 85],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Show the first few rows
print("Original Data:")
print(df)

# Add a new column: average score
df["Average"] = df[["Math", "Science"]].mean(axis=1)

# Filter: students with average > 85
high_achievers = df[df["Average"] > 85]

# Display results
print("\nHigh Achievers (Average > 85):")
print(high_achievers)

# Basic stats
print("\nSummary Statistics:")
print(df.describe())

df.head(2)

# Interactive session
# This code is designed to be run in an interactive Python environment.
