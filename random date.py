import random  
import time
def getRandomDate(startDate, endDate):  
    print("Printing random date between", startDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date = ", getRandomDate("1/1/2018", "12/12/2025"))
