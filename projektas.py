from tkinter import *
import tkinter.font as font
langas = Tk()
langas.geometry("1400x800")

global font
sriftas1=font.Font(size=25, family= 'Helvetica')
fonas = PhotoImage(file="fonas.png")
label1 = Label(langas, image=fonas)
label1.place(x=0, y=0)
label2 = Label(langas, text="Trumpas bendrųjų biologinių žinių testukas", bg= 'DarkOliveGreen4')
label2['font']= sriftas1
label2.pack(pady=30)
frame1 = Frame(langas)
frame1.pack(pady=20)


class Klausimai:
    def __init__(self, klausimas, atsakymas, teisingas_atsakymas):
        self.klausimas = klausimas
        self.atsakymas = atsakymas
        self.teisingas_atsakymas = teisingas_atsakymas


    def isvalyti_ekrana(self, vaizdas):
        vaizdas.pack_forget()
        klausti()


    def tikrinti(self, raide, vaizdas):
        global teisingas
        if (raide == self.teisingas_atsakymas):
            label = Label(vaizdas, text="Teisingai!", fg='olive drab')
            teisingas += 1
            sriftas1 = font.Font(size=30, family='Helvetica')
            label['font'] = sriftas1
        else:
            label = Label(vaizdas, text="Neteisingai!", fg='firebrick4')
            sriftas1 = font.Font(size=30, family='Helvetica')
            label['font'] = sriftas1
        label.pack()
        vaizdas.after(1000, lambda *args: self.isvalyti_ekrana(vaizdas)) #after:kad iskart neissijungtu


    def formatuoti(self, langas):
        vaizdas = Frame(langas)
        global label
        label = Label(vaizdas, text=self.klausimas, bg= 'DarkSeaGreen')
        sriftas1 = font.Font(size=20, family='Helvetica')
        label['font'] = sriftas1
        mygtukas_a = Button(vaizdas, text=self.atsakymas[0], command=lambda *args: self.tikrinti("A", vaizdas))
        mygtukas_b = Button(vaizdas, text=self.atsakymas[1], command=lambda *args: self.tikrinti("B", vaizdas))
        mygtukas_c = Button(vaizdas, text=self.atsakymas[2], command=lambda *args: self.tikrinti("C", vaizdas))
        mygtukas_d = Button(vaizdas, text=self.atsakymas[3], command=lambda *args: self.tikrinti("D", vaizdas))
        mygtukas_e = Button(vaizdas, text=self.atsakymas[4], command=lambda *args: self.tikrinti("E", vaizdas))
        mygtukas_f = Button(vaizdas, text=self.atsakymas[5], command=lambda *args: self.tikrinti("F", vaizdas))
        mygtukas_g = Button(vaizdas, text=self.atsakymas[6], command=lambda *args: self.tikrinti("G", vaizdas))

        label.pack(side="top")
        mygtukas_a.pack(side="top", pady=10)
        mygtukas_b.pack(side="top", pady=10)
        mygtukas_c.pack(side="top", pady=10)
        mygtukas_d.pack(side="top", pady=10)
        mygtukas_e.pack(side="top", pady=10)
        mygtukas_f.pack(side="top", pady=10)
        mygtukas_g.pack(side="top", pady=10)
        return vaizdas


def klausti():
    global klausimai, langas, numeris, mygtukas, teisingas, kiek_klausimu
    if(len(klausimai) == numeris + 1):
        Label(langas, text="Atsakyta teisingai  " + str(teisingas) + " iš " + str(kiek_klausimu) +" klausimų.").pack()
        sriftas3 = font.Font(size=20, family='Helvetica')
        iseiti = Button(langas, text="Išeiti", bg="indian red", command = langas.destroy)
        iseiti['font'] = sriftas3
        iseiti.place(x=670, y=300)
        papildoma = Label(langas, text="Paaiškinimus žiūrėti meniu juostoje")
        papildoma['font'] = sriftas3
        papildoma.place(x=570, y=230)
        return
    mygtukas.pack_forget()
    numeris += 1
    klausimai[numeris].formatuoti(langas).pack()



klausimai = []
file = open("klausimai.txt", "r")
line = file.readline()
while(line != ""):
    klausimo_string = line
    atsakymas = []
    for i in range (7):
        atsakymas.append(file.readline())

    teisingas_atsakymas = file.readline()
    teisingas_atsakymas = teisingas_atsakymas[:-1]
    klausimai.append(Klausimai(klausimo_string, atsakymas, teisingas_atsakymas))
    line = file.readline()
file.close()
numeris = -1
teisingas = 0
kiek_klausimu = len(klausimai)


sriftas2=font.Font(size=40, family= 'Helvetica')
mygtukas = Button(langas, text="Pradėti",command=klausti)
mygtukas['font']= sriftas2
mygtukas.pack()

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)


def pirmas():

    uzrasas1=Label(langas, text=""
                                "\n Augalai vykdo fotosintezę:"
                                "\n naudodami saulės energiją ir iš atmosferos paimtą "
                                "\n anglies dioksidą bei vandenį, augalai pa(si)gamina "
                                "\n maisto medžiagas (angliavandenius) ir deguonį,"
                                "\n o nesant saulei - vykdo kvėpavimą ir pasigamina "
                                "\ngyvybiniams ir augimo procesams reikalingą energiją."
                                "\n" )
    sriftas4 = font.Font(size=20, family='Helvetica')
    uzrasas1['font'] = sriftas4
    uzrasas1.place(x=460, y=530)
def antras():
    uzrasas2=Label(langas, text=""
                                "\n Žydinčiame vandenyje yra nerekomenduojama maudytis"
                                "\n ir dažniausiai žydėjimą sukelia melsvabakterės, kurios "
                                "\n taip pat ir išskiria toksines medžiagas ir šie endotoksinai gali sukelti:"
                                "\n raumenų spazmus, kepenų cerozę, dusulį, vėžines ligas, kvėpavimo "
                                "\n sutrikimus, haliucinacijas, odos alergiją, bėrimus bei niežulį."
                                "\n Tačiau ne visos melsvabakterės yra toksiškos - dalis jų naudojama maisto "
                                "\n ir farmacijos pramonėje, iš jų gaminami maisto papildai.")
    sriftas4 = font.Font(size=20, family='Helvetica')
    uzrasas2['font'] = sriftas4
    uzrasas2.place(x=400, y=530)
def trecias():
    uzrasas3=Label(langas, text=""
                                "\n Lichenizuoti grybai(kerpės) - tai grybų ir "
                                "\n dumblių simbiontinė sąveika. Dumblio dalis gamina maisto medžiagas, "
                                "\n o grybo dalis apsaugo organizmą nuo išdžiūvimo ir palaiko formą."
                                "\n Grybai užima reikšmingą vietą medicinos istorijoje - antibiotikų (gautų "
                                "\n iš pelėsinio grybo) atradimas - vienas didžiausių XXa.medicinos pasiekimų."
                                "\n                                                                             "
                                "\n                                                                             ")
    sriftas4 = font.Font(size=20, family='Helvetica')
    uzrasas3['font'] = sriftas4
    uzrasas3.place(x=410, y=530)
def ketvirtas():
    uzrasas4=Label(langas, text=""
                                "\n"
                                "\n"
                                "\n Visos gyvybės pagrindas yra angliavandeniai (iš C,H,O), baltymai"
                                "\n (iš C,H,O,N,S), lipidai (iš C,H,O) bei aminorūgštys(DNR) (iš C,H,O, N, P).  "
                                "\n "
                                "\n "
                                "\n "
                                "\n")
    sriftas4 = font.Font(size=20, family='Helvetica')
    uzrasas4['font'] = sriftas4
    uzrasas4.place(x=420, y=530)
def penktas():
    uzrasas5=Label(langas, text=""
                                "\n"
                                "\n"
                                "\n Elektrinių signalų šaltinis biologiniuose objektuose yra gyvos ląstelės, "
                                "\n tad elektra teka visu kūnu. Daugiausia elektrinių impulsų kūne  sugeneruoja  "
                                "\n nervinės ląstelės. "
                                "\n"
                                "\n"
                                "\n")
    sriftas4 = font.Font(size=20, family='Helvetica')
    uzrasas5['font'] = sriftas4
    uzrasas5.place(x=420, y=530)
def sestas():
    uzrasas6=Label(langas, text=""
                                "\n"
                                "\nFluorescencija - reiškinys, kai molekulė, sugėrusi šviesos dalelę, "                 
                                "\n išspinduliuoja ilgesnės šviesos bangos dalelę. Visi gyvieji biologiniai            "
                                "\n   audiniai silpnai fluorescuoja, o cheminiai elementai gali ir stipriai                   "
                                "\n     fluorescuoti juos apšvietus tam tikro bangos ilgio šviesa.                          "
                                "\n"
                                "\n")
    sriftas4 = font.Font(size=20, family='Helvetica')
    uzrasas6['font'] = sriftas4
    uzrasas6.place(x=420, y=530)
def septintas():
    uzrasas7=Label(langas, text=""
                                "\n"
                                "\n"
                                "\n Visi augalai turi fotosintetinančių pigmentų, kuriems reikia šviesos energijos."
                                "\n Dažniausias pigmentas,kuris suteikia augalui žalią spalvą yra chlorofilas.  "
                                "\n Jis žalią šviesą atspindi ir žmogaus akis tą atspindėtą šviesos bangą užfiksuoja."
                                "\n"
                                "\n")
    sriftas4 = font.Font(size=20, family='Helvetica')
    uzrasas7['font'] = sriftas4
    uzrasas7.place(x=420, y=530)
def astuntas():
    uzrasas8=Label(langas, text=""
                                "\n"
                                "\n"
                                "\n"
                                "\n Genetinė medžiaga sudaryta iš angliavandenio, nukleorūgšties (kuri yra iš           "
                                "\n             baltymų(=peptidų)) ir fosforo liekanos.                                             "
                                "\n"
                                "\n")
    sriftas4 = font.Font(size=20, family='Helvetica')
    uzrasas8['font'] = sriftas4
    uzrasas8.place(x=420, y=530)
def devintas():
    uzrasas9=Label(langas, text=""
                                "\n"
                                "\nEsant didesniam smegenų tūriui, neuronai išsidėsto didesniais atstumais vienas "
                                "\n nuo kito, gaunasi retesnis neuronų tinklas, todėl tūriškai didesnės smegenys  "
                                "\nnereiškia, kad individas bus protingesnis :-)  pavyzdžiui dramblys ir žmogus..."
                                "\n "
                                "\n"
                                "\n")
    sriftas4 = font.Font(size=20, family='Helvetica')
    uzrasas9['font'] = sriftas4
    uzrasas9.place(x=420, y=530)


meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išeiti", command=langas.destroy)
submeniu.add_separator()

submeniu.add_command(label="Pirmas", command=pirmas)
submeniu.add_command(label="Antras", comman=antras)
submeniu.add_command(label="Trečias", command=trecias)
submeniu.add_command(label="Ketvirtas", command= ketvirtas)
submeniu.add_command(label="Penktas", command= penktas)
submeniu.add_command(label="Šeštas", command= sestas)
submeniu.add_command(label="Septintas", command= septintas)
submeniu.add_command(label="Aštuntas", command= astuntas)
submeniu.add_command(label="Devintas", command= devintas)


langas.mainloop()
