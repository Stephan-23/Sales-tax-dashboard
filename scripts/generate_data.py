import pandas as pd #load the needed tool

# Sample sales data
data = {
    'Invoice_ID': ['INV001', 'INV002', 'INV003', 'INV004', 'INV005'],
    'Region': ['North', 'South', 'East', 'West', 'North'],
    'Sales_Amount': [2500, 1800, 2300, 1900, 2700],
    'Tax_Rate': [0.10, 0.08, 0.09, 0.07, 0.10]
}

# Create DataFrame (turn data to pandas dataframe)
df = pd.DataFrame(data)

# Calculate Tax and Total
df['Tax_Amount'] = df['Sales_Amount'] * df['Tax_Rate']
df['Total_Amount'] = df['Sales_Amount'] + df['Tax_Amount']

# Save to Excel
df.to_excel('./data/sales_tax_data.xlsx', index=False)

print("✅ Sales data with tax saved to data/sales_tax_data.xlsx")
