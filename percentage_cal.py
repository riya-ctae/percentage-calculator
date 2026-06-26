name = input("Enter the name: ")
ma = int(input("Enter math marks: "))
evs = int(input("Enter EVS marks: "))
hin = int(input("Enter Hindi marks: "))
eng = int(input("Enter English marks: "))
total = ma+evs+hin+eng
per = total/4
print("Total marks:",total)
print("Percentage is:",per)
if(per>90):
    print("Grade A+")
elif(per<90 and per>75):
    print("Grade A")
elif(per<75 and per>65):
    print("Grade B")
elif(per<65 and per>50):
    print("Grade C")
elif(per<50 and per>33):
    print("Grade D")
else:
    print("Grade E")