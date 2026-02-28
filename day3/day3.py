x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
op = input("Enter the operator - ")
z = None
if op == "+":
    z = x + y   
elif op == "-":
    z = x - y
elif op == "*":
    z = x*y
elif op == x/y:
    z = x/y
else:
    z = "Invalid Operator"

print(z)

file = open("data2.txt", 'a')
file.write(f"{x} {op} {y} = {z}\n ")
file.close()

file = open("data2.txt", 'r')
content = file.read()
print(content)
file.close()











# file1 = open("data.txt", "w")
# file1.write("I am the first line\n")
# file1.close()

# file1 = open("data.txt", "r")
# content1 = file1.read()
# print(content1)
# file1.close()

# file1 = open("data.txt", "a")
# file1.write("A new line is added. \n")
# file1.close()

# file1 = open("data.txt", "r")
# content1 = file1.read()
# print(content1)
# file1.close()
