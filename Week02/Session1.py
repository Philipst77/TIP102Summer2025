#Advanced Problem Set Version 1
#---------------------------------------------------------#
#Problem 1
def total_treasures(treasure_map):
    total =0
    for key in treasure_map:
        total+= treasure_map[key]
    return total

#Problem 2
def can_trust_message(message):
    alp = "abcdefghijklmnopqrstuvwxyz"
    holder = []
    for char in message:
        if char in alp:
            holder.append(char)
            if len(holder) == len(alp):
                return True
    return False

#Problem 3
def find_duplicate_chests(chests):
   seen = set()
   duplicates = []
   for num in chests:
       if num in seen:
           duplicates.append(num)
       else:
           seen.add(num)
   return duplicates
#Problem 4
def is_balanced(code):
    freq = {}

    for char in code:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    values = list(freq.values())
    if all(v == values[0] for v in values):
        return True
    return False
#Problem 5
def find_treasure_indices(gold_amounts, target):
    pass
#Advanced Problem Set Version 2
# ---------------------------------------------------------#











# ------------------- Test Cases -------------------
# Advanced Problem Set Version  Test Cases 1

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 


message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))



chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 


gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  
# ------------------- Test Cases -------------------
# Advanced Problem Set Version  Test Cases 2
