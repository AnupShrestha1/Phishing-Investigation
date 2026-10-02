import sys
import re
from pathlib import Path
from email import policy
from email.parser import BytesParser


BASE_DIR = Path(__file__).resolve().parent.parent
EMAIL_DIR = BASE_DIR / "samples" / "emails"


def parse_email(case_id):
    email_path = EMAIL_DIR / f"{case_id}.eml"

    if not email_path.exists():
        print(f"Error: {email_path} not found.")
        return

    with open(email_path, "rb") as f:
        email = BytesParser(policy=policy.default).parse(f)

    print("=== EMAIL DETAILS ===")
    print("Case:", case_id)
    print("Subject:", email["Subject"])
    print("From:", email["From"])
    print("Reply-To:", email["Reply-To"])
    print("Sender:", email["Sender"])
    print("Date:", email["Date"])

    body = email.get_body(preferencelist=("plain",))

    if body:
        print("\n--- EMAIL BODY ---")
        print(body.get_content())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts\\email_parser.py case-001")
        sys.exit(1)

    case_id = sys.argv[1]

    if not re.fullmatch(r"case-\d{3}", case_id):
        print("Error: case ID must use the format case-001.")
        sys.exit(1)

    parse_email(case_id)