print("Welcome to the Website of IRCTC")
a=str(input("1.SCHEDULE\n2.BOOK TICKETS\nENTER THE NUMBER YOU WANT:"))
#options regarding choosing the outputs are given above
#here the schedule is been coded 
if(a=="1"):
    print(" Train Schedule")
    opr=str(input("From     To       Time       Train    Duration    \nBaroda   Ajmer    1Pm-8Pm   BR-AJ-SL  8 Hours    \nPatna    Delhi    9Pm-11Am  PA-DL-AC  14 Hours   \nMumbai   Bhuj     10Am-8Pm  MU-BH-SF  10 Hours   \nAjmer    Delhi    6Am-10Am  AL-DE-Gl  4 Hours    \nPatna    Orissa   1AM-11PM  PA-OR-AC1 11 Hours   \nAjmer    Patna    6AM-11PM  AJ-PA-RC  17 Hours   \n Press Enter to Book Tickets"))
    print("*******************************************************************************")                                                                                                                                   
if(a=="2"):
    print("             Book ticikets            ")
import random
number=random.randint(1000000000,9999999999)
TRIP=random.randint(1,99)
#here the random command  is been used to give us the random generated numbers for the pnr number
opr=str(input("NO From     To       Train    \n1) Baroda   Ajmer    BR-AJ-SL  \n2) Patna    Delhi    PA-DL-AC   \n3) Mumbai   Bhuj     MU-BH-SF  \n4) Ajmer    Delhi    AL-DE-Gl  \n5) Patna    Orissa   PA-OR-AC1 \n6) Ajmer    Patna    AJ-PA-RC  \nPRESS ENTER THE Train NO:"))
if(opr=='1'):
    t="Baroda-Ajmer"
    a=680
elif(opr=='2'):
    t="Patna-Delhi"
    a=1350
elif(opr=='3'):
    t="Mumbai-Bhuj"
    a=980
elif(opr=='4'):
    t="Ajmer-Delhi"
    a=860
elif(opr=='5'):
    t="Patna-Orissa"
    a=1520
elif(opr=='6'):
    t="Ajmer-Patna"
    a=1800
#here the if\elif loops are been used which are to be choosen by the user
cla=str(input("Enter the class preffered:\n1.Genrel\n2.Sleeper\n3.AC-2 TIER\n4.AC-1 TIER\n5.LUXURY\n Enter the no you want:"))
if(cla=="1"):
    clas="Generel"
    prize=200
elif(cla=="2"):
    clas="sleeper"
    prize=300
elif(cla=="3"):
    clas="AC-2 TIER"
    prize=600
elif(cla=="4"):
    clas="AC-1 TIER"
    prize=900
elif(cla=="5"):
    clas="LUXURY"
    prize=1500
#here the if\elif loops are been used which are to be choosen by the user
print("TRAIN:",t)
print("CLASS:",clas)
d=a+prize
print("Basic Fare(1-person):",d)
fr=str(input(" Source Station:"))
to=str(input(" Destination:"))
n=int(input("No. of pasangers :"))
email=str(input("Enter the Email Address of the passanger( Atleast One Required):"))
date=str(input(" Enter the Date you want to Travel( DD-MM-YYYY ):"))
#here the int,str is used to get the preferred format input from the used,int deals with integers,str deals with alphabets and words
passangers={}
for a in range(n):
    key = input("Full Name of passanger :")
    value = int(input(" Phone number of Passanger ( 10 Digits) :"))
    comp=int(input("Enter the Age:"))
    nitro=int(input("Enter the Aadhar card no:",))
fare=d*n
#here the for loop is given to get the details of the passangers,THE loop runs n times given above in the number of passangers
print("The total fare is:",fare) 
opr=str(input("Mode of payment:\n1.ONLINE PAYMENT\n2.PAYTM\nEnter the no you Want:"))
#here the mode of payment is given opreated by the input from the user
if(opr=='1'):
    int(input(" Enter the CARD No:")) 
    str(input("Enter the Expiry date(MM-YYYY):"))
    str(input("Enter the CVV:")) 
#here the card details as input is taken from the user which prints the tickets
elif(opr=='2'):
    int(input("Enter the Paytm Registered No:"))
#here the paytm details as input is taken from the user which prints the tickets
number2=random.randint(1000,9999)
number1=random.randint(1000,9999)
#here number1,2 is used to perform the capacha type of verification by generating random numbers between the given range of input
print("                    Code:",number2)
a=int(input("Enter the code:"))
if(number2==a):
    print("The payment is sucessful RS",fare,"/-","Your Ticket is Printed Below")
    print("**************************************************************************************************")

    print("____________________E-TICKET____________________")

    print("PNR NUMBER:",number)
    print("DATE:",date)
    print("TRIP CODE:","c",TRIP)
    print("TRAIN:",t)
    print("CLASS:",clas)
    print("JOURNEY FROM:",fr)
    print("JOURNEY TO:",to)
    print("No of Passangers:",n)
    print("Full name of a passenger(one only):",key)
    print("Phone no:", value)
    print("AGE:",comp)
    print("Aadhar NO:",nitro)
   
    print("EMAIL-ID:",email)
    print("The Amount sucessfully paid is:",fare,"/-")
    print("*************************NOTE*****************************")
    print("Trip code can be used to get seat number(s) at the source station.\nIt will also be forwarded to the regestired email after the final chart")
    print(" Thank you for choosing IRCTC")

    print("**************************************************************************************************")

else:
    print("The payment is unsucessful")
    print("                  Code:",number1)
    b=int(input("Enter the code AGAIN:"))
    if(number1==b):
        print(" THE PAYMENT IS SUCESSFUL")
        print("The payment is sucessful RS",fare,"/-","Your Ticket is Printed Below")
        print("**************************************************************************************************")

        print("____________________E-TICKET____________________")

        print("PNR NUMBER:",number)
        print("DATE:",date)
        print("TRIP CODE:","c",TRIP)
        print("TRAIN:",t)
        print("CLASS:",clas)
        print("JOURNEY FROM:",fr)
        print("JOURNEY TO:",to)
        print("No of Passangers:",n)
        print("Full name of a passenger(one only):",key)
        print("Phone no:", value)
        print("AGE:",comp)
        print("Aadhar NO:",nitro)
        
        print("EMAIL-ID:",email)
        print("The Amount sucessfully paid is:",fare,"/-")
        print("*************************NOTE*****************************")
        print("Trip code can be used to get seat number(s) at the source station.\nIt will also be forwarded to the regestired email after the final chart")

        print(" Thank you for choosing IRCTC")

        print("**************************************************************************************************")



    else:
        print("You have given too many wrong inputs above.Please try again later")


#here according to the generated codes above a verification of same numbers is done and as the output the ticket is printed
#the payment is sucessful and the positive output is given from the given codes
#if the user inputs the Wrong random codes for two times then the whole loop is been terminated and nothing is given as the output
