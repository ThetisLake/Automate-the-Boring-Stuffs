import webbrowser, sys, pyperclip

#
sys.argv #['mapit.py','870','Valencia','St.']

# Check if command line arguments were passed
if len(sys.argv)>1:
    #['mapit.py','870','Valencia','St.'] -> '870 Valencia St.'      
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#Open designated website         
webbrowser.open(r'http://google.com/maps/place/'+address)    
# Test by coping below
# 780 Tolmie Ave
