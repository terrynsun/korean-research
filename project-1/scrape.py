#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import html
import re
import sys


re_page_start = re.compile("\<page\>")
re_page_end   = re.compile("\</page\>")
pagec = 0

re_braces   = re.compile("\{(.*)\}", re.S)
re_brackets = re.compile("\[\[(.*?)\]\]", re.S)
re_quote    = re.compile(r"'''")
re_single_brackets = re.compile("\[(.*?)\]", re.S)
def replace_brackets(result):
    inner = result.group(1)
    if '|' in result.group(0):
        pipe = re.search("(.*)\|(.*)", inner, re.S)
        return pipe.group(2)
    else:
        return inner

def clean(text):
    text = re_quote.sub('', text)
    if re_braces.search(text):
        text = re_braces.sub("", text)
    brackets = re_brackets.search(text)
    if brackets:
        while re_brackets.search(text):
            a = re_brackets.search(text)
            new_text = re.sub("\[\[(.*?)\]\]", replace_brackets, text, re.S)
            if new_text == text:
                break
            else:
                text = new_text
    text = re_single_brackets.sub('', text)
    return text

def dump_page(page, out):
    page = html.unescape(page)
    soup = BeautifulSoup(page, "xml")
    try:
        if ":" in soup.title.string:
            return
        print("%d: %s" % (pagec, soup.title.string))
        for tag in soup.revision:
            #print (tag.name)
            if tag.name == "text":
                if tag.sha1:
                    tag.sha1.decompose()
                out.write(clean(tag.get_text()))
    except: # disregard all errors
        pass

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Need args")
        exit(1)

    xml = open(sys.argv[1], 'r')
    out = open("wikipedia.txt", 'w')
    page = ""
    for line in xml:
        page += line
        if re.search(re_page_end, line):
            pagec += 1
            dump_page(page, out)
            page = ""
