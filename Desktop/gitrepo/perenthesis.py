txt = "()()[]{}"

j = 0
k = 0
for i in txt:
    if i == "(" or i == "{" or i == "[":
        j += 1
    if i == ")" or i == "}" or i == "]":
        k += 1
if j < k and j != 0 and k != 0:
    print("complete" + str(j))
    print("uncomplete" + str(k - j))
elif j > k and j != 0 and k != 0:
    print("complete" + str(k))
    print("uncomplete" + str(j - k))
elif j == k and j != 0 and k != 0:
    print("complete"+str(k))
