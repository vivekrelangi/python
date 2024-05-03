def get_f_n(f,l,m=''):
    if m:
        f_n="{0} {1} {2}".format(f,m,l)
    else:
        f_n="{0} {1}".format(f,l)
    return f_n.title()
