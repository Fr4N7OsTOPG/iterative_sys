a = str(input())
sum = 0
for i in a:
    sum += ord(i)
if sum > (len(a)-1) * ord("а") + ord("А"):
    print("YES")
else:
    print("NO")
