# Problem: Selecting the perfect car option in my budget range and lifestyle

cars = ['Honda', 'Toyota', 'Audi', 'BMW', 'Acura', 'Mercedes',
        'Lexus', 'McLaren', 'Porsche', 'Maserati']  # list of car brands
carTypes = ['Sedan', 'SUV', 'Van']  # list of car types
cars2 = []  # list for selected cars
carTypes2 = []  # list for chosen car type


def budget():

    print('List of a few car brands: ')

    for a in cars:  # for a in cars list
        print('-', a)  # prints each element inside the cars lists

    print('Your budget should be more than $10,000!')

    # User Input
    low = float(input('What is your minimum budget: $'))
    high = float(input('What is your maximum budget: $'))

    avgBudget = round(((low + high)/2), 2)  # calculates the average budget
    print('Average Budget = $', avgBudget)

    # if and elif statements to append best cars into the cars2 list
    # if avgBudget is less than or equal to 50000 and avgBudget is greater than or equal to 20000
    if avgBudget <= 50000 and avgBudget >= 20000:
        cars2.append(cars[0])
        cars2.append(cars[1])

    # else if avgBudget is less than or equal to 80000 and avgBudget is greater than 50000
    elif avgBudget <= 80000 and avgBudget > 50000:
        cars2.append(cars[6])
        cars2.append(cars[4])

    # else if avgBudget is greater than 80000 and avgBudget is less than or equal to 150000
    elif avgBudget > 80000 and avgBudget <= 150000:
        cars2.append(cars[3])
        cars2.append(cars[5])

    elif avgBudget > 150000:  # else if avgBudget is greater than 150000
        cars2.append(cars[7])
        cars2.append(cars[8])
        cars2.append(cars[9])

    else:
        print('Your average budget is too less')
        exit()
    print('------------------------------')


def carType():

    # Program will recommend what car type would be the better choice
    while True:
        # user enters the number of family members
        x = int(input('Enter the number of people in your family: '))
        if x > 8:
            print('Consider buying a transit van')
            break
        elif x > 5 and x <= 8:
            carTypes2.append(carTypes[2])  # append into list carTypes2
            break
        elif x <= 5:
            carTypes2.append(carTypes[0])
            carTypes2.append(carTypes[1])
            break


def fuelOption():
    ans = ''  # empty string
    while True:  # User will need to enter either yes or no to proceed
        fuelType = input(
            'Enter yes or no if you want to save money in the long run: ').lower()
        if fuelType == 'yes':  # if fuelType is 'yes'
            # concatenate following string to ans
            ans += 'You should go for an electric or hybrid vehicle'
            break
        elif fuelType == 'no':  # if fuelType is 'no'
            ans += 'You should go for a gas vehicle'  # concatenate following string to ans
            break
    print('--------------------------------')
    return ans


def printResults():
    print(fuelOption())
    print('Best car options: ')
    for i in cars2:  # for i in cars2 list
        print(i)
    print('Best car type option(s): ')
    for j in carTypes2:  # for j in carTypes2 list
        print(j)


budget()
carType()
printResults()
