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

styles="a{\
    background-color: rgb(202, 229, 243);\
    border-radius: 5px;\
    display: block;\
    margin-top: 3px;\
    margin-bottom: -15px;\
    padding:10px;\
    text-decoration: none;\
    color: rgb(0, 0, 0);\
    font-family: Arial, Helvetica, sans-serif;\
    font-size: large;\
}\
body{\
    background-color: rgb(31, 63, 82);\
}"

outHtml += styles

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