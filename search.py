from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def search_penguin_by_isbn(isbn):
    # Setup headless browser
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.penguinrandomhouse.com/books/")

        wait = WebDriverWait(driver, 10)
        # Get all matching elements and click the first visible one
        elements = driver.find_elements(By.CLASS_NAME, "search-icon-link")
        # Filter for the visible one
        for el in elements:
            if el.is_displayed():
                el.click()
                break
        else:
            raise Exception("No visible search icon found")

        search_box = wait.until(EC.visibility_of_element_located((By.ID, "search-box")))
        # Step 3: Type query and press Enter
        # Enter ISBN and press Enter
        search_box.send_keys(isbn)
        search_box.send_keys(Keys.ENTER)

        page_title = driver.title.strip()

        # Example structure: "Braided Heritage by Jessica B. Harris: 9780593139776 | PenguinRandomHouse.com: Books"
        if " by " in page_title:
            main_part = page_title.split(" | ")[0]  # Remove site branding
            book_title, rest = main_part.split(" by ", 1)
            author = rest.split(":")[0].strip()
        else:
            print("Could not parse title and author.")

        return {"title": book_title, "author": author, "url": driver.current_url}

    except Exception as e:
        print(f"Search failed: {e}")
        return None
    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    isbn = "9780593139776"
    result = search_penguin_by_isbn(isbn)
    if result:
        print(f"Title: {result['title']}")
        print(f"Author: {result['author']}")
        print(f"URL: {result['url']}")