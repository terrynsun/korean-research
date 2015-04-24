#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import sys


re_pos   = re.compile("\{(.*)\}")
re_mark  = re.compile("\[(.*)\]")
re_defn  = re.compile("\((.*)\)")
re_also  = re.compile(" also:")
re_comma = re.compile(",")
source   = "bab.la"

def if_match(regex, s):
    re = regex.search(s)
    if re:
        return re.group(1)
    else:
        return ""

#    The foreign word
#    Its English translation
#    the source of the translation
#    (optional) an example sentence that uses the word
#    (optional) its part of speech
#    (optional) a definition

def parse_entry(entries, out):
    #print(entry)
    en = entries[0]
    en_w = en.string
    en_meta = "".join(en.next_sibling.strings)
    ko = entries[1]
    ko_w = ko.string

    pos  = if_match(re_pos, en_meta)
    mark = if_match(re_mark, en_meta)
    defn = if_match(re_defn, en_meta)
    defn = re_also.sub("", defn)
    full_defn = "%s; %s" % (mark, defn) if defn else mark

    ko_meta = "".join(ko.next_sibling.strings)
    out.write("%s\t%s\t%s\t%s\t%s\t%s\n" %
                (ko_w, en_w, source, "", pos, full_defn))

def scrape_word(word, out):
    url = "http://en.bab.la/dictionary/english-korean/%s" % word
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html)
    results = soup.find_all(attrs={"class": "result-link"})
    length = len(results)
    i = 0
    while i < length:
        if not results[i].next_sibling:
            i += 1
        else:
            parse_entry(results[i:i+2], out)
            i += 2

if __name__ == '__main__':
    out = open("dict.txt", 'w')
    fname = "eng_list"
    for i, w in enumerate(open(fname)):
        sys.stdout.write("[2K\r%d: %s" % (i, w.strip()))
        scrape_word(w, out)
