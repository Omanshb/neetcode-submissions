class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False


        reference = [0] * 26
        tracker = [0] * 26
        for i in range(len(s1)):
            reference[ord(s1[i]) - ord('a')] += 1
            tracker[ord(s2[i]) - ord('a')] += 1
        if tracker == reference:
            return True
        
        for p in range(len(s1), len(s2)):
            tracker[ord(s2[p]) - ord('a')] += 1
            tracker[ord(s2[p - len(s1)]) - ord('a')] -= 1
            print(tracker)
            if tracker == reference:
                return True

        return False

            
