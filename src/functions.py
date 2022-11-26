import win32clipboard
from datetime import datetime

#YOUR FILEPATH HERE. NOTE: BACK SLASHES ("\") MUST BE TURNED INTO FRONT SLASHES; IF NOT, THE PROGRAM WILL NOT RUN.
filepath = ""

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