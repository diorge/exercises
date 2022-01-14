# https://www.hackerrank.com/challenges/detect-html-links/

import re

line_count = int(input())
lines = [input() for _ in range(line_count)]
data = "\n".join(lines)

exp = r"""<a ([^h]*)href="(?P<link>[^"]*)"([^>]*)>(<[^>]+>)*(?P<name>[^<]*)"""
matches = re.finditer(exp, data)

for match in matches:
    print(match.group("link").strip(), ",", match.group("name").strip(), sep="")
