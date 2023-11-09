This repository contains four Python scripts for use with CorpusSearch 2 (https://corpussearch.sourceforge.net/).

I'm a researcher, not a programmer; these scripts are poorly commented (where they commented at all), may not work as intended on your device, and I can't commit to providing support for them.

***

out2csv2.py takes a CorpusSearch 2 .out file and produces a comma-delimited CSV file of the numerical results (e.g. hits/tokens/total). Usage is:

python out2csv2.py <output_file.out>

This should work with any CorpusSearch-compatible corpus.

***

tokenno.py takes a .psd file and looks for IDs of the format

foo.TokenNumber.bar

It will output a copy of the .psd file in which all these IDs are numbered in ascending order by token: the first one will be foo.1.bar, the second foo.2.bar, etc. Usage is:

python tokenno.py <file.psd>

***

wordcount.py counts the number of words (in the original corpus text!) in a .psd file. It does so by counting anything that looks like a terminal node, then counting more specific things. Usage is:

python wordcount.py <file.psd>

Output looks like this:

"Done. Found 917 terminals, of which 4 were CODE, 41 were token IDs, 112 were punctuation, and 88 were null, leaving 672 words. We also found 27 lemmatized words."

The numbers for CODE and ID are the numbers of terminals with the tags CODE and ID, respectively. The numbers for punctuation are the numbers of terminals with a one-character tag that isn't whitespace (\s) or a word character (\w). The numbers for null elements are the numbers of terminals that either a) begin with an asterisk * or b) are 0, regardless of tag. The "leaving X words" is derived by removing everything from the list of terminals that isn't in the lists of CODE, ID, punctuation, or null elements, and taking the length of that list. The number of "lemmatized words" is the number of terminals containing a hyphen (yes, this is pretty stupid).

***

solidate2.py is a much more niche script, designed specifically for use with the PPCEME (https://www.ling.upenn.edu/hist-corpora/PPCEME-RELEASE-3/index.html). It takes the output of out2csv2 and outputs a new file in which hits/tokens/total for individual texts are summed. Usage is:

python solidate2.py <file.csv>

This is needed because the PPCEME contains three subcorpora: h (Helsinki), p1 (first Penn supplement), and p2 (second Penn supplement). In many cases, there is a sample from the same text from two or more subcorpora. For instance, the New Testament (authnew-e2) has samples in all three subcorpora (authnew-e2-h; authnew-e2-p1; authnew-e2-p2). It mostly doesn't make sense to treat these as separate datapoints, so the script sums each of hits/tokens/total in such cases. For instance, you might have the following situation:

authnew-e2-h: 4 hits
authnew-e2-p1: 5 hits
authnew-e2-p2: 2 hits

The script would give you 11 hits in total for authnew-e2, and similarly for tokens and total.

Note that there are some circumstances in which it makes sense not to do this. For instance, cromwell-e1-h is dated 1537, whereas cromwell-e1-p1 and cromwell-e1-p2 are dated circa 1530. The first version of solidate.py would combine these blindly. solidate2.py (2023) is designed not to do this.
