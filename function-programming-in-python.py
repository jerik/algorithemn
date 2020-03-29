# Course: Functional Programming in Python https://realpython.com/lessons/parallel-processing-multiprocessing-overview/
# Tip
# alternative zum normalen python interpreter, mit bissle mehr komfort
# ipyhton (habe ich wegen, jupyter schon drauf
# bpython sieht auch ganz gut aus, hat mehr doc_strings/erklärungen https://bpython-interpreter.org/screenshots.html
import collections
from pprint import pprint
scientist = [
    {'name': 'Ada Lovelace', 'filed': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emmy Noether', 'filed': 'math', 'born': 1882, 'nobel': False},
]
# run in pyhton shell
# >>> exec(open('filename').read())
# imutable object machen, um diese zu ändern muss man eine kopie machen
Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])
# scientists = [
#     Scientist(name='Ada Lovelance', field='math', born=1815, nobel=False),
#     Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
# ]
# From a list, entries can be delete, not immutable. Better to use a tuple!

# Tupel is a immutable Data set
scientists = (
    Scientist(name='Ada Lovelance', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

# Work with filter
# x is passed in lambda, and you can do comparison with x-stuff
filter(lambda x: x.nobel is True, scientists)  # returns a iterable object in python3
# same
filter(lambda x: x.nobel, scientists)
fs = filter(lambda x: x.nobel, scientists)
print('# show lambda filter with next(fs)')
pprint(next(fs))

# show all elements (do not filter)
filter(lambda x: True, scientists)  # returns a iterable object in python3

# Get a new tuple that is filtered by fileld = physics
print('# show filter x.field by physics')
pprint(tuple(filter(lambda x: x.field == 'physics', scientists)))
# Combining
print('# show filter x.field by physics and x.nobel')
pprint(tuple(filter(lambda x: x.field == 'physics' and x.nobel, scientists)))


# make reusable stuff
def nobel_filter(x):
    return x.nobel is True


print('# show filter with nobel_filter')
pprint(tuple(filter(nobel_filter, scientists)))

# List comprehensiv
print('# show list comprehensiv as alternativ of filter function')
list_comprehensiv = [x for x in scientists if x.nobel is True]
pprint(list_comprehensiv)

print('# show list comprehensiv as tuple as alternativ of filter function')
tuple_list_comprehensiv = tuple([x for x in scientists if x.nobel is True])
pprint(tuple_list_comprehensiv)

print('# show list comprehensiv as tuple (without list zwischenproduct) as alternativ of filter function')
# die [ werden entfernt, dadurch wird das eine generator expression, der ein ad-hoc iterator erstellt
tuple_comprehensiv = tuple(x for x in scientists if x.nobel is True)
pprint(tuple_comprehensiv)

# Work with map function
# map is used to transform a list to a new list
# e.g. calculate age of the persons on the scientists list
names_and_ages = tuple(map(
    lambda x: {'name': x.name, 'age': 2017 - x.born},
    scientists
))
print('# show list of person and their age')
pprint(names_and_ages)

# list_comprehensive example = generator experssion
print('# show list comprehensiv version')
list_comp = tuple({'name': x.name, 'age': 2017 - x.born} for x in scientists)
pprint(list_comp)


def calculate_age(x):
    return {'name': x.name, 'age': 2017 - x.born}


person_ages = tuple(map(calculate_age, scientists))
print('# Person and ages the map way')
pprint(person_ages)

# Working with reduce function
# reduce, reduziert alles auf einen wert, anhand der function und dem iterierbaren object was man übergibt
# needed import for python 3
from functools import reduce

# der accumulator sammelt die berechnungen, initial wert ist hier das dritte argument =0 (d.h. accumulator = 0)
total_age = reduce(
    lambda accumulator, val: accumulator + val['age'],
    names_and_ages,
    0)

print('--> Total age of all scientists person: %s' % total_age)

# alternative python way
print('# alternative python way with sum')
print(sum(x['age'] for x in names_and_ages))


# example: grouping scientists by fields
def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc


scientists_by_field = reduce(
    reducer,
    scientists,
    {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []}
)
print('# scientists group by field')
pprint(scientists_by_field)

# import collections # ensure that you have that
scientists_by_field = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)
)

print('# same result as above but with collections.defaultdict(list)')
pprint(scientists_by_field)

# collections.defaultdict(list), erstellt für jeden eintrag/key den
# es nicht kennt ein neues listeelement mit dem value den man übergibt

# alternative pythonic version
import itertools
scientists_by_field_pyway = {
    item[0]: list(item[1])
    for item in itertools.groupby(scientists, lambda x: x.field)
}
print('# Nearly same result but python way')
pprint(scientists_by_field_pyway)
