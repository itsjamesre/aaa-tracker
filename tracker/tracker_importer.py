# open file & create csvreader
import csv
from test_tracker.models import Test, Club, Specialist, TestType, Specialist, Component, Variable, Winner, Status,BusinessLine

# 0-UIUX, 1-CLUB,2-BL,3-TARGET PRODUCT,4-TEST TYPE,5-COMPONENT,
# 6-VARIABLE,7-JIRA URL,8-TARGET URL,9-TITLE,10-WINNER,11-STATUS

#loop:
with open('thetests.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
    	club = Club(full_name=row[1],short_code=row[0])
    	club.save()
        print(row[9]) # Title
