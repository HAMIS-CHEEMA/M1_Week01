# LOOPS (for and while )

# for loop = Do I know exactly how many times? = YES


total_scores = [10,20,30,40,50,60,70,80,90,100]
total = 0
count = 0
for score in total_scores:
    total = score + total
    count +=1
average = total / count
print("average", average)
# ---------------------
fruits = ["apple", "banana","mango","orange"]
for fruit in fruits:
    print(fruit)


for i in range(2,11,2):        # even nums
    print(i)

for i in range(1,11,2):        # odd nums
    print(i)
# ---------------------------

total = 0             #sum of 1st 50 N_nums
for i in range(1,51):
    total = total + i
print("sum of 1st 50 N_nums",total)
# ---------------------------------
for i in range(1,11):          #range (start , end , steps)
    print(i)
# -----------------------------
text = "you the best one i have ever met."
vowel_count = 0
for char in text:
    if char in "aeiou":
        vowel_count += 1
print("vowels are ", vowel_count )
#--------------------------------
numbers = [16,34,60,77,80,92,85]
largest = numbers[0]
for nums in numbers:
    if nums > largest:
        largest = nums
print("largest number is ", largest)
# ----------------------------------
numbers = [16,34,60,77,80,92,85]
smallest = numbers[0]
for nums in numbers:
    if nums < smallest:
        smallest = nums
print("smallest number is ", smallest)
# --------------------------------------
num = 13
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
# -------------------------------
word = "Madam"
reverse_word = ""
for char in word:
    reverse_word = char + reverse_word
print("reversed =", reverse_word)
#---------------------------------
numbers = [12,20,40,62,6,87,20,91]
even = 0            # count even & odd in a list
odd = 0
for nums in numbers:
    if nums %2==0:
        even +=1
    else:
        odd +=1
print(f"even numbers are {even} and odd numbers are {odd}")
# ----------------------------------
text = "darling"
index = 0
for char in text:
    print(f"index {index} : {char} ")
    index +=1
# ----------------------------
numbers = [ 12,22,30,84,32,10]
search = 22
found = False
for num in numbers:
    if num == search:
        found = True
        break
if found:
    print(f"{search} found in a list ")
else:
    print(f"{search} , not found in a list")

# ---------------------------------------------------------------------
# while loop = Do I know exactly how many times? = NO
counter = 1
sum = 0
n = 15
while counter <= 15:
    sum = counter + sum
    counter +=1
print(f"sum of first {n} = {sum}")
# -----------2-----------
i = 1
while i<= 5:
    print(i)
    i += 1
# ----------3---------------------
i = 5
while i >= 1:
    print(i)
    i -=1
print("go")
# -----------3------
i = 20
while i >= 2:
    print(i)
    i -= 2
# _--------even numbers-------
i = 2
while i <= 20:
    print(i)
    i += 2

# odd numbers
i = 1
while i <=10:
    print(i)
    i += 2
# -------mul table of 41
i = 1
while i <= 10:
    print(f"41 * {i} = {41 * i} ")
    i += 1
# ------keep asking password
password = ""
while password != "viking":
    password = input("enter correct password : ")
print("Access Granted")
# ------double a number
i = 1
while i < 100:
    print(i)
    i = i * 2

# ----------- sum of even nums
i  = 2
sum = 0
while i <= 10:
    old_sum = sum
    sum = i + sum
    print(f"{i} + {old_sum} = {sum}")
    print("increment of 2")
    i += 2
# ---------- reverse steps
i = 60
while i >= 0:
    print(i)
    i -= 5
#------- forward moving
i = 0
while i <=50:
    print(i)
    i += 5

from itertools import count

#------factorial of n
n = 3
fact = 1
while n > 0 :
    fact = fact * n
    n -= 1
print(fact)

n = 4
fact = 1
while n > 0:
    fact = fact * n
    n -= 1
print(fact)
#-------------- count digits
i = 217457
count = 0
while i > 0:
    i = i // 10
    count += 1
print(count)
# -------------------
age = -1
while age < 1 or age > 120:
    age = int(input("Enter valid age (0-120): "))
print(f"Age accepted: {age}")

# -----------shopping_list------
shop_list = []
while True:
    item = input("enter your items here , for stop write 'done' ")
    if item == "done":
        break
    shop_list.append(item)
print(shop_list)



# ------------------------------------------------------------------------------------------------------------------




