# Find the fine
# Given an array of car numbers car[], an array of penalties fine[], and an integer date, determine the total fine collected on that date. The fine is collected based on parity, i.e., on an even date, fines are collected from odd-numbered cars, and on an odd date, fines are collected from even-numbered cars.

# Examples:
# Input: date = 12, car[] = [2375, 7682, 2325, 2352], fine[] = [250, 500, 350, 200]
# Output: 600
# Explanation: The date is 12 (even), so we collect the fine from odd-numbered cars. The odd-numbered cars and the fines associated with them are as follows:
# 2375 -> 250
# 2325 -> 350
# The sum of the fines is 250+350 = 600
# Input: date = 8, car[] = [2222, 2223, 2224], fine[] = [200, 300, 400]
# Output: 300

def totalFine( date, car, fine):

    total = 0

    for i in range(len(car)):

        # Even date → odd cars pay fine
        if date % 2 == 0:

            if car[i] % 2 != 0:
                total += fine[i]

            # Odd date → even cars pay fine
        else:
            if car[i] % 2 == 0:
                total += fine[i]

    return total

print(totalFine(date = 12, car = [2375, 7682, 2325, 2352], fine = [250, 500, 350, 200]))
print(totalFine(date = 8, car = [2222, 2223, 2224], fine = [200, 300, 400]))