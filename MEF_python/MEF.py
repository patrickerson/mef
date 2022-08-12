

def start(input):
    """
    Não recebeu nenhuma parâmetro ainda
    """
    if input == "":
        return False
    if input[0] == "a":
        return s0(input[1:])
    if input[0] == "b":
        return s3(input[1:])
    if input[0] == "c":
        return False

def s0(input):
    """
    Recebeu pelo menos um a
    """
    if input == "":
        return False
    if input[0] == "a":
        return s4(input[1:])
    if input[0] == "b":
        return s1(input[1:])
    if input[0] == "c":
        return False


def s1(input):
    """
    Recebeu um b seguido de a
    """
    if input == "":
        return False
    if input[0] == "a":
        return s4(input[1:])
    if input[0] == "b":
        return s2(input[1:])
    if input[0] == "c":
        return False
    

def s2(input):
    """
    Recebeu um a seguido de 2 b
    """
    if input == "":
        return True
    if input[0] == "a":
        return s0(input[1:])
    if input[0] == "b":
        return s2(input[1:])
    if input[0] == "c":
        return False


def s3(input):
    """
    Não recebeu nenhum a
    """
    if input == "":
        return True
    if input[0] == "a":
        return s0(input[1:])
    if input[0] == "b":
        return s3(input[1:])
    if input[0] == "c":
        return False


def s4(input):
    """
    Recebeu pelo menos um a sem ser seguido por 2 b
    """
    if input == "":
        return False
    if input[0] == "a":
        return s4(input[1:])
    if input[0] == "b":
        return s4(input[1:])
    if input[0] == "c":
        return False

def check_language(input):
    result = start(input)
    if result:
        return f"{input}: pertence"
    return f"{input}: não pertence"

    