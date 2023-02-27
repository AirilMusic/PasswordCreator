c1 = ("ni", "hi", "hura", "gu", "zu", "zuek", "haiek") #columna 1
c2 = ("niri", "hiri", "hari", "guri", "zuri", "zuei", "haiei") #columna 2

no = ("nadin", "hadin", "dadin", "gaitezen", "zaitezen", "zaitezten", "daitezen")
ni = ("nendin", "hendin", "zedin", "gintezen", "zintezen", "zintezten", "zitezen")

nno = (("", "nakian/nakinan", "nakion", "", "nakizun", "nakizuen", "nakien"),
       ("hakidan", "", "hakion", "hakigun", "", "", "hakien"),
       ("dakidan", "dakian/dakinan", "dakion", "dakigun", "dakizun", "dakizuen", "dakien"),
       ("", "gakizkian/gakizkinan", "gakizkion", "", "gakizkizun", "gakizkizuen", "gakizkien"),
       ("zakizkidan", "", "zakizkion", "zakizkigun", "", "", "zakizkien"),
       ("zakizkidaten", "", "zakizkioten", "zakizkiguten", "", "", "zakizkieten"),
       ("dakizkidan", "dakizkian/dakizkinan", "dakizkion", "dakizkigun", "dakizkizun", "dakizkizuen", "dakizkien"))
nni = (("", "nenkian/nenkinan", "nenkion", "", "nenkizun", "nenkizuen", "nenkien"),
       ("henkidan", "", "henkion", "henkigun", "", "", "henkien"),
       ("zekidan", "zekian/zekinan", "zekion", "zekigun", "zekizun", "zekizuen", "zekien"),
       ("", "genkizkian/genkizkinan", "genkizkion", "", "genkizkizun", "genkizkizuen", "genkizkien"),
       ("zenkizkidan", "", "zenkizkion", "zenkizkigun", "", "", "zenkizkien"),
       ("zenkizkidaten", "", "zenkizkioten", "zenkizkiguten", "", "", "zenkizkieten"),
       ("zekizkidan", "zekizkian/zekizkinan", "zekizkion", "zekizkigun", "zekizkizun", "zekizkizuen", "zekizkien"))

nnko = ((),
        (),
        (),
        (),
        (),
        (),
        ())
nnki = ((),
        (),
        (),
        (),
        (),
        (),
        ())

nnno = ((),
        (),
        (),
        (),
        (),
        (),
        ())
nnni = ((),
        (),
        (),
        (),
        (),
        (),
        ())

while True:
    denbora = input("Denbora (Orainaldia/O, Iragana/I): ").lower()
    mota = input("Mota (Nor/N, Nor Nori/NN, Nor Nork/NNK, Nor Nori Nork/NNN): ").lower()
    
    if mota == "nor" or mota == "n":
        if denbora == "orainaldia" or denbora == "o":
            pertsona = input("Pertsona: ").lower()
            if pertsona in c1:
                print(no[c1.index(pertsona)])
        
        elif denbora == "iragana" or denbora == "i":
            pertsona = input("Pertsona: ").lower()
            if pertsona in c1:
                print(ni[c1.index(pertsona)])
    
    elif mota == "nor nori" or mota == "nn":
        if denbora == "orainaldia" or denbora == "o":
            pass
        
        elif denbora == "iragana" or denbora == "i":
            pass
    
    elif mota == "nor nork" or mota == "nnk":
        if denbora == "orainaldia" or denbora == "o":
            pass
        
        elif denbora == "iragana" or denbora == "i":
            pass
    
    elif mota == "nor nori nork" or mota == "nnn":
        if denbora == "orainaldia" or denbora == "o":
            pass
        
        elif denbora == "iragana" or denbora == "i":
            pass
    
    t = input("[+] Press Enter to continue")
    for i in range(30):
        print("\n")
