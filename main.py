
cunostinte_animale = {
    "URS": "Ursul hiberneaza iarna, Specii existente: Ursul brun, ursul grizzly, ursulpolar, ursul negru american, ursul negru asiatic, panda uriaČ, ursul cu ochelari, ursul malaezian Či ursul leneČ",
    "DELFIN": "InteligenČÄ remarcabilÄ: Delfinii sunt consideraČi printre cele mai inteligente animale marine. Ei comunicÄ prin sunete complexe Či pot fi instruiČi sÄ execute sarcini complicate",
    "PINGIUN": "InteligenČÄ remarcabilÄ: Delfinii sunt consideraČi printre cele mai inteligente animale marine. Ei comunicÄ prin sunete complexe Či pot fi instruiČi sÄ execute sarcini complicate",
    "FURNICA ":"ForČÄ incredibilÄ: O furnicÄ poate transporta obiecte de 10â50 ori mai grele decĂ˘t corpul ei"
}

def afiseaza_ora():
    """afsieaza ora curenta a sistemului """
    acum = datetime.datetime.now()
    ora_formatata = acum.strftime ("%H:%M:%S")
    PRINT (f"\n Ora exacta este : {ora_formatata} ")

def afiseaza_data ():
   acum = datetime.datetime.now()
   data_formatata = acum.strftime("%d %B %Y")
   print (f"\n Ora exacta este : {data_formatata} ")

def invata_animale (nume_utlizator):
    """permite utilizatorului sa invete despre animale """
    print ("\n------Sectiunea curiozitati despre animale-------")
    print ("Alege dintre aceste animale : URS, DELFIN, PINGUIN, FURNICA")
    cuvant_cheie = input (f"Despre ce animal ai vrea sa inveti, {nume_utilizator}?").strip().upper()

    
    
    if cuvant_cheie in cunostinte_animale:
        informatie = cunostinte_animale [cuvant_cheie]
        print (f"\n----Descopera:----")
        print (f"Stiai ca? {informatie}")
        print (f"sper ca ai invatat ceva nou, {nume_utlizator}!!")
    else :
        print (f"nu am scris despre acest animal '{cuvant_cheie}', altul din lista aia de noobi!!")
        

def cuvinte_amestecate():
    """Contine logica jocului de ghicit trei cuvinte amestecate cu mesaj adaptat scorului."""
    cuvinte_corecte = [ "COD","PHYTON", "CALCULATOR", "NULLS", "CLASHROYALE"]
    cuvinte_amestecate = ["ODC", "TONHYP", "LTORACLCU", "LLSNU", "SHCLAALYROE"]
    
    scor =0
    numar_cuvinte = len(cuvinte_corecte)
    
    print ("\n------Sectiune de joc------")
     
    for i in range(numar_cuvinte):
        print (f"\n{i+1}.Ghiceste cuvantul amestecat: {cuvinte_amestecate[i]}")
        
        raspuns = input("Raspunsul tau : ").strip().upper()

        if raspuns == cuvinte_corecte [i]:
            print (f"Corect ai ghicit esti main acum sterege nulls , cuvantul corect era {cuvinte_corecte[i]}")
            scor +=1;
        else:
            print (f"Gresit!, Cuvantul era': {cuvinte_corecte[i]}")


        if scor == numar_cuvinte:
           print ("felicitari ai ghicit toate cuvintele")
        elif scor>0:
           print ("Bravo leai ghicit pe cateva, esti main vorba unui !")
        else:
           print ("Nu ai ghicit niciun cuvant mai incearca")
     
           print (f"Ai ghicit {scor} din {numar_cuvinte} cuvinte")


print ("Buna! Sunt asistentul tau virtual, dluAi!")
nume_utilizator = input ("Pentru a incepe , te rof sa-mi spui cum te numesti:  ").capitalize()
print (f"Bine ai venit, {nume_utilizator}! Ma bucur sa te ajut ce optiune ti a starnit curioziatea?")

while True:
   print ("Alege o optiune:")
   print ("Scrie 'ORA' pentru a afla cat este ceasul.")
   print ("Scrie 'DATA' pentru a afla cat este data.")
   print ("Scrie 'JOC' pentru a te juca jocul cuvinte amesteacate.")
   print ("Scrie 'INVATA' pentru a afla despre animale.")
   print ("Scrie 'IESIRE' pentru a incheia conversatia cu dluAi.")

   alegere = input ("Alegerea ta:  "  ).strip().upper()
   
   if alegere == 'ORA':
      afiseaza_ora()

   elif alegere == "DATA":
      afiseaza_data()

   elif alegere == "JOC":
       cuvinte_amestecate()

   elif alegere == "INVATA":
       invata_animale(nume_utilizator)
  
   elif alegere == "IESIRE":
     break
   
   else:
      print (f"\n NU AM INTELES COMANDA '{alegere}'. Incearca din nou din lista de optiuni.")
    

print (f"\n Iti multumesc pentru ca ai pierdut din timp cu mine !{nume_utilizator}! La revedere!")
