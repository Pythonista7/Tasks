import urllib.request
from bs4 import BeautifulSoup


class Scraper():
    """
    My module
    """
    def __init__(self):
        self.url="https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9"
        self.page=urllib.request.Request(self.url,headers={'User-Agent': 'Mozilla/5.0'}) 
        self.file_name="datfile.csv"
        
    def get(self):
        infile=urllib.request.urlopen(self.page).read()
        soup = BeautifulSoup(infile, 'html.parser')
        
        table=soup.find('table',attrs={"class":"tbldata14 bdrtpg"})
        if table==None:
            print("Failed")
        
        f=open(self.file_name,"w")
        
        for row in table.find_all('tr'):
            line=[]
            for col in row.find_all('td',attrs={"class":["bl_12","brdrgtgry"]}):
                line.append(BeautifulSoup.get_text(col).strip().replace(",",""))
                if "\n" in line[0]:    
                    line[0]=line[0][:line[0].index("\n")]
                if(len(line)==0):
                    break
            f.write(','.join(line) + "\n")
        
        f.close()
        return self.file_name
#s=Scraper()
#s.get()