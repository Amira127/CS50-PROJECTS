def main ():
    grocery=get_items()
    g_sorted = dict(sorted(grocery.items()))
    for item in g_sorted:
        print(g_sorted[item],item)

def get_items():
    dic={}
    while True:
        try:
            item = input().upper()
            if item!="":
                if not exist(item,dic) :
                    dic.update({item:1})
                else :
                    dic[item] =dic[item]+1
        except EOFError:
            break
        except KeyError:
            pass
    return dic

def exist (item,dic):
    return dic.get(item)
main()