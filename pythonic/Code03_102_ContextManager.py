t = open('test.txt', 'r')
file_contents = t.read()
t.close()l I
mots = file_contents.split(' ')
mot_count = len(mots)
print(mot_count)
