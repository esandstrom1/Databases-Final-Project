#Ethan Sandstrom
#Databases final project Fall 2023

#Implement basic querying abilities through python

import sqlite3

conn = sqlite3.connect('causes.db')
cursor = conn.cursor()

print("\n\n\n\n\n\n\n\n\n\n")

invalid = True
while invalid:
    num_results = int(input("Return 5 or 10 results? (5 or 10): "))
    if num_results == 5 or num_results == 10:
        invalid = False 


while 1:
    state = input("Enter the name of a state or 'all' to see results for any state\n")
    year = input("Enter a year or 'all' to see results for any year\n")

    if state == "all":
        if year == "all":
            query = f"SELECT Cause_Name, Deaths, Year FROM DATA WHERE Cause_Name != 'All causes' ORDER BY Deaths DESC LIMIT {num_results}"
            cursor.execute(query)
            print(f"Top 5 causes of death from 1999-2005")
        else:
            query = f"SELECT Cause_Name, Deaths, Year FROM DATA WHERE Year=? AND Cause_Name != 'All causes' ORDER BY Deaths DESC LIMIT {num_results}"
            cursor.execute(query, (int(year),))
            print(f"Top 5 causes of death for year {year}")
    else:
        if year == "all":
            query = f"SELECT Cause_Name, Deaths, Year FROM DATA WHERE State=? AND Cause_Name != 'All causes' ORDER BY Deaths DESC LIMIT {num_results}"
            cursor.execute(query, (state,))
            print(f"Top 5 causes of death in {state} from 1999-2017")
        else:
            query = f"SELECT Cause_Name, Deaths, Year FROM DATA WHERE State=? AND Year=? AND Cause_Name != 'All causes' ORDER BY Deaths DESC LIMIT {num_results}"
            cursor.execute(query, (state, year,))
            print(f"Top causes of death in {state} in {year}")

    results = cursor.fetchall()
    for index, row in enumerate(results, start=1):
        num_of_deaths = f"{row[1]:,}"
        if year == "all":
            print(f"#{index:<2}: {row[0]:<20} {num_of_deaths:<6} {row[2]:5}")
        else:
            print(f"#{index:<2}: {row[0]:<15} {num_of_deaths:<5}")
    print()


conn.close()
