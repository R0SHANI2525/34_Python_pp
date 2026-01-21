#que1
numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 237, 412, 566, 731, 210, 912, 216, 244, 896, 101, 867, 355, 430 ]
for i in numbers:
    if i%2==0:
        print(i,end=" ")
    if i==237:
        break
print(end=" ")

#que2
import os
file_path=os.path.abspath(__file__)
file_name=os.path.basename(__file__)
print(file_path)
print(file_name)

#que3
n = 5
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()

#que4
num = int(input("Enter a number: "))
words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
while num > 0:
    digit = num % 10
    print(words[digit])
    num //= 10
