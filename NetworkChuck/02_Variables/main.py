import sys

"""
Variables - Let's build a robot Barista!!
Networkchuck let’s go deeper into Python!! // Python RIGHT NOW!! // EP 2
@see https://www.youtube.com/watch?v=IXr0-J5XXMA
"""


# implements a robot barista ... sort of
def barista():
    print("Hello, welcome to NetworkChuck Coffee!!!!!!! :D !!!")
    name = input("What is our name ? ")
    print(f"Hello {name}, thank you so much for coming in today.")

    return


def main() -> int:
    barista()
    return 0


# main entry point
# see https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    sys.exit(main())