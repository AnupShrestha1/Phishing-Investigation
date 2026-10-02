# Phishing Investigation Lab

A practical SOC/threat-analysis project for investigating phishing and social-engineering emails using preserved evidence, email-header analysis, IOC extraction, safe enrichment, MITRE ATT&CK mapping, and automated analyst reporting.

---

## Overview

This project demonstrates a repeatable workflow for analyzing suspicious emails from initial evidence preservation through final analyst reporting.

The project combines:

* Manual security analysis
* Python-based evidence processing
* IOC extraction and storage
* Safe IOC enrichment
* Social-engineering analysis
* MITRE ATT&CK mapping
* Risk assessment
* Automated PDF report generation

The goal is not to automatically declare every suspicious email malicious. Instead, automation handles repetitive evidence-processing tasks while the analyst makes the final investigative assessment.

---

## Investigation Workflow

```text
Phishing / Social Engineering Email
                ↓
        Preserve Evidence
                ↓
        Analyze Headers
                ↓
     Analyze Sender Identity
                ↓
       Analyze Email Content
                ↓
    Analyze URLs / Attachments
                ↓
         Extract IOCs
                ↓
        Enrich Relevant IOCs
                ↓
 Identify Social-Engineering Techniques
                ↓
      Map to MITRE ATT&CK
                ↓
       Assess Risk / Confidence
                ↓
        Analyst Conclusion
                ↓
     Defensive Recommendations
                ↓
         Generate PDF Report
```

---

## Project Structure

```text
Phishing-Investigation-Lab/
│
├── samples/
│   ├── emails/
│   └── attachments/
│
├── evidence/
│   ├── headers/
│   └── screenshots/
│
├── iocs/
│   ├── urls.csv
│   ├── domains.csv
│   ├── ips.csv
│   ├── hashes.csv
│   └── iocs.json
│
├── scripts/
│   ├── email_parser.py
│   ├── ioc_extractor.py
│   └── report_generator.py
│
├── analysis/
│   ├── case-001.md
│   ├── case-002.md
│   └── case-003.md
│
├── reports/
│   ├── case-001-report.pdf
│   ├── case-002-report.pdf
│   └── case-003-report.pdf
│
├── screenshots/
│
├── docs/
│   ├── methodology.md
│   └── investigation-playbook.md
│
└── README.md
```

---

## Cases Investigated

### Case 001 — McAfee Billing Scam

**Classification:** Phishing / Billing Scam

The message impersonates a security-product billing notification and attempts to create concern about an unexpected charge.

Investigation areas included:

* Authentication anomalies
* Sender identity mismatch
* Financial-payment pretext
* Brand/product impersonation
* Suspicious contact information
* Public scam-report correlation
* IOC extraction
* MITRE ATT&CK mapping

Relevant techniques identified:

* T1566 — Phishing
* T1036 — Masquerading

---

### Case 002 — Military Advance-Fee Scam

**Classification:** Social Engineering / Advance-Fee Scam

The message impersonates a military officer and claims that a large fund requires secure storage.

The investigation identified:

* Authority impersonation
* Military identity claims
* Secrecy and trust-building
* Large-fund claims
* Promise of financial reward
* From/Reply-To inconsistency
* Historical reuse of the same scam narrative

Relevant techniques identified:

* T1566 — Phishing
* T1036 — Masquerading

---

### Case 003 — DBS/POSB Digital Token Phishing

**Classification:** Phishing / Credential-Theft Attempt

The message impersonates DBS/POSB and claims that the recipient's digital banking authentication token requires an update.

The investigation identified:

* Financial-institution impersonation
* Security/authentication pretext
* Account-update call to action
* Unrelated Firebase-hosted sender domain
* External redirect infrastructure
* HTML-only phishing URL
* Legitimate shared infrastructure being used in a suspicious context

Authentication results included SPF PASS and DKIM PASS for Firebase-associated infrastructure, while DMARC returned a processing error.

Relevant techniques identified:

* T1566 — Phishing
* T1036 — Masquerading

---

## Python Automation

### Email Parser

`scripts/email_parser.py`

The parser extracts basic email information:

* Case ID
* Subject
* From
* Reply-To
* Sender
* Date
* Plain-text body

Run it with:

```powershell
python scripts\email_parser.py case-001
```

---

### IOC Extractor

`scripts/ioc_extractor.py`

The IOC extractor automatically identifies:

* URLs
* Domains
* IPv4 addresses
* Email addresses
* MD5 hashes
* SHA-1 hashes
* SHA-256 hashes

Results are stored in:

```text
iocs/
├── urls.csv
├── domains.csv
├── ips.csv
├── hashes.csv
└── iocs.json
```

Run:

```powershell
python scripts\ioc_extractor.py case-001
```

The extractor preserves existing cases and analyst-entered IOC context.

---

### Report Generator

`scripts/report_generator.py`

The report generator converts an investigation Markdown file into a PDF.

It is **case-independent**.

For example:

```powershell
python scripts\report_generator.py case-001
```

reads:

```text
analysis/case-001.md
```

and creates:

```text
reports/case-001-report.pdf
```

A future case can be processed without modifying the generator:

```powershell
python scripts\report_generator.py case-004
```

---

## Investigation Documentation

The project contains two supporting documents.

### Methodology

`docs/methodology.md`

Documents the investigation methodology, including:

* Evidence preservation
* Header analysis
* Sender analysis
* Content analysis
* IOC extraction
* IOC enrichment
* Social-engineering analysis
* MITRE ATT&CK mapping
* Risk assessment
* Automation vs. analyst judgment
* Reporting
* Reproducibility
* Limitations

### Investigation Playbook

`docs/investigation-playbook.md`

Provides a practical step-by-step procedure for investigating a new suspicious email.

---

## IOC Handling

Extracted indicators are not automatically classified as malicious.

Each IOC is evaluated according to its context.

For example, an IP address belonging to Google, Firebase, or another shared service may simply represent legitimate infrastructure.

The investigation therefore follows:

```text
IOC
 ↓
Context
 ↓
Enrichment
 ↓
Assessment
```

rather than:

```text
IOC → Automatically Malicious
```

This is important when investigating phishing campaigns that abuse legitimate cloud, email, hosting, or redirect services.

---

## MITRE ATT&CK

MITRE ATT&CK techniques are mapped only when supported by the observed behavior.

Examples used in the investigations include:

* **T1566 — Phishing**
* **T1036 — Masquerading**

Specific sub-techniques are not assigned automatically. The observed behavior must support the applicable technique definition.

---

## Safety

This project uses static analysis wherever possible.

Investigation rules include:

* Do not click suspicious links.
* Do not execute suspicious attachments.
* Preserve the original `.eml`.
* Use safe/defanged URLs when documenting suspicious destinations.
* Do not interact with potentially malicious infrastructure unnecessarily.
* Use isolated analysis environments when additional technical analysis requires them.

The project is intended for defensive investigation and evidence analysis.

---

## Reproducibility

A new case follows the same general workflow:

```text
1. Preserve the email
2. Parse the email
3. Analyze headers
4. Analyze sender identity
5. Analyze content
6. Inspect URLs / attachments safely
7. Extract IOCs
8. Enrich relevant indicators
9. Identify social-engineering techniques
10. Map supported behavior to MITRE ATT&CK
11. Assess severity and confidence
12. Write the Markdown investigation
13. Generate the PDF report
14. Verify the report
```

The automated components can then be reused for additional cases.

---

## Current Capabilities

The project currently supports:

* `.eml` email parsing
* Header investigation
* Sender/Reply-To analysis
* IOC extraction
* IOC CSV storage
* IOC JSON storage
* Analyst IOC context
* Safe enrichment workflow
* Social-engineering analysis
* MITRE ATT&CK mapping
* Risk assessment
* Markdown case reports
* Automated PDF generation
* Multiple independent investigation cases

---

## Limitations

The current implementation has several limitations:

* The email parser primarily displays the plain-text body.
* HTML-only URLs require additional MIME/HTML-specific extraction.
* IOC extraction can identify hashes that are not necessarily file hashes.
* Shared infrastructure can make attribution difficult.
* Public reputation information may be incomplete or historical.
* Automated extraction does not determine whether an IOC is malicious.
* Analyst judgment remains necessary for classification, enrichment interpretation, MITRE mapping, and risk assessment.

These limitations are intentionally documented rather than hidden.

---

## Future Improvements

Possible future improvements include:

* HTML MIME-part IOC extraction
* Better URL normalization and defanging
* Attachment metadata extraction
* Automatic SHA-256 calculation for preserved attachments
* More structured enrichment
* Additional investigation cases
* Automated timeline extraction
* Improved PDF styling
* Detection-rule generation from confirmed findings

These are future enhancements and are not required for the current investigation workflow.

---

## Project Goal

The project demonstrates how a SOC/threat analyst can combine:

```text
Evidence Handling
        +
Email Security Analysis
        +
IOC Analysis
        +
Threat Intelligence
        +
MITRE ATT&CK
        +
Python Automation
        +
Analyst Reporting
```

into a repeatable phishing-investigation workflow.

The emphasis is on **evidence-based analysis and reusable automation**, rather than simply producing a phishing classification.
