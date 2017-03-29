import sys
import urllib2

def main(): 
	msrp = "https://azure.microsoft.com/en-us/pricing/details/virtual-machines/" + sys.argv[1] + "/"
	page = urllib2.urlopen(msrp)

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page)
	
	all_head=soup.find_all('h3')
	
	h = open(sys.argv[1] + ".txt", "w+")
	for head in all_head:
		print>>h, head		
	h.close()
	
if __name__ == "__main__":
	main()