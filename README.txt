This repository contains two Python scripts for use with the output of CorpusSearch 2 (https://corpussearch.sourceforge.net/).

I'm a researcher, not a programmer; these scripts are poorly commented (where they commented at all), may not work as intended on your device, and I can't commit to providing support for them.

***

out2csv2.py takes a CorpusSearch 2 .out file and produces a comma-delimited CSV file of the numerical results (e.g. hits/tokens/total). Usage is:

python out2csv2.py <output_file.out>

This should work with any CorpusSearch-compatible corpus.

***

solidate.py is a much more niche script, designed specifically for use with the PPCEME (https://www.ling.upenn.edu/hist-corpora/PPCEME-RELEASE-3/index.html). It takes the output of out2csv2 and outputs a new file in which hits/tokens/total for individual texts are summed. Usage is:

python solidate.py <file.csv>

This is needed because the PPCEME contains three subcorpora: h (Helsinki), p1 (first Penn supplement), and p2 (second Penn supplement). In many cases, there is a sample from the same text from two or more subcorpora. For instance, the New Testament (authnew-e2) has samples in all three subcorpora (authnew-e2-h; authnew-e2-p1; authnew-e2-p2). It mostly doesn't make sense to treat these as separate datapoints, so the script sums each of hits/tokens/total in such cases. For instance, you might have the following situation:

authnew-e2-h: 4 hits
authnew-e2-p1: 5 hits
authnew-e2-p2: 2 hits

The script would give you 11 hits in total for authnew-e2, and similarly for tokens and total.

Note that there are some circumstances in which it makes sense not to do this. For instance, cromwell-e1-h is dated 1537, whereas cromwell-e1-p1 and cromwell-e1-p2 are dated circa 1530. If these date differences are important to your research question, either don't use solidate.py or use it and then restore the original numbers for these texts.