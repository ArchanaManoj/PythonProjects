import webbrowser
import os.path

pageTemplate = '''<!DOCTYPE html>
<html>
<head>
  <meta content="text/html; UTF-8" http-equiv="content-type">
  <title>Your Page</title>
</head>
<body>
{matter}
</body>
</html>
'''

def main(matter):
    inner = matter
    contents = pageTemplate.format(**locals())
    openPage(contents)

def pageCreate(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def openPage(webpageText, filename='Drill_72.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    
    pageCreate(webpageText, filename)
    webbrowser.open(os.path.abspath(filename)) 

#main()
