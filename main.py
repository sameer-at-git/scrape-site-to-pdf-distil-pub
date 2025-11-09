# main.py
from collect_links import collect_links
from webpage_to_pdf import webpage_to_pdf

def main():
    links = collect_links()
    for link in links:
        try:
            pdf_path = webpage_to_pdf(link)
            print(f"Saved: {pdf_path}")
        except Exception as e:
            print(f"Error saving {link}: {e}")

if __name__ == "__main__":
    main()
