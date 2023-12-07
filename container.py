
num=int(input("Enter the number of bars required:"))
height=list()
for i in range(0,num):
    height[i]=int(input("Enter the height of each bar:"))
max_vol=0
for j in range(0,num):
    for k in range(0,num):
        if j!=k:
            vol=abs(min(height(j), height(k))*(j-k))
            if (vol>max_val):
                max_vol=vol
print(max_vol)
