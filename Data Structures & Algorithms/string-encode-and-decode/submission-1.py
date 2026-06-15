class Solution:

    def encode(self, strs: List[str]) -> str:

        s =("")     #Eklemeye buradan başlayacağım ama bu ekleyeceğim şey ne olmalı bir string mi?
        
        for i in strs:
            leng=str(len(i))
            s =  s + leng + "§" + i #Üzerine ekliiycem her döngü elemanını bu sayede uç uca eklemiş olucam.Ve uc uca eklerken string uzunşukları ile uzunlukları ayıracak bir ayraç kullandık.
                                                        #Ayracı nasıl yerleştiricem bu noktda 
        return s



    def decode(self, s: str) -> List[str]:

        liste=[]
        i=0

        while i < len(s):

            #Önce kaç elema gideceğimizi bulalım
            j=s.find("§",i) #"5§Hello5§World" için

            uzunluk=int(s[i:j])

            kelime = s[j+1 : j+1+uzunluk]


            liste.append(kelime)




            i = j+1+uzunluk

        return liste









'''
PROBLEM:

*Problem iki fonksiyon ile çalışmakta.Amaç verilen bir string listesindeki 
elemanları birleştirerek tek bir string elemanlı listeye çevirmemiz gerekli.
Bu problemin encode fonksiyonu kısmıdır.

*Daha sonra birleştirilen string tekrardan parçalanmış haline geri getirilecek.

strs = ["Hello","World"]-->["HelloWorld"]-->["Hello","World"]

*Sorum şu şekilde birleştirme işlemini dümdüz mü yapıcam
*Aklıma boşluk ya da sipesififk karakterkere göre parçalamak vardı ama 
bu riskli olacaktır.Sonuçta verdiği string elemanlarında da boşluk virgül
vs...olabilir.
*Bu nedenle ayırma işlemini farklı bir biçimde yapmalıyız.

*Hint 1 de non-ascii karakterler ile ayyırabileceğimizi söylüyor bu durumda eşsiz bir ayraç 
koymam gerekli galiba stringler arası bunu da birleştirme işlemi sırasında yapıcam.
*Ama bu noktada aklıma şu geliyor sting'in içinde herhangib bir şey olabilir,benim belirleyeceğim 
non-ascii karakter de bu stingler içinde bulunabilir.Bu durumda algoritma yeterince iyi olmuyor bence
ama soru böyle istiyorsa stringleri birleştirirken for döngüsünde belli bir karakteri araya koyarak 
birleştiririm daha sonra ona göre ayırıırm.

*Evreka evet dediğim gibi non-ascii karakterler ile ayıramam daha eşsiz bir şey olmalı o da string'in
uzunluğu olabilir her string sonuna o stingin uzunluğunu koyarım: Hello5World5

*Peki sorum şu şekilde bu noktada nasıl tanıyarak ayıracak ve daha öncesinde nasıl birleştiricez.
Yani direkt string uuznluğunu sayı olarak mı yazıcaz
*Şöyleki stringlerin uzunluklarını başlarına yazarak "Burdan itibaren bu kadar indeks al" 
şeklinde bir komut verebiliriz.

*İleri seviye karakter dizilerinin fonksiyonları ile parçalama işlemini yapabiliriz.
split() kullanılabilir.




*stringteki karakterleri baştan okudukça kenara atabiliriz:Yani mesela
encode edilmiş string"HelloWorld" olsun.Bir döngü ile baştan başlayarak 
önce Hello sonra World kelimesini arayabiliriz.Sonuçta birleştirme işlemi
sıraya dayalı yapılacak.(Aslında bu yol da ölü değil yapılabilir ama daha zor olacaktır muhtemelen.)

*Bu temel iskelet ama bunu nasıl yapabiliirm?

*Neyse öncelikle ilk fonksiyona kafa yoralım.Bir string listem var ve bütün elemanları
üst üste ekleyerek tek bir stringde oluşan bir liste oluşturmak istiyorum.
*Bunun için for döngüsü ve basit operatörleri kullanabilirm.






*********ÇÖZÜM*********


Amacımız belirlediğimiz ayraçlar sayesinde kelimelerin uzunluklarına göre parçalaya bilmekti.
Bunun için öncelikle doğru tekdüze string yapımızı ilk fonksiyonda oluşturduk ve bunu bir
Parametre olarak bir sonraki fonksiyona döndürdük.Oluşturduğumuz "5§Hello5§World" yapısı sayesinde
find fonksiyonunu § için kullanarak ne uzunlukta ve nereden itibaren kelimeleri seçebileceğimi
bulmuş olduk ve bulduğum her kelimeyi de bir str olarak listeme ekleyip bir sonraki ayracıma gittim.




'''