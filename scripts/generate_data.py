import pandas as pd #load the needed tool

# Sample sales data
data = {
    'Invoice_ID': ['INV001', 'INV002', 'INV003', 'INV004', 'INV005','INV006', 'INV007', 'INV008', 'INV009', 'INV0010'],
    'Region': ['North', 'South', 'East', 'West', 'North','North', 'North', 'West', 'West', 'East' ],
    'Sales_Amount': [2500, 1800, 2300, 1900, 2700,2506, 1600, 1800, 1900, 2000],
}

# Create DataFrame (turn data to pandas dataframe)
df = pd.DataFrame(data)
# Define tax rates per region
region_tax_rates = {
    'North': 0.10,
    'South': 0.08,
    'East': 0.09,
    'West': 0.07
}

# Map tax rate based on region
df['Tax_Rate'] = df['Region'].map(region_tax_rates)

# Calculate Tax and Total
df['Tax_Amount'] = df['Sales_Amount'] * df['Tax_Rate']
df['Total_Amount'] = df['Sales_Amount'] + df['Tax_Amount']

# Save to Excel
df.to_excel('./data/sales_tax_data.xlsx', index=False)

print("✅ Sales data with tax saved to data/sales_tax_data.xlsx")  
