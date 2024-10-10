n = int(input("Enter the number : ")) # 6 = [1,2,3,6] = [1+2+3] = 6

factors = []
for i in range(1,n+1):#(0,7) 1,2,3,4,5,6
    if n % i == 0:
        factors.append(i)

total = 0
for j in range(0,len(factors)-1):#[1,2,3,6] range(0,3)
    total += factors[j]

if total == n:
    print(f"Yes,the number {n} is a perfect number")

else:
    print(f"The number {n} is not a perfect number")



