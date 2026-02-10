import requests
import os

url = os.getenv('GITHUB_API_URL', 'https://api.github.com') + '/emojis'

print('Emojis URL:', url)
r = requests.get(url)
r.raise_for_status()

emojis = r.json()

# Jekyll front matter
front_matter = '''---
layout: default
title: GitHub Emoji Cheatsheet
---

'''

action_badge = '[![GitHub Emoji Update](https://github.com/jimit105/github-emoji-cheatsheet/workflows/GitHub%20Emoji%20Update/badge.svg?branch=master)](https://github.com/jimit105/github-emoji-cheatsheet/actions)'
header = f'## GitHub Emoji Cheatsheet\n\n{action_badge}\n\n'
table = '|Icon|Emoji Code|\n|---|---|\n'

for key in emojis.keys():
    table += f'|:{key}:|`:{key}:`|\n'

with open('index.md', 'w', encoding='utf-8') as f:
    f.write(front_matter + header + table)

print('Emoji Update Complete')
