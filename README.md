# zipfs-law
Hypothesis testing of Zipf's Law for natural and unnatural languages (NLP SP19)

Contents

_____



**Introduction**

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



**Part One: Zipf's Law for Natural Language (English)**

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

From **figure 1** (below), it is clear all five English texts confirm Zipf's Law
(with only slight deviations from the linear relationship on the extreme ends of
the x-axis, as discussed previously).





