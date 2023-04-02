# HTTP-Status-Code-Analyzer
This Python script tests a list of URLs for their HTTP status codes and categorizes them accordingly. 

# HTTP Status Code Analyzer
The HTTP Status Code Analyzer is a Python command-line tool that tests a list of URLs for their HTTP status codes and categorizes them accordingly. It can help identify URLs that may be broken, have access denied, or experience other issues.

## Usage
### Clone the repository:
git clone https://github.com/YSSVirus/HTTP-Status-Code-Analyzer.git
### Change into the project directory:
cd HTTP-Status-Code-Analyzer
### Run the script with a file containing the list of URLs or domains to test:
python3 status_analyzer.py FILE
Replace FILE with the name of your file.

## Output
The tool will create a directory called Tested_urls and output the categorized URLs to individual files named after their HTTP status codes (e.g. 200_urls.txt, 404_urls.txt).

## Dependencies
The tool uses the requests library to make HTTP requests to the URLs in the input file.

### Contributing
Contributions are welcome! If you would like to add a new feature or fix a bug, please open an issue to discuss the proposed changes.
