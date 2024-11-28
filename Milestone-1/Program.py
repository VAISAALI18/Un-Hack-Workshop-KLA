import pandas as pd
import numpy as np

# Load the datasets
ca = pd.read_csv("Dataset-0\\Dataset-0\\1st\\CareAreas.csv")
md = pd.read_csv("Dataset-0\\Dataset-0\\1st\\metadata.csv")

# Extract the size of mainfield and subfield and carearea
mf = md.iloc[0, 0]  
sf = md.iloc[0, 1] 
c_area=np.abs(ca.iloc[1,1]-ca.iloc[1,2] )

#Adjustment for main field
a=(mf-c_area)/2

# Create a list to store the results for main fields
main_fields = []
mid=-1
# Main field calculation
for i in range(len(ca)):
    mid+=1
    x1 = ca.iloc[i, 1] - a
    x2 = x1 + mf
    y1 = ca.iloc[i, 3] - a
    y2 = y1 + mf
    main_fields.append([mid,x1, x2, y1, y2])

# Convert the list to a DataFrame for main fields
mdf = pd.DataFrame(main_fields)
# Save the DataFrame to a CSV file
mdf.to_csv("C:\\Users\\vaisa\\Downloads\\UNHACK-24\\Dataset-0\\Dataset-0\\1st\\MainFields.csv", index=False)

# Create a list to store the results for subfields
sub_fields = []
c=-1
# Subfield calculation
for i in range(len(ca)):
    mid = ca.iloc[i, 0]
    x1 = ca.iloc[i, 1]
    x2 = x1 + sf
    y1 = ca.iloc[i, 3]
    y2 = y1 + sf

    # Generate subfields for the current row
    while ((y2-ca.iloc[i, 4])<sf):  # Loop through the y2 values
        while ((x2-ca.iloc[i, 2])<sf):  # Loop through the x2 values
            c+=1
            sub_fields.append([ c,x1, x2, y1, y2,mid])
            x1 += sf
            x2 = x1 + sf
        # Reset x1 and x2 for the next y2 value
        x1 = ca.iloc[i, 1]
        x2 = x1 + sf
        y1 += sf
        y2 = y1 + sf

# Convert the list to a DataFrame for subfields
sdf = pd.DataFrame(sub_fields)
# Save the DataFrame to a CSV file
sdf.to_csv("C:\\Users\\vaisa\\Downloads\\UNHACK-24\\Dataset-0\\Dataset-0\\1st\\SubFields.csv", index=False)

print("Main Fields and Sub Fields have been saved successfully.")
