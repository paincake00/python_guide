# <MAIN-PYTHON-DOCS>

import math, sys, random, os, shutil

def is_num_func(inp):
    inp = inp.replace("-", "", 1)
    inp = inp.replace(".", "", 1)
    return inp.isdigit()

def default_input(start_text, is_num):
    inp = None
    while not inp:    
        inp = input(start_text)
    while is_num and not is_num_func(inp):
        inp = input(start_text)
    return inp

def string_methods():
    string = default_input("Enter your string: ", is_num=False)
    print("Method len(): " + str(len(string)))
    print("Method find('e'): " + str(string.find("e")))
    print("Method capitalize(): " + string.capitalize())
    print("Method upper(): " + string.upper())
    print("Method lower(): " + string.lower())
    print("Method isdigit(): " + str(string.isdigit()))
    print("Method isalpha(): " + str(string.isalpha()))
    print("Method count('l'): " + str(string.count("l")))
    print("Method replace('e', 'a'): " + string.replace("e", "a"))
    print("Multiplication: " + string * 2)

    # string slicing
    print("String slicing:")
    print(string[len(string)-1:0:-1])

    website = "https://www.youtube.com"
    this_slice = slice(12, -4)
    print(website + " -> " + website[this_slice])

def math_functions():
    num = default_input("Enter your number: ", is_num = True)
    num = float(num) if num.count(".") == 1 else int(num)
    print("Method round(): " + str(round(num)))
    print("Method ceil(): " + str(math.ceil(num)))
    print("Method floor(): " + str(math.floor(num)))
    print("Method abs(): " + str(abs(num)))     # absolute value
    print("Method pow(): " + str(pow(num, 2)))
    print("Method sqrt(): " + str(math.sqrt(num)) if num >= 0 else "number is negative")
    print("Method max(): " + str(max(num - 1, num, num + 1)))

def nested_loops():
    rows = int(input("Enter count of rows: "))
    columns = int(input("Enter count of columns: "))
    for i in range(0, rows):
        for j in range(0, columns):
            print("@ " if j <= i else "& ", end="")
        print()

def list_methods():
    pets = ["cat", "dog", "parrot", "mouse"]
    print(pets)

    def output():
        for el in pets: print(el, end=" ")
        print()

    print("Method append('spider'): ", end="")
    pets.append("spider")
    output()

    print("Method remove('mouse'): ", end="")
    pets.remove("mouse") 
    output()

    print("Method pop(): ", end="")
    pets.pop()      # remove last element
    output()

    print("Method insert(0, 'golden_fish'): ", end="")
    pets.insert(0, "golden_fish") 
    output()

    print("Method sort(): ", end="")
    pets.sort()     # sort for alphbet order
    output()

    print("Method clear(): ", end="")
    pets.clear() 
    print("* the list is empty *")

def tuples():
    # tuples is ordered and unchangeable
    graphics_cards = "gtx1650", "rx580", "rtx2060"
    print(graphics_cards)

    print("Method count('gtx1650'): ", end="")
    print(graphics_cards.count("gtx1650"))

    print("Method index('rx580'): ", end="")
    print(graphics_cards.index("rx580"))

def sets():
    # sets is unordered, unindexed. No dublicate values
    laptops_labels = {"lenovo", "hp", "asus", "msi"}
    laptops_series = {"ideapad_gaming", "pavilion", "ROG", "titan gt"}

    print("Method add('huawei'): ", end="")
    laptops_labels.add("huawei")
    print(laptops_labels)

    print("Method remove('hp'): ", end="")
    laptops_labels.remove("hp")
    print(laptops_labels)

    # print("Method clear(): ", end="")
    # laptops_labels.clear()
    # print(laptops_labels)

    print("Method update(laptop_series): ", end="")
    laptops_labels.update(laptops_series)
    print(laptops_labels)

    print("Method union(laptops_series): ", end="")    # "OR"
    laptops_names = laptops_labels.union(laptops_series)
    print(laptops_names)

    print("Method difference(): ", end="")             # "subtraction"
    print(laptops_names.difference(laptops_series))    # only laptops labels

    print("Method intersection(): ", end="")           # "AND"
    print(laptops_names.intersection(laptops_series))  # only laptops series

def dictionary():
    # A changeable, unordered collection of unique key:value pairs
    capitals = {'USA': 'Washington DC',     
                'India': 'New Delhi',
                'China': 'Beijing',
                'Russia': 'Moscow'}
    print("Method get('Russia'): ", end="")
    print(capitals.get('Moscow'))

    print("Method keys(): ", end="")
    print(capitals.keys())
    print("Method values(): ", end="")
    print(capitals.values()) 
    print("Method items(): ", end="")           
    print(capitals.items())
    print("Method pop('USA'): ", end="")           
    print(capitals.pop('USA'))
    print("Method update(): ")           
    capitals.update({'Germany':'Berlin'})
    for key,value in capitals.items():
        print("---", key, value)

# *args  -  parameter that will pack all args into a tuple
def args():
    def add(*stuff):
        sum = 0
        for i in stuff:
            sum += i
        return sum
    print("Addition of sequence: ", end="")
    print(add(1,2,3,4,5,6))     # 21

# **kwargs  -  parameter that will pack all args into a dict
def kwargs():
    def hello(**kwargs):
        #print("Hello, " + kwargs['first'] + " " + kwargs['last'])
        print("INFO: ", end="")
        for key,value in kwargs.items():
            print(value, end=" ")
    hello(title="Mr.", first="John", nickname="Bastard", last="Snow")

def string_format():
    animal, item = "cow", "moon"
    print("The {} jumped over the {}".format(animal, item))
    print("The {1} jumped over the {0}".format(item, animal))   #positional arg
    print("The {subj} jumped over the {obj}".format(subj="cow", obj="moon"))   #keyword arg

    lp = "Python"
    print("I use {:20}! And you?".format(lp))
    print("I use {:^20}! And you?".format(lp))
    print("I use {:>20}! And you?".format(lp))
    print("I use {:<20}! And you?".format(lp))

    num = 1000
    print("The number is {:.3f}".format(num))
    print("The number is {:,}".format(num))
    print("The binary number is {:b}".format(num))
    print("The octal number is {:o}".format(num))
    print("The hexadecimal number is {:X}".format(num))
    print("The scientific view of number is {:E}".format(num))

def random_numbers():
    print(random.randint(1,6))
    print(random.random())

    myList = ['rock', 'paper', 'scissors']
    print(random.choice(myList))

    cards = list(range(1, 10)) + ['J', 'Q', 'K', 'A']
    random.shuffle(cards)   #to mix the cards
    print(cards)

def exception_handling():
    try:
        numerator = int(input("Enter a number to divide: "))
        denominator = int(input("Enter a number to divide by: "))
        result = numerator / denominator
    except ZeroDivisionError as e:
        print(e)
        print("You can't divide by zero!")
    except ValueError as e:
        print(e)
        print("Enter only numbers")
    except Exception as e:
        print(e)
        print("smth went wrong :(")    
    else:
        print(result)
    finally:
        print("this is all..")    

def file_detection():
    filename = "precedence_in_python.png"
    path = os.path.abspath(path=".") + "/files/" + filename    # get path to file

    if os.path.exists(path):
        print("That location exists!")
        if os.path.isfile(path):
            print("That is a file. Name: {}".format(filename))
        elif os.path.isdir(path):
            print("That is a directory")
    else:
        print("That location doesn't exist!")            

def file_read():
    try:
        with open("files/smth_text.txt") as file:
            print(file.read())
    except FileNotFoundError:
        print("That file was not found :(")    

def file_write():
    text = "This text has written!"
    with open("files/write_file.txt", "w") as file:
        file.write(text)
    
    # w - write to file
    # r - read from file
    # a - append to file

def file_copy():
    # using std lib: shutil
    # copyfile() =  copies contents of a file
    # copy() =      copyfile() + permisiion mode + destination can be directory
    # copy2() =     copy() + copies metadata (file's creation and modification times)
    shutil.copy2('files/write_file.txt', 'files/copy_text.txt') # src,dst    

def file_move():
    source = "move_file.txt"
    destination = os.path.abspath(path=".") + "/files/" + source

    try:
        if os.path.exists(destination):
            print("There is already a file there")
        else:
            os.replace(source, destination)
            print(source + " was moved")
    except FileNotFoundError:
        print(source+" was not found!")
    except Exception as e:
        print(e) 
        print("smth went wrong :(")               

def file_remove():
    path = "files/delete_file.txt"
    with open(path, "w") as file:
        file.write("")
    os.remove(path)     
    # os.rmdir(path) - for removing directory
    # shutil.rmtree(path) - for removing directory and all files contained within

def modules():
    # module - a file containing python code (vars, funcs, classes and etc)
    sys.path.append("modules")      # sys.path.append(os.path.abspath("modules"))
    from messages import std_lib
    std_lib()

def cmd():
    # to execute current command in terminal
    print(os.system(input('Enter the terminal command: ')))

if __name__ == "__main__":

    RULES = """
    <?> input_promt:
    0 - string_methods
    1 - math_functions
    2 - nested_loops
    3 - list_methods
    4 - tuples
    5 - sets
    6 - dictionary
    7 - *args
    8 - **kwargs
    9 - string_format
    10 - random_numbers
    11 - exception_handling
    12 - file_detection
    13 - file_read
    14 - file_write
    15 - file_copy
    16 - file_move
    17 - file_remove
    18 - modules
    19 - cmd
    -h - show help-table
    -e - stop the program
    """

    dict_promt = {
        '0': 'string_methods()',
        '1': 'math_functions()',
        '2': 'nested_loops()',
        '3': 'list_methods()',
        '4': 'tuples()',
        '5': 'sets()',
        '6': 'dictionary()',
        '7': 'args()',
        '8': 'kwargs()',
        '9': 'string_format()',
        '10': 'random_numbers()',
        '11': 'exception_handling()',
        '12': 'file_detection()',
        '13': 'file_read()',
        '14': 'file_write()',
        '15': 'file_copy()',
        '16': 'file_move()',
        '17': 'file_remove()',
        '18': 'modules()',
        '19': 'cmd()',
        '-h': 'print(RULES)',
        '-e': 'sys.exit()'
    }

    print(RULES)
    while True:
        inp = input("Enter command: ")
        if (inp in dict_promt.keys()):
            eval(dict_promt.get(inp))
        else:
            print("Incorrect command. Repeat plz!")          