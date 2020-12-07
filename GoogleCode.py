import re

s = editor.getText()
s = s.upper()

s = s.replace(".", "-")
s = s.replace("0", "O")
s = re.sub(r'[^A-Z0-9-\r\n]', r'', s)

sArray = s.splitlines()

linelist = []
duplist = []

 

out = ""
count = 0

for line in sArray:
    if line.strip():
        out = out + line + "\r\n"
        count = count+1
        if line in linelist:
            duplist.append(line)
        else:
            linelist.append(line)
            
        

print out

editor.setText(out)


# for code in codes:
#  if code.find("-") > 0:
#	outstr = outstr + code + "\r\n";
#	print(code);
# Inform the user that we've done it
# editor.setText(outstr)

msg = "Total: "+str(count) +  " \r\nRep Num:" + str(len(duplist)) 

if len(duplist) > 0:
    for dupitem in duplist:
        msg = msg + "\r\n" + dupitem
        


notepad.messageBox(msg, "Google Code", 0)
