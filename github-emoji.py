# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:03:09 2020

@author: Jimit.Dholakia
"""


import requests
import os
import time
import urllib.parse

os.environ['TZ'] = 'Asia/Kolkata'
time.tzset()

url = os.getenv('GITHUB_API_URL', 'https://api.github.com') + '/emojis'

print('Emojis URL:', url)
r = requests.get(url)
x = r.json()
keys = list(x.keys())
#single_line = '|Icon|Code|' + '\n' + '|---|---|'
#complete_text = '|Icon|Code' * 3 + '|\n' + '|---|---'*3 + '|'

meta_info = '''<meta name="author" content="Jimit Dholakia">
<meta name="keywords" content="GitHub Markdown Emoji Cheatsheet">

<!-- HTML Meta Tags -->
<meta name="description" content="Complete list of GitHub Markdown Emoji Codes">

<!-- Google / Search Engine Tags -->
<meta itemprop="name" content="GitHub Markdown Cheatsheet">
<meta itemprop="description" content="Complete list of GitHub Markdown Emoji Codes">
<meta itemprop="image" content="meta_img.png">

<!-- Facebook Meta Tags -->
<meta property="og:url" content="https://jimit105.github.io/github-emoji-cheatsheet">
<meta property="og:type" content="website">
<meta property="og:title" content="GitHub Markdown Cheatsheet">
<meta property="og:description" content="Complete list of GitHub Markdown Emoji Codes">
<meta property="og:image" content="meta_img.png">

<!-- Twitter Meta Tags -->
<meta name="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="https://jimit105.github.io/github-emoji-cheatsheet/">
<meta name="twitter:title" content="GitHub Markdown Cheatsheet">
<meta name="twitter:description" content="Complete list of GitHub Markdown Emoji Codes">
<meta name="twitter:image" content="meta_img.png">
'''
current_time = time.strftime('%b %d, %Y %X %Z', time.localtime())
action_badge = '[![GitHub Emoji Update](https://github.com/jimit105/github-emoji-cheatsheet/workflows/GitHub%20Emoji%20Update/badge.svg?branch=master)](https://github.com/jimit105/github-emoji-cheatsheet/actions)'
header = '## GitHub Emoji Cheatsheet  \n\n' + action_badge + '\n\n'
complete_text = meta_info + header + '|Icon|Emoji Code|' + '\n' + '|---|---|' + '\n'

for key in keys:
    text = '|:' + key + ':|`:' + key + ':`|' + '\n'
    complete_text += text
    
with open('index.md', 'w') as f:
    f.write(complete_text)
    
print('Emoji Update Complete')
