'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''
current = 380123456
born_per_y = 52 * 24 * 60 * 10
dies_per_y = 52 * 24 * 60 * 5
immigrants_per_y = 52 * 24 * 60 * 1.5
total_after_1 = current + born_per_y + immigrants_per_y - dies_per_y
print(int(total_after_1))
total_after_2 = total_after_1 + born_per_y + immigrants_per_y - dies_per_y
print(int(total_after_2))
total_after_3 = total_after_2 + born_per_y + immigrants_per_y - dies_per_y
print(int(total_after_3))
