import re
import sys
import os
finalfile = []
newfile = []
repchar = "$"
if (len(sys.argv) == 1):
	print("""usage: formatfix.py filename.py [options]
  options:
    -t, --argument     Replaces all with tabs (default)
    -s, --argument     Replaces all with spaces""")
if len(sys.argv) == 3:
	if sys.argv[2] == "-t":
		repchar = '\t'
	elif sys.argv[2] == "-s":
		repchar = '    '
else:
	repchar = '\t'
with open(sys.argv[1], "r") as f:
	for line in f:
		newfile.append(line)
for l in newfile:
	finalfile.append(re.sub(r'^[ \t]+', lambda m:repchar*len(m.group()), l.replace("    ", "\t"), flags=re.M))
with open(sys.argv[1][:-3] + "_fixed.py", "w") as f:
	for lne in finalfile:
		f.write(lne)

os.remove(sys.argv[1])
os.rename(sys.argv[1][:-3] + "_fixed.py",sys.argv[1])
