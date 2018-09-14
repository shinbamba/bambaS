#the_bomber_men: Shin Bamba, Yin On Chan
#SoftDev1 pd8
#06: StI/O: Divine your Destiny!
#2018-09-13

import csv
import random

values = {} #makes dictionary
with open('occupations.csv') as csvfile: #opens the file for reading as a csvfile
    reader = csv.DictReader(csvfile) #specaltype of reading that lets us use the first row as lables for the columns
    for row in reader:
        values[row['Job Class']] = float(row['Percentage']) #for each row put each column pair in the dictionary
del values['Total'] #delete the last "total" value

def pick_job(dictionary):
    list_jobs = [] #makes empty list
    for key in dictionary:
        num_jobs = int(10*dictionary[key]) #takes the value of each key and makes it put 10x that number of keys into the list
        while num_jobs > 0:
            list_jobs.append(key)
            num_jobs -= 1
    return random.choice(list_jobs) #choose a random value in the mega list

print(pick_job(values))
