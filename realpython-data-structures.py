import logging, sys, pdb
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
# logging.debug(f'Step {i}: {guess}')
# logging.debug('Step: %s' % guess)
# print <map object at ...>: print(list(result))
# pdb.set_trace()


# https://realpython.com/python-data-structures/
def main():
    # run_on_dicts()
    # ordered_dict()
    # default_dict()
    # chain_map()
    # read_only_dicts()
    # mutable_dynamic_arrays()
    # immutable_container()
    # basic_typed_arrays()
    # arr_of_bytes()
    # mutable_arr_of_bytes()
    # data_object_with_dicts()
    # data_objects_with_dataclasses()
    # data_objects_with_named_tuples()
    # data_objects_with_named_tuples_from_typing()
    data_objects_with_simple_namespace()


def hey(ho):
    print(ho)
    logging.debug(ho)
    # hey('fibus: %s' % fibus)
    # lc_letters = [letter for letter in 'human']
    # hey('list comprehension: ' + ('%s ' * len(lc_letters)) % tuple(lc_letters))


# Dictionaries are also often called maps, hashmaps, lookup tables, or associative arrays.
def run_on_dicts():
    phonebook = {
        "bob": 7387,
        "alice": 3719,
        "jack": 7052
    }
    hey(phonebook['alice'])
    squares = {x: x * x for x in range(6)}
    hey(squares)

    tpl = (1, 2, 3)  # use as dict key as lon as they have hashable types in it, e.g. strings and numbers
    foo_dict = {tpl: "this is a tuple as key"}
    hey(foo_dict[tpl])

# Python includes a specialized dict subclass that remembers the insertion order of keys added to it: collections.OrderedDict.
# need: import collections
import collections
def ordered_dict():
    d = collections.OrderedDict(one=1, two=2, three=3)
    d['four'] = 4
    hey(d)
    hey(d.keys())


# The defaultdict class is another dictionary subclass that accepts a callable in its constructor whose return value will be used if
# a requested key cannot be found
from collections import defaultdict
def default_dict():
    dd = defaultdict(list)

    dd['dogs'].append('Rufus')
    dd['dogs'].append('Kathrin')
    dd['dogs'].append('Mr Sniffles')

    hey(dd['dogs'])

from collections import ChainMap
def chain_map():
    dict1 = {'one': 1, 'two': 2, 'three': 3}
    dict2 = {'four': 4, 'five': 5}
    chain = ChainMap(dict1, dict2)
    hey(chain)
    hey(chain['four'])
    hey(chain['one'])


# MappingProxyType is a wrapper around a standard dictionary that provides a read-only view into the wrapped dictionary’s data. 
from types import MappingProxyType
def read_only_dicts():
    writeable = {'one': 1, 'two': 2}
    read_only = MappingProxyType(writeable)

    hey(read_only)
    # read_only['one'] = 23
    writeable['one'] = 42
    hey(read_only)


def mutable_dynamic_arrays():
    # list
    arr = ['one', 'two', 'three']
    hey(arr[0])
    hey(arr)
    arr[1] = 'hello'
    hey(arr)
    del arr[1]  # or del(arr[1])
    hey(arr)
    arr.append(23)
    hey(arr)


def immutable_container():
    # tuple
    arr = ('one', 'two', 'three') # round brackets !!
    hey(arr[0])
    hey(arr)
    # arr[1] = 'hello'  # does not work, throw exception
    # del arr[1]  # does not work, throw exception
    # (Adding elements creates a copy of the tuple)
    a2 = arr + (23,)  # shortcut for tuple (foo,) otherwise you can not concat 2 tuples 
    hey(a2)


# Arrays created with the array.array class are mutable and behave similarly to lists except for one important difference: they’re
# typed arrays constrained to a single data type.
import array
def basic_typed_arrays():
    arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
    hey(arr)
    hey(arr[1])
    arr[1] = 23
    hey(arr)
    del(arr[1])
    hey(arr)
    arr.append(42)
    hey(arr)
    # arr[1] = 'hello'  # does not work, throws an error


def arr_of_bytes():
    arr = bytes((0, 1, 2, 3))  # values 0 <= x <= 255 and immutable
    hey(arr[1])
    hey(arr)
    # hey(bytes((0, 300)))  # throws an error, max 255
    a2 = arr + bytes((4,))  # for some reason only bytes((4)), will show value zero, you need the tracing comma
    hey(a2)
    hey(a2[4])


def mutable_arr_of_bytes():
    arr = bytearray((0,1,2,3))
    hey(arr[1])
    hey(arr)
    arr[1] = 23
    hey(arr)
    hey(arr[1])
    del(arr[1])
    hey(arr)
    hey(len(arr))
    arr.append(42)
    hey('array: %s with len: %s' % (arr, len(arr)))
    hey(arr)
    not_mutable = bytes(arr)
    hey(not_mutable)
    # not_mutable[1] = 23  # throws an error


# TIP:
# Start always with a list, specialize later if needed
# If you’re willing to go beyond the Python standard library, then third-party packages like NumPy and pandas offer a wide range of
# fast array implementations for scientific computing and data science.

# mutable
def data_object_with_dicts():
    car1 = {
        "color": "red",
        "mileage": 3812.4,
        "automatic": True
     }
    car2 = {
        "color": "blue",
        "mileage": 40321,
        "automatic": False
     }

    hey(car2)
    hey(car1)
    hey(car1['mileage'])
    # Dicts are mutable
    car2['mileage'] = 12
    car2['windshield'] = 'broken'
    hey(car2)


from dataclasses import dataclass
@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool


# mutable
def data_objects_with_dataclasses():
    auto1 = Car("red", 3812.4, True)
    hey(auto1)
    hey(auto1.mileage)
    auto1.mileage = 123
    auto1.windshield = "broken"
    hey(auto1)  # windshield ist not show up in the default representation, but is stored!
    hey(auto1.windshield)
    # More to dataclasses, see https://realpython.com/python-data-classes/


# immutable
from collections import namedtuple
def data_objects_with_named_tuples():
    Wagen = namedtuple('Wagen', "color mileage automatic")
    wagen1 = Wagen("red", 3423.8, True)
    hey(wagen1)
    hey(wagen1.mileage)

    
# immutable
from typing import NamedTuple
class Vehicle(NamedTuple):
    color: str
    mileage: float
    automatic: bool

# immutable
def data_objects_with_named_tuples_from_typing():
    veh1 = Vehicle("red", 2343.2, True)
    hey(veh1)
    hey(veh1.mileage)
    # Fields are immutable
    # veh1.mileage = 12  # Throws error, not possible
    # veh1.windshield = 'broken'  # Throws error, not possible

# mutable
from types import SimpleNamespace
def data_objects_with_simple_namespace():
    schiff = SimpleNamespace(color="red", mileage=2343.2, automatic=True)
    hey(schiff)
    hey(schiff.mileage)
    schiff.mileage = 12
    hey(schiff)
    schiff.windshield = 'broken'
    hey(schiff)
    del(schiff.automatic)
    hey(schiff)

# @todo mit listen und dicts arbeiten, data_objects with dicts sind mutable, mit MappingProxyTpye erhält man ein readonly version

# @todo weitermachen




if __name__ == '__main__':
    main()
