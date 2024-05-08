# b = 1
# fiba = 0
# numbers = []
# for i in range(1,11):
#     fiba = b+
#     numbers.append(fiba)
# print(numbers)


a=1
b=1
numbers=[]
for i in range(1,6):
    b+=a
    a+=b
    numbers.append(b)
    numbers.append(a)
print(numbers)


# sum=0
# for i in numbers:
#     sum+=i
# print(f"Сумма чисел Фибоначи: {sum}")


# for i in numbers:
#     if i%2==0:
#         numbers.remove(i)
# print(numbers)


# mas1 = [1,2,3]
# mas2 = [4,5,6]
# print(mas1+mas2)

# for i in range(len(numbers)):
#     numbers[i]=numbers[i]-1
# print(numbers)

for  i in numbers:
    i -=1
    print(i)