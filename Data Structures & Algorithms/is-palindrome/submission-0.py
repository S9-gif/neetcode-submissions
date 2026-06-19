class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.upper()
        liste=list(s)
        liste2=list()
        ters_liste=list()

        for i in liste:
            if i.isalnum()==False:
                continue
                        
            liste2.append(i)


        for i in range(len(liste2)-1,-1,-1):
            ters_liste.append(liste2[i])

        if liste2 == ters_liste:
            return True
        else:
            return False












        '''

PROBLEM:
Verilen string s için palindrome 'luk test ediniz.Palindrome ise True değil ise False döndürünüz

Palindrome string tersten de aynı şekilde yazılabileb cümle veya kelimelerdir.
Yani bütün stringi tersten taradığımızda her harf aynı olmalıdır düz hali gibi


Probleme girişmek adına topicleri inceliyorum
Aslında stringi listeye çevirip bu listenin tersini alıp iki listeyi karşılaştırabiliiriz.

for dögüsü ile range fonksiyonunda gezinirsem bana indeks sayılarını verir elemanlar için i yi köşeli
parantez ile almalıyım.


        '''