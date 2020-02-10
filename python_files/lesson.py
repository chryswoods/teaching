lines = open("people.csv").readlines()

people = {}

for line in lines[1:]:
    data = line.split(",")
    ID = data[0].strip()
    name = data[1].strip()
    people[ID] = name

def find_person(person):
    for ID, name in people.items():
        if person.lower() in name.lower():
            return ID

    print("Cannot find", person)
    return None

lines = open("biographies.tsv").readlines()

bios = {}

for line in lines[1:]:
    data = line.split("\t")
    ID = data[0].strip()
    bio = data[1].strip()
    bios[ID] = bio

lines = open("connections.csv").readlines()

connections = {}

for line in lines[1:]:
    data = line.split(",")
    ID_from = data[0].strip()
    ID_to = data[1].strip()

    # one person can be connected to multiple others, so we 
    # will store a list of all of the people someone is 
    # connected to. First, we need to create the list
    # if we haven't seen this person before...

    if ID_from not in connections:
        connections[ID_from] = []

    if ID_to not in connections:
        connections[ID_to] = []

    # now we append the connection (both from and to)
    connections[ID_from].append(ID_to)
    connections[ID_to].append(ID_from)

def print_info(person):
    ID = find_person(person)

    if ID is None:
        return

    print(people[ID])
    print("Biography:", bios[ID])
    
    print("================")
    print("This person is connected to")

    for connection in connections[ID]:
        print(people[connection])

print_info("Claxton")
