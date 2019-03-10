'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

shop = [i + " " + j for i in colors for j in sizes]
print(shop)