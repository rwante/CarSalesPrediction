import requests
from lxml import html
from openpyxl import Workbook,load_workbook

def araba_marka_cekme():
    url = "https://www.arabam.com/ikinci-el/otomobil/"
    r = requests.get(url)
    tree = html.fromstring(r.content)
    araba_markalari = []
    for i in range(1,58):
        xpath = '//*[@id="js-hook-for-listen-scroll-cta"]/div[1]/ul[2]/li/ul/li['+str(i)+']/a'
        xpath1 = '/html/body/div[3]/div[5]/div[4]/div/div[1]/form/div[1]/ul[2]/li/ul/li['+str(i)+']/span/text()'
        sonuc1 = tree.xpath(xpath1)
        düz1 = sonuc1[0].strip()
        düz2 = düz1[1:-1]
        düz2 = düz2.replace(".","")
        if int(düz2) > 1000:
            sonuc = tree.xpath(xpath)
            araba_markalari.append(sonuc[0].get("href"))
    return araba_markalari

def araba_ozel(araba_markalari):
    t = 1
    for i in araba_markalari:
        url = 'https://www.arabam.com'+i
        dosya_ismi=str(t)
        dosya = open(dosya_ismi,"w+")
        t += 1
        for j in range(1,51):
            url1 = url+'?page='+str(j)
            r = requests.get(url1)
            tree = html.fromstring(r.content)
            for k in range(1,23):
                try:
                    xpath = '/html/body/div[3]/div[5]/div[4]/div/div[2]/table/tbody/tr['+str(k)+']/td[2]/h3/a'
                    sonuc = tree.xpath(xpath)
                    dosya.write(sonuc[0].get("href")+"\n")
                except:
                    pass
def araba_ozellik_cekme():
    wb = load_workbook("Veri.xlsx")
    ws = wb.active
    ws.append(["Marka", "Seri", "Model","Yil","Yakit","Vites","Motor Hacmi","Motor Gücü","Km","Ilan Tarihi","Fiyat"])
    for i in range(1,19):
        dosya_ismi = str(i)
        dosya = open(dosya_ismi,"r")
        for j in range(1,1000):
            try:

                url = 'https://www.arabam.com'+dosya.readline().rstrip()
                r = requests.get(url)
                tree = html.fromstring(r.content)
                fiyatxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/div[1]/div/span'
                markaxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[3]/span[2]'
                serixpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[4]/span[2]'
                modelxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[5]/span[2]'
                yilxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[6]/span[2]'
                yakitxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[7]/span[2]'
                vitesxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[8]/span[2]'
                motorhxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[9]/span[2]'
                motorgxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[10]/span[2]'
                kmxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[11]/span[2]'
                ilantxpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[2]/span[2]'
                sonucfiyat = tree.xpath(fiyatxpath)
                sonucmarka = tree.xpath(markaxpath)
                sonucseri = tree.xpath(serixpath)
                sonucmodel = tree.xpath(modelxpath)
                sonucyil = tree.xpath(yilxpath)
                sonucyakit = tree.xpath(yakitxpath)
                sonucvites = tree.xpath(vitesxpath)
                sonucmotorh = tree.xpath(motorhxpath)
                sonucmotorg = tree.xpath(motorgxpath)
                sonuckm = tree.xpath(kmxpath)
                sonucilant = tree.xpath(ilantxpath)

                ws.append([sonucmarka[0].text,sonucseri[0].text,sonucmodel[0].text,sonucyil[0].text,sonucyakit[0].text,
                           sonucvites[0].text,sonucmotorh[0].text,sonucmotorg[0].text,sonuckm[0].text,sonucilant[0].text,
                           sonucfiyat[0].text])

            except:
                pass
    wb.save("Veri.xlsx")
    wb.close()




#araba_ozel(araba_marka_cekme())
araba_ozellik_cekme()

