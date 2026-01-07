print("QUEL PERSONNAGE DE SHERLOCK ETES-VOUS ?")
sh=0
jw=0
jm=0
mh=0
mr=0
my=0
eh=0
def q1():
    global sh,jw,jm,mh,mr,my,eh
    print("Quelle est votre couleur préférée ?")
    ans_1 = input("A) Question puérile, je n'ai pas de couleur préférée. \nB) Noir\nC) Bleu\nD) Rouge\nE) Rose\nF) Jaune\nG) Vert\nVotre choix ? ")
    if ans_1 == "A":
        sh = sh + 5
        my = my + 8
        eh = eh + 4
        q2()
    elif ans_1 == "B":
        sh = sh + 3
        jm = jm + 6
        my = my + 1
        eh = eh + 4
        q2()
    elif ans_1 == "C":
        sh = sh + 2
        jw = jw + 5
        mh = mh + 1
        mr = mr + 1
        my = my + 1
        eh = eh + 1
        q2()
    elif ans_1 == "D":
        jm = jm + 4
        eh = eh + 1
        q2()
    elif ans_1 == "E":
        mh = mh + 6
        mr = mr + 7
        q2()
    elif ans_1 == "F":
        jw = jw + 3
        mh = mh + 2
        q2()
    elif ans_1 == "G":
        jw = jw + 2
        mh = mh + 1
        mr = mr + 2
        q2()
    else:
        print("Vous devez choisir une lettre.")
        q1()

def q2():
    global sh,jw,jm,mh,mr,my,eh
    print("Quelle est votre boisson préférée ?")
    ans_1 = input("A) Thé \nB) Café\nC) Soda\nD) Eau\nE) Lait\nVotre choix ? ")
    if ans_1 == "A":
        sh = sh + 9
        jw = jw + 7
        jm = jm + 6
        mh = mh + 2
        mr = mr + 6
        my = my + 8
        eh = eh + 4
        q3()
    elif ans_1 == "B":
        sh = sh + 3
        mh = mh + 3
        mr = mr + 4
        eh = eh + 2
        q3()
    elif ans_1 == "C":
        jm = jm + 3
        eh = eh + 1
        q3()
    elif ans_1 == "D":
        sh = sh + 1
        jw = jw + 1
        mh = mh + 3
        my = my + 2
        eh = eh + 1
        q3()
    elif ans_1 == "E":
        jw = jw + 1
        jm = jm + 1
        mh = mh + 2
        eh = eh + 1
        q3()
    else:
        print("Vous devez choisir une lettre.")
        q2()

def q3():
    global sh,jw,jm,mh,mr,my,eh
    print("Votre passe-temps favori :")
    ans_1 = input("A) Dessiner/peindre \nB) Lire/écrire\nC) Jouer/écouter de la musique\nD) Cuisiner\nE) Se promener\nVotre choix ? ")
    if ans_1 == "A":
        jm = jm + 1
        eh = eh + 5
        q4()
    elif ans_1 == "B":
        sh = sh + 1
        jw = jw + 6
        jm = jm + 1
        mh = mh + 5
        mr = mr + 1
        my = my + 5
        q4()
    elif ans_1 == "C":
        sh = sh + 6
        jm = jm + 6
        mh = mh + 3
        mr = mr + 2
        eh = eh + 5
        q4()
    elif ans_1 == "D":
        jw = jw + 1
        mh = mh + 2
        mr = mr + 6
        my = my + 5
        q4()
    elif ans_1 == "E":
        sh = sh + 3
        jw = jw + 3
        jm = jm + 2
        mr = mr + 1
        q4()
    else:
        print("Vous devez choisir une lettre.")
        q3()

def q4():
    global sh,jw,jm,mh,mr,my,eh
    print("Combien d'amis avez-vous ?")
    ans_1 = input("A) Je n'ai pas d'amis. C'est inutile. \nB) Un seul\nC) Entre 2 et 5 amis très proches\nD) Plein !\nVotre choix ? ")
    if ans_1 == "A":
        sh = sh + 4
        jm = jm + 7
        my = my + 9
        eh = eh + 8
        q5()
    elif ans_1 == "B":
        sh = sh + 6
        jw = jw + 2
        jm = jm + 1
        mh = mh + 1
        q5()
    elif ans_1 == "C":
        jw = jw + 6
        jm = jm + 2
        mh = mh + 8
        mr = mr + 4
        my = my + 1
        eh = eh + 2
        q5()
    elif ans_1 == "D":
        jw = jw + 2
        mh = mh + 1
        mr = mr + 6
        q5()
    else:
        print("Vous devez choisir une lettre.")
        q4()

def q5():
    global sh,jw,jm,mh,mr,my,eh
    print("Quelle est/était votre matière préférée à l'école ? ")
    ans_1 = input("A) J'aimais pas l'école \nB) Maths\nC) Anglais\nD) Sciences\nE) Art/musique/sport\nF) Histoire-géographie\nVotre choix ? ")
    if ans_1 == "A":
        sh = sh + 6
        jm = jm + 6
        mr = mr + 1
        my = my + 1
        eh = eh + 6
        q6()
    elif ans_1 == "B":
        sh = sh + 1
        jw = jw + 3
        jm = jm + 1
        mh = mh + 2
        mr = mr + 1
        my = my + 1
        eh = eh + 1
        q6()
    elif ans_1 == "C":
        jw = jw + 4
        mh = mh + 1
        mr = mr + 5
        my = my + 1
        q6()
    elif ans_1 == "D":
        sh = sh + 3
        jw = jw + 1
        jm = jm + 2
        mh = mh + 6
        my = my + 1
        eh = eh + 1
        q6()
    elif ans_1 == "E":
        jw = jw + 2
        jm = jm + 1
        mr = mr + 2
        eh = eh + 2
        q6()
    elif ans_1 == "F":
        mh = mh + 1
        mr = mr + 1
        my = my + 6
        q6()
    else:
        print("Vous devez choisir une lettre.")
        q5()

def q6():
    global sh,jw,jm,mh,mr,my,eh
    print("Si vous étiez un animal, lequel seriez-vous ?")
    ans_1 = input("A) Chat \nB) Chien\nC) Pie/corbeau\nD) Renard\nE) Hibou\nVotre choix ? ")
    if ans_1 == "A":
        sh = sh + 5
        jm = jm + 5
        mh = mh + 1
        mr = mr + 2
        my = my + 2
        eh = eh + 4
        q7()
    elif ans_1 == "B":
        jw = jw + 6
        mh = mh + 7
        mr = mr + 4
        q7()
    elif ans_1 == "C":
        sh = sh + 3
        jm = jm + 5
        mh = mh + 1
        mr = mr + 2
        my = my + 1
        eh = eh + 4
        q7()
    elif ans_1 == "D":
        sh = sh + 1
        jw = jw + 2
        mh = mh + 1
        mr = mr + 1
        eh = eh + 2
        q7()
    elif ans_1 == "E":
        sh = sh + 1
        jw = jw + 2
        mr = mr + 1
        my = my + 7
        q7()
    else:
        print("Vous devez choisir une lettre.")
        q6()

def q7():
    global sh,jw,jm,mh,mr,my,eh
    print("Quel adjectif vous décrit le mieux ?")
    ans_1 = input("A) Gentil \nB) Timide\nC) Créatif\nD) Intelligent\nE) Solitaire\nVotre choix ? ")
    if ans_1 == "A":
        jw = jw + 6
        mh = mh + 6
        mr = mr + 7
    elif ans_1 == "B":
        mh = mh + 3
        jw = jw + 1
    elif ans_1 == "C":
        sh = sh + 1
        jw = jw + 2
        jm = jm + 2
        mh = mh + 1
        mr = mr + 3
        eh = eh + 1
    elif ans_1 == "D":
        sh = sh + 7
        jw = jw + 2
        jm = jm + 6
        mh = mh + 1
        mr = mr + 1
        my = my + 8
        eh = eh + 7
    elif ans_1 == "E":
        sh = sh + 3
        jm = jm + 3
        my = my + 3
        eh = eh + 3
    else:
        print("Vous devez choisir une lettre.")
        q7()

q1()
variables = {"Sherlock Holmes":sh,"John Watson":jw,"Jim Moriarty":jm,"Eurus Holmes":eh,"Molly Hooper":mh,"Mycroft Holmes":my,"Mrs Hudson":mr}
result=max(variables, key=variables.get)
print(result)
tries = sorted(variables.items(), key=lambda item: item[1], reverse=True)
for nom, valeur in tries:
    print(f"{nom}: {valeur}")