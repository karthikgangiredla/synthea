import pandas as pd  

# Load the cleaned CSV  
df = pd.read_csv("cleaned_file.csv", low_memory=False)  

# Remove columns with more than 90% null values  
threshold = 0.9 * len(df)  
df_cleaned = df.dropna(thresh=threshold, axis=1)  

# Save the cleaned file  
df_cleaned.to_csv("final_cleaned_file.csv", index=False)  
