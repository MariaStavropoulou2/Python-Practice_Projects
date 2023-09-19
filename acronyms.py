def acronyms(text):
    text = text.split()
    a = " "
    for i in text:
        a = a+str(i[0]).upper()
    print(a)

user_input = str(input("Enter a Phrase: "))
acronyms(user_input)