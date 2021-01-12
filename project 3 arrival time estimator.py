from datetime import datetime, timedelta, date, time

import locale

#lfg!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def date_input():
    while True:
        date = input("Estimated date of departure (YYYY-MM-DD): ")
        format = '%Y-%m-%d'
        try:
            date = datetime.strptime(date, format)
            return date
        except ValueError:
            print("Invalid format. Please try again.")
            continue

def time_input():
    while True:
        time = input("Estimated time of departure (HH:MM AM/PM): ")
        format = '%I:%M %p'
        try:
            time = datetime.strptime(time, format)
            return time
        except ValueError:
            print("Invalid format. Please try again.")
            continue

def miles_input():
    while True:
        miles = input("Enter Miles: ")
        try:
            miles = int(miles)
            if miles <= 0:
                print("Invalid entry. Please enter a number greater than zero.")
            else:
                return miles
        except ValueError:
            print("Invalid format. Please Try again.")
            continue
def mph_input():
    while True:
        speed = input("Enter Miles per Hour: ")
        try:
            mph = int(speed)
            if mph <= 0:
                print("Invalid entry. Please enter a number greater than zero.")
            else:
                return mph
        except ValueError:
            print("Invalid format. Please Try again.")
            continue
        
def run_it(date, time, miles, mph):
    merged = datetime.combine(date.date(), time.time())
    h = int(miles/mph)
    m1 = (miles % mph)
    m2 = mph/60
    if(m1 == 0):
        m = 0
    else:
        m = int(m1 / m2)

    print("Estimated Travel Time")
    print("Hours: ", h)
    print("Minutes: ", m)

    estimatedtime = merged + timedelta(hours=h) + timedelta(minutes=m)
    format = '%Y-%m-%d'
    new_date = datetime.strftime(estimatedtime, format)
    format = '%I:%M %p'
    new_time = datetime.strftime(estimatedtime, format)
    print("Estimated date of arrival: ", new_date)
    print("Estimated time of arrival: ", new_time)
    

def main():
    print("Arrival Time Estimator")
    print("")
    choice = "y"
    while choice.lower() == "y":
        date = date_input()
        time = time_input()
        miles = miles_input()
        mph = mph_input()
        run_it(date, time, miles, mph)
        choice = input("Continue (y/n)? ").lower()
    print("")
    print("Calc-you-later!")

    
if __name__ == "__main__":
    main()
    




