import textwrap

def formatter(string, char):
    try:
        char = int(char)
        
        if not string:
            raise ValueError
        if char <= 0:
            raise ValueError
    except ValueError:
        return "\nErro nos valores! Confira se seus Inputs estão corretos!"

    return textwrap.fill(string, char)
    