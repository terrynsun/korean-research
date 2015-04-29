CIS526: Language Research: Korean
=================================

## 1. Monolingual data (1 pt)

Downloaded the [Korean Wikipedia dumps](http://dumps.wikimedia.org/kowiki/).
Used BeautifulSoup with lxml (an XML parsing library) to extract to document
body text for each page. The resulting dump file contains all of the body text
for each Wikipedia page, including headings. Meta pages (lists of other pages)
are omitted. Basic Wikipedia formatting has been removed (text between braces is
removed; double brackets are removed to leave link text present, appropriately
handled if there is a `[[display|link]]`).

The original dump was 1.8G. I parsed 763,540 pages for about 3.3 million
lines at a total of 182M. The submitted file is about 51M.

* Python: `scrape.py`
* Data: `monolingual-data/wikipedia.txt.bz2`

## 2. Bilingual data (1 pt)

Data is taken from the Tanzil project compiling translations of the Quran. Two
files that are sentence-aligned (one per line). 93,540 lines.

Origin: http://opus.lingfil.uu.se/Tanzil.php
Citation:
 Jörg Tiedemann, 2012, Parallel Data, Tools and Interfaces in OPUS. In
 Proceedings of the 8th International Conference on Language Resources and
 Evaluation (LREC 2012)

* Korean: `bilingual-data/Tanzil.ko`
* English: `bilingual-data/Tanzil.en`

## 5. Language Identification (2 pts)

Discriminative Language ID system for Romanized Korean (since Hangeul is trivial to identify). Korean text is from The Chosun Ilbo [http://www.chosun.com/], a South Korea daily with circulation of over 1,800,000. Articles are written in Hangeul, so I used an online converter [http://www.lexilogos.com/keyboard/korean_conversion.htm] to generate Romanized text. English text comes from the Wikipedia article on South Korea [http://en.wikipedia.org/wiki/South_Korea].

Features are generated from `kor_pretrain.txt`, also taken from The Chosun Ilbo. The features are the 12-most-frequent 2-letter, 3-letter, and 4-letter sequences in the text. The classifier is a logistic ridge regression, fit to 60 percent of the data. The remaining 40 percent is set aside as a test set.

The classifier achieved 0.9912 accuracy, averaged across 10 trials. This high accuracy (together with the small amount of data used) indicates that Romanized Korean contains distinct letter sequences that make it easy to recognize.

Data is already prepared. To run the model:

`python languageIdMain.py`

Files:
* `generateData.py` - Use NLTK tokenizer to clean up raw data and pick out sentences.
* `generateFeatures.py` - Compute k-most-frequent letter sequences in pretrain data.
* `languageIdMain.py` - Generate features for train/test sentences, fit logistic regression and report accuracy.
* Data: `kor_pretrain`, `eng_raw`, `eng`, `kor_raw`, `kor`, `features`

## 6. Twitter data (2 pts)

Run the commands below to query for tweets within the bounding box of Korea:

`cd twitter-data/twitter-streamer/streamer`

`python streamer.py -f=place.full_name,created_at,user.name,coordinates.coordinates,text --locations="123.48,33.14,129.16,38.89" > korean_tweets`

* 100 Labeled Twitter Data: `twitter-data/korean_tweets`
	- 55 non-Korean tweets and 45 Korean tweets
	- each line consists of flag for Korean/non-Korean, Name of Location, Coordinates of Location, Tweet text

## 8. Bilingual dictionary (1 pt)

Wrote a online dictionary scraper with BeatifulSoup to query bab.la. The output
is a TSV file with the columns:

foreign word, english word, translation, part of speech, definition

The english corpus consisted of the 1000 most common words, as decided by [ESL
Desk](http://www.esldesk.com/vocabulary/words) (which had the most easily
copy-able list).

* Python: `dictionary/scrape.py`
* Dictionary: `dictionary/dict.tsv`
* Dictionary from A to Z: directly scrapped from the text dictionary data 
* Of [English Word - POS Tag - Meaning] format. Idioms (either noun or verbal phrases) do not have POS Tag. If there are more than one meanings, then it is separated either by semicolon or comma.
