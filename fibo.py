fibonacci = [0,1]
n = int(input("Enter a number"))
for i in range(n-2):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
print(fibonacci)