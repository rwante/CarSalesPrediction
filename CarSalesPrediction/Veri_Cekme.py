import requests
from lxml import html

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
    for i in range(1,2):
        dosya_ismi = str(i)
        dosya = open(dosya_ismi,"r")
        for j in range(1,1001):
            url = 'https://www.arabam.com'+dosya.readline()
            r = requests.get(url)
            tree = html.fromstring(r.content)
            marka_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[3]/span[2]'
            seri_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[4]/span[2]'
            model_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[5]/span[2]'
            yil_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[6]/span[2]'
            yakit_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[7]/span[2]'
            vites_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[8]/span[2]'
            motorhacmi_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[9]/span[2]'
            motorgücü_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[10]/span[2]'
            km_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[11]/span[2]'
            tarih_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/ul/li[2]/span[2]'
            fiyat_xpath = '//*[@id="js-hook-for-observer-detail"]/div[2]/div[1]/div/span'
            sonuc_marka = tree.xpath(marka_xpath)
            sonuc_seri = tree.xpath(seri_xpath)
            sonuc_model = tree.xpath(model_xpath)
            sonuc_yil = tree.xpath(yil_xpath)
            sonuc_yakit = tree.xpath(yakit_xpath)
            sonuc_vites = tree.xpath(vites_xpath)
            sonuc_motorh = tree.xpath(motorhacmi_xpath)
            sonuc_motorg = tree.xpath(motorgücü_xpath)
            sonuc_km = tree.xpath(km_xpath)
            sonuc_tarih = tree.xpath(tarih_xpath)
            sonuc_fiyat = tree.xpath(fiyat_xpath)
            print(sonuc_marka)
            print(sonuc_seri)
            print(sonuc_model)
            print(sonuc_yil)
            print(sonuc_yakit)
            print(sonuc_vites)
            print(sonuc_motorh)
            print(sonuc_motorg)
            print(sonuc_km)
            print(sonuc_tarih)
            print(sonuc_fiyat)



#araba_ozel(araba_marka_cekme())
araba_ozellik_cekme()

