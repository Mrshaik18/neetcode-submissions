class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}

        for word in strs:
            counts=[0]*26

            for char in word:
                counts[ord(char)-ord('a')]+=1
            
            key=tuple(counts)

            if key not in anagram:
                anagram[key]=[word]
            else:
                anagram[key].append(word)
        return list(anagram.values())

    
        