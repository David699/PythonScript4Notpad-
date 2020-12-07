import re
s = editor.getText();
s = s.upper();
s = s.replace("1","I");
s = s.replace(" ","");
s = s.replace(".","-");
#editor.setText(s)



codes = s.split("\r\n")
print(codes)

outstr = ""

for code in codes:
  if code.find("-") > 0:
	aaa = re.sub(r'[^A-Z0-9-\r\n]', r'', code)
	outstr = outstr + aaa + "\r\n";
	print(code);
# Inform the user that we've done it
editor.setText(outstr)
notepad.messageBox("complete", "steam code", 0)