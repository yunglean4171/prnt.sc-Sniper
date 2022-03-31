from os import mkdir, path
import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from string import ascii_lowercase
from random import choice
import lxml
from PIL import Image
import pytesseract
import shutil
from main import *

#pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe'
#^ Uncomment this line if youre using windows!

file_path = os.path.abspath(os.path.dirname(__file__))

def start(number):
    if path.exists(f"{file_path}/keywords.txt") & path.exists(f"{file_path}/imgs") & path.exists(f"{file_path}/hits"):
        sniping(number)
    elif not path.exists(f"{file_path}/imgs"):
        mkdir(f"{file_path}/imgs")
        print("imgs directory has been created")
        start()
    elif not path.exists(f"{file_path}/hits"):
        mkdir(f"{file_path}/hits")
        print("hits directory has been created")
        start(number)
    else:
        print("keywords.txt file doesnt exist creating one...")
        open(f"{file_path}/keywords.txt", "x")
        print("Key words txt file has been created put keywords into file and press ENTER to start sniping")
        input(inputterminal)
        sniping(number)

def sniping(number):
    urls = generate_urls(int(number))
    for url in urls:
	    load_url(url)

def readimg(path, imgname):
	img = Image.open(path+imgname)
	text = pytesseract.image_to_string(img)
	checkforhits(text, imgname)

def load_url(url):
	"""
	Scrapes the image URL from the webpage and sends the url to save_img() to be saved.
	"""
	path = f"{file_path}/imgs"
	file_ext = ".png"
	req = Request(url, headers={"User-Agent":"Mozilla/5.0"})
	webpage = urlopen(req).read()
	soup = BeautifulSoup(webpage, "lxml")
	img = soup.find("img", {"class":"no-click screenshot-image"}).get("src")
	if not img.startswith("https://image.prntscr.com/image/"):
		newurl = generate_urls(1)[0]
		return load_url(newurl)
	save_img(img, f"{url[-6:]}{file_ext}", f"{file_path}/imgs/")

def save_img(img, filename, path):
	"""
	Opens the image URL and saves the image.
	"""
	print(f"Loading <{filename}>...")
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding': 'none',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive'}
	try:
		req = Request(img, headers=hdr)
		webpage = urlopen(req).read()
		with open(path+filename, "wb") as f:
			f.write(webpage)
		print(f"Success.")
		readimg(path, filename)
	except:
		print(f"Image failed..")

def generate_urls(n):
	"""
	Generates a list of URLs by concatenating two random letters followed by four random numbers to the end of the URL prefix.
	"""
	prefix = "https://prnt.sc/"
	urls = []
	i = 0
	while i < n:
		chars = [choice(ascii_lowercase) for _ in range(2)]
		nums = [str(choice(range(10))) for _ in range(4)]
		img = "".join(chars+nums)
		url = f"{prefix}{img}"
		if url not in urls:
			urls.append(url)
			i += 1
	return urls

def checkforhits(imgtext, imgpath):
	keywords = open(f"{file_path}/keywords.txt", "r")
	Lines = keywords.readlines()
	for line in Lines:
		if line in imgtext:
			print(f"Hit! --> {line.strip()}\n")
			shutil.move(f"{file_path}/imgs/"+imgpath, f"{file_path}/hits/"+imgpath)
			break
