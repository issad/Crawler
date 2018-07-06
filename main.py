import os
import pickle
os.chdir('C:\Users\ISSAD Adel\Desktop\ISSADsystem\MoteurDeRecherche\code')
url=input("Donnez le lien avec lequel vous voulez commencer:      ")
page=get_page(url)
index=collect_all_keys_web(page)
index=hash_table(index)
key=input("Votre recherche:    ")
if key not in search_key_word(index):
    print("Page introuvable")
else:
    for e in index:
        if e[0]==key:
            for i in e[1]:
                print i
os.system("pause")
