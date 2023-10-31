def openlevelfile(level):
    f = open(level,"r")

    x=0                       #FUNCTION TO TAKE FILENAME "LEVEL.DAT" AND RETURN LIST WITH ELEMENTS FOR EACH ROW.
    columns = []              #ROW ELEMENTS ARE LISTS WITH ELEMENTS OF CHARACTERS IN ROW

    while True:
        line = f.readline()
        row = []
        i=1
        for element in line:
            if(element != " "):
                row.append(element)
            i+=1 
        print(row)
        columns.append(row)
        if(row):
            print("e")
        else:
            break
    return columns

print(openlevelfile("level.dat"))