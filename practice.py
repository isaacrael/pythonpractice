__author__ = '184766'

"""
while True:
    print "This is a test"
    answer = raw_input("Enter your answer")
    if answer.strip() == "quit":
        break
"""

# Open file for reading
file = open("states.txt", "r")

states = []
for line in file:
    print(line)
    states.append(line)
    print(states)
file.close()

# Sort the list of states & print
states.sort()
print(states)
