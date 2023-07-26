import os
import random
import requests

# load 10_000 most common words from an URL
url = "https://www.mit.edu/~ecprice/wordlist.10000"
try:
    response = requests.get(url)
except Exception as e:
    print(f"Exception {e} caught...")
else:
    text = response.text
finally:
    print(f"Status code of the response: {response.status_code}")

words = text.splitlines()
my_text = random.choices(words, k=120)

with open(os.path.join(os.getcwd(), "data", "words.txt"), mode="wb") as f:
    for k in range(10):
        f.write((" ".join(my_text[k*12:(k+1)*12]) + "\n").encode())

# split list into list of sublists
list1 = ["a", "q", "g", "q", "r", "t", 111]
list_of_sublists = [list1[i*3:(i+1)*3] for i in range(len(list1) // 3 + 1)]

