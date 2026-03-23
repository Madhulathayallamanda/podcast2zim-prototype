import feedparser

url = input("Enter podcast RSS URL: ")

feed = feedparser.parse(url)

print("\nPodcast Title:", feed.feed.get("title", "No title"))

print("\nEpisodes:\n")

for entry in feed.entries[:5]:
    print("-", entry.get("title", "No title"))
