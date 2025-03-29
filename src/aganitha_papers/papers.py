import requests
import pandas as pd
import time

# PubMed API endpoint
PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_papers(query, max_results=10):
    """
    Fetch paper IDs from PubMed based on the query.
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }

    response = requests.get(PUBMED_SEARCH_URL, params=params)
    response.raise_for_status()
    data = response.json()

    # Extract PubMed IDs
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    
    return paper_ids

def fetch_full_details(paper_ids):
    """
    Fetch full details for a list of PubMed IDs.
    """
    if not paper_ids:
        return []

    ids = ",".join(paper_ids)

    params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml"
    }

    response = requests.get(PUBMED_FETCH_URL, params=params)
    response.raise_for_status()

    from xml.etree import ElementTree as ET
    root = ET.fromstring(response.content)

    papers = []
    for article in root.findall(".//PubmedArticle"):
        paper = {
            "PubmedID": "",
            "Title": "",
            "Authors": "",
            "Journal": "",
            "PublicationDate": "",
            "Affiliations": "",
            "Abstract": ""
        }

        # Extract ID
        paper["PubmedID"] = article.findtext(".//PMID")

        # Extract Title
        paper["Title"] = article.findtext(".//ArticleTitle", "")

        # Extract Authors
        authors = []
        for author in article.findall(".//Author"):
            last_name = author.findtext("LastName", "")
            fore_name = author.findtext("ForeName", "")
            authors.append(f"{fore_name} {last_name}".strip())
        paper["Authors"] = ", ".join(authors)

        # Extract Journal Name
        paper["Journal"] = article.findtext(".//Journal/Title", "")

        # Extract Publication Date
        pub_date = article.find(".//PubDate")
        if pub_date is not None:
            year = pub_date.findtext("Year", "")
            month = pub_date.findtext("Month", "")
            day = pub_date.findtext("Day", "")
            paper["PublicationDate"] = f"{year}-{month}-{day}".strip("-")

        # Extract Affiliations
        affiliations = []
        for aff in article.findall(".//AffiliationInfo/Affiliation"):
            affiliations.append(aff.text)
        paper["Affiliations"] = "; ".join(affiliations)

        # Extract Abstract
        abstract = article.findtext(".//Abstract/AbstractText", "")
        paper["Abstract"] = abstract

        papers.append(paper)

        # Rate limiting (avoid PubMed API throttling)
        time.sleep(0.5)

    return papers

def filter_non_academic_authors(papers):
    """
    Filter out papers with only non-academic affiliations.
    If a paper has both academic and non-academic affiliations, include it.
    """
    filtered_papers = []
    
    # Academic keywords list
    academic_keywords = ["university", "college", "institute", "school", "faculty", "department"]

    for paper in papers:
        affiliations = paper.get("Affiliations", "")
        
        # Ensure we have affiliations to process
        if affiliations:
            affiliations_list = affiliations.lower().split(",")  # Split multiple affiliations

            # Check if at least one academic affiliation is present
            is_academic = any(
                any(keyword in affiliation for keyword in academic_keywords)
                for affiliation in affiliations_list
            )

            if is_academic:
                filtered_papers.append(paper)

    return filtered_papers


def save_to_csv(papers, output_file):
    """
    Save the paper details to a CSV file.
    """
    df = pd.DataFrame(papers)
    df.to_csv(output_file, index=False)
    print(f" Results saved to {output_file}")
