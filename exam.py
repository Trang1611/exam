#bai1 
#a)
def gcd(a,b):
    import math
    return (math.gcd(a, b))
print(gcd(40,38))

#b)
def frac(a,b):
    import math
    c = a / math.gcd(a,b)
    d = b / math.gcd(a,b)
    return (c,'/',d)
print(frac(40,38))


#bai2
def n(n):
    a = []
    #a)
    for i in range (n):
        x = int(input("Hay nhap so: "))
        a.append(x)
    b = sum(a)
    print("Tong cua mang la", b)

    #b)
    min = a[0]
    for i in range (len(a)):
        if i < min:
            min = 1
    print ("So be nhat cua mang la", min)

    #c)
    max = a[0]
    for i in range (len(a)):
        if i > max:
            max = 1
    print ("So lon nhat cua mang la", max)

    #d)
    so_lan_x_hien_ra = 0
    y = int(input("Hay nhap so x de xem xuat hien bao nhieu lan: "))
    for i in range (len(a)):
        if a[i] == y:
            so_lan_x_hien_ra += 1
    print("So lan xuat hien cua x la", so_lan_x_hien_ra)  
print(n(5))


#bai3
def ascending(n):
    a = []
    for i in range (n):
        x = int(input("Hay nhap so: "))
        a.append(x)
    for i in range (len(a)-1):
        for j in range (len(a)-1-i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a
print (ascending(5))


#bai6
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
def check(n):
  stack = []
  if (n%2) != 0:
    return "Invalid"
  else:
    for i in range (n):
      x = input("Hay nhap mot ngoac tuy y: ")
      if x in open_list:
        stack.append(x)
      elif x in close_list:
        compare = close_list.index(x)
        if (len(stack) > 0) and (open_list[compare] == stack[len(stack)-1]):
          stack.pop ()
  if (len(stack) == 0):
    return "Valid"
  else:
    return "Invalid"
print(check(7))



                







