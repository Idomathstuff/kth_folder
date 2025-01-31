import string
from linkedQFile import LinkedQ


# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...

atom_list = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N',
             'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si',
             'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc',
             'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
             'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br',
             'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo',
             'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In',
             'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La',
             'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb',
             'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
             'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl',
             'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac',
             'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk',
             'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db',
             'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class Syntaxfel(Exception):
    pass


def read_formel(q: LinkedQ):
    read_mol(q)

    # if str(q.peek()) == " ":
    #     if str(q.peek()) == '\n':
    #         return
    #     else:
    #         raise Syntaxfel("new line saknas")
global open_bracket
open_bracket = 0


def read_mol(q: LinkedQ):
    global open_bracket

    read_group(q)
    if q.peek() == None:
        return
    elif (str(q.peek()) == ")") and (bool(open_bracket) == True):
        return
    else:
        read_mol(q)


def read_group(q: LinkedQ):
    global open_bracket
    if str(q.peek()) == "(":
        open_bracket += 1
        q.dequeue()
        read_mol(q)
        if str(q.peek()) == ")":
            open_bracket -= 1
            q.dequeue()
            read_num(q)
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet "+str(q))
    if q.peek() == None:
        return

    if str(q.peek()) == ")" and not open_bracket:
        raise Syntaxfel("Felaktig gruppstart vid radslutet "+str(q))
    if str(q.peek()) not in string.ascii_letters+"()":
        raise Syntaxfel("Felaktig gruppstart vid radslutet "+str(q))

    read_atom(q)
    if str(q.peek()).isdigit() and str(q.peek()) != "(":
        read_num(q)


def read_atom(q: LinkedQ):
    Char = read_LETTER(q)
    if Char not in atom_list and q.peek() == None:
        raise Syntaxfel("Okänd atom vid radslutet "+str(q))
    if Char in atom_list and q.peek() in atom_list:
        # q.dequeue()
        return
    elif str(q.peek()) not in string.ascii_letters:  # and Char in atom_list:
        return

    else:
        char = str(q.peek())
        if Char+char.lower() not in atom_list and Char not in atom_list and char in string.ascii_uppercase:
            raise Syntaxfel("Okänd atom vid radslutet "+str(q))
        char = read_letter(q)
        if Char+char not in atom_list:
            raise Syntaxfel("Okänd atom vid radslutet "+str(q))

    # raise Syntaxfel("Okänd atom vid radslutet "+str(q))


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
            return
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


if __name__ == "__main__":
    # test_str = "Na H2O Si(C3(COOH)2)4(H2O)7 Na332 C(Xx4)5 C(OH4)C C(OH4C H2O)Fe H0 H1C H02C Nacl a (Cl)2)3 ) 2"
    # for x in list(test_str.split(" ")):
    #     if x=="#":
    #         break
    #     print(x,kolla_syntax(x))

    main()
