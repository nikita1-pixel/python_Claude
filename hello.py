string = "968-Maria, (D@t@ Engineer );; 27y  ".lower()
print(len(string))
name = string.strip()[4:9]
print(f"name : {name} ")
role = string.strip()[12:26].replace("@", "a")

print(f"role : {role}")

age = string.strip()[30:32]
print(f"age : {age}")


print(f"name : {name} | role : {role} | age : {age} ")
