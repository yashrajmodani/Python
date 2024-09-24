#file handling


import csv

data = [
    {'name': 'Nikhil', 'age': '23',  'grade': 9.0},
    {'name': 'Mayur', 'age': '23',  'grade' : 'marks mat  dede'},
    {'name': 'Aditya', 'age': '23', 'grade' : 9.3},
    {'name': 'Sagar', 'age': '23', 'grade': 9.5},
    {'name': 'Prateek', 'age': '23',  'grade': 7.8},
    {'name': 'Sahil', 'age': '23', 'grade': 9.1}
]

with open('university_records.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)