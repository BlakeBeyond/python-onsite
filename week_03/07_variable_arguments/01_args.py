'''
Write a script with a function that demonstrates the use of *args.

'''


def lazy_teaching (*args):
    print(args[1], args[2])
    if args[3]:
        print(args[2] * args[3])
    if args[6]:
        print("you've had enough arguments already")