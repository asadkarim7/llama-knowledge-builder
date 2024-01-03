def clean_data(papers_list):
    """
    Cleans the data by removing newlines and trailing spaces.
    :param papers_list: list of papers
    :return: data that has been cleaned
    """
    cleaned_data = []
    for paper in papers_list:
        paper = paper.replace('\n', ' ').strip()
        cleaned_data.append(paper)
    return cleaned_data