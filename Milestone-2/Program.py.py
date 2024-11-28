import pandas as pd
import numpy as np

# Load the datasets
ca = pd.read_csv("Dataset-1\\2nd\\careareas.csv")
md = pd.read_csv("Dataset-1\\2nd\\metadata.csv")

# Extract the size of mainfield and subfield and carearea
mf = md.iloc[0, 0]
sf = md.iloc[0, 1]
c_area = np.abs(ca.iloc[1, 1] - ca.iloc[1, 2])

# Adjustment for main field
a = np.sqrt(mf)/ 2

# Create a list to store the results for main fields
main_fields = []
mid = -1

# Dictionary to keep track of highest y1 for each x1
x1_y1_dict = {}

# Main field calculation
for i in range(len(ca)):
    
    if (ca.iloc[i, 1] - a) < 0:
        x1 = ca.iloc[i, 1]
    else:
        x1 = ca.iloc[i, 1] - a
    x2 = x1 + mf
    if (ca.iloc[i, 3] - a) < 0:
        y1 = ca.iloc[i, 3]
    else:
        y1 = ca.iloc[i, 3] - a

    # Update dictionary with the highest y1 for each x1
    if x1 not in x1_y1_dict:
        x1_y1_dict[x1] = y1
    else:
        x1_y1_dict[x1] = max(x1_y1_dict[x1], y1)

# Create main fields based on the highest y1 values

for x1, y1 in x1_y1_dict.items():
    x2 = x1 + mf
    y2 = y1 + mf
    mid+=1
    main_fields.append([mid, x1, x2, y1, y2])

# Convert the list to a DataFrame for main fields
mdf = pd.DataFrame(main_fields, columns=['mid', 'x1', 'x2', 'y1', 'y2'])
# Save the DataFrame to a CSV file
mdf.to_csv("Dataset-1\\2nd\\Mainfield.csv", index=False)

# Create a list to store the results for subfields
sub_fields = []
c = -1

# Subfield calculation
for i in range(len(ca)):
    mid = ca.iloc[i, 0]
    x1 = ca.iloc[i, 1]
    x2 = x1 + sf
    y1 = ca.iloc[i, 3]
    y2 = y1 + sf

    # Generate subfields for the current row
    while ((y2 - ca.iloc[i, 4]) < sf):  # Loop through the y2 values
        while ((x2 - ca.iloc[i, 2]) < sf):  # Loop through the x2 values
            c += 1
            sub_fields.append([c, x1, x2, y1, y2, mid])
            x1 += sf
            x2 = x1 + sf
        # Reset x1 and x2 for the next y2 value
        x1 = ca.iloc[i, 1]
        x2 = x1 + sf
        y1 += sf
        y2 = y1 + sf

# Convert the list to a DataFrame for subfields
sdf = pd.DataFrame(sub_fields, columns=['SID', 'x1', 'x2', 'y1', 'y2', 'mid'])
# Save the DataFrame to a CSV file
sdf.to_csv("Dataset-1\\2nd\\SubField.csv", index=False)

print("Main Fields and Sub Fields have been saved successfully.")
