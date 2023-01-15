from bs4 import BeautifulSoup as btu
import requests as req 
import time 
import sys 
class TNProcject():
	def __init__(self):
		self.urlThread  = "https://threatpost.com/"
		self.urlHelp = "https://www.helpnetsecurity.com/view/news/"
		self.urlThe = "https://thehackernews.com/?m=1"
		self.urlVetur = "https://venturebeat.com/feed/"
		self.urlCom = "https://www.computerworld.com/index.rss"
		self.urlNal = "https://tech.co/feed"
		self.urlNeo = "https://www.neowin.net/news/rss/"
		self.urlRadar = "https://www.techradar.com/rss"
		self.urlNex = "https://thenextweb.com/feed"
		self.urlHigh = ["https://www.techrepublic.com/rssfeeds/topic/wearable-tech/","https://www.techrepublic.com/rssfeeds/topic/virtualization/","https://www.techrepublic.com/rssfeeds/topic/software/", "https://www.techrepublic.com/rssfeeds/topic/samsung/","https://www.techrepublic.com/rssfeeds/topic/networking/","https://www.techrepublic.com/rssfeeds/topic/mobile/","https://www.techrepublic.com/rssfeeds/topic/microsoft/","https://www.techrepublic.com/rssfeeds/topic/internet/","https://www.techrepublic.com/rssfeeds/topic/hardware/","https://www.techrepublic.com/rssfeeds/topic/google/","https://www.techrepublic.com/rssfeeds/topic/android/", "https://www.techrepublic.com/rssfeeds/topic/artificial-intelligence/","https://www.techrepublic.com/rssfeeds/topic/analyst-insights/"]
		
		self.headers = {"User-Agnet":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25"}
		
	def appThread(self):
			istekNewsThread  = req.get(self.urlThread)
			htmlNewsThread = istekNewsThread.text
			soupNewsThread = btu(htmlNewsThread, "html.parser")
			divNewsThread = soupNewsThread.find_all("figure")			
			for iNewsThread in divNewsThread:
				linkThread = iNewsThread.find("a").get('href') 
				resimNewsThread= iNewsThread.find("a").find("img").get("src")
				requests__Thread = req.get(linkThread)
				htmlNewsThread = requests__Thread.text
				soupNewsThread = btu(htmlNewsThread, 'html.parser')
				TitleNewsThread= soupNewsThread.find("h1",{"class":"c-article__title"}).text
				contentThread = soupNewsThread.find_all("div",{"class":"c-article__content js-reading-content"})
				try:
					DataTimeNewsThread = soupNewsThread.find("time").text
				except:
					pass
				ContentEndThread = ' '.join(e.text for p in contentThread for e in p.findAll(text=True))
				data= {
				"title":TitleNewsThread,
				"link":linkThread,
				"resim":resimNewsThread,
				"date":DataTimeNewsThread,
				"text":ContentEndThread,
				}
				print(data)
				time.sleep(20)
	def appHelp(self):
		istekNewsHelp= req.get(self.urlHelp, headers=self.headers)
		htmlNewsHelp = istekNewsHelp.text
		soupNewsHelp = btu(htmlNewsHelp, "html.parser")
		divNewsHelp = soupNewsHelp.find_all("article", {"class":"entry-preview entry-variant-A"})
		#DivNewsHelp => Linklerin bulundugu class 
		for iNewsHelp in divNewsHelp:
			linkNewsHelp = iNewsHelp.find("a").get("href") # Link 
			resimNewsHelp = iNewsHelp.find("div",{'class':"entry-preview__media"}).find("a").find("img").get("src")
			istek_2NewsHelp = req.get(linkNewsHelp)
			html_2NewsHelp = istek_2NewsHelp.text
			soup_2NewsHelp = btu(html_2NewsHelp, "html.parser")
			timeNewsHelp = soup_2NewsHelp.find("time").text #DataTime
			contentNewsHelp = soup_2NewsHelp.find_all("div",{"class":"entry-content"}) # Content
			contentNewsHelp2 = soup_2NewsHelp.find_all("p") # Example Content 
			TitleNewsHelp = soup_2NewsHelp.find("h1", class_="entry-title").text # Title
			ContentEndHelp = ' '.join(w_3.text for w_2 in contentNewsHelp for w_3 in w_2.findAll(text=True))
			dataNewsHelp= {
				"title":TitleNewsHelp,
				"link":linkNewsHelp,
				"resim":resimNewsHelp,
				"date":timeNewsHelp,
				"icerik":ContentEndHelp
				}
	def appThe(self):
				istekNewsThe = req.get(self.urlThe)
				htmlNewsThe= istekNewsThe.text
				soupNewsThe = btu(htmlNewsThe, "lxml")
				divNewsThe = soupNewsThe.find_all("div",{"class":"body-post clear"})
				for iNewsThe in divNewsThe:
					linkNewsThe = iNewsThe.find("a",{"class":"story-link"}).get("href")
					istek2NewsThe = req.get(linkNewsThe)
					html2NewsThe = istek2NewsThe.text
					soup2NewsThe = btu(html2NewsThe, "lxml")
					titleNewsThe = soup2NewsThe.find("h1",{"class":"story-title"}).text # Title
					DateNewsThe = soup2NewsThe.find("span" ,{"class":"author"}).text # Date 
					resimNewsThe = soup2NewsThe.find("div",{"class":"articlebody clear cf"}).find("div",{"class":"separator"}).find("a").get("href")
					contentNewsThe = soup2NewsThe.find_all("p") 
					ContentEndNewsThe = ' '.join(NewsPageText.text for The in contentNewsThe for NewsPageText in The.findAll(text=True)) # Content
					dataNewsThe= {"title":titleNewsThe,"link":linkNewsThe,"resim":resimNewsThe,"date":DateNewsThe,"icerik":ContentEndNewsThe}
				
					
					
					
	def appVetur(self):
		istekNewsVetur = req.get(self.urlVetur)
		htmlNewsVetur = istekNewsVetur.text
		soupNewsVetur = btu(htmlNewsVetur, features="xml")
		linkNewsVetur = soupNewsVetur.find_all("link")[3:]
		for iNewsVetur in linkNewsVetur:
				__linkNewsVetur = iNewsVetur.text
				__istekNewsVetur = req.get(__linkNewsVetur)
				__htmlNewsVetur = __istekNewsVetur.text
				__soupNewsVetur = btu(__htmlNewsVetur, "lxml")
				titleNewsVetur = __soupNewsVetur.find("div",{"class":"Article__header-top"}).find("h1").text
				timeNewsVetur = __soupNewsVetur.find("time").text
				imgNewsVetur = __soupNewsVetur.find("img").get("src")
				contentNewsVetur = __soupNewsVetur.find("div",{"class":"article-content"}).text
				dataNewsVetur = {
				"title":titleNewsVetur,
				"link":__linkNewsVetur,
				"resim":imgNewsVetur,
				"date":timeNewsVetur
				}
	def appCom(self):
		istekNewsCom = req.get(self.urlCom, headers=self.headers)
		htmlNewsCom = istekNewsCom.text
		soupNewsCom = btu(htmlNewsCom, features="xml")
		linkNewsCom = soupNewsCom.find_all("link")[2:]
		for iNewsCom in linkNewsCom:
			try:
				_NewsRequests = iNewsCom.text
				_istekNewsCom = req.get(_NewsRequests)
				_htmlNewsCom = _istekNewsCom.text
				_soupNewsCom = btu(_htmlNewsCom, "lxml")
				titleNewsCom = _soupNewsCom.find("h1",{"itemprop":"headline"}).text
				imgNewsCom = _soupNewsCom.find("figure",{"itemprop":"image"}).find("img").get("data-original")
				dateNewsCom = _soupNewsCom.find('span',{"class":"pub-date"}).get("content")
				contentNewsCom = _soupNewsCom.find_all("div",{"itemprop":"articleBody"})
			except:
				pass
			EndContentCom = ''.join(com.text for iCom in contentNewsCom for com in iCom.findAll(text=True))
			comdata = {
			"title":titleNewsCom,
			"link":_NewsRequests,
			"date":dateNewsCom,
			"img":imgNewsCom
			}
			print(comdata)
			time.sleep(10)
			
	def appNal(self):
		istekNewsNal = req.get(self.urlNal)
		htmlNewsNal = istekNewsNal.text
		soupNewsNal = btu(htmlNewsNal, features="xml")
		linkNewsNal = soupNewsNal.find_all("link")[2:]
		for iNewsNal in linkNewsNal:
			nalNewslink = iNewsNal.text
			nalNewsistek = req.get(nalNewslink)
			htmlNews_nal = nalNewsistek.text
			soupNews_nal = btu(htmlNews_nal, "lxml")
			titleNewsNal = soupNews_nal.find("h1",{"class":"entry-header-title"}).text
			timeNewsNal = soupNews_nal.find("time",{"class":"date"}).text
			imgNewsNal =soupNews_nal.find("div",{"class":"post-thumbnail entry-thumbnail"}).find("img",{"class":"no-lazy-loading"}).get("srcset")
			resimNewsNal = imgNewsNal.split(",")[0]
			contentNewsNal = soupNews_nal.find("div",{"class":"entry-content"})
			EndContentNewsNal = ''.join(iNal.text for iNal in contentNewsNal)
			dataNal = {
			"title":titleNewsNal,
			"date":timeNewsNal,
			"link":nalNewslink,
			"img":resimNewsNal,
			"content":EndContentNewsNal
			}
			
	def appNeo(self):
			istekNewsNeo = req.get(self.urlNeo, headers=self.headers)
			htmlNewsNeo = istekNewsNeo.text
			soupNewsNeo = btu(htmlNewsNeo, features="xml")
			linkNewsNeo = soupNewsNeo.find_all("link")[5:]
			resimNewsNeo = soupNewsNeo.find_all("description")[5:]
			imgNeo = [] 
			sayac = 0
			for resimNewsNeo in resimNewsNeo:
				textimgNeo= resimNewsNeo.text
				imgSoupNeo = btu(textimgNeo, "lxml")
				imgNewsNeo = imgSoupNeo.find("img").get("src")
				imgNeo.append(imgNewsNeo)
			for iNewsNeo in linkNewsNeo:
				NewslinkNeo = iNewsNeo.text
				istekNews_Neo = req.get(NewslinkNeo)
				htmlNews_Neo = istekNews_Neo.text
				soupNews_Neo = btu(htmlNews_Neo, "lxml")
				titleNewsNeo = soupNews_Neo.find("h1",{"class":"article-title"}).text.strip()
				timeNewsNeo = soupNews_Neo.find("time",{"class":"published"}).get("datetime")
				imgNews_Neo = imgNeo[sayac]
				contentNewsNeo = soupNews_Neo.find_all("div",{"class":"article-content"})
				contentEndNewsNeo = ''.join(neo.text for iNeo in contentNewsNeo for neo in iNeo.findAll(text=True))
				
	def appRadar(self):
			istekNewsRadar = req.get(self.urlRadar, headers=self.headers)
			htmlNewsRadar = istekNewsRadar.text
			soupNewsRadar = btu(htmlNewsRadar, features="xml")
			linkNewsRadar = soupNewsRadar.find_all("link")[2:]
			for iNewsRadar in linkNewsRadar:
				linkNews_Radar = iNewsRadar.text
				istekNews_Radar = req.get(linkNews_Radar)
				htmlNews_Radar = istekNews_Radar.text
				soupNews_Radar = btu(htmlNews_Radar, "lxml")
				titleRadar = soupNews_Radar.find("h1").text
				resimRadar = soupNews_Radar.find("a",{"data-component-tracking-label":"Pinterest"}).get("href").split("&")[1].replace("media=","")
				pubdateRadar = soupNews_Radar.find("time",{"class":"relative-date"}).text
				contentRadar = soupNews_Radar.find_all("div",{"class":"text-copy bodyCopy auto"})
				EndContentRadar = ''.join(iRadar.text for i_radar in contentRadar for iRadar in i_radar.findAll(text=True))
				
	def appAuto(self):
			istekNews = req.get(self.urlNex, headers=self.headers)
			htmlNews = istekNews.text
			soupNews = btu(htmlNews , features="xml")
			linkNews = soupNews.find_all("link")[2:]
			resimNewsN = soupNews.find_all("enclosure")
			rrNex = []
			sayacNex = 0
			for iResim in resimNewsN:
				resimNex = iResim.get('url')
				rrNex.append(resimNex)
			for iNewsNex in linkNews:
				linkNewsNex = iNewsNex.text
				if linkNewsNex.startswith("https://thenextweb.com"):
					try:
						istekNewsNex = req.get(linkNewsNex)
						htmlNewsNex = istekNewsNex.text
						soupNewsNex = btu(htmlNewsNex, "lxml")
						titleNewsNex = soupNewsNex.find("h1",{"class":"c-header__heading"}).text.strip()
						pubdateNewsNex = soupNewsNex.find("time").text
						contentNewsNex = soupNewsNex.find("div",{"class":"c-richText c-richText--large"})
						EndContentNewsNex = ''.join(inEx.text for iNex in contentNewsNex for iNex in inEx.findAll(text=True))
						print(EndContentNewsNex)
					except:
						continue 
				else:
					pass
	
	def HighMainData(self):
		for imain in self.urlHigh:
			Requests__  = req.get(imain, headers=self.headers)
			Html__ = Requests__.text
			soupFe = btu(Html__, features="xml")
			DivLink = soupFe.find_all("link")[2:]
			for iDiv in DivLink:
				DivRequests = req.get(iDiv.text, headers=self.headers)
				DivHtml = DivRequests.text
				DivSoup = btu(DivHtml, "lxml")
				try:
					DivTitle = DivSoup.find("h1",{"class":"heading-title"}).text.strip()					
					DivDate = DivSoup.find("time").text.strip()
					Divİmg = DivSoup.find("figure").find("img").get("src")
					DivContent = DivSoup.find("section",{"class":"article-body"}).text
					
					print(DivContent)
					print(iDiv.text)
					
				except:
					pass
		break
			
		
if __name__=="__main__":
	Start = TNProcject()
	Start.HighMainData()
	#Start.appAuto() # bu Çalisiyor Tamemn duzgun ✓ 
	#Start.appRadar() # bu çalışıyor Tamamen duzgun ✓
	#Start.appNeo()# bu çalışıyor Tamamen duzgun ✓
	#Start.appNal() bu çalışıyor Tamamen dupzgun ✓
	#Start.appCom() # bu Çalisiyor Tamemn duzgun ✓ 
	#Start.appVetur() bu Çalisiyor Tamemn duzgun ✓ 
	#Start.appHelp() bu çalışıor Tamamen duzgun ✓
	#Start.appThe() bu çalışıyor Tamamen duzgun ✓
	#Start.appThread() bu çalışıyor Tamamen duzgun  ✓








# ag olusturma 


#mobile 

#microsft 

#intenet 
#donaim

#google 

# android 