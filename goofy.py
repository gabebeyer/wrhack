import urllib2
import urllib
import httplib
import re 
import subprocess
import os

string_input = raw_input("Enter String!")
myList = string_input.split(" ")
GLOBAL_URL = "http://www.wordreference.com"


def urlOpener(word):
	url = (GLOBAL_URL + "/es/translation.asp?tranword=" + word)
	httplib.HTTPConnection.debuglevel = 1           
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')] 
	response = str(opener.open(url).read())
	return response

def getFiles():
	inc = 0
	for word in myList:
		html_source = urlOpener(word)
		match = re.findall(r'\/audio\/.*\.mp3', str(html_source))	
		try:
			matchString = match[0]
		except:
			print ("Word Not Found!!!")
		matchString = matchString.split(" ")[0]
		if matchString.endswith("'"):
		    matchString = matchString[:-1]
		print(word + " ---> " + matchString)
		urllib.urlretrieve (GLOBAL_URL + matchString, str(inc) + ".mp3")
		inc += 1

def playAudio():
	currentDIR = str(os.getcwd())
	for i in os.listdir(os.getcwd()):
		if i.endswith(".mp3"):
			audio_file = (currentDIR + "/" + i)
			print audio_file

			if os.name()[0] == "Linux":
		
				subprocess.call(["avplay", audio_file])
			else:
				
				subprocess.call(["afplay", audio_fil])
								    
	  		os.remove(audio_file)

if __name__ == "__main__":
    getFiles()
    playAudio()
