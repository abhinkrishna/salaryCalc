n=int(input("Enter the number of dates : "))
amt=[]
exp=[]
prf=[]    #amt-exp
for  i in range(0,n):
    print("DAY ",i+1)
    amt.append(float(input("Enter the Amount  : ")))
    exp.append(float(input("Enter the Expence : ")))
    prf.append(float((amt[i]-exp[i])))
    print("Profit            :",prf[i])
#Finding sum
amt_sum=0
exp_sum=0
prf_sum=0
for  i in range(0,n):
    amt_sum=amt_sum+amt[i]
    exp_sum=exp_sum+exp[i]
    prf_sum=prf_sum+prf[i]
#Printing Sums
print("\n")
print("*******Summary*******")
print("Total Amount  : ",amt_sum)
print("Total Expence : ",exp_sum)
print("Total Profit  : ",prf_sum)
#General expense
gen_exp=int(input("Enter General Expense : "))
real_prf=prf_sum-gen_exp
print("Real Profit :",real_prf)
print("\n")

#Reading percentages
fst_prcntge = int(input("Enter the First Percentage ([0-100]eg:80) : "))
scnd_prcntge = int(input("Enter the Second Percentage ([0-100]eg:80) : "))

#Finding % and Prnting
prf_fst = real_prf * (fst_prcntge/100)
prf_scnd = real_prf * (scnd_prcntge/100)
print("\n")
print("First " , fst_prcntge , "%   : " ,prf_fst)
print("Second " , scnd_prcntge , "% : " ,prf_scnd)

ans=input("\nDo you want to save this (Y/N) : ")
if(ans=='y' or ans=='Y'):
    #Fetching data from mcnt
    f_mcnt=open("Data/mcnt",'r')
    m_data=int(f_mcnt.readline())
    f_mcnt.close()
    #Fetching data from ycnt
    f_ycnt=open("Data/ycnt",'r')
    y_data=int(f_ycnt.readline())
    f_ycnt.close()
    #Finding Month
    month=['Jan','Feb','Mar','Arp','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
    year=['2016','2017','2018','2019','2020','2021','2022']
    #Making File Name
    newfile_name='Exports/'+month[m_data]+year[y_data]+'.txt'
    #Creating a file with month and year
    newfile=open(newfile_name,'w')
    #Creating a statement line
    line1="Number of Days  : "+str(n)
    line2="\n\nTotal Amount    : "+str(amt_sum)
    line3="\nTotal Expence   : "+str(exp_sum)
    line4="\nTotal Profit    : "+str(prf_sum)
    line5="\n\nGeneral Expense : "+str(gen_exp)
    line6="\nReal Profit     : "+str(real_prf)
    line7="\n\nFirst   "+ str(fst_prcntge) +"%  : "+str(prf_fst)
    line8="\nSecond "+ str(scnd_prcntge) +"%  : "+str(prf_scnd)
    txt=line1+line2+line3+line4+line5+line6+line7+line8
    #Writing to file
    newfile.write(txt)
    newfile.close()
    print("Done! File created successfully")
    end = input("Press any key to exit...")
    #Updating Month
    m_data=m_data+1
    f_mcnt=open("Data/mcnt",'w')
    if(m_data<12):
        f_mcnt.write(str(m_data))
    else:
        f_mcnt.write('0')
        #Updating Year
        y_data=y_data+1
        f_ycnt=open("Data/ycnt",'w')
        f_ycnt.write(str(y_data))
    f_mcnt.close()
else:
    print("\n\nPress ender to close")
    end = input("Press any key to exit...")
