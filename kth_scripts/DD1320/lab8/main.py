import string
from linkedQFile import LinkedQ
import sys

error_type = []


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
    char = q.peek()
    if char in string.ascii_uppercase:
        q.dequeue()
        return
    error_type.append("LETTER")
    raise SyntaxError("Saknad stor bokstav vid radslutet"+' '+str(q))


def read_letter(q: LinkedQ):
    char = q.peek()
    if char in string.ascii_lowercase:
        q.dequeue()
        return
    error_type.append("letter")
    raise SyntaxError("Litenbokstav saknas"+' '+str(q))


def read_num(q: LinkedQ):
    char: str = q.dequeue()
    if char.isdigit():
        if int(char) == 0:
            error_type.append('num')
            raise SyntaxError("För litet tal vid radslutet ")
        while str(q.peek()).isdigit():
            char += q.dequeue()
        if 2 <= int(char):
            return
    error_type.append('num')
    raise SyntaxError("För litet tal vid radslutet ")


def store_kem(kem: str) -> LinkedQ:
    q = LinkedQ()
    for x in kem:
        q.enqueue(x)
    return q

def koll(kem):
    q = store_kem(kem)
    read_molekyl(q)

def kolla_syntax(kem: str):
    q = store_kem(kem)
    try:
        read_molekyl(q)
        error_type.append(None)
    except SyntaxError:
        pass
    return q


def main():
    tmp_list = []
    q_list = []
    svar = sys.stdin.readline().split()
    for x in svar:
        if x!= "#":
            tmp_list.append(x)

    error_msg = {None: "Formeln är syntaktiskt korrekt",
                 'LETTER': "Saknad stor bokstav vid radslutet",
                 'letter': "Litenbokstav saknas",
                 'num': "För litet tal vid radslutet "}
    for x in tmp_list:
        q = kolla_syntax(str(x))
        q_list.append(q)
    

    for i in range(len(error_type)):
        if q_list[i].isEmpty():
            print(error_msg[error_type[i]])
        else:
            print(error_msg[error_type[i]],q_list[i])



if __name__ == "__main__":
    main()
