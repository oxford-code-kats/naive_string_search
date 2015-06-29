import timeit

setup = """
from naive_search import word_search

with open('sample_text.txt', 'r') as f:
	text = f.read() 
"""

msg = "naive word count"
print(msg)
print(min(timeit.Timer('search_term="here"; word_search(search_term, text)', 
	setup=setup).repeat(repeat=1, number=100)))

setup = """
from collections import Counter

with open('sample_text.txt', 'r') as f:
	text = f.read() 
"""

msg = "python word count"
print(msg)
print(min(timeit.Timer('search_term="here"; wordcount = Counter(text.split())', 
	setup=setup).repeat(repeat=1, number=100)))