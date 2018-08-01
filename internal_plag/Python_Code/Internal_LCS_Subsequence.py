import collections

###### SOURCE: http://www.stokastik.in/dynamic-programming-in-natural-language-processing-longest-common-subsequence/


def Longest_Common_Subsequence(s1, s2):
    tokens1, tokens2 = s1.split(), s2.split()
    cache = collections.defaultdict(dict)
    for i in range(-1, len(tokens1)):
        for j in range(-1, len(tokens2)):
            if i == -1 or j == -1:
                cache[i][j] = 0
            else:
                if tokens1[i] == tokens2[j]:
                    cache[i][j] = cache[i - 1][j - 1] + 1
                else:
                    cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    return cache[len(tokens1) - 1][len(tokens2) - 1]
