# coding:utf-8
import re, sys, pyperclip

url_org = ''
argv_len = len(sys.argv)
if argv_len == 1:
    url_org = str(pyperclip.paste())

elif argv_len == 2:
    url_org = str(sys.argv[1])

pattern   = r'^http(s)?://(www\.)?amazon\.co\.jp/.+/dp/([a-zA-Z0-9]+).+$'
repattern = r'https://www.amazon.co.jp/dp/\3'
url_mod = re.sub(pattern, repattern, url_org)
pyperclip.copy(url_mod)
print (url_mod)