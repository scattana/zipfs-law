# zipfs-law
Hypothesis testing of Zipf's Law for natural and unnatural languages (NLP SP19)

**Contents**

_____

* Introduction
* Part One: Zipf's Law for Natural Language
* Part Two: Zipf's Law for Unnatural Language
* Analysis and Results

_____



###Introduction

This project will test Zipf's Law on large samples of natural language as well
as samples of randomly-generated text, used to simulate non-natural language.

Zipf's Law is a phenomenon seemingly characteristic of nearly all natural
languages that defines an inverse relationship between word frequency and rank. 
That is, in any given text, the 30th most commonly-used word will appear
three more times than the 90th most commonly-used word.

This relationship can be represented by the equation ``c * r = k`` where ``c`` is
a word's count (i.e. how many times the word appears in the text), ``r`` is the
word's rank (1st highest word count, 2nd highest, etc.) and ``k`` is some constant
of proportionality (which should the same within the same text).



###Part One: Zipf's Law for Natural Language (English)

Five large text samples (ranging from 45,000 to 260,000 words) were analyzed
through a custom function, _zipf_, which calculates frequency distribution
(bag-of-words model) and plots word frequency (y-axis) versus word rank (x-axis).

To visualize the inverse relationship, logorithmic scaling was used; however,
the _zipf_ function permits the disabiling of log scaling through an option parameter
(log=False). Note: disabling the _log_ parameter will make the graphs very
difficult to analyze, because every text has a disproportionate number of words
whose count is one (i.e. they only appear once in the text). These are often obscure
words or references to specific people or places, and as such, they act as outliers
in the non-logorithmic graph. By using log scaling, the inverse relationship
**is evident through a linear relationship between the scaled y and x axes**
The presence of a linear relationship confirms Zipf's Law, while its absense 
would disprove the Law.

From **Figure 1** (below), it is clear all five English texts confirm Zipf's Law
(with only slight deviations from the linear relationship on the extreme ends of
the x-axis, as discussed previously).

![alt-text](https://github.com/scattana/zipfs-law/blob/master/fig1.png "Figure 1: Zipf's Law for Natural Language Samples")

###Part Two: Zipf's Law for Unnatural (simulated) Language

From the above results, it's clear Zipf's Law holds true for natural language
(at least, for English, though other studies have been conducted proving this Law
on texts of many other languages). However, if a _simulated_ language is studied,
will Zipf's Law?

To simulate language, a simple approach is used to generate random strings based
on a subset of the English language characters. Spaces are dynamically added to the
character set such that an average word length can be ensured with reasonable accuracy,
and the Python `random.choice()` function is employed to generate a psuedo-random
text. This text is passed to the _zipf_ function in much the same way, and again
plotted in terms of frequency versus rank (again with default logorithmic scaling).

From *Figure 2* (below), Zipf's Law _does not_ appear to hold for even a large
(one million character/approx. 200,000 word) text sample. There is only a very rough
linear relationship between the logs of frequency and rank, skewed even more heavily
on either end of the x-axis. For discussion related to why this might be the case,
see the *Analysus and Results* section, below.

![alt-text](https://github.com/scattana/zipfs-law/blob/master/fig1.png "Figure 2: Zipf's Law for Non-Natural Language Samples")

###Analysis and Results






