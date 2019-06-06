def updateMonth():
    newfile=open("mcnt",'w')
    txt=int(input("Enter month in number : "))
    newfile.write(str(txt-1))
    newfile.close()
def updateYear():
    newfile=open("ycnt",'w')
    print("2016 - 0")
    print("2017 - 1")
    print("2018 - 2")
    print("2019 - 3")
    print("2020 - 4")
    print("2021 - 5")
    print("2022 - 6")
    txt=int(input("Enter Year : "))
    newfile.write(str(txt))
    newfile.close()
print("M for Month")
print("Y for Year")
print("B for Both")
res=input("What to update (M/Y/B) : ")
if(res=='M' or res=='m'):
    updateMonth()
elif(res=='Y' or res=='y'):
    updateYear()
elif(res=='B' or res=='b'):
    updateMonth()
    updateYear()
else:
    print("Invalid Response")
