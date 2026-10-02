# Phishing Investigation Methodology

## 1. Purpose

This project provides a repeatable methodology for investigating phishing and social-engineering emails using preserved email evidence, header analysis, IOC extraction, safe enrichment, MITRE ATT&CK mapping, and analyst reporting.

The objective is to reproduce a practical SOC/threat-analysis workflow while keeping potentially unsafe content isolated from the analyst environment.

The methodology is designed to support multiple investigation cases without assuming that every suspicious email uses the same technique or infrastructure.

---

## 2. Investigation Principles

The investigation follows these principles:

* Preserve the original email before analysis.
* Perform static analysis whenever possible.
* Do not open suspicious links.
* Do not execute suspicious attachments.
* Treat extracted IOCs as indicators requiring context, not automatically as malicious artifacts.
* Distinguish legitimate shared infrastructure from malicious use of that infrastructure.
* Separate authentication results from sender legitimacy.
* Record evidence before drawing conclusions.
* Attribute external reputation findings to their sources.
* Keep analyst judgment separate from automated extraction.
* Use consistent terminology and evidence standards across cases.

---

## 3. Investigation Workflow

Each case follows the following workflow:

```text
Email Sample
    ↓
Evidence Preservation
    ↓
Header Analysis
    ↓
Sender Identity Analysis
    ↓
Email Content Analysis
    ↓
URL / Attachment Analysis
    ↓
IOC Extraction
    ↓
IOC Enrichment
    ↓
Social-Engineering Analysis
    ↓
MITRE ATT&CK Mapping
    ↓
Risk Assessment
    ↓
Analyst Conclusion
    ↓
Defensive Recommendations
    ↓
PDF Report
```

---

## 4. Evidence Preservation

The original `.eml` file is preserved in:

```text
samples/emails/
```

The original evidence should not be modified during investigation.

Relevant header evidence can be preserved separately under:

```text
evidence/headers/
```

Screenshots and other supporting evidence are stored under:

```text
evidence/screenshots/
```

Preserving the original message allows the investigation to be reproduced and provides a reliable source for later analysis.

---

## 5. Header Analysis

Email headers are examined for information including:

* From
* Reply-To
* Sender
* To
* Date
* Message-ID
* Received headers
* Sending IP addresses
* Authentication-Results
* SPF
* DKIM
* DMARC
* Microsoft composite authentication where present
* Spam-confidence indicators where present

Authentication results are interpreted carefully.

For example:

* SPF PASS indicates that the sending infrastructure was authorized for the relevant envelope-sender domain.
* DKIM PASS indicates that the message signature was successfully verified for the signing domain.
* DMARC results describe authentication/alignment processing and must be interpreted according to the specific result.
* Composite authentication is a receiving-system assessment and is not absolute proof of sender legitimacy.

Authentication of a domain does not establish that the domain legitimately represents the organization claimed in the email.

---

## 6. Sender Identity Analysis

The claimed identity of the sender is compared with the actual authenticated infrastructure.

Relevant relationships include:

* Display name vs. email address
* From vs. Reply-To
* From vs. Sender
* Claimed organization vs. sender domain
* Sender domain vs. DKIM signing domain
* Sender infrastructure vs. claimed organization

A mismatch does not automatically prove malicious activity, but it can become significant when combined with suspicious content or social-engineering indicators.

---

## 7. Content Analysis

The message body is examined for social-engineering characteristics such as:

* Financial requests
* Account-security claims
* Credential requests
* Urgency
* Threats or consequences
* Requests for secrecy
* Authority impersonation
* Rewards or financial promises
* Suspicious contact information
* Unexpected account or payment notifications
* Requests to follow links or provide information

The analyst determines whether the message represents phishing, advance-fee fraud, impersonation, another form of social engineering, or another classification supported by the evidence.

---

## 8. URL and Attachment Analysis

URLs are analyzed without interacting with potentially malicious destinations.

The investigation records:

* URL
* Domain
* URL path
* Redirect infrastructure
* Relationship between the URL and the claimed organization

Legitimate third-party infrastructure may appear in malicious messages. Therefore, the presence of a legitimate service does not automatically make that service malicious.

Attachments are analyzed statically when present.

The investigation does not require executing an attachment to establish that a message is suspicious.

---

## 9. IOC Extraction

The project automates repetitive IOC extraction using:

```text
scripts/ioc_extractor.py
```

The extractor identifies:

* IPv4 addresses
* Email addresses
* Domains
* URLs
* MD5 hashes
* SHA-1 hashes
* SHA-256 hashes

The extracted indicators are stored in:

```text
iocs/
├── urls.csv
├── domains.csv
├── ips.csv
├── hashes.csv
└── iocs.json
```

The IOC database preserves information from previous cases and avoids unnecessary duplication.

Analyst-entered context is preserved separately from automated extraction.

---

## 10. IOC Assessment

IOC extraction does not automatically determine whether an indicator is malicious.

Each indicator is considered in context.

For example:

* A Google IP address may represent legitimate Google mail infrastructure.
* A Firebase IP address may represent legitimate shared hosting.
* A Gmail address may be legitimate infrastructure used by an attacker.
* A suspicious sender domain may be significant because of its relationship to the claimed organization rather than because the domain itself is conclusively malicious.

Therefore, the investigation distinguishes between:

```text
Extracted IOC
    ↓
Context
    ↓
Enrichment
    ↓
Assessment
```

rather than:

```text
Extracted IOC → Automatically Malicious
```

---

## 11. Safe IOC Enrichment

Selected indicators may be enriched using safe external sources.

Examples include:

* DNS information
* Domain information
* Public reputation information
* Historical abuse reports
* Public scam reports
* Public security research

Enrichment findings are treated as supporting evidence.

A shared hosting provider or infrastructure service should not be classified as malicious solely because an attacker used it.

Where historical abuse is relevant, the finding should be described as evidence concerning the specific use of the infrastructure rather than as proof that the entire service is malicious.

---

## 12. Social-Engineering Analysis

The investigation identifies the psychological or social mechanisms used by the message.

Examples include:

### Financial impersonation

The attacker presents the message as coming from a bank, payment provider, security company, or other financial organization.

### Authority impersonation

The attacker claims to be a military officer, executive, government official, or other trusted authority.

### Security pretext

The attacker claims that an account, token, password, or security mechanism requires immediate action.

### Urgency

The message creates pressure by suggesting that an account, payment, service, or transaction will be affected if the recipient does not act.

### Reward or financial promise

The message promises money or another benefit in exchange for cooperation.

### Brand impersonation

The message copies branding, terminology, formatting, or other characteristics associated with a legitimate organization.

These techniques are assessed together with the technical evidence.

---

## 13. MITRE ATT&CK Mapping

Relevant behaviors are mapped to MITRE ATT&CK techniques when supported by the evidence.

The mapping should describe the observed behavior rather than assign techniques solely because they are commonly associated with phishing.

For example:

* **T1566 — Phishing**
* **T1036 — Masquerading**

More specific sub-techniques should only be assigned when the evidence and applicable ATT&CK definitions support the mapping.

The absence of an attachment means that an attachment-specific phishing sub-technique should not be assigned.

---

## 14. Risk Assessment

Each case receives:

* Severity
* Confidence

Severity represents the potential impact of the observed activity.

Confidence represents how strongly the available evidence supports the investigation's conclusion.

The assessment considers factors such as:

* Target sensitivity
* Financial impact
* Credential-theft potential
* Authentication evidence
* Sender identity inconsistencies
* Social-engineering indicators
* Malicious or suspicious infrastructure
* Historical evidence
* Potential consequences of successful interaction

Severity and confidence are analyst assessments based on the collected evidence.

---

## 15. Automation vs. Analyst Judgment

Automation is intentionally limited to tasks that are repetitive and evidence-oriented.

### Automated

The project automates:

* Email parsing
* IOC extraction
* IOC database updates
* CSV generation
* JSON generation
* PDF report generation

### Manual

The analyst determines:

* Case classification
* IOC maliciousness
* Header interpretation
* Enrichment significance
* Social-engineering techniques
* MITRE ATT&CK mapping
* Severity
* Confidence
* Final conclusion
* Defensive recommendations

This separation reduces the risk of treating automated extraction as an automated verdict.

---

## 16. Reporting

Investigation findings are documented in:

```text
analysis/
```

Each case uses a separate Markdown file:

```text
analysis/case-001.md
analysis/case-002.md
analysis/case-003.md
```

The reusable report generator converts the Markdown investigation into a PDF:

```text
python scripts\report_generator.py case-001
```

The resulting report is stored in:

```text
reports/case-001-report.pdf
```

The same generator can process future cases without modifying the Python script.

For example:

```text
analysis/case-004.md
        ↓
report_generator.py case-004
        ↓
reports/case-004-report.pdf
```

---

## 17. Reproducibility

A new case should follow the same general process:

1. Preserve the `.eml` sample.
2. Run the email parser.
3. Run IOC extraction.
4. Inspect the headers.
5. Analyze sender identity.
6. Analyze the message content.
7. Inspect URLs and attachments safely.
8. Enrich relevant indicators.
9. Determine social-engineering techniques.
10. Map supported behavior to MITRE ATT&CK.
11. Assess severity and confidence.
12. Document the investigation in Markdown.
13. Generate the PDF report.
14. Verify the generated report.

This allows the project to demonstrate repeatable investigation rather than a collection of unrelated one-off analyses.

---

## 18. Limitations

The methodology has several limitations.

* IOC extraction depends on the content available in the email.
* HTML-only URLs may require MIME/HTML-specific extraction.
* Shared infrastructure can make infrastructure-based attribution difficult.
* Authentication results do not independently establish sender legitimacy.
* Public reputation sources may contain incomplete or historical information.
* An IOC appearing in a phishing email is not necessarily malicious.
* Automated extraction can identify indicators but cannot reliably replace analyst judgment.
* Some conclusions may remain uncertain when the available evidence is incomplete.

These limitations should be documented rather than hidden from the final assessment.
