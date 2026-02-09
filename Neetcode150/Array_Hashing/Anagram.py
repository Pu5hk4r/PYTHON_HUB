def isAnagram(s:str, t:str)->bool:
    if(len(s) != len(t)):
        return False
    s.lower()
    t.lower()

    count = [0] * 26

    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    return all(x==0 for x in count)


string1 = "Pushkar"
string2 = "rushkaP"

isAnagram(string1,string2)
