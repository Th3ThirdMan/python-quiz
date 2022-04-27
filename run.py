"""
# Module pyfiglet needed for ASCII output for start and game over functions.
# Module needed to add a brief delay in output.
# Module needed to enact random question data for the quiz.
"""
import time
import random
import pyfiglet


class Question:
    """
    This class creates a method to initialize question objects.
    """

    def __init__(self, query, answer):
        self.query = query
        self.answer = answer


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


questions = [
    Question(questions_quiz[0], "a"),
    Question(questions_quiz[1], "b"),
    Question(questions_quiz[2], "c"),
    Question(questions_quiz[3], "d"),
    Question(questions_quiz[4], "a"),
    Question(questions_quiz[5], "b"),
    Question(questions_quiz[6], "c"),
    Question(questions_quiz[7], "d"),
    Question(questions_quiz[8], "a"),
    Question(questions_quiz[9], "b"),
    Question(questions_quiz[10], "c"),
    Question(questions_quiz[11], "d"),
]


def user_choice():
    """
    Function to accept user choice of answers.
    """
    options = input("Please choose an option:- (A, B, C, or D)\n")
    selection = options.lower()
    selection = options.strip()
    if selection not in ['a', 'b', 'c', 'd']:
        print('This is not a valid selection.\n\n')
        return user_choice()

    return selection


def display_quiz(questions):
    """
    This function is designed to get input of a user's name.
    This function is designed to display questions.
    This function checks if answers are correct or incorrect.
    """
    while True:
        name = input("\nPlease enter your name below:\n\n")
        if name.isalpha():
            break
    print("The quiz requires characters from A-Z only:\n")
    print(f"\n Let us now start the Python Quiz, {name}\n\n")
    time.sleep(2)
    new_list = random.sample(questions, 10)
    score = 0
    for sample in new_list:
        print(sample.query)
        if user_choice() == sample.answer:
            score += 1
            print("\nThat is correct\n\n")
            time.sleep(1.5)
        else:
            print("\nThat is incorrect\n\n")
            time.sleep(1.5)
    print("Thank you for completing the quiz, " + name + "\n\n")
    print("You got", score, "out of 10 questions correct!\n\n")
    time.sleep(2)
    print("Thanks for playing! \n")
    time.sleep(1)
    endgame_image()
    time.sleep(1)
    print("Press R to replay the quiz\n")
    print("Press Q to quit the quiz and return to start menu")
    print()
    time.sleep(2)
    gameover_menu()


def quiz_instructions():
    """
    Function to display quiz instructions to the user.
    """
    print("These are the instructions to the Python Quiz!\n\n")
    time.sleep(2)
    print("1. The quiz contains questions relating to Python.")
    print("2. The quiz contains 10 questions.")
    print("3. It is a multiple choice quiz, so you can choose "
          "answers from A to D")
    print("4. Your score will be revealed at the end of the quiz.\n\n")

    time.sleep(2)
    print("It's now time to start the quiz!\n\n")


def nav_menu():
    """
    Function that gives users ability to navigate around the quiz.
    Restart or Quit function.
    """
    press_key = input().lower()
    if press_key == "p":
        time.sleep(2)
        print("Nice to see you back and ready to play!\n")
        time.sleep(2)
        display_quiz(questions)

    if press_key == "q":
        time.sleep(2)
        print("Have a nice day! Please come back and play again some time!\n")
        time.sleep(2)
        start_game()

    else:
        print("Invalid choice. Please press either P or Q.\n")
        time.sleep(1)
        nav_menu()


def gameover_menu():
    """
    This is a function to display a menu.
    The menu gives options to replay or quit the quiz.
    """
    press_key = input().lower()
    if press_key == "r":
        time.sleep(2)
        print("....starting the quiz...\n\n")
        time.sleep(2)
        quiz_instructions()
        display_quiz(questions)
    if press_key == "q":
        time.sleep(2)
        print()
        time.sleep(2)
        display_menu()
    else:
        print("Invalid input!")
        time.sleep(1)
        print("Press either R, Q")
        gameover_menu()


def display_menu():
    """
    This is a function to display a menu to start the quiz.
    This is a function to read through the instructions.
    """
    print("Please Enter A to start the quiz.\n")
    print("Please Enter B to go to Instructions.\n\n")
    menu = (input("A: Start Quiz    B: Instructions\n").lower())
    if menu == "a":
        time.sleep(1)
        display_quiz(questions)
    if menu == "b":
        print("Please check out the Quiz instructions")
        time.sleep(3)
        quiz_instructions()
        print("Press P to proceed to the Quiz\n")
        print("Press Q to quit")
        nav_menu()
    if menu not in ['a', 'b']:
        print('Invalid choice! Please choose A or B to proceed\n\n')
        return display_menu()


def start_image():
    """
    This is a function that enacts an ASCII output.
    """
    result = pyfiglet.figlet_format("The Python Quiz")
    print("\n\nHello and Welcome to.... ")
    print(result)
    time.sleep(2)


start_image()


def endgame_image():
    """
    This is a function that enacts ASCII text output
    """
    image = pyfiglet.figlet_format("This is the end of the Quiz: "
                                   "Thanks for playing!")
    print(image)
    time.sleep(1.5)


def start_game():
    """
    Function to start the Python Quiz game.
    """
    time.sleep(2)

    display_menu()


start_game()
