import requests,os,json,time
from config import cookie, universes

def badgecreate(universe):
    time.sleep(5)
    count = requests.get(f"https://badges.roblox.com/v1/universes/{universe}/free-badges-quota").json()
    print(count)
    
    for i in range(count):
        with requests.session() as session:
            session.cookies[".ROBLOSECURITY"] = cookie
            header = session.post("https://catalog.roblox.com/")
            session.headers["X-CSRF-TOKEN"] = header.headers["X-CSRF-TOKEN"]
            session.headers["Origin"] = "https://www.roblox.com/"
            session.headers["Referer"] = "https://www.roblox.com/"
            base = f"https://badges.roblox.com/v1/universes/{universe}/badges"
            d = {"name":"badg ename","description":"badge description","paymentSourceType":"User","expectedCost":0} # edit here
            badge = session.post(base, data=d, files = {"upload_file":open("icon.png","rb")}).json()
            try:
                print(badge['id'])
            except KeyError or IndexError:
                print(badge['errors'][0]["message"])
                badgecreate(universe)
                return

for i in universes:
    badgecreate(i)
