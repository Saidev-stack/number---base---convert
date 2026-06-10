#Find the decimel value for b16 number
def find_inb16 (n_inb16):
    """
    Find the decimel value for b16 number
    Parameters:
    -----------
    n_inb16 : value in B16
    Returns:
    --------
    The value in B16
    """
    n_inb16 = n_inb16.upper()
    b16_lettres = ['A','B','C','D','E','F']
    values = [10, 11, 12, 13, 14, 15]
    if n_inb16 in b16_lettres:    
        return values[b16_lettres.index(n_inb16)]
    else:
        return int(n_inb16)    
#Find the b16 value for decimel number
def hex_of_dec (n_in_b10):
    """
    Find the b16 value for decimel number
    Parameters:
    -----------
    n_in_b10 (int): value in B10
    Returns:
    --------
    The value in B10
    """
    b16_lettres = ['A','B','C','D','E','F']
    values = [10, 11, 12, 13, 14, 15]
    if n_in_b10 in values:    
        return b16_lettres[values.index(n_in_b10)]
    else:
        return str(n_in_b10) 
#Convert the number from any base _Binary to Hexadecimal_ bases to decimal base  
def to_dec (nbr_in_str, base_from):
    """
    Convert the number from any base _Binary to Hexadecimal_ bases to decimal base
    Parameters:
    -----------
    nbr_in_str (str) : the number to convert in a string
    base_from (int) : the base of the given number
    Returns:
    --------
    (int) the number in decimal base
    """
    nbr_in_dec = 0
    p = len(nbr_in_str) - 1
    for c in nbr_in_str:
        if find_inb16(c) >= base_from:
            return False
        nbr_in_dec += find_inb16(c) * pow(base_from, p)
        p -= 1
    return int(nbr_in_dec)
#Convert the number from decimal base to the choosen base
def dec_to (nbr_in_dec, base_to):
    """
    Convert the number from decimal base to the choosen base
    Parameters:
    -----------
    nbr_in_dec (int) : the number in decimal base
    base_to (int) : the base to convert to
    Returns:
    --------
    (str) the number in base_to
    """
    if nbr_in_dec == 0:
        return "0"
    result = ""
    while nbr_in_dec > 0:
        remainder = nbr_in_dec % base_to
        result += hex_of_dec(remainder)
        nbr_in_dec //= base_to

    return result[::-1]

print('                         ========== Welcome ==========')
ans = input("You want to convert some numbers ? entre 'yes' and let's go => ")
bases = {
    1: 2,
    2: 8,
    3: 10,
    4: 16
}
while(ans == 'yes'):
    print("Base numbers convertations")
    print("\n menu :")
    print("1 - Binary\n 2 - Octal\n 3 - Decimal\n 4 - Hexadecimal")
    
    base_from = int(input("Choose the number base to convert (1 to 4):"))
    base_to = int(input("Choose which base to convert your number (1 to 4):"))
    
    number = input("Entre your number : ")

    if base_from in bases and base_to in bases:
        val = to_dec(number, bases[base_from])
        if val == False :
            print("Invalide number for this base")
        else:
            print(number, "in Base", bases[base_to], " : ", dec_to(val, bases[base_to]))
    else:
        print("Invalide bases!")
    ans = input("You want to try again ? entre 'yes' and let's go => ")
print("Goodbay, have a good day!")
