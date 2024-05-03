from collections import OrderedDict
fav_languages = OrderedDict()

fav_languages['jen']=['python','ruby']
fav_languages['sarah']=['C']
fav_languages['edward']=['ruby','go']
fav_languages['phil']=['python','haskell']

for name, langs in fav_languages.items():
    print(name+":")
    for lang in langs:
        print("- "+lang)