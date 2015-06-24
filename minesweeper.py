import tkinter
import random










def pol_param():
    size = 50   
    a = 8
    b = 8
    n = 10
    return [size, a, b, n]





def perevod(a, v, d):
    f = a*v + d
    return f




def sozd_bomb(a, b, n):
    m = []
    for x in range(n):
        k = (random.randrange(a * b))
        while k in m:
            k = (random.randrange(a * b))
        m.append (k)
    return m



def prov(m, f):
    if f in m:
        return 1
    else:
        return 0






def sh_kl(m, f, a, b):
    if f in m:
        return("*")
    c = [prov (m, (f + 1)), prov (m, (f - 1)), prov (m, (f + a)), prov (m, (f - a)), prov (m, (f + a + 1)), prov (m, (f + 1 - a)), prov (m, (f - 1 - a)), prov (m, (f - 1 + a))]
    if (f+1) // a == 0:
        c[3] = 0
        c[5] = 0
        c[6] = 0
    if (f+1) > a*(b-1):
        c[2] = 0
        c[4] = 0
        c[7] = 0
    if (f+1) % a == 0:
        c[0] = 0
        c[4] = 0
        c[5] = 0
    if (f+1) % a == 1:
        c[1] = 0
        c[6] = 0
        c[7] = 0
    l = sum([i for i in c]) 
    return l

def sh_znach(m, a, b):
    pole = []
    for i in range(b):
        pole.append([0] * a)
    for x in range(a):
        for y in range(b):
            pole[x][y] = sh_kl(m, perevod(a, x, y), a, b)
    return pole



def mas(m, a, b):
    pole = []
    for i in range(b):
        s = []
        for t in range(a):
            s.append([0, 0, 0])
        pole.append(s)
    for x in range(a):
        for y in range(b):
            f = perevod(a, x, y)
            pole[x][y][0] = m[x][y]
    pole.append(0)
    return pole





def right_click(x, y, pole, a, b, size, canvas):
    if pole[-1] == 0:
        if pole[y][x][1] == 0:
            if pole[y][x][2] == 0:
                pole[y][x][2] = 1
            else:
                pole[y][x][2] = 0
        paint(pole, a, b, size, canvas)
    return (pole)



def left_click(x, y, pole, a, b, size, canvas):
    if pole[-1] == 0:
        if pole[y][x][2] == 0:
            pole[y][x][1] = 1
            if pole[y][x][0] == "*":
                pole[-1] = 1
                print("lose")
                for x in range(a):
                    for y in range(b):
                        pole[x][y][1] = 1
                        pole[x][y][2] = 0
            else:
                g = 0
                k = 0
                for x in range(a):
                    for y in range(b):
                        if pole[x][y][0] != "*":
                            g = g + 1
                for x in range(a):
                    for y in range(b):
                        if pole[x][y][1] == 1:
                            k = k + 1   
                if k == g:
                    print("win")
                    pole[-1] = 1
        paint(pole, a, b, size, canvas) 
    return (pole)



def first(x, y, pole, a, b, size, canvas, m):
    s = y*a + x
    if s in m:
        k = (random.randrange(a * b))
        while k in m:
            k = (random.randrange(a * b))
        m.append(k)
        m.remove(s)
        pole = sh_znach(m, a, b)
        pole = mas(pole, a, b)
        pole[y][x][1] = 1
        paint(pole, a, b, size, canvas)
    else:
        left_click(x, y, pole, a, b, size, canvas)
    return(pole)  



def LClick(event, size, pole, a, b, canvas, m):
    global k
    x, y = event.x, event.y
    y = y//size
    x = x//size
    if k == 0:
        k = 1
        first(x, y, pole, a, b, size, canvas, m)
    else:
        left_click(x, y, pole, a, b, size, canvas)
    return(pole)





def RClick(event, size, pole, a, b, canvas):
    x, y = event.x, event.y
    y = y//size
    x = x//size
    right_click(x, y, pole, a, b, size, canvas)
    return(pole)








def paint(pole, a, b, size, canvas):
    canvas.delete("all")
    for i in range(a):
        canvas.create_line(i*size, 0, i*size, b*size, fill = "green")
    for i in range(b):
        canvas.create_line(0, i*size, a*size, i*size, fill = "green")
    for x in range(a):
        for y in range(b):
            if pole[y][x][1] == 1:
                canvas.create_text((x+0.5)*size,(y+0.5)*size, text=str(pole[y][x][0]), fill = "green")
    for x in range(a):
        for y in range(b):
            if pole[y][x][2] == 1:
                canvas.create_text((x+0.5)*size,(y+0.5)*size, text="f", fill = "red")






dan = pol_param()
size = dan[0]

a = dan[1]
b = dan[2]

canvas = tkinter.Canvas(width=a*size, height=b*size)
for i in range(a):
    canvas.create_line(i*size, 0, i*size, b*size, fill = "green")
for i in range(b):
    canvas.create_line(0, i*size, a*size, i*size, fill = "green")



k = 0



m = sozd_bomb(dan[1], dan[2], dan[3])


canvas.pack()
pole = sh_znach(m, a, b)


pole = mas(pole, a, b)
paint(pole, a, b, size, canvas)
canvas.bind("<Button-3>", lambda evt: RClick(evt, size, pole, a, b, canvas))
canvas.bind("<Button-1>", lambda evt: LClick(evt, size, pole, a, b, canvas, m))
canvas.mainloop()
