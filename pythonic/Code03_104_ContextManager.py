f = open('test.txt', 'r')
file_contents = f.read()
f.close()

word = file_contents.split(' ')
word_count = len(word)
print(word_count)
