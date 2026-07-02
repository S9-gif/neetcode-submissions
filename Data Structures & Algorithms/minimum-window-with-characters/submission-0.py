    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        from collections import Counter

        need = Counter(t)       # {'A':1, 'B':1, 'C':1}
        window = {}

        required = len(need)    # kaç farklı karakter karşılanmalı
        formed = 0              # şu an kaç farklı karakter karşılandı

        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Bu karakter t'de gerekiyor mu ve yeterince var mı?
            if char in need and window[char] == need[char]:
                formed += 1

            # Tüm karakterler karşılandıysa → pencereyi daralt
            while formed == required:
                # Sonucu güncelle
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Sol karakteri çıkar
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return result