t = open('test.txt', 'r')
file_contents = t.read()
t.close()
tokens = file_contents.split(' ')
token_count = len(tokens)
print(token_count)
