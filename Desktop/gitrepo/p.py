txt = "{)"

# x = txt.find("("), ("["), ("{")
# y = txt.find(")"), ("]"), ("}")

x = txt.find("(") and txt.find("[") and txt.find("{")
y = txt.find(")") and txt.find("]") and txt.find("}")

if x < y:
    print("complete")
else:
    print("incomplete")
