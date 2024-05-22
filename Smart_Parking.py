#Import Time
import re
from datetime import datetime
import datetime

Vehicle_Number=['XX XX XX XXXX']
Vehicle_Type=[]
vehicle_Name=[]
Owner_Name=[]
Date=[]
Time=[]
bikes=100
cars=250
bicycles=78
auto=100
def main():
    global bikes,cars,bicycles,auto
    try:
        while True:
            print("----------------------------------------------------------------------------------------")
            print("\t\tParking Management System")
            print("----------------------------------------------------------------------------------------")
            print("1.Vehicle Entry")
            print("2.Remove Entry" )
            print("3.View Parked Vehicle ")
            print("4.View Left Parking Space ")
            print("5.Amount Details ")
            print("6.Bill")
            print("7.Close Programme ")
            print("+---------------------------------------------+")
            ch=int(input("\tSelect option:"))
            if ch==1:
                
                no=True

                Vehicle_Number = []  # List to store unique vehicle number plates

                while no:
                    Vno = input("\tEnter vehicle number (e.g., MP-23-TY-6763) - ").upper()
                    Vno=Vno.replace("-"," ")              
                    def is_valid_plate_number(Vno):
                        pattern =r"[A-Z]{2} [0-9]{2} [A-Z]{2} [0-9]{4}"  # Regular expression for state-code-series-digits
                        return bool(re.fullmatch(pattern, Vno))  # Check full match using re.fullmatch
                    if Vno == "":
                        print("###### Enter a vehicle number. ######")
                    elif is_valid_plate_number(Vno):
                        if Vno in Vehicle_Number:
                            print("###### Vehicle Number Already Exists. ######")
                        else:
                            Vehicle_Number.append(Vno)
                        no = False  # Exit the loop once a valid unique plate is entered
                    else:
                        print("###### Enter a valid vehicle number in the format 'XX-XX-XX-XXXX'. ######")

                    print("Vehicle Number(s) entered:")
                    for plate in Vehicle_Number:
                        print(plate)

                # while no==True:
                #     Vno=input("\tEnter vehicle number (XXXX-XX-XXXX) - ")
                #     plate_parts =Vno.split()  # Split into individual strings
                #     Vno= "".join(plate_parts)  # Join without spaces
                    
                #     if Vno=="":
                #         print("###### Enter Vehicle No. ######")
                #     elif Vno in Vehicle_Number:
                #         print("###### Vehicle Number Already Exists")
                #     elif len(Vno)==12:
                #         no=not True
                #         Vehicle_Number.append(Vno)
                #     else:
                #         print("###### Enter Valid Vehicle Number ######")

                #   This is used to enter the type of vechicle.
                
                typee=True
                while typee==True:
                    Vtype=str(input("\tEnter vehicle type(Bicycle=A/Bike=B/Car=C/Auto=D):")).lower()
                    if Vtype=="":
                        print("######.....................Enter Vehicle Type..................... ######")
                    elif Vtype=="a":
                        Vehicle_Type.append("Bicycle")
                        bicycles-=1
                        typee=not True
                    elif Vtype=="b":
                        Vehicle_Type.append("Bike")
                        bikes-=1
                        typee=not True
                    elif Vtype=="c":
                        Vehicle_Type.append("Car")
                        cars-=1
                        typee=not True
                    elif Vtype=="d":
                        Vehicle_Type.append("Auto")
                        auto-=1
                        typee=not True
                    else:
                        print("###### Please Enter Valid Option ######")
                
                # this is used to enter the vechicle name.

                name=True
                while name==True:
                    vname=input("\tEnter vehicle name - ")
                    if vname=="":
                        print("########Please Enter Vehicle Name ########")
                    else:
                        vehicle_Name.append(vname)
                        name=not True
                o=True
                while o==True:
                    OName=input("\tEnter owner name - ")
                    if OName=="":
                        print("###### Please Enter Owner Name ######")
                    else:
                        Owner_Name.append(OName)
                        o=not True
                
                


                




                # # Get the current date
                # today = datetime.today()

                # # Format the date as DD-MM-YYYY
                # formatted_date = today.strftime("%d-%m-%Y")  # Use "-" as separator

                # # Print the formatted date
                # print(formatted_date)



                
                
                
                d=True
                while d==True:
                # Get the current date object
                    today = datetime.date.today()

                    # Format the date object in DD-MM-YYYY format using strftime()
                    formatted_date = today.strftime("%d-%m-%Y")

                    Date.append(formatted_date)
                    d=not True

                t=True
                while t==True:
                    current_time = datetime.datetime.now()
                    formatted_time = current_time.strftime("%H:%M:%S")  # Use %H for 24-hour format
                    Time.append(formatted_time)
                    t=not True
                print("\n............................................................Record detail saved..................................................................")
            
            
            elif ch==2:
                no=True
                while no==True:
                    Vno=input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ").upper()
                    if Vno=="":
                        print("###### Enter Vehicle No. ######")
                    elif len(Vno)==12:
                        if Vno in Vehicle_Number:
                            i=Vehicle_Number.index(Vno)
                            Vehicle_Number.pop(i)
                            Vehicle_Type.pop(i)
                            vehicle_Name.pop(i)
                            Owner_Name.pop(i)
                            Date.pop(i)
                            Time.pop(i)
                            no=not True
                            print("\n............................................................Removed Sucessfully..................................................................")
                        elif Vno not in Vehicle_Number:
                            print("###### No Such Entry ######")
                        else:
                            print("Error")
                    else:
                        print("###### Enter Valid Vehicle Number ######")
            elif ch==3:
                count=0
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tParked Vehicle")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("Vehicle No.\tVehicle Type        Vehicle Name\t       Owner Name\t     Date\t\tTime")
                print("----------------------------------------------------------------------------------------------------------------------")
                for i in range(len(Vehicle_Number)):
                    count+=1
                    print(Vehicle_Number[i],"\t  ",Vehicle_Type[i],"\t            ",vehicle_Name[i],"\t       ",Owner_Name[i],"      " ,Date[i],"          ",Time[i])
                print("----------------------------------------------------------------------------------------------------------------------")
                print("------------------------------------------ Total Records - ",count,"-------------------------------------------------------")
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch==4:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tSpaces Left For Parking")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\tSpaces Available for Bicycle - ",bicycles)
                print("\tSpaces Available for Bike - ",bikes)
                print("\tSpaces Available for Car - ",cars)
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch==5:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("\t\t\t\tParking Rate")
                print("----------------------------------------------------------------------------------------------------------------------")
                print("*1.Bicycle      Rs20 / Hour")
                print("*2.Bike         Rs40/ Hour")
                print("*3.Car          Rs60/ Hour")
                print("----------------------------------------------------------------------------------------------------------------------")
            elif ch==6:
                print(".............................................................. Generating Bill ..........................................................................")
                no=True
                while no==True:
                    Vno=input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ").upper()
                    if Vno=="":
                        print("###### Enter Vehicle No. ######")
                    elif len(Vno)==12:
                        if Vno in Vehicle_Number:
                            i=Vehicle_Number.index(Vno)
                            no=not True
                        elif Vno not in Vehicle_Number:
                            print("###### No Such Entry ######")
                        else:
                            print("Error")
                    else:
                        print("###### Enter Valid Vehicle Number ######")
                print("\tVehicle Check in time - ",Time[i])
                print("\tVehicle Check in Date - ",Date[i])
                print("\tVehicle Type - ",Vehicle_Type[i])
                inp=True
                amt=0
                while inp==True:
                    hr=input("\tEnter No. of Hours Vehicle Parked - ").lower()
                    if hr=="":
                        print("###### Please Enter Hours ######")
                    elif int(hr)==0 and Vehicle_Type[i]=="Bicycle":
                        amt=20
                        inp=not True
                    elif int(hr)==0 and Vehicle_Type[i]=="Bike":
                        amt=40
                        inp=not True
                    elif int(hr)==0 and Vehicle_Type[i]=="Car":
                        amt=60
                        inp=not True
                    elif int(hr)>=1:
                        if Vehicle_Type[i]=="Bicycle":
                            amt=int(hr)*int(20)
                            inp=not True
                        elif Vehicle_Type[i]=="Bike":
                            amt=int(hr)*int(40)
                            inp=not True
                        elif Vehicle_Type[i]=="Car":
                            amt=int(hr)*int(60)
                            inp=not True
                print("\t Parking Charge - ",amt)
                ac=18/100*int(amt)
                print("\tAdd. charge 18 % - ",ac)
                print("\tTotal Charge - ",int(amt)+int(ac))
                print("..............................................................Thank you for using our service...........................................................................")
                a=input("\tPress Any Key to Proceed - ")
            elif ch==7:
                print("..............................................................Thank you for using our service...........................................................................")
                print("                                     ***(: Bye Bye :)***")
                break
                quit
    except:
        main()
main()