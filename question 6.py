string = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
lc = ""
uc = ""
space = 0
even = ""
odd = ""
number = "1234567890"
symbol = ""


for i in string:
    if i in alpha:
        lc += i
    elif i in alpha.upper():
        uc += i
    elif i in number:
        if int(i) % 2 == 0:
            even+=i
        else:
            odd += i
    elif i == " ":
         space += 1
    else:
         symbol += i
print(symbol+ " " +lc+ " " +uc+ " " +odd+ " " +even+ " " +str(space))
