import string
from linkedQFile import LinkedQ
from molgrafik import*

# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...
atomdata = "H  1.00794\
    He 4.002602\
    Li 6.941\
    Be 9.012182\
    B  10.811\
    C  12.0107\
    N  14.0067\
    O  15.9994\
    F  18.9984032\
    Ne 20.1797\
    Na 22.98976928\
    Mg 24.3050\
    Al 26.9815386\
    Si 28.0855\
    P  30.973762\
    S  32.065\
    Cl 35.453\
    K  39.0983\
    Ar 39.948\
    Ca 40.078\
    Sc 44.955912\
    Ti 47.867\
    V  50.9415\
    Cr 51.9961\
    Mn 54.938045\
    Fe 55.845\
    Ni 58.6934\
    Co 58.933195\
    Cu 63.546\
    Zn 65.38\
    Ga 69.723\
    Ge 72.64\
    As 74.92160\
    Se 78.96\
    Br 79.904\
    Kr 83.798\
    Rb 85.4678\
    Sr 87.62\
    Y  88.90585\
    Zr 91.224\
    Nb 92.90638\
    Mo 95.96\
    Tc 98\
    Ru 101.07\
    Rh 102.90550\
    Pd 106.42\
    Ag 107.8682\
    Cd 112.411\
    In 114.818\
    Sn 118.710\
    Sb 121.760\
    I  126.90447\
    Te 127.60\
    Xe 131.293\
    Cs 132.9054519\
    Ba 137.327\
    La 138.90547\
    Ce 140.116\
    Pr 140.90765\
    Nd 144.242\
    Pm 145\
    Sm 150.36\
    Eu 151.964\
    Gd 157.25\
    Tb 158.92535\
    Dy 162.500\
    Ho 164.93032\
    Er 167.259\
    Tm 168.93421\
    Yb 173.054\
    Lu 174.9668\
    Hf 178.49\
    Ta 180.94788\
    W  183.84\
    Re 186.207\
    Os 190.23\
    Ir 192.217\
    Pt 195.084\
    Au 196.966569\
    Hg 200.59\
    Tl 204.3833\
    Pb 207.2\
    Bi 208.98040\
    Po 209\
    At 210\
    Rn 222\
    Fr 223\
    Ra 226\
    Ac 227\
    Pa 231.03588\
    Th 232.03806\
    Np 237\
    U  238.02891\
    Am 243\
    Pu 244\
    Cm 247\
    Bk 247\
    Cf 251\
    Es 252\
    Fm 257\
    Md 258\
    No 259\
    Lr 262\
    Rf 265\
    Db 268\
    Hs 270\
    Sg 271\
    Bh 272\
    Mt 276\
    Rg 280\
    Ds 281\
    Cn 285"
atomdata = atomdata.split()
atom_dic = {atomdata[i]: atomdata[i+1] for i in range(0, len(atomdata)-1, 2)}
atom_list = list(atom_dic.keys())


class Syntaxfel(Exception):
    pass


global open_bracket
open_bracket = 0

global Big_ruta
Big_ruta = Ruta()


def read_formel(q: LinkedQ):
    tmp = read_mol(q)
    return tmp


def read_mol(q: LinkedQ):
    global open_bracket
    grup_ruta = read_group(q)
    if q.peek() == None:
        return grup_ruta
    elif (str(q.peek()) == ")") and (bool(open_bracket) == True):
        return grup_ruta
    else:
        grup_ruta.next = read_mol(q)
    return grup_ruta


def read_group(q: LinkedQ):

    global open_bracket

    rutan = Ruta()

    if str(q.peek()) == "(":
        open_bracket += 1
        q.dequeue()
        mol_ruta = read_mol(q)
        if str(q.peek()) == ")":
            open_bracket -= 1
            q.dequeue()
            num = read_num(q)
            rutan.atom = "()"
            rutan.num = int(num)
            rutan.down = mol_ruta
            return rutan
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet "+str(q))
    if q.peek() == None:
        return

    if str(q.peek()) == ")" and not open_bracket:
        raise Syntaxfel("Felaktig gruppstart vid radslutet "+str(q))
    if str(q.peek()) not in string.ascii_letters+"()":
        raise Syntaxfel("Felaktig gruppstart vid radslutet "+str(q))

    atom = read_atom(q)
    if str(q.peek()).isdigit() and str(q.peek()) != "(":
        num = read_num(q)
        rutan.atom = atom
        rutan.num = int(num)
    elif atom:
        rutan.atom = atom
    return rutan


def read_atom(q: LinkedQ):
    Char = read_LETTER(q)

    if Char not in atom_list and q.peek() == None:
        raise Syntaxfel("Okänd atom vid radslutet "+str(q))
    if Char in atom_list and q.peek() in atom_list:
        return Char
    elif str(q.peek()) not in string.ascii_letters and Char in atom_list:
        return Char

    elif str(q.peek()) in string.ascii_letters:
        char = str(q.peek())
        if Char+char.lower() not in atom_list and Char not in atom_list and char in string.ascii_uppercase:
            raise Syntaxfel("Okänd atom vid radslutet "+str(q))
        char = read_letter(q)
        if Char+char not in atom_list:
            raise Syntaxfel("Okänd atom vid radslutet "+str(q))
        return Char+char




def read_LETTER(q: LinkedQ):
    char = str(q.peek())
    if char in string.ascii_uppercase:
        q.dequeue()
        return char
    elif char in string.ascii_lowercase:
        raise Syntaxfel("Saknad stor bokstav vid radslutet "+str(q))


def read_letter(q: LinkedQ):
    char = q.peek()
    if char in string.ascii_lowercase:
        q.dequeue()
        return char
    raise Syntaxfel("Litenbokstav saknas "+str(q))


def read_num(q: LinkedQ):
    char: str = str(q.dequeue())
    if char.isdigit():
        if int(char) == 0:
            raise Syntaxfel("För litet tal vid radslutet "+str(q))
        while str(q.peek()).isdigit():
            char += q.dequeue()
        if 2 <= int(char):
            return char
    else:
        if char != str(None):
            raise Syntaxfel("Saknad siffra vid radslutet "+char+str(q))
        raise Syntaxfel("Saknad siffra vid radslutet "+str(q))
    raise Syntaxfel("För litet tal vid radslutet "+str(q))


def store_kem(kem: str) -> LinkedQ:
    q = LinkedQ()
    for x in kem:
        q.enqueue(x)
    return q


def kolla_syntax(kem: str):
    global open_bracket
    open_bracket = 0

    q = store_kem(kem)
    try:
        read_formel(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel)


def main():
    tmp_list = []
    while True:
        svar = input()
        if svar == "#":
            break
        tmp_list.append(svar)
    for x in tmp_list:
        print(kolla_syntax(x))


def weight(rutan: Ruta) -> float:
    w = 0
    atom_dic["()"] = 0
    if rutan != None:
        w += float(atom_dic[rutan.atom]) * rutan.num
        w += weight(rutan.next)
        w += weight(rutan.down) * rutan.num
    return w


if __name__ == "__main__":

    q = store_kem("Na332NaNa(O3(CO)2)4")
    q = store_kem("Si(C3(COOH)2)4(H2O)7")
    indata = input("Molekyl: ")
    q = store_kem(indata)
    mol = read_formel(q)
    mg = Molgrafik()
    print("vikt:", weight(mol))
    mg.show(mol)

