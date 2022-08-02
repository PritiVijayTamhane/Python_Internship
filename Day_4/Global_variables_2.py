'''___Program for global variables___'''

Name = "XYZ"

def myfunc():

  global Name 
  Name = "ABC" 
  print(Name) 

myfunc()

print("My name is " + Name)
