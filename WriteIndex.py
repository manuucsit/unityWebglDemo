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

# link dirs
for labels in folders:
    outHtml = outHtml + '<a href="manuucsit.github.io/unityWebglDemo/' + labels + '">'+labels+'</a><br>'

outHtml = outHtml + '</body></html>'

f = open("index.html", 'wt')
f.write(outHtml)
f.close()

f = open("index.html", "rt")
print(f.read())
f.close()
