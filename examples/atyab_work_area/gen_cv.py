import pandas as pd
from datetime import datetime, timedelta

# Generate date range from March 3, 2024, to today
start_date = datetime(2024, 3, 3)
end_date = datetime.now()
date_range = pd.date_range(start=start_date, end=end_date)

# List of trainee names
trainee_names = ["Abbas", "Abdul Aziz", "Haitham", "Lujain", "Maather", "Rudaina", "Sara", "Sughiya", "Ziyad"]

# Create the DataFrame
data = {
    "Date": [],
    "Trainee": [],
    "Attendance": []
}

for current_date in date_range:
    for trainee in trainee_names:
        data["Date"].append(current_date.date())
        data["Trainee"].append(trainee)
        data["Attendance"].append("Present")

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = "genz_attendance_records.csv"
df.to_csv(csv_file_path, index=False)
