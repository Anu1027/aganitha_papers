import typer
from typing import List
from aganitha_papers.papers import (
    fetch_papers, 
    fetch_full_details, 
    filter_non_academic_authors, 
    save_to_csv
)

app = typer.Typer()

@app.command()
def fetch(
    query: List[str] = typer.Argument(..., help="Search query for PubMed"),  
    output: str = typer.Option("output/results.csv", help="Output CSV file"),
    debug: bool = typer.Option(False, help="Enable debug mode")
):
    """
    Fetch papers from PubMed, filter them, and save to CSV.
    """
    query_str = " ".join(query)  # Join multi-word arguments properly

    if debug:
        print(f" Query: {query_str}")
        print(f" Output file: {output}")

    # Step 1: Fetch IDs
    paper_ids = fetch_papers(query_str)
    total_ids = len(paper_ids)

    # Step 2: Fetch full details
    papers = fetch_full_details(paper_ids)

    # Step 3: Filter non-academic authors
    filtered_papers = filter_non_academic_authors(papers)
    filtered_count = len(filtered_papers)
    excluded_count = total_ids - filtered_count

    # Step 4: Save to CSV
    save_to_csv(filtered_papers, output)

    # Display stats
    typer.echo(f" Results saved to {output}")
    typer.echo(f" Total papers fetched: {total_ids}")
    typer.echo(f" Papers kept (academic + mixed): {filtered_count}")
    typer.echo(f" Papers excluded (non-academic only): {excluded_count}")

if __name__ == "__main__":
    app()
