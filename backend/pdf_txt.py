from pypdf import PdfReader
import json
import re
from datetime import datetime 
import glob
from pathlib import Path

# As a function?


for path in sorted(glob.glob("././test*.pdf")):
# def get_stuff(path):
    reader = PdfReader(path)
    text = "\n".join(p.extract_text() for p in reader.pages)
    results = {}

    flat = re.sub(r"\s+", " ", text)
    cash = re.search(r"(Cash\s*Subtotal)\s*:?\s *\$?\s*([\d,]+\.\d{2})", flat, re.IGNORECASE)
    visa = re.search(r"(Visa\s*Subtotal)\s*:?\s *\$?\s*([\d,]+\.\d{2})", flat, re.IGNORECASE)
    discover = re.search(r"(Discover\s*Subtotal)\s*:?\s *\$?\s*([\d,]+\.\d{2})", flat, re.IGNORECASE)
    mastercard = re.search(r"(MasterCard\s*Subtotal)\s*:?\s *\$?\s*([\d,]+\.\d{2})", flat, re.IGNORECASE)
    strip_date = re.search(r"[A-Za-z]{3},\s*[A-Za-z]{3}\s+\d{1,2},\s*\d{4}", flat)
    user_match = re.search(r"Users?\s*:?\s*([^()]+?)\s*\(([^)]+)\)", flat, re.IGNORECASE)

    #results["File_name"]=path

    if strip_date:
        dt = datetime.strptime(strip_date.group(), "%a, %b %d, %Y")
        
        weekday=dt.strftime("%a")
        month=dt.strftime("%b")
        date=dt.strftime("%d")
        year=dt.strftime("%Y")
        
        results["Weekday"]=weekday
        results["Month"]= month
        results["Date"]=date
        results["Year"]=year

    if user_match:
        results["Users"] = user_match.group(1)
        results["POS_username"] = user_match.group(2)
    else:
        print("Users not found")
        
    matches = [
        ("Cash", cash),
        ("Visa", visa),
        ("Discover", discover),
        ("MasterCard", mastercard),
    ]

    for name, match in matches:
        if match:
            results[match.group(1)] = match.group(2)
        else:
            print(f"{name} not found")
        
    folder_path = Path("test_out")
    folder_path.mkdir(parents=True, exist_ok=True)
    out_path = folder_path / Path(path).with_suffix(".json").name
    
    with open(out_path, "w", encoding="utf-8") as fp:
        json.dump(results, fp, indent=4)
