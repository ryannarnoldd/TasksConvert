import sys
import json

tasks = open('tasks.txt', 'r').readlines()
history = json.load(open('history.json', 'r'))

dateStart = sys.argv[1]
year_and_month = dateStart[:7]
day = int(dateStart[8:])

for task in tasks:
    date = year_and_month + '-' + f'{day:02d}'
    task, verse = task.split(' - ')

    history[date] = {
        'title': '',
        'description': task,
        'verse': verse.strip()
    }

    day += 1
    
json.dump(history, open('history.json', 'w'), indent=4)