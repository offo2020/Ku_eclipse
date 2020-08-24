TEXT = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# prvy sposob
ABC = tuple('abcdefghijklmnopqrstuvwxyzAB')

TEXT2 = ''

for p in TEXT:
    if p == ' ':
        TEXT2 += ' '
    elif p in ABC:
        i = ABC.index(p)
        TEXT2 += ABC[i+2]
    else:
        TEXT2 += p

print(TEXT2)

# alebo len cez string - a nemam problem s y,z
ABC = 'abcdefghijklmnopqrstuvwxyzab'

TEXT2 = ''

for p in TEXT:
    if p == ' ':
        TEXT2 += ' '
    elif p in ABC:
        i = ABC.find(p)
        TEXT2 += ABC[i+2]
    else:
        TEXT2 += p

print(TEXT2)


# alebo takto:

ABC = 'abcdefghijklmnopqrstuvwxyz'
NEW_ABC = 'cdefghijklmnopqrstuvwxyzab'

TABLE = TEXT.maketrans(ABC, NEW_ABC)
print(TEXT.translate(TABLE))
