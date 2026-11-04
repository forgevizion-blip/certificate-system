"""
Roster Generator for Hackathon Certificate System
Reads student data and writes to roster.csv and roster_standard.csv
preserving leading zeros for Google Sheets.
Columns: Registration No., Name, Team, Email, Certificate ID 1, Certificate ID 2,
         Certificate ID 3, Certificate ID 4, Certificate ID 5, Status
"""

import csv
from pathlib import Path

FIELDNAMES = [
    "Registration No.",
    "Name",
    "Team",
    "Email",
    "Certificate ID 1",
    "Certificate ID 2",
    "Certificate ID 3",
    "Certificate ID 4",
    "Certificate ID 5",
    "Status"
]

def generate_roster(students, output_path="roster.csv", use_formula_text=True):
    """
    students: list of tuples: (reg_no, name, team, email)
    """
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(FIELDNAMES)
        
        for student in students:
            reg_no = student[0]
            name = student[1]
            team = student[2]
            email = student[3] if len(student) > 3 else f"{reg_no}@example.com"
            
            # Format reg_no to preserve leading zeros in Google Sheets
            reg_val = f'="{reg_no}"' if use_formula_text else str(reg_no)
            writer.writerow([reg_val, name, team, email, "", "", "", "", "", ""])

if __name__ == "__main__":
    sample_students = [
        ("00101", "Alice Johnson", "Null Pointers", "alice.johnson@example.com"),
        ("00102", "Bob Smith", "Byte Bandits", "bob.smith@example.com"),
        ("00103", "Charlie Brown", "Kernel Panic", "charlie.brown@example.com"),
        ("00104", "Diana Prince", "Stack Overflowers", "diana.prince@example.com"),
        ("00105", "Evan Wright", "Syntax Terrors", "evan.wright@example.com"),
    ]
    base_dir = Path(__file__).parent
    
    # 1. roster.csv (with formula text for Sheets import)
    out_file = base_dir / "roster.csv"
    generate_roster(sample_students, out_file, use_formula_text=True)
    print(f"Generated {out_file}")
    
    # 2. roster_standard.csv (plain CSV)
    out_standard = base_dir / "roster_standard.csv"
    generate_roster(sample_students, out_standard, use_formula_text=False)
    print(f"Generated {out_standard}")
