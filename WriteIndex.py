import os

folders = []

listDirs = os.listdir()

for x in listDirs:
  if os.path.isdir(x) and x[0] != '.':
    folders.append(x)

outHtml = '<!DOCTYPE html>\n\
<html lang="en">\n\
<head>\n\
  <title>AR Anims</title>\n\
</head>\n\
<body>\n\
  '

# link dirs
for labels in folders:
    outHtml = outHtml + '\t<a href="' + labels + '/index.html">'+labels+'</a><br>\n'

outHtml = outHtml + '</body>\n</html>'

f = open("index.html", 'wt')
f.write(outHtml)
f.close()

f = open("index.html", "rt")
print(f.read())
f.close()

os.system('git add index.html')
os.system('git commit -m "[Triggers] Index" --no-verify')