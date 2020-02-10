# Python Files

You need to download these data files

* [people.csv](https://raw.githubusercontent.com/chryswoods/teaching/master/python_files/people.csv)
* [biographies.tsv](https://raw.githubusercontent.com/chryswoods/teaching/master/python_files/biographies.tsv)
* [connections.csv](https://raw.githubusercontent.com/chryswoods/teaching/master/python_files/connections.csv)

## Reading a file

Read all lines of a file into a list

```python
lines = open("people.csv").readlines()
```

You can loop over all lines and print them using

```python
for line in lines:
    print(line)
```

Note that this also printed the 'newline' at the end of each line.
You can remove this by "stripping" the line - this means removing
unnecessary newlines and whitespace within the line

```python
for line in lines:
    print(line.strip())
```

## Comma separated lines

Split comma separated lines using the `split` function, e.g.

```python
for line in lines:
    data = line.strip().split(",")
    print(data)
```

Normally the first line is a header, so skip this line

```python
for line in lines[1:]:
    data = line.strip().split(",")
    print(data)
```

## Placing data into a dictionary

The file associates an ID with a person's name. We can store this
in a dictionary using...

```python
people = {}

for line in lines[1:]:
    data = line.split(",")
    ID = data[0].strip()
    name = data[1].strip()
    people[ID] = name
```

## Finding the ID of a person

We can find the ID of a person by searching through the dictionary

```python
for ID, name in people.items():
    if "brunel" in name.lower():
        print(ID, name)
```

We can create a function that finds the ID of a person

```python
def find_person(person):
    for ID, name in people.items():
        if person.lower() in name.lower():
            return ID

    print("Cannot find", person)
    return None


print(find_person("Brunel"))
```

## Biographies

We can load all of the biographies. These are in a tab separated file. We
use `\t` to mean "tab"

```python
lines = open("biographies.tsv").readlines()

bios = {}

for line in lines[1:]:
    data = line.split("\t")
    ID = data[0].strip()
    bio = data[1].strip()
    bios[ID] = bio

print(bios[find_person("Brunel")])
```

## Connections

We can load all of the connections

```python
lines = open("connections.csv").readlines()

connections = {}

for line in lines[1:]:
    data = line.split(",")
    ID_from = data[0].strip()
    ID_to = data[1].strip()

    # one person can be connected to multiple others, so we 
    # will store a list of all of the people someone is 
    # connected to. First, we need to create the list
    # if we haven't seen this person before...

    if ID_from not in connections:
        connections[ID_from] = []

    if ID_to not in connections:
        connections[ID_to] = []

    # now we append the connection (both from and to)
    connections[ID_from].append(ID_to)
    connections[ID_to].append(ID_from)

print(connections[find_person("Brunel")])
```

## Printing connections

We can print the connections by looking up the IDs from `people`

```python
brunel = find_person("Brunel")

print(people[brunel], "is connected to")

for connection in connections[brunel]:
    print(connections[connection])
```

## Putting it all together...

We can create a function that prints out useful information
about a person

```python
def print_info(person):
    ID = find_person(person)

    if ID is None:
        return

    print(people[ID])
    print("Biography:", bios[ID])
    
    print("================")
    print("This person is connected to")

    for connection in connections:
        print(people[connection])

print_info("Brunel")
```

## Complete script

Here is the complete script that will load data and let you print
information about any person

```python
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

print(bios[find_person("Brunel")])

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

```

