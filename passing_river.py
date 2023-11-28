from tkinter import *
from PIL import Image, ImageTk
import time, winsound

def fresize(s, nw, nh):
    img = Image.open(s)
    resized = img.resize((nw, nh))
    new_img = ImageTk.PhotoImage(resized)
    return new_img

def check(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2

def eat(a):
    if len(a) == 0 or len(a) == 1: return
    if len(a) == 3:
        time.sleep(0.1)
        w.coords(wolf, gx, gy)
        w.itemconfig(goat, state = 'hidden')
        winsound.PlaySound('resources/chomp.wav', winsound.SND_FILENAME)
    elif len(a) == 2:
        currcx, currcy = w.coords(cabbage)
        currgx, currgy = w.coords(goat)
        if 'Cabb' in a and 'Goat' in a:
            time.sleep(0.1)
            w.coords(goat, currcx, currcy)
            w.itemconfig(cabbage, state = 'hidden')
            winsound.PlaySound('resources/chomp.wav', winsound.SND_FILENAME)
        elif 'Wolf' in a and 'Goat' in a:
            time.sleep(0.1)
            w.coords(wolf, currgx, currgy)
            w.itemconfig(goat, state = 'hidden')
            winsound.PlaySound('resources/chomp.wav', winsound.SND_FILENAME)
        else: return
    game_over()

def game_over(evt=None):
    global boat_stat
    boat_stat = "GV"
    w.coords(txt_restart, swidth//2, sheight//2)
    w.itemconfig(txt_restart, state='normal')
    w.itemconfig(rect_gameover, state='normal')
    w.itemconfig(txt_gameover, state='normal')

def check_win(evt=None):
    global left, ship, right, boat_stat
    if left == [] and ship == []:
        boat_stat = "GV"
        w.coords(txt_restart, swidth//2, sheight//2+100)
        w.itemconfig(txt_restart, state='normal')
        w.itemconfig(rect_win, state='normal')
        w.itemconfig(txt_win, state='normal')
    else: return

def restart(e):
    global cx, cy, wx, wy, gx, gx, bmx, bmy, left, right, ship, boat_stat
    w.itemconfig(rect_gameover, state='hidden')
    w.itemconfig(txt_gameover, state='hidden')
    w.itemconfig(rect_win, state='hidden')
    w.itemconfig(txt_win, state='hidden')
    w.itemconfig(txt_restart, state = 'hidden')
    w.itemconfig(cabbage, state = 'normal')
    w.itemconfig(goat, state = 'normal')
    w.itemconfig(wolf, state = 'normal')

    update_score(0)

    w.coords(cabbage, cx, cy)
    w.coords(wolf, wx, wy)
    w.coords(goat, gx, gy)
    w.coords(boatman, bmx, bmy)
    ship = []
    right = []
    left = ["Cabb", "Goat", "Wolf"]
    boat_stat = 0

def update_score(n):
    global bc
    bc = n
    w.itemconfig(txt_score, text=f"Number of river crossings: {n}")

def move(e):
    global boat_stat, rectx1, recty1, rectx2, recty2, rev, left, right, ship
    # if boat_stat == "GV":
    #     restart(None)
    #     return
    cabbx, cabby = w.coords(cabbage)
    cx1 = cabbx - cwidth//2
    cy1 = cabby - cheight//2
    cx2 = cabbx + cwidth//2
    cy2 = cabby + cheight//2
    # cabbrect = w.create_rectangle(cx1, cy1, cx2, cy2)

    goatx, goaty = w.coords(goat)
    gx1 = goatx - gwidth//2
    gy1 = goaty - gheight//2
    gx2 = goatx + gwidth//2
    gy2 = goaty + gheight//2
    # goatrect = w.create_rectangle(gx1, gy1, gx2, gy2)

    wolfx, wolfy = w.coords(wolf)
    wx1 = wolfx - wwidth//2
    wy1 = wolfy - wheight//2
    wx2 = wolfx + wwidth//2
    wy2 = wolfy + wheight//2
    # wolfrect = w.create_rectangle(wx1, wy1, wx2, wy2)
    
    boatmx, boatmy = w.coords(boatman)
    if check(e.x, e.y, cx1, cy1, cx2, cy2) and boat_stat != -1 and boat_stat != "GV":
        if "Cabb" in left and boat_stat == 0 and ship == []:
            w.coords(cabbage, boatmx+30, boatmy-5)
            left.remove("Cabb")
            ship.append("Cabb")
        elif "Cabb" in right and boat_stat == 1 and ship == []:
            w.coords(cabbage, boatmx+30, boatmy-5)
            right.remove("Cabb")
            ship.append("Cabb")
        elif "Cabb" in ship:
            ship.remove("Cabb")
            if boat_stat == 0:
                w.coords(cabbage, cx, cy)
                left.append("Cabb")
                check_win()
            else:
                w.coords(cabbage, cxr, cyr)
                right.append("Cabb")
                check_win()
        print(left, ship, right)
    elif check(e.x, e.y, gx1, gy1, gx2, gy2) and boat_stat != -1 and boat_stat != "GV":
        if "Goat" in left and boat_stat == 0 and ship == []:
            w.coords(goat, boatmx+40, boatmy-30)
            left.remove("Goat")
            ship.append("Goat")
        elif "Goat" in right and boat_stat == 1 and ship == []:
            w.coords(goat, boatmx+40, boatmy-30)
            right.remove("Goat")
            ship.append("Goat")
        elif "Goat" in ship:
            ship.remove("Goat")
            if boat_stat == 0:
                w.coords(goat, gx, gy)
                left.append("Goat")
                check_win()
            else:
                w.coords(goat, gxr, gyr)
                right.append("Goat")
                check_win()
        print(left, ship, right)
    elif check(e.x, e.y, wx1, wy1, wx2, wy2) and boat_stat != -1 and boat_stat != "GV":
        if "Wolf" in left and boat_stat == 0 and ship == []:
            w.coords(wolf, boatmx+40, boatmy-30)
            left.remove("Wolf")
            ship.append("Wolf")
        elif "Wolf" in right and boat_stat == 1 and ship == []:
            w.coords(wolf, boatmx+40, boatmy-30)
            right.remove("Wolf")
            ship.append("Wolf")
        elif "Wolf" in ship:
            ship.remove("Wolf")
            if boat_stat == 0:
                w.coords(wolf, wx, wy)
                left.append("Wolf")
                check_win()
            else:
                w.coords(wolf, wxr, wyr)
                right.append("Wolf")
                check_win()
        check_win()
        print(left, ship, right)
    elif check(e.x, e.y, rectx1, recty1, rectx2, recty2):
        # w.itemconfig(goat, state='hidden')
        if boat_stat != "GV":
            if boat_stat == 0:
                boat_stat = -1
                move_ship()
                boat_stat = 1
                rev = left
            elif boat_stat == 1:
                boat_stat = -1
                move_ship_rev()
                boat_stat = 0
                rev = right
            eat(rev)

def move_ship(evt=None):
    global dx, dy, bc
    update_score(bc+1)
    for i in range (45):
        # x, y = w.coords(boat)
        w.move(boatman, dx, dy)
        if "Cabb" in ship: w.move(cabbage, dx, dy)
        if "Goat" in ship: w.move(goat, dx, dy)
        if "Wolf" in ship: w.move(wolf, dx, dy)
        # w.coords(cabbage, x+30, y-5)
        window.update()
        time.sleep(0.02)
def move_ship_rev(evt=None):
    global dx, dy, bc
    update_score(bc+1)
    for i in range (45):
        # x, y = w.coords(boat)
        w.move(boatman, -dx, -dy)
        if "Cabb" in ship: w.move(cabbage, -dx, -dy)
        if "Goat" in ship: w.move(goat, -dx, -dy)
        if "Wolf" in ship: w.move(wolf, -dx, -dy)
        # w.coords(cabbage, x+30, y-5)
        window.update()
        time.sleep(0.02)


# Init
window = Tk()
window.title("Passing River")
window.iconbitmap("resources/boatman.ico")

#Constants
swidth, sheight = window.winfo_screenwidth(), window.winfo_screenheight()
bgwidth = sheight*1440//1008

cwidth, cheight = 90, 70
cx, cxr = 470, 900
cy, cyr = 605, 360

gwidth, gheight = 95, 114
gx, gxr = 350, 800
gy, gyr = 570, 300

wwidth, wheight = 130, 120
wx, wxr = 210, 670
wy, wyr = 500, 200

bmwidth, bmheight = 210, 124
bmx = 430
bmy = 440

rectx1, recty1, rectx2, recty2 = 950, 570, 1100, 630
dx, dy = 3, -2

#Variables
boat_stat = 0
left = ["Cabb", "Goat", "Wolf"]
ship = []
right = []
rev = []
bc = 0

#Main code
window.geometry(f"{swidth}x{sheight}")

#Canvas
w = Canvas(window, width = swidth, height = sheight, bg="#ffffff")
w.pack()
bg_img = fresize("resources/Bg.png", bgwidth, sheight)
bg = w.create_image(swidth//2, sheight//2, image=bg_img)

#Sprites
cabbage_img = fresize("resources/Cabbage.png", cwidth, cheight)
cabbage = w.create_image(cx, cy, image = cabbage_img, anchor = CENTER)

goat_img = fresize("resources/Goat.png", gwidth, gheight)
goat = w.create_image(gx, gy, image = goat_img, anchor = CENTER)

wolf_img = fresize("resources/Wolf.png", wwidth, wheight)
wolf = w.create_image(wx, wy, image = wolf_img, anchor = CENTER)

boatman_img = fresize("resources/Boatman.png", bmwidth, bmheight)
boatman = w.create_image(bmx, bmy, image = boatman_img, anchor = CENTER)

btn_go = w.create_rectangle(rectx1, recty1, rectx2, recty2, fill = 'white', outline = 'black')
txt_go = w.create_text(rectx1 + (rectx2 - rectx1)//2, recty1 + (recty2 - recty1)//2, text="GO", fill="black", font="Arial 20")

rect_gameover = w.create_rectangle(swidth//2-260, sheight//2-120, swidth//2+260, sheight//2+20, fill='white')
txt_gameover = w.create_text(swidth//2, sheight//2-50, text = "Game Over!!!", fill = 'red', font = "Arial 60")
w.itemconfig(rect_gameover, state='hidden')
w.itemconfig(txt_gameover, state='hidden')

rect_win = w.create_rectangle(swidth//2-260, sheight//2-20, swidth//2+260, sheight//2+120, fill='white')
txt_win = w.create_text(swidth//2, sheight//2+50, text = "You Win!!!", fill = '#e8b009', font = "Arial 70")
w.itemconfig(rect_win, state='hidden')
w.itemconfig(txt_win, state='hidden')

txt_restart = w.create_text(swidth//2, sheight//2, text = "Press \"Space\" to restart", font = "Arial 14")
w.itemconfig(txt_restart, state = 'hidden')

rect_score = w.create_rectangle((swidth-bgwidth)//2, 0, (swidth-bgwidth)//2+300, 40, fill = 'white')
txt_score = w.create_text((swidth-bgwidth)//2 + 150, 20, text = "Number of river crossings: 0", font = "Arial, 16")

window.bind("<Button-1>", move)
window.bind("<space>", restart)

#Mainloop
# window.after(200, move_ship)
window.state('zoomed')
window.mainloop()