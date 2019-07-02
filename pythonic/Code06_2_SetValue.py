class Person():
    pass
person = Person()
first_key = 'first'
first_val = 'Corey'
setattr(person, first_key, first_val)
first = getattr(person, first_key)
print(first) I
