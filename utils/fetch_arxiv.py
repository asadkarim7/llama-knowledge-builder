import urllib.request
import xml.etree.ElementTree as ET
import time

def fetch_papers():
    """
    Fetches papers from arXiv, with the search query "llama".
    :return: papers_list: list of papers
    """
    url = 'http://export.arxiv.org/api/query?search_query=ti:llama&start=0&max_results=70'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    root = ET.fromstring(data)

    papers_list = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
        paper_info = f"Title: {title}\nSummary: {summary}\n"
        papers_list.append(paper_info)

    time.sleep(3)  # Sleep for 3 seconds to comply with ArXiv's rate limit

    return papers_list
