class MultiFunctions:
    def subFields():
        aiList=("Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing")
        print("Sub-fields in AI are:")
        for field in aiList:
            print(field)

    def oddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(str(num)+ " is Even number")
        else:
            print(str(num)+ " is Odd number")

    def eligible():
        gender=input("Enter your gender:")
        age=int(input("Enter your age:"))
        print("Your Gender:"+gender)
        print("Your Age:"+str(age))
        if((gender == "Male" and age >= 21) or (gender == "Female" and age >= 18)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        marks=(("Subject1",98),("Subject2",87),("Subject3",95),("Subject4",95),("Subject5",93))
        total=0
        for subject,mark in marks:
          print(f"{subject}={mark}")
          total=total+mark
    
        print("Total:"+str(total))
        percentage=total/500*100
        print("Percentage:"+str(percentage))

    def triangle(height,breadth,height1,height2,breadth1):
        print("Height:"+str(height))
        print("breadth:"+str(breadth))
        print("Area formula: (Height*Breadth)/2")
        area=(height*breadth)/2
        print("Area of Triangle:"+str(area))
        print("Height1:"+str(height1))
        print("Height2:"+str(height2))
        print("Breadth:"+str(breadth1))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=height1+height2+breadth1
        print("Perimeter of Triangle:"+str(perimeter))   
       