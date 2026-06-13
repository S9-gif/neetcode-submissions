class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        anagrams = dict()


        for i in strs:
            x=tuple(sorted(i)) #for ile listedeki ilk kelimeyi alıp harflerine ayırdık ve alfabetik sıraladık.
                               #Keza key olarak liste kullanamayacağımız için değiştirilemez olan tuple kullandık. 
            if x not in anagrams:

                anagrams[x]=[] #Bu sayede anagramda bulunmayan,key olacak parçalamalarımızdan birini boş bir key value olarak döndürdük.
            
            #anagram isimli 
            
            anagrams[x].append(i)#Hala aynı for döngüsü i̇çinde olduğum için key ataması yaptıktan sonra üzerinde bulunduğum elemanı o key'e value olarak ekleyebiliyorum

            #benden çıktı olarak gruplanmış kelimeleri istediği için buradaki hash map de value lara denk gelen kısmı istiyor aslında o yüzden Hatch map'den value ları alacağım.

        return list(anagrams.values())

















'''
PROBLEM:
*Önceki problemden çıkarttığım ders üzerine problemı anlama aşamasına daha
özenli davranıcam.

*Problemin istediği strs adı ile verilen ve string tipinde veriler içeren
dizide anagram olan kelimeleri gruplayarak çıktı vermek,çıktının belli bir
kriteri yok anagramların gruplu olması yeterli.

*Topic olarak hash table yani sözlükler ve sorting verilmiş.Sorting anagram
bulmak için hash table grublamak için kullanılacak.

*Hash_map kullanarak nasıl gruplayacağım
Şöyle bir yapıyı kurabiliriz key olarak parçalanmış ve sıralanmış kelimeler
value olarak de buna uyan kelimeleri getireceğiz.






'''