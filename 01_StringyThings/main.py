import sys

"""
This is a multiline string.
Python does not know multiline comments /* ... */ like C.
BUT! One can define multiline strings, and Python will ignore these as long as they are not used.
"""


# our shiny main function
def main() -> int:  # here we gave a type hint for integer
    print('this is spartaaa!')
    # this is a single line comment - awesome :D
    print("Tony Stark said: \"I am Iron Man!\"")  # print with escaping
    print("This will be\nshown on\nmultiple lines!")

    print("""Three quotation marks
define a multiline string so no escaped
newline characters are necessary""")

    print("Funky " + "string " + "concatenation!")

    # define a variable, and print it's value using a format string
    number = 42
    print(f'Surprise, the number is {number}!')

    # print a string N times!
    nTimes = 3
    print('This is sparta! ' * nTimes)

    return 0  # be nice and return an int


# seems to be the idiomatic usage of main entry point
# see https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    sys.exit(main())
