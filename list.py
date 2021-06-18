# taking Recipie of any thing from user and then displaying
list = []
dish = input("Enter the name of dish\n")
# no. of lines you have in recipie
count = int(input('Enter no. of lines you have in Your recipie\n'))
line_no = 1
while count > 0 :
    list.append(input(f'Enter {line_no} point\n'))
    line_no+=1
    count-=1
print(f"Your Recipie of {dish.upper()} is")
for item in list :
    print(item)
