import re

#FORMATTYPE.MAC
#FORMATTYPE.UNIX
notepad.setFormatType(FORMATTYPE.WIN)


s = editor.getText();
 
#editor.setText(s)



lines = s.split("\r\n")
#print(lines)
domainlist = []
finalDomainlist = []
outstr = ""

blackList = ["app-measurement.com","umeng.com","google","apple.com"]

#tmpstr contain a key in the blackList
def isInBlackList( tmpstr ):
   #skip all *.cn ,we will add .cn to avoid too many domins end with .cn to be added
   if tmpstr.endswith(".cn") == True:
	#print(tmpstr+" isInBlackList ") 
	return True
		
   for blackItem in blackList: 
	if blackItem in tmpstr: 
		#print(tmpstr+" isInBlackList ") 
		return True

   #print(tmpstr+" is not in BlackList ") 
   return False	
   
 


for line in lines:
  strsInLine = line.split(" ")
  for strL in strsInLine:
	if strL.endswith(".com") == True or strL.endswith(".cn") == True or strL.endswith(".net") == True or strL.endswith(".org") == True or strL.endswith(".edu") == True or strL.endswith(".org") == True:
		if strL not in domainlist:
			domainlist.append(strL)
			#print(strL)
            
  
#print(outstr)
# Inform the user that we've done it

dupCount = 0

for domain in domainlist:
	parts = domain.split(".")
	partsLen = len(parts)
	#print(parts)
	if partsLen >= 2:
		if parts[partsLen-2] != "":
			domain2part = parts[partsLen-2] +"." + parts[partsLen-1]
			#print(domain2part)
			if domain2part not in finalDomainlist:
				finalDomainlist.append(domain2part)
				print(domain2part + " add to finalDomainlist")
			else:
				print(domain2part + " is dupliate")
				dupCount += 1
			
fulloutstr = ""	
for outline in domainlist:
	fulloutstr = fulloutstr + outline + "\r\n"

blackCount = 0
for sss in finalDomainlist:
	if isInBlackList(sss) == False:
		outstr = outstr + sss + "\r\n"
	else:
		print(sss + " is In BlackList")
		blackCount += 1

print("====================blackCount:dupCount==========================")
print(blackCount)
print(dupCount)				
print("================================================================")	
print(outstr)	
notepad.messageBox("complete", "domainlist", 0)