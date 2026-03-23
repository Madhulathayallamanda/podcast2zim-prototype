import feedparser
import requests

rss_link = input("Enter podcast RSS link: ")

feed = feedparser.parse(rss_link)

print("\nPodcast:", feed.feed.get("title"))

print("\nDownloading first 2 episodes...\n")

count = 0

for entry in feed.entries:
    if count == 2:
        break

    title = entry.get("title", "no_title")
    
    # getting audio link
    if "enclosures" in entry and len(entry.enclosures) > 0:
        audio_url = entry.enclosures[0].href
        
        print("Downloading:", title)

        try:
            response = requests.get(audio_url)
            
            filename = f"episode_{count}.mp3"
            with open(filename, "wb") as f:
                f.write(response.content)

            print("Saved as", filename)

        except:
            print("Failed to download")

    count += 1
