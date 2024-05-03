questions = ['name', 'quest', 'favorite color']
answers = ['lancerlot', 'the holy grail', 'blue']
for q, a in zip(questions,answers):
    print('What is your {0}? It is {1}.'.format(q, a))