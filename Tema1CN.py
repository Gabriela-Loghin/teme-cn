import numpy as np
import random


# Exercitiul 1:
def precizie_masina_liniara():
    a = 1.0
    b = 1.0

    while True:
        if a + b == a:
            break
        b = b / 10

    return b * 10


def precizie_masina_binara():
    a = 1.0
    b = 1.0
    while True:
        if a + b == a:
            break
        b = b / 2

    return b * 2


# Exercitiul 2 :
def asociatvitate_adunare():
    a = 1.0
    b = precizie_masina_liniara() / 10
    c = precizie_masina_liniara() / 10
    suma1 = a + (b + c)
    suma2 = (a + b) + c
    #  if( suma1 != suma2) : print("Adunarea efectuata de calculator nu este asociativa!")
    return suma1, suma2, suma1 == suma2


def asociativitate_inmultire(incercari):
    for i in range(incercari):
        a = np.random.random(1)
        b = np.random.random(1)
        c = np.random.random(1)
        m1 = (a[0] * b[0]) * c[0]
        m2 = a[0] * (b[0] * c[0])
        if m1 != m2:
            return m1, m2, m1 == m2, i, a[0], b[0], c[0]


def polynom_calculus(a0, a1, a2, a3, a4, b0, b1, b2, b3, b4, y):
    # p4(y) = a0 + y*a1 + y^2*a2 + y^3*a3 + y^4*a4
    p = a0 + y * a1 + y ** 2 * a2 + y ** 3 * a3 + y ** 4 * a4
    q = b0 + y * b1 + y ** 2 * b2 + y ** 3 * b3 + y ** 4 * b4
    return p, q


def all_polynom(x, choose):
    # sinus
    a_sin = [1805490264.690988571178600370234394843221, -164384678.227499837726129612587952660511,
             3664210.647581261810227924465160827365, -28904.140246461781357223741935980097,
             76.568981088717405810132543523682]
    b_sin = [2298821602.638922662086487520330827251172, 27037050.118894436776624866648235591988,
             155791.388546947693206469423979505671,
             540.567501261284024767779280700089, 1.0]

    p_sin, q_sin = polynom_calculus(a_sin[0], a_sin[1], a_sin[2], a_sin[3], a_sin[4], b_sin[0], b_sin[1], b_sin[2],
                                    b_sin[3], b_sin[4], x**2)
    if q_sin < 1e-12 :
        q_sin = 1e-12
    # TODO:verificare q
    # cosinus
    a_cos = [1090157078.174871420428849017262549038606, -321324810.993150712401352959397648541681,
             12787876.84952387894405188532559387817, -150026.206045948110568310887166405972,
             538.333564203182661664319151379451]
    b_cos = [1090157078.174871420428867295670039506886, 14907035.776643879767410969509628406502,
             101855.811943661368302608146695082218, 429.772865107391823245671264489311, 1.0]
    p_cos, q_cos = polynom_calculus(a_cos[0], a_cos[1], a_cos[2], a_cos[3], a_cos[4], b_cos[0], b_cos[1], b_cos[2],
                                    b_cos[3], b_cos[4], x**2)
    if q_cos < 1e-12 :
        q_cos = 1e-12
    # ln
    a_ln = [75.151856149910794642732375452928, -134.730399688659339844586721162914, 74.201101420634257326499008275515,
            -12.777143401490740103758406454323, 0.332579601824389206151063529971]
    b_ln = [37.575928074955397321366156007781, -79.890509202648135695909995521310, 56.215534829542094277143417404711,
            -14.516971195056682948719125661717, 1.0]

    p_ln, q_ln = polynom_calculus(a_ln[0], a_ln[1], a_ln[2], a_ln[3], a_ln[4], b_ln[0], b_ln[1], b_ln[2],
                                  b_ln[3], b_ln[4], x**2)
    if q_ln < 1e-12 :
        q_ln = 1e-12

    if choose == "sin":
        calcul = x*p_sin/q_sin
        print("x*p(x^2)/q(x^2) = ", calcul)
        return calcul
    elif choose == "cos":
        calcul = p_cos/q_cos
        print("p(x^2)/q(x^2) = ", calcul)
        return calcul
    else:
        calcul = x*p_ln/q_ln
        print("z*p(z^2)/q(z^2) = ", calcul)
        return calcul


def x_calculus():
    x_sin = random.uniform(-1.0, 1.0)
    x_cos = random.uniform(-1.0, 1.0)
    x_ln = random.uniform(1 / np.sqrt(2), np.sqrt(2))
    z_ln = (x_ln - 1) / (x_ln + 1)

    calcul_sin_x = ((1 / 4) * np.pi * x_sin)
    print("sin(1/4pix) = sin(", calcul_sin_x, ") = ", end="")
    rez_sin = all_polynom(x_sin, "sin")
    sin_matematic = np.sin(x_sin*np.pi*1/4)
    print("sin formula matematica: ", sin_matematic)
    print("Modulul diferentei: ", np.abs(sin_matematic - rez_sin))
    print("")

    calcul_cos_x = ((1 / 4) * np.pi * x_cos)
    print("cos(1/4pix) = cos(", calcul_cos_x, ") = ", end="")
    rez_cos = all_polynom(x_cos, "cos")
    cos_matematic = np.cos(x_cos * np.pi * 1 / 4)
    print("cos formula matematica: ", cos_matematic)
    print("Modulul diferentei: ", np.abs(cos_matematic - rez_cos))
    print("")

    print("ln(x) = ln(", x_ln, ") = ", end="")
    rez_ln = all_polynom(z_ln, "ln")
    ln_matematic = np.log(x_ln)  # ln is exponential -> it would be np.log(np.exp(x_ln)), but the result is wrong
    print("ln formula matematica: ", ln_matematic)
    print("Modulul diferentei: ", np.abs(ln_matematic - rez_ln))
    print("")

#BONUS :
pi=np.math.pi
def x_calculus_sin(x):
    y= x*4/pi

    rez_sin = all_polynom(y, "sin")
    return rez_sin

def x_calculus_cos(x):
    y=x*4/pi

    rez_cos = all_polynom(y, "cos")
    return rez_cos

def reducere_x_sin(x):
    pi = np.math.pi
    if x>=0 and x<pi/4:
        sin_x = x_calculus_sin(x)
        sin_matematic = np.sin(x)
        dif = sin_x-sin_matematic
        print("Aproximarea folosind formule de reducere:",sin_x)
        print("Rezultatul matematic:",sin_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif))

    if x>=pi/4 and x<pi/2:
        sin_x = x_calculus_cos(pi/2-x)
        sin_matematic = np.sin(x)
        dif = sin_x - sin_matematic
        print("Aproximarea folosind formule de reducere:", sin_x)
        print("Rezultatul matematic:", sin_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif))

    if x>=pi/2 and x<pi:
        sin_x = x_calculus_cos(x-pi/2)
        sin_matematic = np.sin(x)
        dif = sin_x - sin_matematic
        print("Aproximarea folosind formule de reducere:", sin_x)
        print("Rezultatul matematic:", sin_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif) )

    if x>=pi and x<2*pi :
        sin_x = -x_calculus_sin(x-pi)
        sin_matematic = np.sin(x)
        dif = sin_x - sin_matematic
        print("Aproximarea folosind formule de reducere:", sin_x)
        print("Rezultatul matematic:", sin_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif))

    if x >= 2*pi :
        sin_matematic = np.sin(x)

        while (x >= 2 * pi):
            x = x % (2 * pi)

        sin_x = x_calculus_sin(x)

        dif = sin_x - sin_matematic
        print("Aproximarea folosind formule de reducere:", sin_x)
        print("Rezultatul matematic:", sin_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif))


def reducere_x_cos(x):
    pi = np.math.pi

    if x >= 0 and x < pi / 4:
        cos_x = x_calculus_cos(x)
        cos_matematic = np.cos(x)
        dif = cos_x - cos_matematic
        print("Aproximarea folosind formule de reducere:", cos_x)
        print("Rezultatul matematic:", cos_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif))

    if x >= pi / 4 and x < pi / 2:
        cos_x = x_calculus_sin(pi / 2 - x)
        cos_matematic = np.cos(x)
        dif = cos_x - cos_matematic
        print("Aproximarea folosind formule de reducere:", cos_x)
        print("Rezultatul matematic:", cos_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif))

    if x >= pi / 2 and x < pi:
        cos_x = x_calculus_sin(x + pi / 2)
        cos_matematic = np.cos(x)
        dif = cos_x - cos_matematic
        print("Aproximarea folosind formule de reducere:", cos_x)
        print("Rezultatul matematic:", cos_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif))

    if x >= pi and x < 2 * pi:
        cos_x = -x_calculus_cos(x + pi)
        cos_matematic = np.cos(x)
        dif = cos_x - cos_matematic
        print("Aproximarea folosind formule de reducere:", cos_x)
        print("Rezultatul matematic:", cos_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif))

    if x >= 2 * pi:
        cos_matematic = np.cos(x)

        while( x>=2*pi):
            x=x%(2*pi)
        cos_x = x_calculus_cos(x)

        dif = cos_x - cos_matematic
        print("Aproximarea folosind formule de reducere:", cos_x)
        print("Rezultatul matematic:", cos_matematic)
        print("Eroarea dintre cele doua valori este :", np.abs(dif))


if __name__ == '__main__':
    pi=np.math.pi
    print("Rezolvare exercitiul 1 : precizia masina de tip liniar ne da urmatorul rezultat =>",
          precizie_masina_liniara())
    print("")
    print("Rezolvare exercitiul 1 : precizia masina de tip binar ne da urmatorul rezultat =>", precizie_masina_binara())
    print("")
    print("Rezolvare exercitiul 2 (asoc. adunarii): ", asociatvitate_adunare())
    print("")
    print("Rezolvare exercitiul 2 (asoc. inmultirii): ", asociativitate_inmultire(100))
    print("")
    print("Rez ex 3: ")
    x_calculus()
    print("")
    #BONUS:
    print("Bonus: Calcul sin:")
    print(reducere_x_sin(5*pi))
    print("")
    print("Bonus: Calcul cos:")
    print(reducere_x_cos(5*pi))
