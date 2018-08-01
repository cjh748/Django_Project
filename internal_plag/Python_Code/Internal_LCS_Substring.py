from difflib import SequenceMatcher


def Longest_Common_Substring(string1, string2):
    ##### SOURCE: https://stackoverflow.com/questions/18715688/find-common-substring-between-two-strings
    match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
    return len(string1[match.a: match.a + match.size].split())
