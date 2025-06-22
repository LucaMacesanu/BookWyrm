import csv

def read_isbns_from_csv(csv_file_path):
    """
    Reads a CSV file and extracts the first column as a list of ISBN strings.
    
    Args:
        csv_file_path (str): Path to the CSV file.

    Returns:
        List[str]: List of ISBN strings from the first column.
    """
    isbns = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[0].strip():
                isbns.append(row[0].strip())
    return isbns

if __name__=="__main__":
    isbns = read_isbns_from_csv("./sample_isbns.csv")
    print(isbns)