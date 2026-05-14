import warnings
warnings.filterwarnings('ignore')
import os
import gzip

from collections import Counter
from pprint import pprint

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

np.random.seed(123)
import string
import nltk
from nltk.corpus import stopwords
from nltk.text import TextCollection
from nltk.collocations import BigramCollocationFinder
from nltk.metrics.association import BigramAssocMeasures
nltk.download('punkt_tab') #Tokens not getting printed in absence of this
import sklearn

from sklearn.manifold import TSNE

from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
tqdm.pandas()
import watermark


import sys
import matplotlib
import pandas
import numpy

print("Python:", sys.version)
print("Matplotlib:", matplotlib.__version__)
print("Pandas:", pandas.__version__)
print("NumPy:", numpy.__version__)

text="""May had a little lamb, little lamb,
little lamb. 'Mary' had a little lamb whose fleece was white as now.
And everywhere that Mary went, Mary went, MARY went. Everywhere
that mary went, The lamb was sure to go"""

punctuation=set(string.punctuation)
print(punctuation)

#from IPython.display import display - For Jupyter notebook only
#identify tokens
print(text)
tokens=nltk.word_tokenize(text,'english')
print(tokens)
print(tokens[4])
# from nltk.tokenize import word_tokenize
# print("NLTK loaded OK")

tokens = nltk.tokenize.WordPunctTokenizer().tokenize(text)
print(tokens)
print(tokens[12])


