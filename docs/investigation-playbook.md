# Phishing Investigation Playbook

## 1. Purpose

This playbook provides a practical procedure for investigating suspicious phishing and social-engineering emails in the `Phishing-Investigation-Lab`.

It is intended to provide a consistent process for each investigation case while keeping potentially dangerous content isolated from the analyst environment.

---

## 2. Safety Rules

Before investigating a suspicious message:

* Preserve the original email.
* Do not click suspicious links.
* Do not copy suspicious URLs into a normal browser.
* Do not execute suspicious attachments.
* Do not open unknown files unless the investigation environment is specifically designed for safe analysis.
* Prefer static analysis.
* Use defanged indicators when documenting potentially dangerous URLs.
* Treat public reputation results as supporting evidence rather than automatic verdicts.

---

## 3. Case Preparation

Create or preserve the case using the standard structure:

```text
samples/emails/case-XXX.eml
analysis/case-XXX.md
reports/case-XXX-report.pdf
```

If supporting evidence is required:

```text
evidence/headers/case-XXX-headers.txt
evidence/screenshots/
```

The original email should remain unchanged.

---

## 4. Step 1 — Parse the Email

Run the reusable email parser:

```powershell
python scripts\email_parser.py case-XXX
```

Review:

* Subject
* From
* Reply-To
* Sender
* Date
* Message body

Record unusual relationships between these fields.

---

## 5. Step 2 — Analyze the Headers

Inspect the complete headers.

Pay particular attention to:

```text
Authentication-Results
Received
From
Reply-To
Sender
Message-ID
Date
```

Record:

* Sending IP
* Envelope sender
* SPF result
* DKIM result
* DKIM signing domain
* DMARC result
* Composite authentication
* Spam-confidence indicators when present

### Important interpretation rule

Do not treat authentication success as proof that the message is legitimate.

For example:

```text
SPF PASS
DKIM PASS
```

may only demonstrate that the message was authorized and signed by the sending domain.

Compare that domain with the organization the message claims to represent.

---

## 6. Step 3 — Analyze Sender Identity

Compare:

```text
Display Name
      ↓
From Address
      ↓
Reply-To
      ↓
Sender
      ↓
Authenticated Domain
```

Look for:

* Display-name impersonation
* Unexpected Reply-To addresses
* Different From and Reply-To domains
* Unrelated sender domains
* Free-mail addresses used for organizational impersonation
* Infrastructure that does not match the claimed organization

Document the mismatch rather than immediately declaring the sender compromised.

---

## 7. Step 4 — Analyze the Message Content

Read the message without interacting with its links or attachments.

Look for:

### Urgency

Examples:

* "Your account will be disabled."
* "Immediate action required."
* "Your payment failed."

### Authority

Examples:

* Bank representatives
* Military personnel
* Executives
* Government officials
* Security teams

### Financial pressure

Examples:

* Unexpected charges
* Refund claims
* Invoices
* Payment requests
* Investment opportunities

### Credential or security requests

Examples:

* Password resets
* Token updates
* Account verification
* MFA requests
* Security confirmation

### Reward or secrecy

Examples:

* Large financial rewards
* Requests to keep information confidential
* Requests to move communication to a private email

Record the specific language that supports the assessment.

---

## 8. Step 5 — Inspect URLs Safely

Do not open suspicious URLs.

Instead, extract and document:

* Full URL
* Domain
* Subdomain
* Path
* Redirect domain
* Tracking parameters
* Relationship to the claimed organization

Use defanged notation when appropriate:

```text
hxxps://example[.]com/login
```

If the visible text says:

```text
Update Your Account
```

but the underlying link uses an unrelated domain, document that discrepancy.

Legitimate third-party services may be used in malicious campaigns. Therefore:

```text
Third-party infrastructure ≠ automatically malicious
```

The important question is how the infrastructure is being used in the specific message.

---

## 9. Step 6 — Inspect Attachments Safely

If attachments exist:

* Record the filename.
* Record the file type.
* Record the size.
* Calculate cryptographic hashes when appropriate.
* Do not execute the file.
* Do not enable macros.
* Do not open suspicious documents in a normal desktop environment.

Document whether the attachment appears relevant to the social-engineering objective.

If there is no attachment, explicitly record that fact.

---

## 10. Step 7 — Extract IOCs

Run:

```powershell
python scripts\ioc_extractor.py case-XXX
```

The extractor identifies:

* URLs
* Domains
* IP addresses
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

Review the extracted results rather than assuming every value is malicious.

---

## 11. Step 8 — Validate IOC Context

For each relevant IOC, determine why it appears in the message.

Examples:

```text
domain → sender domain
domain → redirect infrastructure
domain → legitimate embedded image
IP → sending infrastructure
IP → DNS resolution
email → visible sender
email → Reply-To
hash → attachment
hash → email metadata
```

This distinction is important because the same indicator type can have very different investigative significance.

---

## 12. Step 9 — Enrich Relevant Indicators

Only enrich indicators that are useful to the investigation.

Possible enrichment includes:

* DNS resolution
* Domain information
* Public reputation
* Historical abuse reports
* Public security research
* Public scam reports

Record the source and what it actually establishes.

Avoid statements such as:

```text
The IP belongs to X, therefore X is malicious.
```

Instead document the relationship precisely:

```text
The IP is shared infrastructure used by the service.
Public reporting documents abuse of the service in other campaigns.
The service itself is not classified as malicious.
```

---

## 13. Step 10 — Identify Social-Engineering Techniques

Determine which techniques are supported by the message.

Possible findings include:

* Financial-institution impersonation
* Brand impersonation
* Authority impersonation
* Security pretext
* Urgency
* Account-update request
* Payment or billing deception
* Advance-fee fraud
* Reward-based manipulation
* Secrecy requests

Support each finding with evidence from the email.

---

## 14. Step 11 — Map to MITRE ATT&CK

Map only techniques supported by the evidence.

Common examples include:

```text
T1566 — Phishing
T1036 — Masquerading
```

Do not automatically assign a phishing sub-technique simply because a message contains a link or attachment.

Confirm that the observed behavior satisfies the applicable ATT&CK definition before using a specific sub-technique.

---

## 15. Step 12 — Determine Severity and Confidence

Assign:

### Severity

Consider:

* Potential financial impact
* Credential-theft potential
* Account-compromise potential
* Sensitivity of the impersonated organization
* Potential consequences for the recipient

### Confidence

Consider:

* Strength of header evidence
* Sender identity mismatch
* Social-engineering indicators
* IOC context
* Enrichment evidence
* Historical evidence
* Consistency between independent findings

Document why the selected severity and confidence are appropriate.

---

## 16. Step 13 — Write the Case Analysis

Create:

```text
analysis/case-XXX.md
```

Use the established report structure:

1. Case Summary
2. Header and Authentication Analysis
3. Sender Identity Analysis
4. Content and Social-Engineering Analysis
5. URL and Attachment Analysis
6. IOC Assessment
7. Enrichment Findings
8. MITRE ATT&CK Mapping
9. Investigation Timeline
10. Risk Assessment
11. Analyst Conclusion
12. Recommended Defensive Actions

The exact sections may be adjusted when a case requires different evidence, but the investigation should remain logically structured.

---

## 17. Step 14 — Generate the PDF Report

Run:

```powershell
python scripts\report_generator.py case-XXX
```

The generator reads:

```text
analysis/case-XXX.md
```

and creates:

```text
reports/case-XXX-report.pdf
```

The generator is case-independent and should not require changes when a new investigation is added.

---

## 18. Step 15 — Verify the Report

Open the generated PDF and verify:

* Title
* Case information
* Headings
* Paragraph formatting
* Bullet lists
* Numbered lists
* IOC tables
* URLs and domai
