#!/usr/bin/env python3
import re
import sys
from urllib.request import urlretrieve

import requests

with requests.session() as session:
    r = session.get(sys.argv[1])

    # one shouldn't use regexes to parse html, but in this case they are good enough
    img_list = [
        s.strip('" ')
        for s in re.search(r"Array\(([^)]+)\)", r.text).groups()[0].split(",")
    ]
    book_path = re.search(r'Bilderverzeichnis += +"([^"]+)"', r.text).groups()[0]

    print("Downloading...")
    for img in img_list:
        print(img)
        path = "https://www.dmg-lib.org" + book_path + "/thumbs/1_0002/" + img
        urlretrieve(
            "https://www.dmg-lib.org" + book_path + "/thumbs/1_0002/" + img, img
        )

    print("Download completed.")
