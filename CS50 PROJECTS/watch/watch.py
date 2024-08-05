import re


def main():
     print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'<iframe (?:\w|=|"|-| )*src="https?://(?:www\.)?youtube\.com/embed/(.+)"(?: title=(.+)*)?></iframe>', s, re.IGNORECASE):
        url = 'https://youtu.be/'+matches.group(1)
        return url

    return None

if __name__ == "__main__":
    main()