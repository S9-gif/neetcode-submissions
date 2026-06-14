class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frekanslar = dict()


        for i in nums:

            frekanslar[i]=1+frekanslar.get(i,0)   #Burda elemanı kendisini değil elemanı görünce +1 yapmam gerekli ama nasıl doğru olarak yapıcam.(Burası problemli doğru yazım nasıl bilmiyorum)

        #Elimdeki frekanslar hash_map'i için sözlüğü sort edersem(edebiliyor muyum bilmiyotum ama)

        items=sorted(frekanslar.items(),key=lambda x: x[1] ,reverse=True)#İtemler burda tule olarak dönecek.key=lambdax:x[1] ile de neye göre sıralayacağımızı belirledik,ki burda ikinci eleman olan values olacak

        #hatta azalana göre sıralayabilirsem ilk k elemanı çekmem yeterli olacaltır.
        #Value'lara göre büyükten küçüğe sıralamam lazım

        #countS[s[i]] = 1 + countS.get(s[i], 0)





        #Şİmdi hazırlanmış olan frekanslar hashmap'inden verilen k kadar uygun key çekicem
        #Burda ilk k elemanı items üzerinden ne yazarak çekicem

        sayac=0
        liste=list()

        for j ,w in items:

            liste.append(j)

            sayac+=1
            if sayac==k:

                return liste
















        '''

PROBLEM:

*Sorudan anladığım verilen bir tamsayı dizisinden k frekansı kadar tekrar
elemanları çıktı olarak vericem.

Hayır yanlış anladım
*Frekansı en yüksek olan k tane değeri döndür
Burda frekanslar 1->1 tane
                 2->2 tane
                 3->3 tane
    k=2 olduğunden en yüksek frekanslı iki tanesini alıyorum
    2 ve 3


*Önceki problemdeki gibi her adım için dizi elemanına bakıp yoksa hash map'e
bir key olarak ekleyebilir ve aynı döngüde value olarak da ekleme yapabiliriz.


        
        
        
        
        '''
