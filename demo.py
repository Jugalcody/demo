def isArmstrong(a): # To check the number is armstrong or not
   s=0
   a=str(a)
   for i in a:
       s=s+(int(i)*int(i)*int(i))
   if int(a)==s:
            return True
   else:
            return False


