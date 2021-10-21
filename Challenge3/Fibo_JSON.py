import json

full_list = []

# Get the input from user
n = input("Enter the number between 0 to 100 for fibonaci series: ")

#Verify that is number between 0 to 100
if n < 0:
    n = input("Enter the number between 0 to 100 for fibonaci series: ")
elif n > 100:
    n = input("Enter the number between 0 to 100 for fibonaci series: ")
else:
  n=n

# Function to calculate fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    listVal = []
    for i in range(1, n):
            c = a + b
            a = b
            b = c
            listVal.append(b)
    return listVal

full_list = fibonacci(n)
total = sum(full_list)

x = {
  "member-count": n-1,
  "sequence": full_list,
  "total": total
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
