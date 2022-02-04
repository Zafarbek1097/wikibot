import  wikipedia

wikipedia.set_lang('uz')
x = wikipedia.search('Toshkent')
for y in x:
    print(y)

print(wikipedia.summary("Toshkent"))
