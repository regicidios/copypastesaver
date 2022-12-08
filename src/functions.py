import win32clipboard
import os
from datetime import datetime

filepath = os.path.expanduser("~/Desktop")

def getclipboard():
    try:
        win32clipboard.OpenClipboard()
        clipboardtext = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return clipboardtext
    except TypeError:
        return "None"

def filemake():
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d-%H-%M-%S")
    textfile = open('{}/copypaste/{}.txt'.format(filepath, filename), 'w')
    textfile.write(getclipboard())