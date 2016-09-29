f = open('./texts/text.txt','r+')
new_text = ''
for word in (f.readline()).split():
    if(word == 'ADJECTIVE'):
        word = input("Enter an adjective:")
    if(word == 'VERB'):
        word = input("Enter a verb:")
    if(word == 'NOUN'):
        word = input("Enter a noun:")
    if(word == 'OBJECT'):
        word = input("Enter an object:")
    new_text= new_text + ' ' + word
f.close()
print(new_text)
f = open('./texts/new_text.txt','w+')
f.write(new_text)
f.close()
input()
