import string
from linkedQFile import LinkedQ

    #   <molekyl> ::= <atom> | <atom><num>
    #   <atom>  ::= <LETTER> | <LETTER><letter>
    #   <LETTER>::= A | B | C | ... | Z
    #   <letter>::= a | b | c | ... | z
    #   <num>   ::= 2 | 3 | 4 | ...

class Syntaxfel(Exception):
    pass

def read_molekyl(q: LinkedQ):
    read_atom(q)
    if q.peek() == None:
        return
    else:
        read_num(q)

def read_atom(q: LinkedQ):
    read_LETTER(q)
    if q.peek() == None or q.peek().isdigit():
        return
    else:
        read_letter(q)

def read_LETTER(q: LinkedQ):
    char = str(q.peek())
    if char in string.ascii_uppercase:
        q.dequeue()
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet"+' '+str(q))


def read_letter(q: LinkedQ):
    char = q.peek()
    if char in string.ascii_lowercase:
        q.dequeue()
        return
    raise Syntaxfel("Litenbokstav saknas"+' '+str(q))


def read_num(q: LinkedQ):
    char: str = q.dequeue()
    if char.isdigit():
        if int(char) == 0:
            raise Syntaxfel("För litet tal vid radslutet ")
        while str(q.peek()).isdigit():
            char += q.dequeue()
        if 2 <= int(char):
            return
    else:
        raise Syntaxfel("Radslutet borde vara ett tal")
    raise Syntaxfel("För litet tal vid radslutet ")

def store_kem(kem: str) -> LinkedQ:
    q = LinkedQ()
    for x in kem:
        q.enqueue(x)
    return q

def kolla_syntax(kem: str):
    q = store_kem(kem)
    try:
        read_molekyl(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel)

if __name__ == "__main__":
    print(kolla_syntax("Na132"))
    print(kolla_syntax("AA"))
