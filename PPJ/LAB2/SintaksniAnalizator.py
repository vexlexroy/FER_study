import sys

f = sys.stdin
intx = list()

# Set up input and current/next tokens
for x in f:
    intx.append(x.replace("\n", ""))
intx.append('@')

# Initialize the current and next tokens
current = intx.pop(0)
next_token = intx[0] if intx else None

# Initialize the tree structure
parse_tree = {"program": []}


def match(expected_token):
    global current, next_token
    if current and expected_token in current:
        current = intx.pop(0) if intx else None
        next_token = intx[0] if intx else None
    else:
        print(f"SyntaxError: Expected {expected_token}, but got {current}")
        sys.exit()





def Program():
    Lista_naredbi()


def Lista_naredbi():
    Naredba()
    Lista_naredbi_prime()


def Lista_naredbi_prime():
    if current and ('IDN' in current or 'KR_ZA' in current):
        Lista_naredbi()


def Naredba():
    if current and 'IDN' in current:
        Naredba_pridruzivanja()
    elif current and 'KR_ZA' in current:
        Za_petlja()
    else:
        print(f"SyntaxError: Unexpected token: {current}")
        sys.exit()


def Naredba_pridruzivanja():
    if current and 'IDN' in current:
        match('IDN')
    else:
        print(f"SyntaxError: Expected IDN, but got {current}")
        sys.exit()

    match('OP_PRIDRUZI')
    E()


def Za_petlja():
    match('KR_ZA')
    if current and 'IDN' in current:
        match('IDN')
    else:
        print(f"SyntaxError: Expected IDN, but got {current}")
        sys.exit()

    match('KR_OD')
    E()
    match('KR_DO')
    E()
    Lista_naredbi()
    match('KR_AZ')


def E():
    T()
    E_lista()


def E_lista():
    if current and ('OP_PLUS' in current or 'OP_MINUS' in current):
        match(current)
        E()


def T():
    P()
    T_lista()


def T_lista():
    if current and ('OP_PUTA' in current or 'OP_DIJELI' in current):
        match(current)
        T()


def P(parent):
    if current and 'OP_PLUS' in current:
        match('OP_PLUS')
        P()
    elif current and 'OP_MINUS' in current:
        match('OP_MINUS')
        P()
    elif current and 'L_ZAGRADA' in current:
        match('L_ZAGRADA')
        E()
        match('D_ZAGRADA')
    elif current and 'IDN' in current:
        match('IDN')
    elif current and 'BROJ' in current:
        match('BROJ')
    else:
        print(f"SyntaxError: Unexpected token: {current}")
        sys.exit()


# Start parsing
Program()
if current == '@':
    print("Parsing successful!")
else:
    print(f"SyntaxError: Unexpected token at the end: {current}")
    sys.exit()
