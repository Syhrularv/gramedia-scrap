import urllib3, wget, os
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
allbooks = []
allctgry = []
alllinks = []
index = 1


nama = input("Judul Buku : ")
r = http.request('GET','https://ebooks.gramedia.com/search?s='+nama)
soup = BeautifulSoup(r.data,'html.parser')
list = soup.find_all(class_='search_list')

for x in list:
    books = []
    link = x.find('a')
    url = link['href']
    item = x.find_all('span')
    for i in item:
        if 'title' in str(i):
            books.append(i.get_text())
        else:
            pass

    allbooks.append(books[2])
    allctgry.append(books[1])
    alllinks.append(url)

#print(allbooks)
#print(alllinks)

def donglot(name,url):
    x = 1
    try:
       os.mkdir(name)
       os.chdir(name)
    except:
       os.chdir(name)

    url = url
    r = http.request('GET',url)
    soup = BeautifulSoup(r.data,'html.parser')
    desc = soup.find('div',{'itemprop':'description'})
    desc2 = soup.find_all('table')
    desc3 = str(desc2[1].get_text()).split()
    f = open('deskripsi.txt','a')
    f.write(str(desc.get_text())+'\n\n')
    f.close()

    for i in desc3:
        if i == ':':
           pass
        else:
           if x % 2 == 0:
              f = open('deskripsi.txt','a')
              f.write(' : ' + str(i) + '\n')
              f.close()
              x += 1
           else:
              f = open('deskripsi.txt','a')
              f.write(str(i))
              f.close()
              x += 1

    preview = soup.find(id='previews')
    print('Sedang Mendonglot...')
    for i in preview.find_all("img"):
        file = wget.download(i['src'])
        print(' Images Downloaded : ' + file)

print('Berikut Buku Yg Mungkin Anda Cari : ')
for y in allbooks:
   print('['+str(index)+'] ' + y)
   index += 1
print('[n] Tidak Ada')

ask = input('Pilih > ')
if ask == 'n' or ask == 'N':
   print('Maaf Buku Tidak Di Temukan / Kesalahan Pengetikan')
elif ask == '1':
   donglot(allbooks[0],alllinks[0])
elif ask == '2':
   donglot(allbooks[1],alllinks[1])
elif ask == '3':
   donglot(allbooks[2],alllinks[2])
elif ask == '4':
   donglot(allbooks[3],alllinks[3])
elif ask == '5':
   donglot(allbooks[4],alllinks[4])
elif ask == '6':
   donglot(allbooks[5],alllinks[5])
elif ask == '7':
   donglot(allbooks[6],alllinks[6])
elif ask == '8':
   donglot(allbooks[7],alllinks[7])
elif ask == '9':
   donglot(allbooks[8],alllinks[8])
elif ask == '10':
   donglot(allbooks[9],alllinks[9])
else:
   print('Pilih yg bner ajg')
