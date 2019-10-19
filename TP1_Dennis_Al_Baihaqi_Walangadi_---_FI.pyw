import turtle
import random

#Tanya berapa panjang sisi persegi terpendek
try:
    panjangkotak = int(turtle.numinput("Rotating Colorful Squares and Disks",                       #Judul
                                       "Please enter the side length of the first square [20-60]",  #Kalimat input
                                       40,                                                          #Default input
                                       minval=20,                                                   #Batas minimum
                                       maxval=60))                                                  #Batas maksimum
#Error handling jika user tekan cancel
except TypeError:
    exit()

#Mempersiapkan Turtle
turtle.title("Rotating Colorful Squares and Disks") #Judul window
turtle.colormode(255)
turtle.hideturtle()
turtle.speed(0)
turtle.pu()

#Loop Kotak Warna-warni
hitungkotak = 0
hitungsisi = 0
derajatkotak = 0
#Tentukan posisi awal di kiri
turtle.setpos(-200, 0)

while hitungkotak < 72:
   turtle.pd()
   #Random warna pake turtle.fillcolor(r,g,b)
   turtle.fillcolor(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
   turtle.begin_fill()

   #Nested loop untuk membuat kotak
   for i in range(4):
       turtle.left(90)
       turtle.fd(panjangkotak)

   #Penutup sebelum repeat
   turtle.pu()
   turtle.end_fill()
   turtle.setheading(derajatkotak)

   #Selalu bertambah sisinya 2
   panjangkotak += 2
   hitungkotak += 1
   hitungsisi += 1
   derajatkotak -= 5

#Deklarasi variabel lingkaran
hitunglingkaran = 0
derajatlingkaran = 0
panjanglingkaran = panjangkotak/2

#Loop lingkaran
while hitunglingkaran < 36:
    turtle.goto(200, 0)
    turtle.pd()
    turtle.fillcolor(random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255))  # Random warna pake turtle.fillcolor(r,g,b)
    turtle.begin_fill()
    turtle.setheading(derajatlingkaran)
    turtle.circle(panjanglingkaran)
    turtle.end_fill()
    turtle.pu()
    hitunglingkaran += 1
    derajatlingkaran += 10
    panjanglingkaran -= 2

#Menulis jumlah geometri
turtle.goto(0, -250)
turtle.color('blue')
turtle.begin_fill()
turtle.write("There are "+str(hitungkotak)+" Squares and "+str(hitunglingkaran)+" Disks", False, align="center", font=("Arial", 24, "normal"))
turtle.end_fill()

#Exit jika klik windows
turtle.exitonclick()
