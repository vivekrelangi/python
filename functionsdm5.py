def bp(f,l,a=None):
    p={'f':f,'l':l}
    if a:
        p['a']=a
    return p

m=bp('jimi','hendrix',27)
print(m)

m=bp('jimi','hendrix')
print(m)