class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch in word:
            for i in range(len(word)):
                if word[i] == ch:
                    return word[:i+1][::-1] + word[i+1:]
        return word