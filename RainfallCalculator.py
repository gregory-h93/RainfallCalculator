def toFixed(value, digits):
    return "%.*f" % (digits, value)

def firstHalf():
    firstHalfRainfall = [0] * (6)
    months = [""] * (6)
    
    months[0] = "January"
    months[1] = "February"
    months[2] = "March"
    months[3] = "April"
    months[4] = "May"
    months[5] = "June"
    index = 0
    total = 0
    counter = 0
    for index in range(counter, 6 - 1 + 1, 1):
        print("Enter the rainfall for " + months[index] + ": ")
        firstHalfRainfall[index] = float(input())
        while firstHalfRainfall[index] < 0:
            print("Invalid input! Enter the rainfall for " + months[index] + ": ")
            firstHalfRainfall[index] = float(input())
        counter = counter + 1
    lowest = getLowest(firstHalfRainfall, 6)
    highest = getHighest(firstHalfRainfall, 6)
    total = getTotal(firstHalfRainfall, 6)
    average = total / 6
    print("The lowest rainfall for the first half was " + str(lowest) + " inches of rain.")
    print("The highest rainfall for the first half was " + str(highest) + " inches of rain.")
    print("The total rainfall for the first half was " + str(total) + " inches of rain.")
    print("The average rainfall for the first half is " + toFixed(average,2) + " inches of rain.")

def getHighest(array, arraySize):
    highest = array[0]
    for index in range(1, arraySize - 1 + 1, 1):
        if array[index] > highest:
            highest = array[index]
    
    return highest

def getLowest(array, arraySize):
    lowest = array[0]
    for index in range(1, arraySize - 1 + 1, 1):
        if array[index] < lowest:
            lowest = array[index]
    
    return lowest

def getTotal(array, arraySize):
    total = 0
    for index in range(0, arraySize - 1 + 1, 1):
        total = total + array[index]
    
    return total

def secondHalf():
    secondHalfRainfall = [0] * (6)
    months = [""] * (6)
    
    months[0] = "July"
    months[1] = "August"
    months[2] = "September"
    months[3] = "October"
    months[4] = "November"
    months[5] = "December"
    index = 0
    total = 0
    counter = 0
    for index in range(counter, 6 - 1 + 1, 1):
        print("Enter the rainfall for " + months[index] + ": ")
        secondHalfRainfall[index] = float(input())
        while secondHalfRainfall[index] < 0:
            print("Invalid input! Enter the rainfall for " + months[index] + ": ")
            secondHalfRainfall[index] = float(input())
        counter = counter + 1
    lowest = getLowest(secondHalfRainfall, 6)
    highest = getHighest(secondHalfRainfall, 6)
    total = getTotal(secondHalfRainfall, 6)
    average = total / 6
    print("The lowest rainfall for the second half was " + str(lowest) + " inches of rain.")
    print("The highest rainfall for the second half was " + str(highest) + " inches of rain.")
    print("The total rainfall for the second half was " + str(total) + " inches of rain.")
    print("The average rainfall for the second half is " + toFixed(average,2) + " inches of rain.")

def wholeYear():
    wholeYearRainfall = [0] * (12)
    months = [""] * (12)
    
    months[0] = "January"
    months[1] = "February"
    months[2] = "March"
    months[3] = "April"
    months[4] = "May"
    months[5] = "June"
    months[6] = "July"
    months[7] = "August"
    months[8] = "September"
    months[9] = "October"
    months[10] = "November"
    months[11] = "December"
    index = 0
    total = 0
    counter = 0
    for index in range(counter, 12 - 1 + 1, 1):
        print("Enter the rainfall for month " + months[index] + ": ")
        wholeYearRainfall[index] = float(input())
        while wholeYearRainfall[index] < 0:
            print("Invalid input! Enter the rainfall for " + months[index] + ": ")
            wholeYearRainfall[index] = float(input())
        counter = counter + 1
    lowest = getLowest(wholeYearRainfall, 12)
    highest = getHighest(wholeYearRainfall, 12)
    total = getTotal(wholeYearRainfall, 12)
    average = total / 12
    print("The lowest rainfall for the whole year was " + str(lowest) + " inches of rain.")
    print("The highest rainfall for the whole year was " + str(highest) + " inches of rain.")
    print("The total rainfall for the whole year was " + str(total) + " inches of rain.")
    print("The average rainfall for the whole year is " + toFixed(average,2) + " inches of rain.")

# Main
while True:    #This simulates a Do Loop
    print("Would you like to calculate the rainfall for the first 6 months, the last 6 months, or the whole year? (1,2, or 3)")
    which = int(input())
    while which < 1 or which > 3:
        print("Invalid input! Please enter a number within the designated range. Would you like to calculate the rainfall for the first 6 months, the last 6 months, or the whole year? (1,2, or 3)")
        which = int(input())
    if which == 1:
        firstHalf()
    else:
        if which == 2:
            secondHalf()
        else:
            wholeYear()
    print("Would you like to run another calculation? (Y/N)")
    again = input()
    while again != "Y" and again != "y" and again != "N" and again != "n":
        print("Please enter in (Y/N). Would you like to run another calculation? (Y/N)")
        again = input()
    if not(again == "Y" or again == "y"): break   #Exit loop
print("You have chosen to end the program. Goodbye!")
