import os

folders = os.listdir()

for x in folders:
  if '.' in x:
    folders.remove(x)

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

os.system('git add index.html')
os.system('git commit -m "[Triggers] Index" --no-verify')