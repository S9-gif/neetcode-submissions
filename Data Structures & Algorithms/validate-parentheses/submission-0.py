class Solution:
    def isValid(self, s: str) -> bool:
        

        #Önce s stringindeki tüm elemanları append ile stack listesine push ettik diyelim bu durumda
        #listem==> ["(", "[", "{", "}", "]", ")"] oldu bakmamız istenen her parantezin doğru sıra ve 
        #türdeşi parantez ile kapanması


        eslesmeler = {")": "(", "}": "{", "]": "["}     #Bu sözlük olmadan eşlemeleri yapamam.
        stack=[]

        for i in s:
            

            if  i == "(" or i == "[" or i == "{":
                stack.append(i)   #Bu sayede sadece açılış elemanlarını stack'e eklemiş oldum.


            
            elif i == ")" or i == "]" or i == "}":
                if not stack:
                    return False
                y=stack.pop()
                if y != eslesmeler[i]: #Burda hata almadıysa döngüye devam etmeli 
                    return False
                

        if stack:
            return False
        return True #Her hangi bir yere takılmazsa her şey yerindedir

            




            #Bir kapama elemanı gördüğümde bu pop edilen ile eşit ise doğru yoldayım demektir.İtere etmeye devam ederim
            #Ama bir sorunla karşılaşırsam direkt return False deriz.


            #Peki şimdi kontrolü nasıl sağlıycam?
            #Pop yapsam ve pop yapılınca o değeri bir değere atayabilirim de bu parantez değerleri 
            #aynı değil ki, yani nasıl eşletşt,rme yapıcam?==>Önceden kural gibi yazdığım bir sözlük
            #ile yazıcam.

            #Hint2 de her açılış parantezinş stacke ekle diyor.Eğer üzerinde durduğun karakter kapanış
            #karakteri ise açılışı için stack e bak.Bu şuanda sadece karşılıklı bir parantez var mı diyr
            #bakıyoruz.Bizim bir de sıra kontrolü yapmamız lazım.Ama bunu komplike düşünmek yerine sıra 
            #karşılaştırması yapabiliriz.

'''

şöyle yapabiliriz her açılış elemanını gördüğümüzde onu bir stacke aktaralım mesela
["(", "[", "{"] olsun daha sonra döngü ile gezmeye devsm ederek ilk denk geldiğimiz elemanın
bu stack deki elemanlardan pop edilenin yani son elemanın kapanış karşılığı olduğunu kontrol 
etmeliyiz AMA burda anlam veremediğim parantez elemanlarını nasıl tanıycaz direkt if i (,[,{ gibi
bir sorgu mu yapıcaz.
'''





















        



'''


PROBLEM:

Problemin istediği ,parantezlerden tiplerinden oluşan s stringinde açılan her parantez doğru sıra ile doğru
parantezce kapanıyorsa true döndürücez öbür durumda falsa döndürücez.

Konu başlığımız stack









'''