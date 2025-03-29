Aganitha Papers - PubMed Research Papers Filtering Tool
A CLI application for fetching and filtering research papers from PubMed, excluding papers with only non-academic affiliations and saving the filtered results to a CSV file.

🚀 Project Overview
This project is designed to automate the process of fetching research papers from PubMed based on a given query. The application:

Fetches papers using PubMed API.

Filters out papers with only non-academic affiliations.

Includes papers with mixed affiliations.

Saves the results into a CSV file containing detailed metadata.

Includes unit tests to ensure correctness of the filtering logic.

🔥 Features
✅ Fetches research papers from PubMed using custom queries.
✅ Filters out papers with non-academic-only affiliations.
✅ Includes papers with mixed academic and non-academic affiliations.
✅ Saves the results in a structured CSV file.
✅ Provides debugging options to display query and execution details.
✅ Includes unit tests for filtering logic validation.

🛠️ Tech Stack
Language: Python

Dependency Management: Poetry

Libraries:

requests → To make API calls.

pandas → For handling and saving CSV data.

typer → For building the CLI.

rich → For formatted console output.

unittest → For unit testing.

⚙️ Project Structure
bash
Copy
Edit
/aganitha-papers
 ├── output/                     # CSV output files
 │     └── results.csv           # Final filtered papers
 │
 ├── src/                        # Source code
 │     └── aganitha_papers/
 │             ├── __init__.py   # Init file
 │             ├── main.py       # CLI entry point
 │             ├── papers.py     # Paper fetching and filtering logic
 │
 ├── tests/                      # Unit tests
 │     └── test_papers.py        # Tests for filtering logic
 │
 ├── .gitignore                  # Files to ignore in version control
 ├── pyproject.toml              # Poetry project configuration
 ├── poetry.lock                 # Poetry dependencies lock file
 ├── README.md                   # Project documentation
 └── LICENSE                     # License information (if added)
🚀 Installation and Setup
✅ 1. Clone the Repository
bash
Copy
Edit
git clone <your-repository-url>
cd aganitha-papers
✅ 2. Install Poetry
If you don’t have Poetry installed, run:

bash
Copy
Edit
pip install poetry
✅ 3. Install Dependencies
Run the following command to install all dependencies:

bash
Copy
Edit
poetry install
✅ 4. Activate the Virtual Environment
To activate the Poetry environment:

bash
Copy
Edit
poetry shell
🔥 Usage
✅ Fetching Papers
To fetch papers based on a query:

bash
Copy
Edit
poetry run python src/aganitha_papers/main.py fetch "cancer treatment" --debug
cancer treatment → Your search query.

--debug → (Optional) Enables debug mode to display query info and filtering stats.

✅ Sample Output:

java
Copy
Edit
📊 Total papers fetched: 10  
📚 Papers kept (academic + mixed): 9  
❌ Papers excluded (non-academic only): 1  
✅ Results saved to output/results.csv  
📊 CSV Output Format
The resulting results.csv contains the following fields:

PubmedID: The unique ID of the paper.

Title: Title of the research paper.

Authors: List of authors.

Journal: Journal name where the paper was published.

PublicationDate: Date of publication.

Affiliations: Author affiliations.

Abstract: Abstract of the paper.

✅ Running Unit Tests
The project includes unit tests to verify the filtering logic.
Run the tests using:

bash
Copy
Edit
poetry run python -m unittest tests/test_papers.py
🔥 Troubleshooting
If you encounter module import issues, ensure you set the PYTHONPATH:

bash
Copy
Edit
$env:PYTHONPATH = "src"   # For Windows
export PYTHONPATH=src     # For Linux/Mac
📌 Known Issues
API Rate Limits: The PubMed API may impose rate limits. In such cases, consider adding retries or handling rate-limit errors.

Non-standard affiliations: Some papers might have inconsistent affiliation formats, which could affect filtering accuracy.

📚 References
PubMed API Documentation

Poetry Documentation

👨‍💻 Contributing
Contributions are welcome!
If you’d like to contribute:

Fork the repository.

Create a new branch.

Commit your changes.

Open a pull request.

⚖️ License
This project is licensed under the MIT License.
See the LICENSE file for more details.