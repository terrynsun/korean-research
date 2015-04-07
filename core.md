# Core Requirement

Korean is a SOV (subject-object-verb) language. The relative order of words in a sentence is fixed, but both the subject and object can be dropped (and become implied) from a sentence.
너 (you) 밥 (rice) 먹었어 (ate)?

Adjectives are pre-pended to the noun that they modify, and can be appended in series.
빨간 (red) 사과 (apple)

The modern system of classifying Korean words uses 9 parts of speech. Words do not have grammatical gender.

Substantitives (category of nouns) are subdivided into nouns, pronouns, and numerals. Nouns are made plural with a suffix 들 (*deul*), but only when the plurality of the modified noun is not contextually known.

There are two sets of numerals, one native Korean and one Sino-Korean (based on the Chinese numerals). There is a distinction made between the two systems, where each countable should be expressed with only one of the two systems.

TODO: "How many cases and/or genders does the language have?"

Verbs are inflected for tense. Verbs are separated into processual verbs (action verbs) and descriptive verbs (eg. 붉다 *bukda*, "to be red").

Both verbs and nouns inflect for politeness.

(Not sure what to say about these examples. We should tag each word.)
야, 밥 먹어. (Casual)
진지 잡수세요. (Polite)

너 밥 먹고있어? (Eating meal)
너 밥 먹었어? (Ate a meal)

밥 먹었어 (Spoken language)
밥 먹었다 (Written language)

Pronouns are differentiated by level of politeness. There are no formal 3rd person pronouns used. Instead, level of formality is implied by context in the sentence.

|     | Singular                             | Plural                       |
|-----|--------------------------------------|------------------------------|
| 1st | 나 (*na*), 저 (*jeo*)                | 우리 (*uri*), 저희 *jeohui*) |
| 2nd | 너 (*neo*)                           | 너희 (*neohui*)              |
| 3rd | 그 (*geu*, he)/그녀 (*geunyeo*, she) | 그들 (*geudeul*)             |

## Speakers

Korean is the official language of South and North Korean, and is worldwide
spoken by about 80 million people. Of those, about 51 million reside in South
Korea, and about 7 million overseas (2013). 80% of Korean expatriates live in
China, the US, and Japan.

## Script, publications

Korean uses an alphabet known as Hangul. Hangul has 24 letter grouped into blocks (*han*), which each represent a syllable. For example, the block 한 (*han*) is a composition of the letters ㅎ (h), ㅏ (a), ㄴ (n). Internally, the letters in a block are ordered left to right and top to bottom, and sequences of blocks are written left-to-right.

There is approximately a 100% literacy rate (reading/writing) within South Korea. The country has many major publications, including books, newspapers, journals, websites, etc. There are no major impediments for literacy.

## MT Systems
Most Machine Translation systems have systems in Korean (e.g., Google, Bing, and Korean local web provider Naver). 
The following paragrah is an excerpt from Wikipedia's article on Computer Science:
"There is a sub-field of computer science applications can be divided into purely theoretical and practical skills in the field of computer systems running on your computer. It is calculated as the basic properties and also some theoretical calculations to study the complexity of the problem is very abstract, and other computer graphics and it focuses on real-world applications. Another sub-field focuses on the calculation execution. For example, programming language theory and study the approach of calculation described above, the computer program itself study investigating different aspects of using the programming language and the complex system, human-computer interaction with the computer to calculate a useful and humans emphasis to easily create a universally accessible."

## NLP Tools in Korean
There are exists many NLP tools that allow people to computationally analyze Korean language. Penn has Korean NLP group which consists of three main projects: Korean XTAG, Korean Treebank, and Korean/English Machine Translation (http://www.cis.upenn.edu/~xtag/koreantag/). Korean XTAG is an on-going project attempting to develop a Korean grammar using Feature-Based Lexicalized Tree Adjoining Grammar (LTAG) formalism. A Korean Treebank is a corpus annotated with morphological and syntactic information, similar to what we have seen in other tree banks. Korean Corpus is also available, which is retrieved mostly from the texts of military language training manuals. Along with Korean Corpus, the Part-of-speech tagging method is available.

Also, there is a Korean NLP package written in Python, called "KoNLP." (http://dm.snu.ac.kr/~epark/docs/2014-10-10-hclt.pdf) It provides the basic functionality of NLP analysis such as POS tagging, and the structure of the package resembles that of NLTK package. 

