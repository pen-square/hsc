import re
import math

#Funktionen zum Ersetzen von ganzzahligen Jahreszahlen und -intervallen:
def replace_dd4(match):
    m = match.group()
    d1 = int(m[:4])
    d2 = int(m[-4:])
    mittel = str(math.ceil((d2-d1)/2+d1))
    d3 = int(mittel[:2])
    d4 = int(mittel[-2:])
    if d4 < 50:
        d5 = 1
    elif d4 > 49:
        d5 = 2
    mittel50 = str(d3+1) + ',' + str(d5)
    return mittel50

def replace_dd3(match):
    m = match.group()
    d1 = int(m[:3])
    d2 = int(m[-3:])
    mittel = str(math.ceil((d2-d1)/2+d1))
    d3 = int(mittel[0])
    d4 = int(mittel[-2:])
    if d4 < 50:
        d5 = 1
    elif d4 > 49:
        d5 = 2
    mittel50 = str(d3+1) + ',' + str(d5)
    return mittel50

def replace_d4(match):
    m = match.group()
    d1 = int(m[:2])
    d2 = int(m[-2:])
    if d2 < 50:
        d3 = 1
    elif d2 > 49:
        d3 = 2 
    d50 = str(d1+1) + ',' + str(d3)
    return d50

def replace_d3(match):
    m = match.group()
    d1 = int(m[0])
    d2 = int(m[-2:])
    if d2 < 50:
        d3 = 1
    elif d2 > 49:
        d3 = 2 
    d50 = str(d1+1) + ',' + str(d3)
    return d50

dict_lang = {
    'oberdeutsch': '10',
    'ostobd.,': '11',
    'bairisch': '11',
    'bair.': '11',
    'bair.-österr.': '11',
    'österr.': '11',
    'nordbair.': '11',
    'oberpfälz.': '11',
    'mittelbair.': '11',
    'westmittelbair.': '11',
    'ostmittelbair.': '11',
    'südbair.': '11',
    'westobd.': '12',
    'alem.': '12',
    'niederalem.': '12',
    'oberrhein.': '12',
    'elsäss.': '12',
    'hochalem.': '12',
    'südalem.': '12',
    'oberalem.': '12',
    'ostalem.': '12',
    'westalem.': '12',
    'südwestalem.': '12',
    'westl. Hochalem.': '12',
    'östl. Hochalem.': '12',
    'schwäb.': '12',
    'ostschwäb.': '12',
    'westschwäb.': '12',
    'westobd.': '12',
    'südwestdt.': '12',
    'schweiz.': '12',
    'ostschweiz.': '12',
    'ostfrk.': '13',
    'ostfränk.': '13',
    'oberfrk.': '13',
    'nürnberg.': '13',
    'westmd.': '21',
    'wmd.': '21',
    'mittelfrk.': '21',
    'mittelrhein.': '21',
    'rheinfrk.': '21',
    'rheinfränkisch': '21',
    'nordrheinfrk.': '21',
    'südrheinfrk.': '21',
    'moselfrk.': '21',
    'ripuar.': '21',
    'köln.': '21',
    'hess.': '21',
    'ostmd.': '22',
    'omd.': '22',
    'thür.': '22',
    'nordthür.': '22',
    'schles.': '22',
    'obersächs.': '22',
    'mnd.': '30',
    'westnd.': '31',
    'nordnd.': '31',
    'niedersächs.': '31',
    'nordniedersächs.': '31',
    'westfäl.': '31',
    'ostfäl.': '31',
    'elbostfäl.': '31',
    'niederrhein.': '31',
    'ostnd.': '32',
    'mndl.': '40',
    'Mndl.': '40',
    'ndl.': '40',
    'fläm.': '40',
    'westfläm.': '40',
    'ostfläm.': '40',
    'südostfläm.': '40',
    'niederfrk.': '40',
    'rhein\-maasländ.': '40',
    'brabant.': '40',
    'holl.': '40',
    'holländ.': '40',
    'südholländ.': '40',
    'westmndl.': '40',
    'frühnhd.': '51',
    'ahd.': '52',
    'altsächsisch': '53',
}

with open('hsc_mss_data_1.csv') as file:
    list = file.read().split("\n")
list.pop()
for line in list:
    lsp = line.split(';')
### Spalte "time":
    l1 = str(lsp[1])
# Klammern+Inhalt, Doppelleerzeichen, Eckklammern entfernen:
    a1 = re.sub(r'\(.*?\)', r'', l1)
    a2 = re.sub('  ', ' ', a1)
    a3 = re.sub(r'\[(.*?)\]', r'\1', a2)
# Vereinheitlichung von Jahresangaben mit Jh(d).:
    a4 = re.sub(r'1\. Viertel.? (\d+?)\. Jhd?\.?', r'\1,1', a3)
    a5 = re.sub(r'2\. Viertel.? (\d+?)\. Jhd?\.?', r'\1,1', a4)
    a6 = re.sub(r'3\. Viertel.? (\d+?)\.? Jhd?\.?', r'\1,2', a5)
    a7 = re.sub(r'4\. Viertel.? (\d+?)\. Jhd?\.?', r'\1,2', a6)
    a8 = re.sub(r'(.)\. Hälfte (\d+?)\. Jhd?\.?', r'\2,\1', a7)
    a9 = re.sub(r'(.)\. H\. (\d+?)\. Jhd?\.??', r'\2,\1', a8)
    a10 = re.sub(r'Ende \d+?\. ?/ ?Anfang (\d+?)\. Jhd?\.?', r'\1,1', a9)
    a11 = re.sub(r'Ende \d+?\. oder Anfang (\d+?)\. Jhd?\.?', r'\1,1', a10)
    a12 = re.sub(r'Ende ?(\d+?)\. Jhd?\.?', r'\1,2', a11)
    a13 = re.sub(r'Anfang (\d+?)\. Jhd?\.?', r'\1,1', a12)
    a14 = re.sub(r'Mitte (\d+?)\. Jhd?\.?', r'\1,2', a13)
    a15 = re.sub(r'1\. Drittel (\d+?)\. Jhd?\.?', r'\1,1', a14)
    a16 = re.sub(r'2\. Drittel (\d+?)\. Jhd?\.?', r'\1,2', a15)
    a17 = re.sub(r'3\. Drittel (\d+?)\. Jhd?\.?', r'\1,2', a16)
    a18 = re.sub(r'noch (\d+?)\. Jhd?\.?', r'\1,2', a17)
    a19 = re.sub(r'1\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,1', a18)
    a20 = re.sub(r'2\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,1', a19)
    a21 = re.sub(r'3\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,1', a20)
    a22 = re.sub(r'4\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,1', a21)
    a23 = re.sub(r'5\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,1', a22)
    a24 = re.sub(r'6\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,2', a23)
    a25 = re.sub(r'7\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,2', a24)
    a26 = re.sub(r'8\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,2', a25)
    a27 = re.sub(r'9\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,2', a26)
    a28 = re.sub(r'10\. Jahrzehnt (\d+?)\. Jhd?\.?', r'\1,2', a27)
    a29 = re.sub(r'(\d+?)\.? und \d+?\. Jhd?\.?', r'\1,2', a28)
    a30 = re.sub(r'(\d+?)\. ?\+ ?\d+?\. Jhd?\.?', r'\1,2', a29)
    a31 = re.sub(r'\d+?\. ?/ ?(\d+?)\.? Jhd?\.?', r'\1,2', a30)
    a32 = re.sub(r'\d+?\.? oder (\d+?)\. Jhd?\.?', r'\1,1', a31)
    a33 = re.sub(r'spätes \d+? oder frühes (\d+?)\. Jhd?\.?', r'\1,1', a32)
    a34 = re.sub(r'spätes \d+? ?/ ?frühes (\d+?)\. Jhd?\.?', r'\1,1', a33)
    a35 = re.sub(r'frühes (\d+?)\. Jhd?\.?', r'\1,1', a34)
    a36 = re.sub(r'spätes (\d+?)\. Jhd?\.?', r'\1,2', a35)
    a37 = re.sub(r'(\d+?)\. ?-\d+?\. Jhd?\.?', r'\1,2', a36)
    a38 = re.sub(r'(\d+?)\. ?Jhd?\.?', r'\1,2', a37)
    a39 = re.sub(r'\d+?\. ?/ ?(\d+?)\. Jhd?\.?', r'\1,1', a38)
# Ganzzahlige Jahreszahlen:
    a40 = re.sub(r'\d{4}-\d{4}', replace_dd4, a39)
    a41 = re.sub(r'\d{3}-\d{3}', replace_dd3, a40)
    a42 = re.sub(r'\d{4}', replace_d4, a41)
    a43 = re.sub(r'\d{3}', replace_d3, a42)
# Reduktion auf Zahl, wenn Angabe xx,x bzw. x,x vorhanden:
    a44 = re.sub(r'(?<=\d\d,\d).*', '', a43)
    a45 = re.sub(r'.*(?=\d\d,\d)', '', a44)
    a46 = re.sub(r'(?<!\d)(\d,\d).*', r'\1', a45)
    a47 = re.sub(r'.*(?<!\d)(\d,\d)', r'\1', a46)
# Merge zurück in die line:
    lsp[1] = a47

### Spalte "lang":
    l2 = str(lsp[2])
    b1 = re.sub(r' \(.*?\)', '', l2)
    b2 = re.sub(r'\[.*?\]', '', b1)
    b3 = re.sub(r'Bl. .*?: ?', '', b2)
    b4 = re.sub(r'I*?: ', '', b3)
    b5 = re.sub(r'V*?: ', '', b4)
    b6 = re.sub(r'X*?: ', '', b5)
    b7 = re.sub(r'"', '', b6)
    b8 = re.sub(r'\d', '', b7)
    b9 = re.sub('  ', ' ', b8)
    b10 = re.sub(r'\(|\)', '', b9)
    b11 = re.sub('\w+.?', lambda m: dict_lang.get(m.group(), m.group()), b10)
    b12 = re.sub('-', ' ', b11)
    b13 = re.sub('obd.', '10', b12)
    b14 = re.sub('md.', '20', b13)
    b15 = re.sub('nd.', '30', b14)  
    b16 = re.findall(r'\d\d', b15)
    if b16:
        b17 = set(b16)
        if len(b17) == 1:
            b18 = ''.join(b17)
        else:
            b17_first = [x[0] for x in b17]
            if b17_first.count(b17_first[0]) == len(b17_first):
                b17_last = [x[1] for x in b17]
                if b17_last.count(str(0)) == 0:
                    b18 = str(b17_first[0]) + '0'
                else:
                    b17.remove(str(b17_first[0]) + '0')
                    if len(b17) == 1:
                        b18 = ''.join(b17)
                    else: 
                        b18 = str(b17_first[0]) + '0'
            else:
                b18 = 'ambig'
    else:
        b18 = b15
# Merge zurück in die line:    
    lsp[2] = b18

### Spalte "place":
    l3 = str(lsp[3])
    c1 = re.sub(r' \(.*?\)', '', l3)
    c2 = re.sub(r' ?\?', '', c1)
    c3 = re.sub(r'\[.*?\]', '', c2)
    with open('ent.txt') as file_ent:
        list_ent = file_ent.read().split("\n")
    c_ent = []
    for n in list_ent:
        if n in c3:
            c_ent.append(n)
    if c_ent:
        c3 = ' '.join(c_ent)
    else:
        c3 = c2
# Merge zurück in die line:    
    lsp[3] = c3

    ljo = ';'.join(lsp)
    with open('hsc_mss_data_strip.csv', 'a') as file2:
        file2.write(ljo + '\n')
    print(str(list.index(line)+1) + "/" + str(len(list)))
print('Done!')