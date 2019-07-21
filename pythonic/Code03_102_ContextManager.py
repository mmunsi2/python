t = open('test.txt', 'r')
file_contents = t.read()
t.close()l I
word = file_contents.split(' ')
word_count = len(word)
print(word_count)
