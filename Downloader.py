import requests
import os


def downloader(link, format, name="Downloaded", dir=""):
    try:
        url = requests.get(url=link)
        file = open(f"{dir}{name}.{format}", "wb")
        file.write(url.content)
        return True
    except:
        return False


def similarLinksDownloader(pageLink, simLink, format, name="Downloaded", dir=""):
    try:
        downloader(
            pageLink,
            "html",
            "source",
            dir,
        )
        sourceFile = open(f"{dir}source.html", "r")
        links = []
        repetitive = None
        for line in sourceFile:
            firstIndex = line.find(simLink)
            lastIndex = 0
            if firstIndex != -1:
                lastIndex = line.find('"', firstIndex)
                thisLink = line[firstIndex:lastIndex]
                # Check for duplicate value
                for link in links:
                    repetitive = False
                    if thisLink == link:
                        repetitive = True
                        break
                if not repetitive:
                    links.append(thisLink)
        for index, link in enumerate(links):
            x = downloader(
                link,
                {format},
                f"{name}-{index+1}",
                dir,
            )
        os.remove(sourceFile)
        return True
    except:
        return False
