letterlijst = ['a', 'b', 'c']
print(letterlijst)

def wijzig(letterlijst):
    letterlijst.remove('a')
    letterlijst.remove('b')
    letterlijst.remove('c')
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')
    print(letterlijst)

wijzig(letterlijst)
