# regex practice 11/08/2023
# Extract phone numbers and email addresses from clipboard text - replace them in your clipboard    

import re
import pyperclip

# Create a regex for phone numbers
pnRegex = re.compile(r'''
(\d{3}|(\d{3}))? # area code
(\s*|-|\.) # separator
(\d{3}) # first 3 digits of pn
(\s*|-|\.) # separator
(\d{4}) # last 4 digits of pn
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension (optional
''' , re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@                 # @
[a-zA-Z0-9.-]+   # domain
(\.[a-zA-z]{2,4})+ # top-level domain
)''' , re.VERBOSE)


clipboard = str(pyperclip.paste())
matches = []

for groups in pnRegex.findall(clipboard):
    pn = '-'.join([groups[0],groups[3],groups[5]])
    if groups[8] != '':
        pn += ' x' + groups[8]
    matches.append(pn)

for groups in emailRegex.findall(clipboard):
    matches.append(groups[0])

if len(matches) > 0:    
    newClipboard = '\n'.join(matches)
    pyperclip.copy(newClipboard)
    print("Copied to clipboard: ")
    print(newClipboard)
else:
    print("No phone numbers or emails found")
