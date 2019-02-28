'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively.

'''

week_dict = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
day_number = int(input("Which day of the week by numbers? :"))


if day_number not in week_dict:
    print("Other")

elif day_number in week_dict:
    print(week_dict[day_number])

#not sure how a nested if applies here - it was only messing it up