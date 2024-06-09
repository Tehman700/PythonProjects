one = ["0","0","0"]
two = ["0","0","0"]
three = ["0","0","0"]

map = [one,two,three]

ttt = input("ENTER WHERE YOU WANT TO MARK THE SPOT\n")

new = ttt.split(",")


if new[0]=='A':
    a = 0
elif new[0] =='B':
    a=1
elif new[0]== 'C':
    a=2

if new[0] ==  'a':
    a= 0
elif new[0] == 'b':
    a=1
elif new[0] == 'c':
    a=2


map[int(new[1])-1][int(a)] = "X"


print(f"{one}\n{two}\n{three}")




a = ["0","0","0"]
b = ["0","0","0"]
c = ["0","0","0"]

new_dd = [a,b,c]

ttt = input("ENTER WHERE YOU WANT TO MARK THE SPOT\n")

new = ttt.split(",")


new_dd[int(new[0])][int(new[1])] = "ttt"
print(f"{a}\n{b}\n{c}")
