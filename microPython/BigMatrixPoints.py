"""
    Deze module bereken en organiseert de totale punten van de sjoelbak.
    Ook wordt bijgehouden in welk gat de stenen zitten.

"""
# DE VAKKEN WORDEN GETELD VAN LINKS NAAR RECHTS
_MAX_INDEX = 4 #De index van vakken
TEXT_STENEN_PER_VAK = "Stenen per vak:"
TEXT_PUNTEN_PER_VAK = "punten van vak:"
RESET_PUNTEN = [0, 0, 0, 0, 0]
RESET_STONES_IN_HOLES = [TEXT_STENEN_PER_VAK, 0, 0, 0, 0]


_holesUpdates = [] # Stenen added in these holes 
_punten_tot   = RESET_PUNTEN.copy()                # _punten_tot[0] is het totaalen punten
_puntenPerVak = (TEXT_PUNTEN_PER_VAK, 2, 3, 4, 1)  # index start bij 1, punten
_stenenPerVak = RESET_STONES_IN_HOLES.copy()       # index start bij 1, punten


""""
    Deze fuctie is om de totalen punten bij te houden en de totalen punten per vak.
    DE VAKKEN WORDEN GETELD VAN LINKS NAAR RECHTS, DUS DE 2 PUNTEN GAT IS 1 , 3 PUNTEN GAT IS 2......
    Als je deze functie aan roept word er eerst een puntenTotaal en totaal punten per vak aangeroepen. 
    Daaraan word het speelvak (ver vak de hoeveelheid stenen) door gestuurd waar index 0 niet gebruikt word. 
    Daarna word er een String verstuurd met de laste gescorde vak als 'vak1' door gestuurd
"""
def puntenTotaal(debug=False):
    if debug:
        print(f"Punten Totaal: {_punten_tot[0]} \tPunten Totaal Vak 1: {_punten_tot[1]} \tPunten Totaal Vak 2: {_punten_tot[2]} \tPunten Totaal Vak 3: {_punten_tot[3]} \tPunten Totaal Vak 4: {_punten_tot[4]}")
    return _punten_tot,_stenenPerVak,_holesUpdates


""""
    Deze fuctie resetten de punten.
"""
def reset():
    global _punten_tot, _stenenPerVak,_holesUpdates
    _punten_tot = RESET_PUNTEN.copy()
    _stenenPerVak = RESET_STONES_IN_HOLES.copy()
    _holesUpdates = []
    
"""
    Zit er in elk vak 1 steen, dan krijg je 20 punten.
"""
def _calculatescore(debug=False):
    global _punten_tot, _stenenPerVak
    totaal = sum(_punten_tot[1:])
    minValue = min(_stenenPerVak[1:])
    if debug:
        print(_stenenPerVak[1:], "in alle gaten", minValue)
    _punten_tot[0] = totaal + 10 * minValue

def _updateScore(debug=False):
    index = 1
    while index <= _MAX_INDEX:
        _punten_tot[index] = _stenenPerVak[index] * _puntenPerVak[index]
        index += 1
    _calculatescore(debug)

"""
    DE VAKKEN WORDEN GETELD VAN LINKS NAAR RECHTS.
    Dit is de add fuctie geef de punten die gescoord zijn door als bijvoorbeeld vak1= 1
"""
def add(vak1=0, vak2=0, vak3=0, vak4=0, debug=False):
    global _stenenPerVak, _punten_tot, _holesUpdates
    _stenenPerVak[1] += vak1
    _stenenPerVak[2] += vak2
    _stenenPerVak[3] += vak3
    _stenenPerVak[4] += vak4
    
    _holesUpdates = []
    if vak1 != 0:    
        _holesUpdates.append(1)
    if vak2 != 0:
        _holesUpdates.append(2)
    if vak3 != 0:
        _holesUpdates.append(3)
    if vak4 != 0:
        _holesUpdates.append(4)
        
    for x, y in enumerate(_stenenPerVak[1:]):
        if y < 0:
            _stenenPerVak[x+1] = 0
            print(">> Waarschuwing: Er kan geen negatieve steen zijn in het speel veld. Dat spelveld/vak word terug gezet naar 0")
    _updateScore(debug)
    
    if debug:
        print(_stenenPerVak)
        print(f"Punten Totaal: {_punten_tot[0]} \tPunten Totaal Vak 1: {_punten_tot[1]} \tPunten Totaal Vak 2: {_punten_tot[2]} \tPunten Totaal Vak 3: {_punten_tot[3]} \tPunten Totaal Vak 4: {_punten_tot[4]}")


if __name__ == '__main__':
    print("Start test")
    
    add(1,0,0,0)
    assert _punten_tot == [2, 2, 0, 0, 0]
    s, d, f = puntenTotaal()
    assert s == [2, 2, 0, 0, 0], "Score is 2"
    assert d == [TEXT_STENEN_PER_VAK, 1, 0, 0, 0], "Only in 1 is a stone"
    assert len(f) == 1, "One position added"
    assert f[0] == 1, "vak last eddited is 1"
    assert _stenenPerVak == [TEXT_STENEN_PER_VAK, 1, 0, 0, 0]
    add(vak1=1)
    assert _stenenPerVak == [TEXT_STENEN_PER_VAK, 2, 0, 0, 0]
    add(vak2=2)
    assert _stenenPerVak == [TEXT_STENEN_PER_VAK, 2, 2, 0, 0]
    add(vak3=2)
    assert _stenenPerVak == [TEXT_STENEN_PER_VAK, 2, 2, 2, 0]
    add(vak4=2)
    assert _punten_tot == [40, 4, 6, 8, 2]
    assert _stenenPerVak == [TEXT_STENEN_PER_VAK, 2, 2, 2, 2]
    add(vak4=-2)
    assert _stenenPerVak == [TEXT_STENEN_PER_VAK, 2, 2, 2, 0]
    add(vak4=-2)
    assert _stenenPerVak == [TEXT_STENEN_PER_VAK, 2, 2, 2, 0]
    
    s, d, f = puntenTotaal()
    assert s == [18, 4, 6, 8, 0], "Score is 2"
    assert d == [TEXT_STENEN_PER_VAK, 2, 2, 2, 0], "Only in 1 is a stone"
    assert len(f) == 1, "One stone added"
    assert f[0] == 4, "vak last eddited is 1"
    
    reset()
    s,d,f = puntenTotaal()
    print(s,d,f)
    assert s == RESET_PUNTEN, "reset so empty"
    assert d == [TEXT_STENEN_PER_VAK, 0, 0, 0, 0], "reset so empty"
    assert len(f) == 0, "everything is reset"
    
    add(vak1=2, vak4=-2)
    s,d,f = puntenTotaal()
    assert len(f) == 2, "2 fields added"
    
    print("All tests passed..")