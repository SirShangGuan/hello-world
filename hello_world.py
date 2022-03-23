#!/opt/homebrew/bin/python3

from pyuvm import *
from allpairspy import AllPairs


parameters = [
    ["Brand X", "Brand Y"],
    ["98", "NT", "2000", "XP"],
    ["Internal", "Modem"],
    ["Salaried", "Hourly", "Part-Time", "Contr."],
    [6, 10, 15, 30, 60],
]
# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))

my_object = uvm_object("my_object")
type(my_object)

print("object name:", my_object.get_name())
print("Hello World 2 !!!!")