mylist = [1, 2, "1", [1, 2], "2", (1, 2)]
for i in mylist:
    if type(i) == tuple:
        print(f"{i} -- кортеж") 
    elif type(i) == list:
        print(f"{i} -- список")
    else: 
        print(f"{i} -- не кортеж і не список")
