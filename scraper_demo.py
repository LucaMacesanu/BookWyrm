import search
import csv_utils

if __name__=="__main__":
    isbns = csv_utils.read_isbns_from_csv("./sample_isbns.csv")
    for isbn in isbns:
        book_info = search.search_penguin_by_isbn(isbn)
        if book_info:
            print(f"Title: {book_info['title']}")
            print(f"Author: {book_info['author']}")