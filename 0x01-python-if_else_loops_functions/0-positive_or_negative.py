#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print("{:d} is positive".format(number))
<<<<<<< HEAD
    elif number == 0:
        print("{:d} is zero".format(number))
        else:
            print("{:d} is negative".format(number))
=======
elif number < 0:
    print("{:d} is negative".format(number))
else:
    print("{:d} is zero".format(number))
>>>>>>> c35725bf74534379f1f94ff7bb962d561151e23b
