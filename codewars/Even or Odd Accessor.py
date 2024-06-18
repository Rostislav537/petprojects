# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers. The function should also return "Even" or "Odd" when accessing a value at an integer index.
#
# For example:
#
# evenOrOdd(2); //'Even'
# evenOrOdd[2]; //'Even'
# evenOrOdd(7); //'Odd'
# evenOrOdd[7]; //'Odd'



class EvenOrodd:
    def __call__(self, num):
        return "Even" if num%2 == 0 else "Odd"
    def __getitem__(self, item):
        return "Even" if item % 2 == 0 else "Odd"


even_or_odd = EvenOrodd()

