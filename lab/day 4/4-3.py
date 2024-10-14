arr=[1,2,2,26,5,4,4,4,6,6,82,2,1,2,2]
k = int(input("Enter the number : "))
count = 0
for num in arr:
  if num == k:
    count = count + 1
print(count)