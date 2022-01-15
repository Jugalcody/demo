a=int(input("Enter a num : "))
s=0
a=str(a)
for i in a:
  s=s+(int(i)*int(i)*int(i))
if int(a)==s:
      print(f"{a} is an armstrong number ")
else:
      print(f"{a} is not an armstrong number")

