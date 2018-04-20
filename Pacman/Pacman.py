#-*- coding: utf-8 -*-
from tkinter import *
import random
import time
import winsound
from time import strftime

pencere=Tk()
pencere.geometry("705x555")
başlık=pencere.title("Pacman")

BSaniye=int(strftime("%S"))
BDakika=int(strftime("%M"))
başlangıç=[BDakika,BSaniye]
Süre=["a"]

canvas1=Canvas(bg="black", width=250, height=250)
canvas1.pack(expand=1, fill=BOTH)

yüz=PhotoImage(file="karekter.png")
göster=canvas1.create_image(55, 55, image=yüz)
konum=[60,55]
duvar=PhotoImage(file="duvar.png")
nokta=PhotoImage(file="altın.png")

içDuvar={20:[25,60,95,130,165,200,235,270,305,340,375,410,445,480,515,550,585,620,655,690],  55:[25,130,410,445,620,690],  90:[25,130,200,235,270,305,340,410,445,480,515,550,620,690],
         125:[25,200,270,445,550,690],  160:[25,60,95,130,200,340,375,655,690],  195:[25,200,235,270,305,340,375,410,445,480,515,550,585,690],  230:[25,60,130,410,445,515,585,620,690],
         265:[25,60,95,130,165,200,235,270,340,410,585,690],  300:[25,270,480,515,550,585,655,690],  335:[25,95,165,270,305,340,375,480,690],
         370:[25,95,130,165,200,270,375,410,480,585,620,655,690],  405:[25,95,200,270,340,375,480,550,585,690],  440:[25,95,130,200,375,445,480,585,655,690],
         475:[25,200,235,305,655,690],  510:[25,60,95,130,165,200,235,270,305,340,375,410,445,480,515,550,585,620,655,690]}

n1=canvas1.create_image(55,125,image=nokta)
n2=canvas1.create_image(230,55,image=nokta)
n3=canvas1.create_image(335,55,image=nokta)
n4=canvas1.create_image(230,125,image=nokta)
n5=canvas1.create_image(300,160,image=nokta)
n6=canvas1.create_image(440,160,image=nokta)
n7=canvas1.create_image(475,55,image=nokta)
n8=canvas1.create_image(510,125,image=nokta)
n9=canvas1.create_image(580,160,image=nokta)
n10=canvas1.create_image(650,55,image=nokta)
n11=canvas1.create_image(55,195,image=nokta)
n12=canvas1.create_image(90,230,image=nokta)
n13=canvas1.create_image(230,230,image=nokta)
n14=canvas1.create_image(230,300,image=nokta)
n15=canvas1.create_image(370,300,image=nokta)
n16=canvas1.create_image(475,230,image=nokta)
n17=canvas1.create_image(545,230,image=nokta)
n18=canvas1.create_image(650,230,image=nokta)
n19=canvas1.create_image(650,335,image=nokta)
n20=canvas1.create_image(510,335,image=nokta)
n21=canvas1.create_image(335,370,image=nokta)
n22=canvas1.create_image(405,405,image=nokta)
n23=canvas1.create_image(370,475,image=nokta)
n24=canvas1.create_image(510,475,image=nokta)
n25=canvas1.create_image(650,405,image=nokta)
n26=canvas1.create_image(265,475,image=nokta)
n27=canvas1.create_image(125,335,image=nokta)
n28=canvas1.create_image(125,405,image=nokta)
n29=canvas1.create_image(55,475,image=nokta)
n30=canvas1.create_image(55,370,image=nokta)

kalp=PhotoImage(file="kalp.png")
kalp1=canvas1.create_image(320,540,image=kalp)
kalp2=canvas1.create_image(290,540,image=kalp)
kalp3=canvas1.create_image(350,540,image=kalp)
canHakkı=[kalp2,kalp1,kalp3]

altın={n1:[55,125],n2:[230,55],n3:[335,55],n4:[230,125],n5:[300,160],n6:[440,160],n7:[475,55],n8:[510,125],n9:[580,160],n10:[650,55],n11:[55,195],n12:[90,230],
       n13:[230,230],n14:[230,300],n15:[370,300],n16:[475,230],n17:[545,230],n18:[650,230],n19:[650,335],n20:[510,335],n21:[335,370],n22:[405,405],n23:[370,475],
       n24:[510,475],n25:[650,405],n26:[265,475],n27:[125,335],n28:[125,405],n29:[55,475],n30:[55,370]}

canavarResmi=PhotoImage(file="canavar.png")
canavar=canvas1.create_image(545,475,image=canavarResmi)
canavar2=canvas1.create_image(125,300,image=canavarResmi)
canavar3=canvas1.create_image(580,160,image=canavarResmi)
canavarKonum=[545,475]
canavarKonum2=[125,300]
canavarKonum3=[580, 160]
dizi=[canavarKonum,canavarKonum2,canavarKonum3]
dizi2=[canavar,canavar2,canavar3]

for i in içDuvar:
    for j in range (0,len(içDuvar[i]),1):
        göster2=canvas1.create_image(içDuvar[i][j]-5, i, image=duvar)

sözlük=[[11,33]]
skor=[0]
yazı2=Label(text=skor[0],fg="White", bg="Black", font="Times 13")
yazı2.place(x=65,y=528)

def kontrolEt():

    SSaniye=int(strftime("%S"))
    SDakika=int(strftime("%M"))

    if(başlangıç[1]>SSaniye):
        if(başlangıç[0]>SDakika):
            b=başlangıç[0]-SDakika+1
            dakika=60-b
        else:
            dakika=SDakika-başlangıç[0]-1
        a=başlangıç[1]-SSaniye
        saniye=60-a
    else:
        dakika=SDakika-başlangıç[0]
        saniye=SSaniye-başlangıç[1]
    yazı=str(dakika)+":"+str(saniye)
    Süre[0]=yazı
    süreSil=Label(text="                           ", fg="Black", bg="Black")
    süreSil.place(x=610,y=528)

    süre=Label(text=yazı, fg="White", bg="Black", font="Times 13")
    süre.place(x=610,y=528)

    deger=1
    sayı=0
    for i in içDuvar:
        for j in range (0,len(içDuvar[i]),1):
            if(konum[0]==içDuvar[i][j] and konum[1]==i):
                deger=0

    for i in altın:
        if(altın[i][0]==konum[0]-5 and altın[i][1]==konum[1]):
            canvas1.delete(i)
            for a in range(0,len(sözlük),1):
                if(sözlük[a][0]==altın[i][0] and sözlük[a][1]==altın[i][1]):
                    sayı=1
            if(sayı==0):
                sözlük.append(altın[i])
                skor[0]=skor[0]+100
                yazı2=Label(text=skor[0],fg="White", bg="Black", font="Times 13")
                yazı2.place(x=60,y=528)
                winsound.PlaySound("altın.wav", winsound.SND_ASYNC)

    if(deger==0):
        return 0
    else:
        return 1
can=[0]
def yanma():
    x=konum[0]-5
    y=konum[1]
    yüz=[x, y]
    if(yüz==canavarKonum or yüz==canavarKonum2 or yüz==canavarKonum3):
        canvas1.delete(canHakkı[can[0]])
        can[0]=can[0]+1
        winsound.PlaySound("hata.wav", winsound.SND_ASYNC)

    if(can[0]==3):
        time.sleep(.2)
        canvas1.delete("all")

        skor2=Label(text="                           ", fg="Black", bg="Black")
        skor2.place(x=20, y=528)

        süre1=Label(text="                           ", fg="Black", bg="Black")
        süre1.place(x=575, y=528)
        sonYazı="Skor: "+str(skor[0])+"\nSüre: "+Süre[0]
        yazı=Label(text=sonYazı, fg="White", bg="Black", font="Times 25")
        yazı.place(x=275, y=200)

yazı1=Label(text="Skor: ",fg="White", bg="Black", font="Times 13")
yazı1.place(x=20,y=528)

süre1=Label(text="Süre: ",fg="White", bg="Black", font="Times 13")
süre1.place(x=575,y=528)

def sağa(globals):
    sayı=[35,0]
    konum[0]=konum[0]+sayı[0]
    deger=kontrolEt()
    if(deger==0):
        konum[0]=konum[0]-sayı[0]
    else:
        canvas1.move(göster, 35, 0)
        canvar()
        yanma()

def sola(globals):
    sayı=[-35,0]
    konum[0]=konum[0]+sayı[0]
    deger=kontrolEt()
    if(deger==0):
        konum[0]=konum[0]-sayı[0]
    else:
        canvas1.move(göster, -35, 0)
        canvar()
        yanma()

def yukarı(globals):
    sayı=[0,-35]
    konum[1]=konum[1]+sayı[1]
    deger=kontrolEt()
    if(deger==0):
        konum[1]=konum[1]-sayı[1]
    else:
        canvas1.move(göster, 0, -35)
        canvar()
        yanma()

def aşagı(globals):
    sayı=[0,35]
    konum[1]=konum[1]+sayı[1]
    deger=kontrolEt()
    if(deger==0):
        konum[1]=konum[1]-sayı[1]
    else:
        canvas1.move(göster, 0, 35)
        canvar()
        yanma()

def canvar():

    def Yukarı(asd):
        sayı=[0,-35]
        dizi[asd][1]=dizi[asd][1]+sayı[1]
        canvas1.move(dizi2[asd], 0, -35)

    def Aşagı(asd):
        sayı=[0,35]
        dizi[asd][1]=dizi[asd][1]+sayı[1]
        canvas1.move(dizi2[asd], 0, 35)

    def Sağa(asd):
        sayı=[35,0]
        dizi[asd][0]=dizi[asd][0]+sayı[0]
        canvas1.move(dizi2[asd], 35, 0)

    def Sola(asd):
        sayı=[-35,0]
        dizi[asd][0]=dizi[asd][0]+sayı[0]
        canvas1.move(dizi2[asd], -35, 0)

    canavarHareketi={"[615, 475]":[Yukarı,Sola],"[615, 440]":[Aşagı,Yukarı],"[580, 475]":[Sağa,Sola],"[545, 475]":[Sağa,Sola,Yukarı],"[615, 405]":[Aşagı,Sağa],"[650, 405]":[Sola],
                     "[545, 440]":[Aşagı,Sola],"[510, 440]":[Sağa,Aşagı,Yukarı],"[510, 475]":[Yukarı,Sağa,Sola],"[475, 475]":[Sağa,Sola],"[440, 475]":[Sağa,Sola],
                     "[405, 475]":[Sağa,Sola,Yukarı],"[370, 475]":[Sağa,Sola],"[335, 475]":[Sağa,Yukarı],"[335, 440]":[Sola,Aşagı],"[300, 440]":[Sağa,Sola,Yukarı],
                     "[265, 440]":[Sağa,Sola,Aşagı],"[265, 475]":[Yukarı],"[230, 440]":[Sağa,Yukarı],"[230, 405]":[Yukarı,Aşagı],"[230, 370]":[Yukarı,Aşagı],
                     "[230, 335]":[Yukarı,Aşagı,Sola],"[195, 335]":[Sağa,Yukarı],"[230, 300]":[Aşagı,Sola],"[195, 300]":[Sağa,Sola,Aşagı],"[160, 300]":[Sağa,Sola],
                     "[125, 300]":[Sağa,Sola,Aşagı],"[125, 335]":[Yukarı],"[90, 300]":[Sağa,Sola],"[55, 300]":[Sağa,Aşagı],"[55, 335]":[Aşagı,Yukarı],"[55, 370]":[Aşagı,Yukarı],
                     "[55, 405]":[Aşagı,Yukarı],"[55, 440]":[Aşagı,Yukarı],"[55, 475]":[Sağa,Yukarı],"[90, 475]":[Sağa,Sola],"[125, 475]":[Sağa,Sola],"[160, 475]":[Sola,Yukarı],
                     "[160, 440]":[Yukarı,Aşagı],"[160, 405]":[Aşagı,Sola],"[125, 405]":[Sağa],"[300, 405]":[Yukarı,Aşagı],"[300, 370]":[Sağa,Aşagı],"[335, 370]":[Sola],
                     "[510, 405]":[Yukarı,Aşagı],"[510, 370]":[Yukarı,Aşagı,Sağa],"[510, 335]":[Aşagı,Sağa],"[545, 370]":[Sola,Yukarı],"[545, 335]":[Sağa,Sola,Aşagı],
                     "[580, 335]":[Sağa,Sola],"[615, 335]":[Sağa,Sola,Yukarı],"[650, 335]":[Sola],"[405, 440]":[Yukarı,Aşagı],"[405, 405]":[Sağa,Aşagı],"[440, 405]":[Sola,Yukarı],
                     "[440, 370]":[Yukarı,Aşagı],"[440, 335]":[Sola,Yukarı,Aşagı],"[405, 335]":[Sağa,Yukarı],"[615, 300]":[Yukarı,Aşagı],"[615, 265]":[Aşagı,Sağa],
                     "[650, 265]":[Yukarı,Sola],"[650, 230]":[Yukarı,Aşagı],"[650, 195]":[Sola,Aşagı],"[615, 195]":[Sağa,Yukarı],"[615, 160]":[Sola,Yukarı,Aşagı],
                     "[615, 125]":[Aşagı,Sağa,Sola],"[650, 125]":[Sola,Yukarı],"[650, 90]":[Yukarı,Aşagı],"[650, 55]":[Aşagı],"[580, 160]":[Sağa,Sola,Yukarı],
                     "[580, 125]":[Sağa,Yukarı,Aşagı],"[580, 90]":[Yukarı,Aşagı],"[580, 55]":[Sola,Aşagı],"[545, 55]":[Sağa,Sola],"[510, 55]":[Sağa,Sola],"[475, 55]":[Sağa],
                     "[545, 160]":[Sağa,Sola],"[440, 300]":[Yukarı,Aşagı,Sola],"[440, 265]":[Aşagı,Sağa],"[475, 265]":[Yukarı,Sağa,Sola],"[475, 230]":[Aşagı],"[510, 265]":[Sağa,Sola],
                     "[545, 265]":[Yukarı,Sola],"[545, 230]":[Aşagı],"[405, 300]":[Aşagı,Sağa,Sola],"[370, 300]":[Sağa,Sola,Yukarı],"[335, 300]":[Sağa,Sola],"[300, 300]":[Yukarı,Sağa],
                     "[300, 265]":[Yukarı,Aşagı],"[370, 265]":[Yukarı,Aşagı],"[370, 230]":[Sola,Aşagı],"[335, 230]":[Sağa,Sola],"[300, 230]":[Sağa,Sola,Aşagı],"[265, 230]":[Sağa,Sola],
                     "[230, 230]":[Sağa,Sola],"[195, 230]":[Sağa,Sola],"[160, 230]":[Sağa,Yukarı],"[160, 195]":[Yukarı,Aşagı,Sola],"[125, 195]":[Sağa,Sola],"[90, 195]":[Aşagı,Sağa,Sola],
                     "[90, 230]":[Yukarı],"[55, 195]":[Sağa],"[510, 160]":[Sağa,Sola,Yukarı],"[510, 125]":[Sola,Aşagı],"[475, 125]":[Sağa,Aşagı],"[475, 160]":[Sağa,Sola,Yukarı],
                     "[440, 160]":[Sağa,Sola],"[405, 160]":[Yukarı,Sağa],"[405, 125]":[Sola,Aşagı],"[370, 125]":[Sola,Sağa,Yukarı],"[335, 125]":[Sağa,Sola],"[300, 125]":[Sağa,Aşagı],
                     "[300, 160]":[Sola,Yukarı],"[265, 160]":[Sağa,Sola],"[230, 160]":[Yukarı,Sağa],"[230, 125]":[Aşagı],"[370, 90]":[Yukarı,Aşagı],"[370, 55]":[Sola,Aşagı],
                     "[335, 55]":[Sağa,Sola],"[300, 55]":[Sola,Sağa],"[265, 55]":[Sağa,Sola],"[230, 55]":[Sola,Sağa],"[195, 55]":[Sağa,Sola],"[160, 55]":[Sağa,Aşagı],
                     "[160, 90]":[Aşagı,Yukarı],"[160, 125]":[Yukarı,Aşagı,Sola],"[160, 160]":[Aşagı,Yukarı],"[125, 125]":[Sola,Sağa],"[90, 125]":[Sola,Sağa,Yukarı],
                     "[55, 125]":[Sağa,Yukarı],"[55, 90]":[Aşagı,Yukarı,Sağa],"[90, 90]":[Yukarı,Aşagı,Sola],"[90, 55]":[Aşagı,Sola],"[55, 55]":[Sağa,Aşagı]}
    deger=0

    for i in canavarHareketi:
        if(deger==1):
            break
        if (str(dizi[0])==i):
            sayı=random.randrange(0,len(canavarHareketi[i])); deger=1
            canavarHareketi[i][sayı](0)

    for i in canavarHareketi:
        if(deger==2):
            break
        if (str(dizi[1])==i):
            sayı=random.randrange(0,len(canavarHareketi[i])); deger=2
            canavarHareketi[i][sayı](1)

    for i in canavarHareketi:
        if(deger==3):
            break
        if (str(dizi[2])==i):
            sayı=random.randrange(0,len(canavarHareketi[i])); deger=3
            canavarHareketi[i][sayı](2)

pencere.bind_all('<Key-Right>',sağa)
pencere.bind_all('<Key-Left>',sola)
pencere.bind_all('<Key-Up>',yukarı)
pencere.bind_all('<Key-Down>',aşagı)
pencere.mainloop()
