prompt="\nTell me something,and I'll "
prompt+="repeat it back to you."
prompt+="\nEnter 'quit' to end the program "

message=""
while message!='quit':
    message=input(prompt)

    if message!='quit':
        print(message)

prompt="\nTell me something,and I'll "
prompt+="repeat it back to you."
prompt+="\nEnter 'quit' to end the program "
active=True
while active:
    message=input(prompt)

    if message =='quit':
        active=False
    else:
        print(message)

prompt="\nWhat cities have you visited?"
prompt+="\nEnter 'quit' when you're done. "

while True:
    city=input(prompt)

    if city == 'quit':
        break
    else:
        print("I've been to "+city+"!")