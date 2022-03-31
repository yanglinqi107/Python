from urllib import parse

s = '\xa0400'
s = s.encode('unicode_escape')
print(s)

ss = s.decode('utf8').replace('\\x', '%')
print(ss)

un = parse.unquote(ss)
print(un)

s='wer\xa040 0'
print(s)