
class person(object):
    pass


pgone = person()

pgone.a1=1233
pgone.a2=4566
print(pgone.a1,pgone.a2)

def gen(a):
    a.a1 = 123
    a.a2 = 456


gen(pgone)

print(pgone.a1,pgone.a2)