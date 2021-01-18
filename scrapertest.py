#!/usr/bin/python3

from urllib.request import urlopen
import re

url = "http://158.69.76.135/level1.php"
page = urlopen(url)
html = page.read().decode("utf-8")
pattern = "<form>*?</form>"
match_results = re.search(pattern, html, re.IGNORECASE)
form = match_results.group()
form = re.sub("<.*?>", "", form)
print(form)
