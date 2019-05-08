import os 
import csv
import string

csv_path = os.path.join("employee_data.csv")

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

new_employee_data = []

with open(csv_path, newline = '') as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        Emp_ID = row["Emp ID"]
        First_Name = row["Name"].split(" ")[0]
        Last_Name = row["Name"].split(" ")[1]
        Year = row["DOB"].split("-")[0]
        Month = row["DOB"].split("-")[1]
        Date = row["DOB"].split("-")[2]
        DOB = f"{Month}/{Date}/{Year}"
        SSN_last4 = row["SSN"].split("-")[2]
        SSN = f"***-**-{SSN_last4}"
        State = us_state_abbrev[row["State"]]
        new_employee_data.append(
            {
                "Emp ID": Emp_ID, 
                "First Name": First_Name, 
                "Last Name": Last_Name, 
                "DOB": DOB, 
                "SSN": SSN, 
                "State": State
            }
        )

_, filename = os.path.split(csv_path)


output_path = os.path.join("output", filename)
with open(output_path, "w") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)





    
