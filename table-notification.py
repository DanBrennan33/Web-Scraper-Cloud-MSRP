import sys
import urllib2
import itertools

def main(): 
	msrp = "https://azure.microsoft.com/en-us/pricing/details/virtual-machines/" + sys.argv[1] + "/"
	page = urllib2.urlopen(msrp)
 
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page)
	
	flag = 0

	all_head=soup.find_all('h3')
	
	with open(sys.argv[1] + ".txt") as f:
		if len(all_head) > sum(1 for _ in f):
			flag = 1
			
	sys.exit(flag)
			
			
if __name__ == "__main__":
	main()

