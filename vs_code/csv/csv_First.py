import pandas as pd
import datetime

current_time = datetime.datetime.now()
# initialise data dictionary.
data_dict = {'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
			
			'Time': [current_time, current_time, current_time, current_time,
						current_time, current_time, current_time, current_time,
						current_time, current_time],
		
			'Coordinates': [(12,45,78,65), (20,12,78,54), (30,25, 60, 70), (10,15, 21, 22), (25,60, 70,
								15), (60,33,78,43), (70,11,46,74),
								(15,64,86,34), (21,24,84,12), (22,75,23,75)]}

# Create DataFrame
data = pd.DataFrame(data_dict)

# Write to CSV file
data.to_csv(f"Customers{1}.csv")

# Print the output.
print(data)
