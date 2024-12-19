from moduloVeicoli import Autobus,Auto

#test per programma senza bonus: togliere gli apici alla riga successiva e quelli dopo l'invocazione di main se si e` implementatata questa versione"
"""
def main():
    print("\nTest con 2 auto e 2 autobus:")
    automobiliID=("AB123CD", "AF234EF")
    autobusInfo=(("11",("via Roma","via Poseidonia")),("21",("via Canalone","via Vinciprova")))
    strada=Strada(automobiliID,autobusInfo)
    auto1=strada.getVeicolo("AB123CD")
    auto2=strada.getVeicolo("AF234EF")
    bus1=strada.getVeicolo("11")
    bus2=strada.getVeicolo("21")
    
    auto1.sonoARiserva()
    auto2.sonoARiserva()
    bus1.arrivaAllaFermata()
    bus1.arrivaAllaFermata()
    
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    

    
if __name__=="__main__":
    main()
"""

"""
Il programma deve stampare (gli orari ovviamente sono diversi):
Test con 2 auto e 2 autobus:
L’auto AB123CD sta facendo benzina
L’auto AF234EF sta facendo benzina
L’autobus 11 sta effettuando una fermata alle ore 19:52:37
L’autobus 11 sta effettuando una fermata alle ore 19:52:37
L’autobus 21 sta effettuando una fermata alle ore 19:52:37
L’autobus 21 sta effettuando una fermata alle ore 19:52:37
"""

#test per programma con bonus: togliere gli apici alla riga successiva e quelli dopo l'invocazione di main se si e` implementatata questa versione"
"""
def main():
    print("\nTest con 2 auto e 2 autobus:")
    automobiliID=("AB123CD", "AF234EF")
    autobusInfo=(("11",("via Roma","via Poseidonia")),("21",("via Canalone","via Vinciprova")))
    strada=Strada(automobiliID,autobusInfo)
    auto1=strada.getVeicolo("AB123CD")
    auto2=strada.getVeicolo("AF234EF")
    bus1=strada.getVeicolo("11")
    bus2=strada.getVeicolo("21")
    
    auto1.sonoARiserva()
    auto2.sonoARiserva()
    bus1.arrivaAllaFermata()
    bus1.arrivaAllaFermata()
    
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    

    print("\nOra usiamo un numero diverso di veicoli")
    automobiliID=("AB123CD", "AF234EF","BG345KL")
    autobusInfo=(("11",("via Roma","via Poseidonia")),("21",("via Canalone","via Vinciprova")),("10", ("piazza delle Concordia", "via Ligea")),
                 ("1", ("piazza Malta", "Vietri sul Mare")))
    strada=Strada(automobiliID,autobusInfo)
    auto1=strada.getVeicolo("AB123CD")
    auto2=strada.getVeicolo("AF234EF")
    auto3=strada.getVeicolo("BG345KL")
    bus1=strada.getVeicolo("11")
    bus2=strada.getVeicolo("21")
    bus3=strada.getVeicolo("10")
    bus4=strada.getVeicolo("1")

    auto3.sonoARiserva()
    auto1.sonoARiserva()
    auto2.sonoARiserva()
    bus4.arrivaAllaFermata()
    bus3.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus1.arrivaAllaFermata()
    bus1.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus3.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus3.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    
if __name__=="__main__":
    main()
"""

"""
Il programma con bonus deve stampare  (gli orari ovviamente sono diversi):
Test con 2 auto e 2 autobus:
L’auto AB123CD sta facendo benzina
L’auto AF234EF sta facendo benzina
L’autobus 11 sta effettuando una fermata alle ore 19:44:58
L’autobus 11 sta effettuando una fermata alle ore 19:44:58
L’autobus 21 sta effettuando una fermata alle ore 19:44:58
L’autobus 21 sta effettuando una fermata alle ore 19:44:58

Ora usiamo un numero diverso di veicoli
L’auto BG345KL sta facendo benzina
L’auto AB123CD sta facendo benzina
L’auto AF234EF sta facendo benzina
L’autobus 1 sta effettuando una fermata alle ore 19:44:58
L’autobus 10 sta effettuando una fermata alle ore 19:44:58
L’autobus 21 sta effettuando una fermata alle ore 19:44:58
L’autobus 11 sta effettuando una fermata alle ore 19:44:58
L’autobus 11 sta effettuando una fermata alle ore 19:44:58
L’autobus 21 sta effettuando una fermata alle ore 19:44:58
L’autobus 10 sta effettuando una fermata alle ore 19:44:58
L’autobus 21 sta effettuando una fermata alle ore 19:44:58
L’autobus 21 sta effettuando una fermata alle ore 19:44:58
L’autobus 10 sta effettuando una fermata alle ore 19:44:58
L’autobus 21 sta effettuando una fermata alle ore 19:44:58
L’autobus 21 sta effettuando una fermata alle ore 19:44:58
    
"""  


#test per programma con superbonus:  togliere gli apici alla riga successiva e quelli dopo l'invocazione di main se si e` implementatata questa versione"
"""
def main():
    print("\nTest con 2 auto e 2 autobus:")
    automobiliID=("AB123CD", "AF234EF")
    autobusInfo=(("11",("via Roma","via Poseidonia")),("21",("via Canalone","via Vinciprova")))
    strada=Strada(automobiliID,autobusInfo)
    auto1=strada.getVeicolo("AB123CD")
    auto2=strada.getVeicolo("AF234EF")
    bus1=strada.getVeicolo("11")
    bus2=strada.getVeicolo("21")
    
    auto1.sonoARiserva()
    auto2.sonoARiserva()
    bus1.arrivaAllaFermata()
    bus1.arrivaAllaFermata()
    bus1.arrivaAlCapolinea()
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus2.arrivaAlCapolinea()

    print("\nOra usiamo un numero diverso di veicoli")
    automobiliID=("AB123CD", "AF234EF","BG345KL")
    autobusInfo=(("11",("via Roma","via Poseidonia")),("21",("via Canalone","via Vinciprova")),("10", ("piazza delle Concordia", "via Ligea")),
                 ("1", ("piazza Malta", "Vietri sul Mare")))
    strada=Strada(automobiliID,autobusInfo)
    auto1=strada.getVeicolo("AB123CD")
    auto2=strada.getVeicolo("AF234EF")
    auto3=strada.getVeicolo("BG345KL")
    bus1=strada.getVeicolo("11")
    bus2=strada.getVeicolo("21")
    bus3=strada.getVeicolo("10")
    bus4=strada.getVeicolo("1")

    auto3.sonoARiserva()
    auto1.sonoARiserva()
    auto2.sonoARiserva()
    bus4.arrivaAllaFermata()
    bus3.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus1.arrivaAllaFermata()
    bus1.arrivaAlCapolinea()
    bus1.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus2.arrivaAlCapolinea()
    bus2.arrivaAlCapolinea()
    bus3.arrivaAllaFermata()
    bus4.arrivaAlCapolinea()
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus3.arrivaAlCapolinea()
    bus3.arrivaAllaFermata()
    bus4.arrivaAlCapolinea()
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus3.arrivaAlCapolinea()
if __name__=="__main__":
    main()

"""

"""
Il programma con superbonus deve stampare  (gli orari ovviamente sono diversi)::
Test con 2 auto e 2 autobus:
L’auto AB123CD sta facendo benzina
L’auto AF234EF sta facendo benzina
L’autobus 11 sta effettuando una fermata alle ore 19:39:44
L’autobus 11 sta effettuando una fermata alle ore 19:39:44
L’autobus 11 è arrivato al capolinea: ora il suo tragitto e` ('via Poseidonia', 'via Roma')
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 è arrivato al capolinea: ora il suo tragitto e` ('via Vinciprova', 'via Canalone')

Ora usiamo un numero diverso di veicoli
L’auto BG345KL sta facendo benzina
L’auto AB123CD sta facendo benzina
L’auto AF234EF sta facendo benzina
L’autobus 1 sta effettuando una fermata alle ore 19:39:44
L’autobus 10 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 11 sta effettuando una fermata alle ore 19:39:44
L’autobus 11 è arrivato al capolinea: ora il suo tragitto e` ('via Poseidonia', 'via Roma')
L’autobus 11 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 è arrivato al capolinea: ora il suo tragitto e` ('via Vinciprova', 'via Canalone')
L’autobus 21 è arrivato al capolinea: ora il suo tragitto e` ('via Canalone', 'via Vinciprova')
L’autobus 10 sta effettuando una fermata alle ore 19:39:44
L’autobus 1 è arrivato al capolinea: ora il suo tragitto e` ('Vietri sul Mare', 'piazza Malta')
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 10 è arrivato al capolinea: ora il suo tragitto e` ('via Ligea', 'piazza delle Concordia')
L’autobus 10 sta effettuando una fermata alle ore 19:39:44
L’autobus 1 è arrivato al capolinea: ora il suo tragitto e` ('piazza Malta', 'Vietri sul Mare')
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 10 è arrivato al capolinea: ora il suo tragitto e` ('piazza delle Concordia', 'via Ligea')

                 
    
    
    
    
"""
