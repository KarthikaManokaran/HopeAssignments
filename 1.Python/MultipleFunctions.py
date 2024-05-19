class multiple_functions():
    
    def SubFields():
        list =['Machine Learning','Neural Network','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub_fields in AI are:")
        for subfields in list:
            print(subfields)
            
    def OddEven():
        Num = int(input("Enter a Number:"))
        if(Num%2)==0:
            print(Num,"is Even Number")
        else:
            print(Num,"is Odd Number")
            
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="male"):
            if(age<21):
                print("Not-Eligible")
            else:
                print("Eligible")
        else:
            if(age<18):
                print("Not-Eligible")
            else:
                print("Eligible")
                
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total=(sub1+sub2+sub3+sub4+sub5)
        Percentage=Total/5
        print("Total:",Total)
        print("Percentage:",Percentage)
        
    def triangle():
        Height=float(input("Height:"))
        Breadth=float(input("Breadth:"))
        Area_of_triangle=1/2*Height*Breadth
        print("Area formula:(Height*Breadth)/2")
        print("Area of triangle:",Area_of_triangle)
        Height1=float(input("Height1:"))
        Height2=float(input("Height2:"))
        Breadth1=float(input("Breadth1:"))
        Perimeter_of_triangle=Height1+Height2+Breadth1
        print("Perimeter formula:Height1+Height2+Breadth1")
        print("Perimeter of triangle:",Perimeter_of_triangle)
    
    
        
    
    