with open('/home/patrick/Bureau/GITS/altair/altair/models/pkl.txt') as f:
    while True:
        try:
            first_line = f.readline()
        except EOFError:
            break
