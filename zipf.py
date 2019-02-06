# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:07:56 2019

@author: scatt
"""

# Hypothesis testing of Zipf's Law on natural and non-natural (i.e. randomly generated) language
# for analysis and discussion, see "README.md"

import pylab
from nltk.book import *
from nltk.probability import FreqDist
import random
import string

# Create a frequency distribution of the given text and plot in order to visualize Zipf's Law
def zipf(text, name, new_figure=False):
    fdis = dict(FreqDist(text))
    freq = [item[1] for item in sorted(fdis.items(), key=lambda kv: kv[1], reverse=True)]
    rank = [item+1 for item in range(len(sorted(fdis.items(), key=lambda kv: kv[1], reverse=True)))]
    
    # Test print the first ten items and their frequencies from the given text
    #print('\n'.join([str(rank[i])+': '+str(freq[i]) for i in range(10)]))
    
    # plot freq vs rank using pylab
    # (plotting will occur on the same plot unless 'new_figure' parameter is 'True')
    if new_figure:
        pylab.figure()
    pylab.plot(rank,freq, label=name)
    
    # change plot to log scale to visually confirm Zipf's Law
    # see discussion in README.md
    pylab.xscale("log")
    pylab.yscale("log")
    
    # add axis labels, title, and legend
    pylab.xlabel('Rank')
    pylab.ylabel('Frequency')
    pylab.title('Logorithmic Frequency vs Rank for Words in a Text')
    pylab.legend(loc='upper right')
    
def generate_text(subset=8, text_len=1000000, approx_word_len=5):
    if subset>26:
        subset=26     # max chars in alphabet
    if subset<1:
        subset=8     # default chars (a-h, plus the space character) to use in random string generation
    
    
    if approx_word_len>subset:
        approx_word_len=subset

    # generate random string of 'words'
    chars = list(string.ascii_lowercase)[:subset]
    for i in range(int(subset/approx_word_len)):
        chars.append(' ')               # add the number of spaces required to maintain an approx. word length (specified)
    zipf(''.join(random.choice(chars) for _ in range(text_len)).split(' '),'Randomly-Generated String, avg word len='+str(approx_word_len), new_figure='True')
    

def main():
    # call zipf for natural language sample(s)
    zipf(text1, "Moby Dick")         
    zipf(text2, "Sense and Sensibility")        
    zipf(text3,"The Book of Genesis")        
    zipf(text4, "Inaugural Address Corpus")         
    zipf(text5, "Sample Chat Corpus")         
    # call zipf for random language sample(s)
    generate_text(approx_word_len=6)
    
if __name__ == "__main__":
    # conditionally call main
    main()

