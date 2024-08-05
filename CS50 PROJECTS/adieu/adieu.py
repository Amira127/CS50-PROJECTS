def main():
    import inflect
    p = inflect.engine()
    names = get_names ()
    names[2] = "to "+ names[2]
    if len(names)==3:
        mylist= p.join(names, conj='')
    elif len(names)==4:
        mylist = p.join(names, final_sep="")
    else:
        mylist = p.join(names)
    print()
    print(mylist)



def get_names ():
    list=["Adieu" , "adieu"]
    while True:
        try:
            name=input("Name:").title()
            if name=="":
                pass
        except EOFError:
            break
        list.append(name)
    return list

if __name__ == "__main__":
    main()