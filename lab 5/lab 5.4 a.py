#Student ID : 1201201564
#Student Name : Goh Jia Chen

def rectangle(w,l):
    area = w * l
    return area

def triangle(w,l):
    area = w * l / 2
    return area

width = float(input("Enter width   : "))
length = float(input("Enter length  : "))

area_rec = rectangle(width,length)
area_tri = triangle(width,length)

print("Rectangle area : {:.2f}".format(area_rec))
print("Triangle area  : {:.2f}".format(area_tri))