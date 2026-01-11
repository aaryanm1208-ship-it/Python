c={
    "Name":"Virat",
    "Keys":"King",
    list:["a","b","c"]
}
print(c)

Output:=
{'Name': 'Virat', 'Keys': 'King', <class 'list'>: ['a', 'b', 'c']}

=== Code Execution Successful ===



name={1,2,3,4}
print(name)
print(type(name))

Output:=
{1, 2, 3, 4}
<class 'set'>

=== Code Execution Successful ===



name={1,2,3,4,4,"hello","hello"}
print(name)
print(type(name))

Output:=
{1, 2, 3, 4, 'hello'}
<class 'set'>

=== Code Execution Successful ===



name={1,2,3,4,4,"hello","hello"}
name.add(21)
name.remove(4)

name.pop()
print(name)
print(type(name))

Output:=
{1, 2, 3, 21}
<class 'set'>

=== Code Execution Successful ===



name={1,2,3,4,4,"hello","hello"}
name.add(21)
name.remove(4)
name.clear()

print(name)
print(type(name))

Output:=
set()
<class 'set'>

=== Code Execution Successful ===



name={1,2,3,4,4,"hello","hello"}
name.add(21)
name.remove(4)
print(name)
print(type(name))
print(len(name))

Output:=
{1, 2, 3, 21, 'hello'}
<class 'set'>
5

=== Code Execution Successful ===



meanings = {
    "table": "a piece of furniture",
    "cat":"a small animal"
}

print(meanings)
meanings["table"]="list of facts and figures"
print(meanings)
 
 =======OR======

meanings = {
    "table": ["a piece of furniture","Lists of figures"],
    "cat":"a small animal"
}

print(meanings)

Output:=
{'table': ['a piece of furniture', 'Lists of figures'], 'cat': 'a small animal'}

=== Code Execution Successful ===