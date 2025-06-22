from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def get_book_info(isbn):
    # Set Chrome options for headless mode
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Set up the Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Go to the ISBN search page
        driver.get(f"https://isbnsearch.org/isbn/{isbn}")
        time.sleep(2)  # Give the page time to load

        # Look for title and author in the updated structure
        info_box = driver.find_element(By.CLASS_NAME, "bookinfo")

        title = info_box.find_element(By.TAG_NAME, "h1").text
        
        # Find all <p> tags inside bookinfo
        paragraphs = info_box.find_elements(By.TAG_NAME, "p")
        author = "Unknown"
        for p in paragraphs:
            try:
                label = p.find_element(By.TAG_NAME, "strong")
                if "Author" in label.text:
                    author = p.text.replace("Author:", "").strip().strip('"')
                    break
            except:
                continue

        return {"title": title, "author": author}

    except Exception as e:
        print(f"Error retrieving book info: {e}")
        return None
    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    # isbn_input = input("Enter ISBN: ").strip()
    isbn_input = 9780593139776
    book_info = get_book_info(isbn_input)
    if book_info:
        print(f"Title: {book_info['title']}")
        print(f"Author: {book_info['author']}")
