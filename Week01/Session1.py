# Problem 1: Welcome Function
def welcome():
    print("Welcome to The Hundred Acre Wood!")  # Prints a static welcome message

# Problem 2: Greeting Function
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")  # Personalized welcome

# Problem 3: Character Catchphrase
def printCharacterCatchPhrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

# Problem 4: Return item at index x
def get_item(items, x):
    if 0 <= x < len(items):
        return items[x]
    return None

# Problem 5: Sum all elements of the hunny_jars list
def sum_honey(hunny_jars):
    res = 0
    for num in hunny_jars:
        res += num
    return res

# Problem 6: Double each value in the hunny_jars list
def doubled(hunny_jars):
    return [x * 2 for x in hunny_jars]  # Using list comprehension

# Problem 7: Count how many race_times are below a given threshold
def count_less_than(race_times, threshold):
    count = 0
    for x in race_times:
        if x < threshold:
            count += 1
    return count

# Problem 8: Print a numbered to-do list
def print_todo_list(tasks):
    print("Pooh's To Dos:")
    for i, item in enumerate(tasks, start=1):
        print(f"{i}. {item}")

# Problem 9: Check if all quantities are even (can be paired)
def can_pair(item_quantities):
    for item in item_quantities:
        if item % 2 != 0:
            return False
    return True

# Problem 10: Return a list of all divisors of quantity
def split_haycorns(quantity):
    res = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            res.append(i)
    return res

# Problem 11: Remove the letters T, I, G, E, R from the string (case-insensitive)
def tiggerfy(s):
    res = ""
    for char in s:
        if char.lower() in "tiger":
            continue
        res += char
    return res

# Problem 12: Return indices of "thistle" in a list
def locate_thistles(items):
    res = []
    for i, item in enumerate(items):
        if item == "thistle":
            res.append(i)
    return res

# Advanced Probnlem Set Version 1

def linear_search(lst, target):
    
    for i, item in enumerate(lst):
        if item == target:
            return 
        return -1

# ------------------- Test Cases -------------------

if __name__ == "__main__":
    print("== Problem 1 ==")
    welcome()

    print("\n== Problem 2 ==")
    greeting("Philip")

    print("\n== Problem 3 ==")
    printCharacterCatchPhrase("Pooh")
    printCharacterCatchPhrase("Piglet")

    print("\n== Problem 4 ==")
    items = ["piglet", "pooh", "roo", "rabbit"]
    print(get_item(items, 2))  # "roo"
    print(get_item(items, 5))  # None

    print("\n== Problem 5 ==")
    hunny_jars = [2, 3, 4, 5]
    print(sum_honey(hunny_jars))  # 14
    hunny_jars = []
    print(sum_honey(hunny_jars))  # 0

    print("\n== Problem 6 ==")
    hunny_jars = [1, 2, 3]
    print(doubled(hunny_jars))  # [2, 4, 6]

    print("\n== Problem 7 ==")
    race_times = [1, 2, 3, 4, 5, 6]
    print(count_less_than(race_times, 4))  # 3
    race_times = []
    print(count_less_than(race_times, 4))  # 0

    print("\n== Problem 8 ==")
    task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    print_todo_list(task)
    print()
    task = []
    print_todo_list(task)

    print("\n== Problem 9 ==")
    item_quantities = [2, 4, 6, 8]
    print(can_pair(item_quantities))  # True
    item_quantities = [3, 5, 7, 8]
    print(can_pair(item_quantities))  # False
    item_quantities = []
    print(can_pair(item_quantities))  # True

    print("\n== Problem 10 ==")
    print(split_haycorns(6))  # [1, 2, 3, 6]
    print(split_haycorns(1))  # [1]

    print("\n== Problem 11 ==")
    print(tiggerfy("suspicerous"))  # "suspcous"
    print(tiggerfy("Trigger"))      # ""
    print(tiggerfy("Hunny"))        # "Hunny"

    print("\n== Problem 12 ==")
    items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    print(locate_thistles(items))  # [0, 3]
    items = ["book", "bouncy ball", "leaf", "red balloon"]
    print(locate_thistles(items))  # []
    
    #Advanced Problem Set Version 1
    
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'

    print(linear_search(items, target))