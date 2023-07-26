import random
from string import ascii_uppercase
from more_itertools import locate, batched

# Note on sampling using random package:
#   (1) random.choice: sample one element from an iterable without replacement
#   (2) random.choices: sample k elements WITH replacement
#   (3) random.sample: sample k elements WITHOUT replacement

l = [random.choice(ascii_uppercase[:10]) for k in range(1000)]

#######################################################################################################################
############################## FINDING SPECIFIC ELEMENT IN A LIST #####################################################
# P1: find positions of all Cs in the list using list comprehensions
c_indexes = [key for key, val in enumerate(l) if val == "C"]
# P2: find positions of all Cs using a different method
c_indexes2 = list(locate(l, lambda x: x == "C"))
print(c_indexes == c_indexes2)
# sort list of 3-tuples by its 2nd element
lt = [random.choices(range(1000), k=3) for i in range(10)]
lt.sort(key=lambda x: x[1])
#######################################################################################################################


#######################################################################################################################
#######################################  SPLIT LIST INTO CHUNKS #######################################################
l = list(range(14))
chunklen = 3
# Solution 1: manual
chunks = []
for i in range(len(l) // chunklen + 1):
    chunks.append(l[i*chunklen:((i+1)*chunklen)])

# Solution 2: use batched() from the more_itertools package
chunks2 = list(batched(l, 3))
#######################################################################################################################
