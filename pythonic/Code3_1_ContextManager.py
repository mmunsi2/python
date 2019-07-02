f = open('test.txt', 'r')
file_contents = f.read()
f.close()l I

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
