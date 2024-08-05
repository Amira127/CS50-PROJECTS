def main ():
    camelcase=get_camel_case()
    snake_case=snakecase(camelcase)
    print("snake_case:", snake_case)

def get_camel_case ():
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    while True:
        string=input("camelCase:")
        length=0
        while length <len(string) and string[length].upper() in alphabet:
            length+=1
        if length==len(string):
            return string

def snakecase(mixedcase):
    snakecase=""
    for pos in mixedcase:
        if pos == pos.upper():
            snakecase=snakecase+"_"+pos
        else:
            snakecase=snakecase+pos
    return snakecase.lower()


main()