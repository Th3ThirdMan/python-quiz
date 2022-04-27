"""
# Module pyfiglet needed for ASCII output for start and game over functions.
# Module needed to add a brief delay in output.
# Module needed to enact random question data for the quiz.
"""
import time
#import random
import pyfiglet


questions_quiz = [
    "Who created Python?\n\n"
    "A: Guido van Rossum\n"
    "B: Brendan Eich\n"
    "C: Bill Gates\n"
    "D: Tim Berners-Lee",
    "In what year was Python released?\n\n"
    "A: 1990\n"
    "B: 1991\n"
    "C: 1992\n"
    "D: 1993\n",
    "What famous comedy act was Python named after?\n\n"
    "A: Laurel and Hardy\n"
    "B: Statler & Waldorf\n"
    "C: Monty Python\n"
    "D: Penn and Teller\n",
    "What is a Tuple?\n\n"
    "A: Nothing to do with Python\n"
    "B: A song\n"
    "C: A flower\n"
    "D: Something that is used to store multiple items in a single variable\n",
    "What keyword is used to define a function in Python?\n\n"
    "A: def\n"
    "B: let\n"
    "C: var\n"
    "D: const\n",
    "What is short Else If in Python?\n\n"
    "A: if\n"
    "B: elif\n"
    "C: else\n"
    "D: Elves\n",
    "What does IDE stand for?\n\n"
    "A: It Doesn't Exist\n"
    "B: Internally Developed Environ\n"
    "C: Integrated Development Environment\n"
    "D: It Does Exist\n",
    "What returns a random float number between 0 and 1?\n\n"
    "A: setstate()\n"
    "B: randrange()\n"
    "C: randint()\n"
    "D: random()\n",
    "What does JSON stand for?\n\n"
    "A: JavaScript Object Notation\n"
    "B: July September October November\n"
    "C: Java Object Noteriety\n"
    "D: Who's Jason?\n",
    "To get a data type of an object, what function would one use?\n\n"
    "A: int()\n"
    "B: type()\n"
    "C: range()\n"
    "D: str()\n",
    "Who composed the poem, 'The Zen of Python'?\n\n"
    "A: Alan Peters\n"
    "B: John Peters\n"
    "C: Tim Peters\n"
    "D: Rob Peters\n",
    "Python has overtaken what language to be the most "
    "popular in schools?\n\n"
    "A: German\n"
    "B: Italian\n"
    "C: Spanish\n"
    "D: French\n"
]


def start_image():
    """
    This is a function that enacts an ASCII output.
    """
    result = pyfiglet.figlet_format("The Python Quiz")
    print("\n\nHello and Welcome to.... ")
    print(result)
    time.sleep(2)


start_image()


def start_game():
    """
    Function to start the Python Quiz game.
    """
    time.sleep(2)


start_game()
