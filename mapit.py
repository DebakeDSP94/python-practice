import webbrowser
import sys
import pyperclip

sys.argv  # ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
# This opens a Google Maps page in the default browser to the address you just
# copied to the clipboard. For example, if you copied the address 870 Valencia St.
# in San Francisco to the clipboard, running this program will open Google Maps
# to that address. Or if you ran this program without first copying an address,
# it would use the address you hardcoded into the program.
