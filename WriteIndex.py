import os

folders = os.listdir()
folders.remove('.git')

outHtml = '<!DOCTYPE html>\
<html lang="en">\
<head>\
  <title>AR Anims</title>\
</head>\
<body>\
  '

#link dirs


outHtml = outHtml + '<h1> this is a test <h1>\
    </body>\
    </html>'

f = open("index.html", 'wt')
f.write(outHtml)
f.close()

f=open("index.html", "rt")
print(f.read())
f.close()