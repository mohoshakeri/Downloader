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


def similar_links_downloader(page_link, sim_link, format, name="Downloaded", dir=""):
    try:
        downloader(
            page_link,
            "html",
            "source",
            dir,
        )
        source_file = open(f"{dir}source.html", "r")
        links = []
        repetitive = None
        for line in source_file:
            first_index = line.find(sim_link)
            last_index = 0
            if first_index != -1:
                last_index = line.find('"', first_index)
                this_link = line[first_index:last_index]
                # Check for duplicate value
                for link in links:
                    repetitive = False
                    if this_link == link:
                        repetitive = True
                        break
                if not repetitive:
                    links.append(this_link)
        for index, link in enumerate(links):
            x = downloader(
                link,
                {format},
                f"{name}-{index+1}",
                dir,
            )
        os.remove(source_file)
        return True
    except:
        return False
