#This would read from config in real app. Just here for simplicity

blacklist = [
    "youtube.com",
    "reddit.com",
]

def checker(url):
    
    if url:
        for site in blacklist:
            if site in url:
                return True
    return False