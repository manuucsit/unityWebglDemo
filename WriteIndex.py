import os

folders = os.listdir()

for x in folders:
  if x.__contains__('.'):
    folders.remove(x)

folders.remove('.github')

outHtml = '<!DOCTYPE html>\
<html lang="en">\
<head>\
  <title>AR Anims</title>\
</head>\
<body>\
  '

# link dirs
for labels in folders:
    outHtml = outHtml + '<a href="' + labels + '">'+labels+'</a><br>'

outHtml = outHtml + '</body></html>'

f = open("index.html", 'wt')
f.write(outHtml)
f.close()

f = open("index.html", "rt")
print(f.read())
f.close()
