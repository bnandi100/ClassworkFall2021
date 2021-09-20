#def my_input():
    #string_1=input("enter coordinate: ")
    #return string_1

def exercise(z1,z2,x3):
#def exercise(x1,y1,x2,y2,x3):
    x1=z1[0]
    y1=z1[1]
    x2=z2[0]
    y2=z2[1]
    m=(y2-y1)/(x2-x1)
    b=y2-m*x2
    y3 = m*x3 + b
    print(y3)
    return y3

if __name__ == "__main__":
    #z1=my_input()
    #z2=my_input()
    #x3=my_input()
    #exercise(z1,z2,x3)
    exercise((3,2),(4,5),1)
    #exercise(3,2,4,5,1)
