import os
import time
import requests as req
from datetime import datetime


name = str(datetime.now())[-4:-1] + "_execute.py"



def log(txt):
	f = open("log.data", 'a', encoding='utf-8')
	f.write(str(datetime.now()) + " | " + str(txt) + "\n")
	f.close()


def get_fresh_file(link):
	global name
	log("[INFO] Down link handled!")

	try:
		r = req.get(link).text
	except Exception as e:
		log("[ERR] get_fresh_file() > Can't download file, cuz: \\\\\\" + str(e) + "\\\\\\")

	try:
		f = open(name, 'w', encoding='utf-8')
		f.write(r)
		f.close()

		return True
	except Exception as e:
		log("[ERR] get_fresh_file() > Can't write file, cuz: \\\\\\" + str(e) + "\\\\\\")

	return False


def get_fresh_link():
	global CODE

	try:
		r = req.get("https://raw.githubusercontent.com/homiinside/get_code/main/link").text

		c_spos = r.find("#$CODE#")
		c_epos = r.find("$#CODE")

		CODE = str(r[c_spos+len("#$CODE#"):c_epos])

		# if CODE == 
		
		spos = r.find("#$LINK#")
		epos = r.find("$#LINK")

		glink = r[spos+len("#$LINK#"):epos]

		log("[INFO] Down link: " + glink)
		if not get_fresh_file(glink):
			return False
		return True
	except Exception as e:
		log("[ERR] get_fresh_link() > Can't get down link, cuz: \\\\\\" + str(e) + "\\\\\\")
		return False



log("\n\n[INFO] Program started! \n")


log("[INFO] Trying to get down link...")
if not get_fresh_link():
	log("[ERR] Bad time... See you later!")
	time.sleep(1000)
	os.system("python " + __file__)

try:
	f = open("CODE.data", 'r')
	cres = f.read()
	f.close()

	if cres == CODE:
		log("[INFO] Codes are same! Exit...")
		exit()
except FileNotFoundError:
	log("[INFO] CODE file doesn't exist!")
	
log("[INFO] All is done, file is here! Starting...")

f = open("CODE.data", 'w')
f.write(CODE)
f.close()

try:
	log("\n--- NEXT DATA WILL WRITE EXEC PROGRAM ---")
	os.system("python " + name)
	log("[INFO] All is done, work end!")
except Exception as e:
	log("[ERR] Can't start file, cuz: \\\\\\" + str(e) + "\\\\\\")
	time.sleep(100)
	os.system("python " + __file__)
