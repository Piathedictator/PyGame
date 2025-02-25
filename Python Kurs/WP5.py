#WP5
#5.1 Substrings
txt = input("Give a sentence: ")

print(txt.split())

#5.2 Counting Characters
satz = input("Give a sentence: ")
satz_set = set(satz)
dict_satz={}
for zeichen in satz:
    if zeichen in dict_satz:
        dict_satz[zeichen]+=1
    else:
        dict_satz[zeichen]=1
print(list(satz))

print(dict_satz)
zeichen_zähler = {}

for zeichen in satz_set:
    zeichen_zähler[zeichen] = satz.count(zeichen)

print("Häufigkeit jedes Zeichens:")
for zeichen, zähler in zeichen_zähler.items():
    print(f"'{zeichen}': {zähler}")