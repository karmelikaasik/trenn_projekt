import tkinter.colorchooser
from tkinter import *
from tkinter import ttk
from alg import *
from tkinter import messagebox
from setsreps import *
import webbrowser
kastitaust = "LightPink1"
def loop():
    list = []
    def kava():
        def var_list():
            if var1.get() == 1:
                list.append("back")
            if var2.get() == 1:
                list.append("chest")
            if var3.get() == 1:
                list.append("shoulders")
            if var4.get() == 1:
                list.append("core")
            if var5.get() == 1:
                list.append("triceps")
            if var6.get() == 1:
                list.append("biceps")
            if var7.get() == 1:
                list.append("calves")
            if var8.get() == 1:
                list.append("quads")
            if var9.get() == 1:
                list.append("hamstrings")
            if var10.get() == 1:
                list.append("glutes")

            if list == []:
                tkinter.messagebox.showerror(title="Error",message = "Please choose at least one group")
            else:
                def siin_on_harj(eesmärk):
                    def tagasi():
                        ex.destroy()
                        kava()
                    ex = Toplevel(esm)
                    esm.wm_withdraw()
                    ex.title("Exercises")
                    ex.geometry("600x800")
                    koord = 10
                    lingid = []
                    harj_var=StringVar()
                    n = 1
                    def ava(var):
                        var = harj_var.get()
                        harj_var.set("")
                        link = lingid[int(var)-1]
                        webbrowser.open(link, new=1)
                    for a in (harjutused(listidelist(list))):
                        nimi = a.split(" - ")[0] +": "+ mitu(list,eesmärk)
                        link = a.split(" - ")[1]
                        lingid.append(link)
                        nr = ttk.Label(ex, text=str(n)+".", font=("Times", 20))
                        nr.place(x=20, y=koord)
                        nimesilt = ttk.Label(ex, text=nimi, font=("Times", 20))
                        nimesilt.place(x=50, y=koord)
                        """linginupp= Button(ex, text="video", font=("Times", 20), command= lambda: ava(link) )
                        linginupp.place(x=500, y =koord)"""
                        koord += 60
                        n+=1
                    valinr = ttk.Label(ex, text="Video nr:", font=("Times", 20))
                    valinr.place(x = 200, y = 610)
                    video = Entry(ex,textvariable = harj_var, font=('Times', 20))
                    video.place(x=150, y=640)
                    vaata = Button(ex, text="Watch",font=('Times', 20), padx=5, pady=5, activebackground='black', activeforeground='white',command = lambda:  ava(video))
                    vaata.place(x=380,y=630)
                    lahku = Button(ex, text="Exit",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='black', activeforeground='white',command = quit)
                    lahku.place(x=300,y=700)
                    refresh = Button(ex, text="Go back",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='black', activeforeground='white',command = tagasi)
                    refresh.place(x=100,y=700)
                    ex.mainloop()

                esm = Toplevel(uus)
                uus.wm_withdraw()
                esm.title("Select your goal")
                esm.geometry("300x500")
                jõud = Button(esm, text="Strength", font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='black', activeforeground='white', command=lambda:siin_on_harj("jõud"))
                jõud.place(x=50, y=50)
                vastupidavus = Button(esm, text="Endurance", font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='black', activeforeground='white', command=lambda:siin_on_harj("vastupidavus"))
                vastupidavus.place(x=50, y=150)
                lihasmass = Button(esm, text="Muscle mass", font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='black', activeforeground='white', command=lambda:siin_on_harj("lihasmass"))
                lihasmass.place(x=50, y=250)
                esm.mainloop()

        uus = Toplevel(win)
        win.wm_withdraw()
        uus.title("Choose")
        uus.geometry("500x700")
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        silt = ttk.Label(uus,text="Choose muscle groups to work", font=("Times",20))
        silt.place(x=50,y=30)
        back = Checkbutton(uus, text="Back",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1', activeforeground='white', variable=var1)
        back.place(x=50,y=100)
        chest = Checkbutton(uus, text="Chest",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1', activeforeground='white',variable=var2)
        chest.place(x = 250,y=100)
        shoulders = Checkbutton(uus, text="Shoulders", font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1', activeforeground='white',variable=var3)
        shoulders.place(x=50,y=200)
        core = Checkbutton(uus, text="Core",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1', activeforeground='white',variable=var4)
        core.place(x=250,y=200)
        triceps = Checkbutton(uus, text="Triceps",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1', activeforeground='white',variable=var5)
        triceps.place(x=50,y=300)
        biceps = Checkbutton(uus, text="Biceps",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1', activeforeground='white',variable=var6)
        biceps.place(x=250,y=300)
        calves = Checkbutton(uus, text="Calves",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1', activeforeground='white',variable=var7)
        calves.place(x=50,y=400)
        quads = Checkbutton(uus, text="Quads",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1', activeforeground='white',variable=var8)
        quads.place(x=250,y=400)
        hamstrings = Checkbutton(uus, text="Hamstrings",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1', activeforeground='white',variable=var9)
        hamstrings.place(x=50,y=500)
        glutes = Checkbutton(uus, text="Glutes", font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='VioletRed1',activeforeground='white',variable=var10)
        glutes.place(x=250,y=500)
        workout = Button(uus,text="Create",font=('Times', 20), padx=10, pady=10, bg="Black", foreground="White", activebackground='VioletRed1', activeforeground='white',\
                command=var_list)
        workout.place(x=150,y=600)
        uus.mainloop()

    def quit():
        win.destroy()

    #avab akna
    win = Tk()
    win.title("Avaleht")
    win.config()
    win.geometry("500x600")

    #nupud
    trenn = Button(win, text="Create a workout",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='black', activeforeground='white', command = kava)
    trenn.place(x=130, y=200)
    välju = Button(win, text="Exit",font=('Times', 20), padx=10, pady=10, bg=kastitaust, activebackground='black', activeforeground='white',command = quit)
    välju.place(x=130, y=300)


    win.mainloop()

loop()