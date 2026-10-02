import re
import json
import sys
import csv
from pathlib import Path
from email import policy
from email.parser import BytesParser


BASE_DIR = Path(__file__).resolve().parent.parent
EMAIL_DIR = BASE_DIR / "samples" / "emails"
IOC_DIR = BASE_DIR / "iocs"

JSON_OUTPUT = IOC_DIR / "iocs.json"

CSV_FILES = {
    "urls": IOC_DIR / "urls.csv",
    "domains": IOC_DIR / "domains.csv",
    "ips": IOC_DIR / "ips.csv",
    "hashes": IOC_DIR / "hashes.csv",
}


def extract_iocs(case_id):
    email_path = EMAIL_DIR / f"{case_id}.eml"

    if not email_path.exists():
        print(f"Error: {email_path} not found.")
        return

    with open(email_path, "rb") as f:
        email = BytesParser(policy=policy.default).parse(f)

    body = email.get_body(preferencelist=("plain",))
    text = body.get_content() if body else ""

    headers = "\n".join(
        str(email.get(header, ""))
        for header in email.keys()
    )

    full_text = headers + "\n" + text

    ips = sorted(set(re.findall(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        full_text
    )))

    emails = sorted(set(re.findall(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        full_text
    )))

    urls = sorted(set(re.findall(
        r"https?://[^\s<>]+",
        full_text
    )))

    domains = sorted(set(
        address.split("@", 1)[1]
        for address in emails
    ))

    hashes = extract_hashes(full_text)

    ioc = {
        "case": case_id,
        "ip_addresses": ips,
        "email_addresses": emails,
        "domains": domains,
        "urls": urls,
        "hashes": hashes
    }

    save_json(ioc)

    update_csv("urls", case_id, urls)
    update_csv("domains", case_id, domains)
    update_csv("ips", case_id, ips)
    update_hash_csv(case_id, hashes)

    print("=== IOC EXTRACTION ===")
    print(json.dumps(ioc, indent=4))
    print(f"\nSaved to {JSON_OUTPUT}")
    print("CSV IOC files updated.")


def extract_hashes(text):
    hashes = []

    # MD5
    md5_pattern = r"\b[a-fA-F0-9]{32}\b"

    # SHA-1
    sha1_pattern = r"\b[a-fA-F0-9]{40}\b"

    # SHA-256
    sha256_pattern = r"\b[a-fA-F0-9]{64}\b"

    for value in re.findall(sha256_pattern, text):
        hashes.append({
            "hash": value.lower(),
            "type": "SHA256"
        })

    for value in re.findall(sha1_pattern, text):
        hashes.append({
            "hash": value.lower(),
            "type": "SHA1"
        })

    for value in re.findall(md5_pattern, text):
        hashes.append({
            "hash": value.lower(),
            "type": "MD5"
        })

    # Remove duplicates.
    unique_hashes = {}

    for item in hashes:
        unique_hashes[item["hash"]] = item["type"]

    return [
        {
            "hash": value,
            "type": hash_type
        }
        for value, hash_type in sorted(unique_hashes.items())
    ]


def save_json(ioc):
    if JSON_OUTPUT.exists():
        try:
            with open(JSON_OUTPUT, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except (json.JSONDecodeError, OSError):
            existing = []
    else:
        existing = []

    if isinstance(existing, dict):
        existing = [existing]

    existing = [
        item for item in existing
        if item.get("case") != ioc["case"]
    ]

    existing.append(ioc)
    existing.sort(key=lambda item: item.get("case", ""))

    with open(JSON_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=4)


def update_csv(ioc_type, case_id, indicators):
    path = CSV_FILES[ioc_type]

    if ioc_type in ("domains", "ips"):
        header = ["case_id", "ioc", "context"]
    else:
        header = ["case_id", "ioc"]

    existing_rows = []

    if path.exists():
        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                row = {
                    key.lstrip("\ufeff"): value
                    for key, value in row.items()
                }

                existing_rows.append(row)

    existing_case_rows = {
        row.get("ioc"): row
        for row in existing_rows
        if row.get("case_id") == case_id
    }

    existing_rows = [
        row for row in existing_rows
        if row.get("case_id") != case_id
    ]

    for indicator in indicators:
        row = {
            "case_id": case_id,
            "ioc": indicator,
        }

        if ioc_type in ("domains", "ips"):
            old_row = existing_case_rows.get(indicator)

            if old_row:
                row["context"] = old_row.get("context", "")
            else:
                row["context"] = ""

        existing_rows.append(row)

    existing_rows.sort(
        key=lambda row: (
            row.get("case_id", ""),
            row.get("ioc", "")
        )
    )

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=header,
            extrasaction="ignore"
        )

        writer.writeheader()
        writer.writerows(existing_rows)


def update_hash_csv(case_id, hashes):
    path = CSV_FILES["hashes"]
    header = ["case_id", "hash", "type", "context"]

    existing_rows = []

    if path.exists():
        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                row = {
                    key.lstrip("\ufeff"): value
                    for key, value in row.items()
                }

                existing_rows.append(row)

    existing_case_rows = {
        row.get("hash"): row
        for row in existing_rows
        if row.get("case_id") == case_id
    }

    existing_rows = [
        row for row in existing_rows
        if row.get("case_id") != case_id
    ]

    for item in hashes:
        hash_value = item["hash"]

        old_row = existing_case_rows.get(hash_value)

        row = {
            "case_id": case_id,
            "hash": hash_value,
            "type": item["type"],
            "context": old_row.get("context", "") if old_row else ""
        }

        existing_rows.append(row)

    existing_rows.sort(
        key=lambda row: (
            row.get("case_id", ""),
            row.get("hash", "")
        )
    )

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=header,
            extrasaction="ignore"
        )

        writer.writeheader()
        writer.writerows(existing_rows)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts\\ioc_extractor.py case-001")
        sys.exit(1)

    case_id = sys.argv[1]

    if not re.fullmatch(r"case-\d{3}", case_id):
        print("Error: case ID must use the format case-001.")
        sys.exit(1)

    extract_iocs(case_id)