import wikipediaapi

def read_wikipedia_page(page_title):
    # Create a Wikipedia object for the English language
    wiki_wiki = wikipediaapi.Wikipedia('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0')

    # Get the page based on the title provided
    page = wiki_wiki.page(page_title)

    # Check if the page exists
    if page.exists():
        print(f"Title: {page.title}\n")
        print(f"Summary:\n{page.summary}\n")
    else:
        print(f"The page '{page_title}' does not exist on Wikipedia.")

def main():
    # Input the title of the Wikipedia page
    page_title = input("Enter the title of the Wikipedia page you want to read: ")
    
    # Read the Wikipedia page
    read_wikipedia_page(page_title)

if __name__ == "__main__":
    main()
