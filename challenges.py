__author__ = 'andrewwhiter'


a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def solve (a):
    x=""
    for c in a:
        if c == "y":
            x += "a"
        elif c =="z":
            x += "b"
        elif c in " ,.'()":
            x += c
        else:
            x += chr(ord(c) + 2)
    return x

print(solve(a))
print(solve("map"))