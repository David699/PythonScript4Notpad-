import re
s = editor.getText();
s = s.upper();
s = s.replace("]","J");
s = s.replace("&","8");
s = s.replace(" ","");
#editor.setText(s)



codes = s.split("\r\n")
print(codes)

outstr = ""

for code in codes:
  if code.startswith("X") == True:
	aaa = re.sub(r'[^A-Z0-9\r\n]', r'', code)
	outstr = outstr + aaa + "\r\n";
	print(code);
  
#print(outstr)
# Inform the user that we've done it
editor.setText(outstr)
notepad.messageBox("finish", "Itunes code", 0)