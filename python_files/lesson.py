
# read all of the lines into a list of lines
lines = open("people.csv").readlines()

# the first line is the headings
header = lines[0].strip()

# create a dictionary to hold all of the people
people = {}

# read in all of the people
for line in lines[1:]:
    # comma-separated values, so split by comma
    data = line.split(",")
    ID = data[0].strip()
    name = data[1].strip()

    # save the person's name in the dictionary
    people[ID] = name

# read all of the lines into a list of lines
lines = open("biographies.tsv").readlines()

# the first line is the headings
header = lines[0]

# create space for the biographies
bios = {}

for line in lines[1:]:
    # tab separated
    data = line.split("\t")

    ID = data[0].strip()
    bio = data[1].strip()

    bios[ID] = bio

# read all of the lines into a list of lines
lines = open("connections.csv").readlines()

# the first line is the headings
header = lines[0]

# create space for all of the connections
connections = {}

for line in lines[1:]:
    # comma-separated
    data = line.split(",")
    ID_from = data[0].strip()
    ID_to = data[1].strip()

    if not ID_from in connections:
        connections[ID_from] = []

    connections[ID_from].append(ID_to)

    if not ID_to in connections:
        connections[ID_to] = []

    connections[ID_to].append(ID_from)

# loop over all people to try to find someone called 'brunel'
for ID, name in people.items():
    if "brunel" in name.lower():
        # say hello to them and print their biography
        print("Hello", name)
        print(bios[ID])

        # now print everyone they are connected to
        print("You are connected to")
        for connection in connections[ID]:
            person = people[connection]
            print(person)

# create a function to search for a specific person
def find_person(person):
    for ID, name in people.items():
        if person.lower() in name.lower():
            return ID

    print("Cannot find", person)

# function to print information about a specific person
def print_info(person):
    ID = find_person(person)

    if ID:
        person = people[ID]
        print("Hello", person)
        print(bios[ID])
        print("You are connected to")
        for connection in connections[ID]:
            print(people[connection])

print_info("Claxton")

print_info("Guppy")
