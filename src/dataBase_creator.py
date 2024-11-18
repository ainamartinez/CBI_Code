import csv
import random
from datetime import datetime, timedelta

# Define the file name
file_name = './files/dataCons.csv'

# We define colum names
columns = ['Date', 'Room 1', 'Cons1', 'Room 2', 'Cons2', 'Room 3', 'Cons3','Room 4', 'Cons4', 'Room 5', 'Cons5', 'Room 6', 'Cons6', 'Room 7', 'Cons7', 'Room 8', 'Cons8', 'Room 9', 'Cons9', 'Room 10', 'Cons10']

# Open the file in write mode
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the column names
    writer.writerow(columns)

print(f"CSV file '{file_name}' created with columns: {columns}")
# Define the start and end dates
start_date = datetime(2024, 6, 1)
end_date = datetime(2024, 6, 18)

# Generate the date range with 30-minute intervals
date_range = [start_date + timedelta(minutes=15*x) for x in range(int((end_date - start_date).total_seconds() / 1800))]

# Write the data rows
with open(file_name, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    for date in date_range: #For each date in the date range
        row = [date.strftime('%Y-%m-%d %H:%M:%S')]
        for i in range(10): #Each room
            # Check if the time is between 1:30 and 7:30
            if 1 <= date.hour < 7 or (date.hour == 7 and date.minute < 30): #We consider that the rooms DON'T consume water between 1:00 and 7:30
                is_open = 0
            else:
                if 7 <= date.hour < 11 or 20 <= date.hour < 23:
                    is_open = random.choices([0, 1], weights=[0.8, 0.2])[0] # 20% chance of no water consumption, 80% chance of water consumption
                else:
                    is_open = random.choices([0, 1], weights=[0.95, 0.05])[0] # 80% chance of no water consumption, 20% chance of water consumption
            
            if is_open == 0:
                consumption = 0
            else:
                if 7 <= date.hour < 11 or 20 <= date.hour < 23:
                    if random.choices([0, 1], weights=[0.9, 0.1])[0] == 1:
                        consumption = round(random.gauss(160, 0.05), 2)
                    else:
                        consumption = round(random.gauss(1.5, 0.1), 2)
                else:
                    consumption = round(random.gauss(1.5, 0.1), 2)
            row.extend([is_open, consumption])
        writer.writerow(row)

print(f"Data rows added to CSV file '{file_name}'")