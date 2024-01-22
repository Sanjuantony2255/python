area_s=lambda a:a*a
area_r=lambda l,b:l*b
area_t=lambda h,b1:0.5*h*b1
a=int(input("enter the sidelength of square:"))
print("area of square is:",area_s(a))
l=int(input("enter the length of rectangle:"))
b=int(input("enter the breadth of rectangle:"))
print("area of rectangle is:",area_r(l,b))
h=int(input("enter the height of triangle:"))
b1=int(input("enter the breadth of triangle:"))
print("area of triangle is:",area_t(h,b1))
