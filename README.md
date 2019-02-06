# zipfs-law
Hypothesis testing of Zipf's Law for natural and unnatural languages (NLP SP19)

**Contents**

_____

* Introduction
* Part One: Zipf's Law for Natural Language
* Part Two: Zipf's Law for Unnatural Language
* Analysis and Results
* Replicating the Study
* References and Further Investigation

_____



### Introduction

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



### Part One: Zipf's Law for Natural Language (English)

Five large text samples (ranging from 45,000 to 260,000 words) were analyzed
through a custom function, _zipf_, which calculates frequency distribution
(bag-of-words model) and plots word frequency (y-axis) versus word rank (x-axis).

To visualize the inverse relationship, logorithmic scaling was used; however,
the _zipf_ function permits the disabiling of log scaling through an optional parameter, `log=False`.

Note: disabling the _log_ parameter will make the graphs very
difficult to analyze, because every text has a disproportionate number of words
whose count is one (i.e. they only appear once in the text). These are often obscure
words or references to specific people or places, and as such, they act as outliers
in the non-logorithmic graph. 

By using log scaling, the inverse relationship **is evident through a linear relationship between the scaled y and x axes**
The presence of a linear relationship confirms Zipf's Law, while its absense would disprove the Law.

From **Figure 1** (below), it is clear all five English texts confirm Zipf's Law
(with only slight deviations from the linear relationship on the extreme ends of
the x-axis, as discussed previously).

![alt-text](https://github.com/scattana/zipfs-law/blob/master/fig2.png "Figure 1: Zipf's Law for Natural Language Samples")

### Part Two: Zipf's Law for Unnatural (simulated) Language

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

From **Figure 2** (below), Zipf's Law _does not_ appear to hold for even a large
(one million character/approx. 200,000 word) text sample. There is only a very rough
linear relationship between the logs of frequency and rank, skewed even more heavily
on either end of the x-axis. For discussion related to why this might be the case,
see the **Analysis and Results** section, below.

![alt-text](https://github.com/scattana/zipfs-law/blob/master/fig1.png "Figure 2: Zipf's Law for Non-Natural Language Samples")

### Analysis and Results

The previous two studies seemingly confirm Zipf's Law and suggest there is indeed
an inverse relationship between word frequency and rank in natural language, and further,
that this is a _unique_ feature of natural language - it can't be easily simulated by
random or pseudo-random text. It would appear there is something unique about natural
languages that enables this result. So, what it is?

Though there may be many underlying factors at play, one such factor is likely the
grammatical structure present in any natural language (although this study was only conducted
on English texts, other studies have proven similar results with many other languages). There
are certain grammatical rules an author or speaker must follow to convey an appropriate message.
Verbs will generally reference a subject, characters in a story must be explicitly mentioned
by name a certain number of times to avoid ambuguity, and pronouns are used to avoid repetitiveness
and prevent wordiness. 

Further, Zipf's Law seems to hold true _for a given text_ - and the domain of a specific text,
whether it is a work of fiction, a religious text, or a speech transcript, will almost certainly
use the same terms more often than a random collection of words and phrases (part two of this study
simulated this effect at a very basic level). While part one of this study used a very diverse set
of domains to test Zipf's Law, ranging from fiction to religion and presidential speeches, Zipf's
Law was confirmed on each of these texts independently.

One final remark: an individual generates speech or text based on _real-world experiences_, from
natural events, from the works of other authors or based on famous speeches from the past. Therefore,
all natural language is seemingly dependent on that which came before it, which may help to explain
why this trend can seen in ancient religious texts as well as modern-day speeches.



##### What's happening at either end of the x-axis in both plots?

For a given text, there may be many words that are only used once. These might be
specific references, names, places, or variations of the same word that only appear
once in the text. These 'solo' words skew the results a bit, because there is no single
'lowest rank' - instead, there can be thousands of words tied for the lowest rank
(where all of these words only appear once!). On the other side, extremely common
words (including stop words like 'a' or 'the') appear a disproportionate number of times
and don't really reflect any information about the author's writing style or natural
language in general - they exist for grammatical purposes. Very little text pre-processing
was conducted on these samples, but implementing stopword filtering, lemmatization,
and similar text pre-processing techniques would likely lessen the extreme behavior of
these results on either end of the x-axis.


### Replication this Study

The full source code for this project is provided in _zipf.py_ and can be run
using Python 3. Other requirements and dependencies include:
* nltk open-source packages, including the `probability` and `book` modules
* matplotlib (used for PyLab plotting)

The Spyder IDE with a custom NLP environment was used for this project, though
PyCharm and Atom are also recommended. All necessary dependencies can be installed
through `conda`, i.e. `conda install nltk`

The study uses the first five English-language texts from the `nltk.book` package,
though different texts can be used by changing the first parameter to `zipf` (called
in `main`).

The optional `new_figure` and `log` parameters in the call to `zipf` create a new figure
for plotting and plot with or without logorithmic scaling, respectively.


### References and Further Investigation

The inspiration for this study came from the Natural Language Toolkit (NLTK) and 
chapter two of [the corresponding text](https://www.nltk.org/book)

Topics related to this study were inspired by CSE-44657 Natural Language Processing
at the University of Notre Dame.

Research conducted on Zipf's Law primarily relied on content from Britannica
[found here](https://www.britannica.com/topic/Zipfs-law) and [related information
about harmonic series from Wolfram](http://mathworld.wolfram.com/ZipfsLaw.html)

The discussion of why Zipf's Law holds true references [this article from PLOS](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005110),
which goes into much greater depth on this topic - and particularly, on the underlying psychlogical factors - than this short study
can hope to provide.

An expansion of this project could use a lemmatization tool (or similar) to conduct
text pre-processing before testing Zipf's Law. This might, theoretically, reduce
the extreme behavior of the graphs on either end of the x-axis, since there would be
fewer variations of words being treated as distinct words.

Thanks for checking out my work! Please feel free to [email me](scattana@nd.edu) with any questions
or comments.



