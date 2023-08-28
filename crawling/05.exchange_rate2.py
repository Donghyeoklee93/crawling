import requests as req
import re

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text

r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

print(captures)


print("--------")
print("exchange rate calculator")
print("--------")
print("")

for c in captures:
    print(c[0] + " : " + c[1])

print()
usd = float(captures[0][1].replace(",", ""))
won = input("Please enter the amount (in KRW) you want to convert to dollars>>>")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} has been exchanged")
