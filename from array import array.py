from array import array
arr1= array("i",[2,4,5,6,4,3,4545,34])
print(arr1)
s=0
avg=0

for i in range(0,9,1):
    print(arr1[i])
    s=s+ arr1[i]
avg= s/10
print("sum=",s)
print("avg=",avg)
