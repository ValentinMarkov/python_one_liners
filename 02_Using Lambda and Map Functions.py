txt = ['lambda functions are anonymous functions.',
       'anonymous functions don\'t have a name.',
       'functions are objects in Python.']

mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

print(list(mark))

# my example
lst_nums = [120, 20, 11, 345, 24, 127, 451]
mark_2 = map(lambda num: (True, num) if num % 2 == 0 else (False, num), lst_nums)

print(list(mark_2))
