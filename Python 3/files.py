#file, #read, #open

# Open a file and close automatically
# r: read
# w: write
# a: append
# +: read and write
# b: binary mode
with open('workfile', 'rw', encoding="utf-8") as f: # If not using the 'with' keyword, call f.close() to close the file
  read_data = f.read() # This reads the entire file \n

# read single lines
f.readline()
# 'This is the first line of the file.\n'
f.readline()
# 'Second line of the file\n'

# read a file line by line
with open('workfile', encoding="utf-8") as f:
  for line in f:
    print(line, end='')

f.readlines() # read all the lines of a file in a list

f.write('This is a test\n') # writes the contents of string to the file, returning the number of characters written
# 15

#######################################################################################
#json

#dumps() - Convert object to JSON
import json
x = [1, 'simple', 'list']
json.dumps(x) 
# '[1, "simple", "list"]'

#dump() - Serialize object to JSON and write into a file
import json
data = {
    "emp1": {"name": "Lisa", "age": 34, "salary": 54000},
    "emp2": {"name": "Elis", "age": 24, "salary": 40000},
}
with open("output.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

#load() - Read a JSON file and convert to python object
import json
with open('data.json', 'r') as f: # data.json contains columns 'name' and 'age' for example
  data = json.load(f)
for name in data['name']: # iterate object
    print(name)




