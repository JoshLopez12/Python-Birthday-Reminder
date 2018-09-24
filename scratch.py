import datetime
import os

#today's date stored in variable and put into MMDD format
date = datetime.date.today()
today = str('{:02d}'.format(date.month)) + str('{:02d}'.format(date.day))

#variables to keep track of number of birthdays, upcoming birthdays, and lines in txt file
birthdayCount = 0
upcomingCount = 0
lineCount = 0

#list of dates for the next week
daysList = []
#list of names with birthdays today
birthdayList = []
#dictionary of names and dates of birthdays in next week
upcomingList = {}

#loop to store dates (MMDD format) for next 7 days in daysList
for x in range(1,8):
    upcoming = (date + datetime.timedelta(days = x))
    upcomingDate = str('{:02d}'.format(upcoming.month)) + str('{:02d}'.format(upcoming.day))
    daysList.append(upcomingDate)

#user enters a file that must be .txt
birthdayFile = input("Enter birthday file: ")
if not birthdayFile.endswith('.txt'):
    print("Error: Input file must be .txt")
    exit()

try:
    file = open(birthdayFile, "r")

    #tests if file is empty
    if os.stat(birthdayFile).st_size == 0:
        print("The file is empty")
    else:
        for line in file:
            lineCount += 1
            wordList = line.split()

            #tests line format
            if len(wordList) < 2:
                print("Warning: Incorrect format on line" , lineCount , ":" , line)
                break

            test = wordList[-1]

            #tests date format
            if len(test) == 4:
                try:
                    mon = int(test[:2])
                    day = int(test[2:])
                except ValueError:
                    print("Warning: Invalid date for " + line.rsplit(' ', 1)[0] + ' (' + test + ')')
                try:
                    d = datetime.date(2000,mon,day)
                except ValueError:
                    print("Warning: Invalid date for " + line.rsplit(' ', 1)[0] + ' (' + test + ')')
            else:
                print("Warning: Invalid date for " + line.rsplit(' ', 1)[0] + ' (' + test + ')')

            #loop that adds names/dates to birthdayList or upcomingList
            for word in line.split():
                if word == today:
                    birthdayList.append(line.rsplit(' ', 1)[0])
                    birthdayCount += 1
                elif word in daysList:
                    upcomingList[line.rsplit(' ',1)[0]] = word
                    upcomingCount += 1
        print("\nBirthdays Today:")
        if birthdayCount == 0:
            print("There are no birthdays today.")
        else:
            #contents of birthdayList are sorted and printed
            for x in sorted(birthdayList):
                print(x)
        print("\nUpcoming Birthdays:")
        if upcomingCount == 0:
            print("There are no birthdays coming up in the next 7 days")
        else:
            #contents of upcomingList dictionary are sorted by value, then key
            for x, y in sorted(upcomingList.items(), key = lambda x: (x[1],x[0])):
                print(x, '(' + y[:2] + '/' + y[2:] + ')')
except IOError:
    print("Error: File is invalid or does not exist")