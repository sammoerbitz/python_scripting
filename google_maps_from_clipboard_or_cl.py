# "Automate the Boring Stuff" - Al Sweigart practice 
import webbrowser, sys, pyperclip

if(sys.argv > 0):
    addr = argv[1:]
else:
    addr = pyperclip.paste()
    

webbrowser.open()