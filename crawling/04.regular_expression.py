import re

# regular expression

s = "hi"
print(re.match(r"hi", s))
print(re.match(r"hey", s))
print(re.match(r"h.", s))
print(re.match(r"..", s))
print(re.match(r".", s))


print(re.match(r"hi1*", s))
print(re.match(r"hi1+", s))
print(re.match(r"hi1?", s))

ss = "color"
print(re.match(r"colou?r", ss))


sss = "how are you?"
print(re.match(r"how are you\?", sss))

ssss = "이 영화는 C등급 입니다"
print(ssss.split("이 영화는 ")[1].split("등급")[0])
print(re.match(r"이 영화는 [ABCF]등급 입니다", ssss))

print(re.findall(r"이 (..)는 (.)등급 입니다", ssss))
