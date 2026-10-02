# Case 001 — Initial Triage

## Subject
Hey - Your Confirmation for GGE is Complete

## Sender
Mardella Hunter <treid5271@gemalim.org>

## Reply-To
treid5271@gemalim.org

## Claimed Sender
Google Calendar <calendar-notification@google.com>

## Initial Indicators
- SPF: None
- DKIM: Fail
- DMARC: None
- Composite authentication: Fail
- Sender IP: 209.85.210.74
- Microsoft SCL: 8
- Urgency/payment theme: Yes
- Claimed brand: McAfee
- Claimed payment: USD 567.11
- Attachment: None observed
- URL: None observed

## Initial Assessment
The email presents itself as a Google Calendar notification while its content claims to be a McAfee subscription renewal requiring a USD 567.11 payment. Authentication results show DKIM failure, no SPF result, no DMARC policy result, and composite authentication failure.

The message uses a payment/renewal theme and provides telephone numbers as a proposed method of contact. These characteristics warrant further phishing investigation.

## Header Authentication Analysis

### SPF
Result: None

No SPF authentication result was established for the message.

### DKIM
Result: Fail

Two DKIM signatures were present:
- google.com
- gemalim-org.20230601.gappssmtp.com

Both signatures failed verification according to the Authentication-Results header.

### DMARC
Result: None

No DMARC authentication result/policy was established for the message.

### Microsoft Composite Authentication
Result: Fail

Microsoft's composite authentication check failed, providing additional evidence that the message did not establish trustworthy sender authentication.

### Spam Confidence
Microsoft SCL: 8

The receiving Microsoft mail infrastructure assigned an SCL of 8, indicating that the message was treated as having a high likelihood of being spam.

### Initial Header Assessment
The authentication results contain multiple anomalies, including DKIM verification failures and composite authentication failure. These findings increase the suspicion associated with the message and should be considered together with the sender identity and message content.

## Content Analysis

### Brand / Identity Inconsistency
The message is presented through Google Calendar infrastructure, while the visible content claims to be a McAfee subscription renewal.

The sender identity is also inconsistent:
- From: Mardella Hunter <treid5271@gemalim.org>
- Sender: Google Calendar <calendar-notification@google.com>
- Organizer: Mardella Hunter <treid5271@gemalim.org>

### Payment / Renewal Theme
The email claims that USD 567.11 will be automatically charged for a subscription renewal.

It provides:
- Order number: CV21153GGE2162
- Product: DefenderX Ultimate
- Plan: 4-Year Warranty
- Payment method: Auto Debit
- Client ID: SB3CU0JWRU
- Activation key: c78f8a3c-957e-4f6a-9c92-cefde6d13392

### Social Engineering Indicators
The message creates a financial concern by stating that a large payment will be processed immediately.

It provides telephone numbers and a business location as contact information:
- (803) 227-9121
- +1-865-489-7049
- 4701 Irving Blvd. Nw #711 Dayton Tn 37321 USA

The combination of a payment claim, automatic renewal, and instructions to contact a support team is consistent with a potential billing-support scam or phishing attempt.

### URL / Attachment Assessment
No actionable URL was identified in the decoded plain-text content.

No attachment was observed during the initial MIME inspection.

### Content Assessment
The decoded content contains multiple identity and branding inconsistencies, a high-value payment claim, and instructions to contact provided telephone numbers.

These indicators increase the likelihood that the message is attempting to create a financial or account-related response from the recipient.

## IOC Enrichment

### IP Address: 209.85.210.74

The sending IP belongs to Google's infrastructure and is associated with the hostname `mail-ot1-f74.google.com`.

Public abuse databases contain reports involving spam and phishing activity associated with this IP. However, the IP is part of shared Google mail infrastructure and should not itself be classified as malicious based solely on these reports.

### Domain: gemalim.org

The sender address uses the `gemalim.org` domain:

`treid5271@gemalim.org`

The domain is significant because it is the domain associated with the visible sender identity, while the message also presents Google Calendar infrastructure in the `Sender` header.

Further domain reputation and ownership analysis should be used before classifying the domain as malicious.

### Domain: google.com

`google.com` appears in the Google Calendar sender address and Message-ID.

Its presence is consistent with the message containing Google infrastructure headers, but it does not establish that the visible sender identity is trustworthy.

### IOC Assessment

The IP address and `google.com` domain are associated with legitimate infrastructure and should not be treated as malicious IOCs solely from extraction.

The `gemalim.org` domain is the primary sender-domain indicator requiring further investigation.

## Domain Investigation

### gemalim.org

Public web searches did not identify reliable reputation information, ownership information, or documented phishing reports for `gemalim.org`.

The absence of public reputation data does not establish that the domain is benign or malicious.

The domain remains suspicious in the context of this message because:

- It is used by the visible sender identity.
- The message presents Google Calendar infrastructure while using a different sender domain.
- DKIM authentication failed for the relevant signatures.
- Microsoft composite authentication failed.
- The message uses a high-value subscription renewal/payment theme.
- The message encourages the recipient to contact a provided support number.

### Domain Assessment

`gemalim.org` should be treated as a suspicious sender-domain indicator for this case, but there is insufficient evidence to independently classify the domain as malicious.

## Telephone and Brand Investigation

### Phone Number: +1-865-489-7049

The phone number `+1-865-489-7049` appears in public scam-reporting records associated with a McAfee Premium Membership refund scam.

This is significant because the same number appears in the investigated email as its support hotline.

The matching number provides independent supporting evidence that the message's claimed McAfee renewal/support scenario is associated with a known scam pattern.

### Phone Number: (803) 227-9121

The number `(803) 227-9121` is presented as the email's primary support number.

Public phone-directory information identifies the number as a South Carolina landline. No reliable evidence was found connecting this specific number to the investigated scam.

The number therefore remains a contextual indicator rather than a confirmed malicious IOC.

### Claimed Product: DefenderX Ultimate

The email claims that the recipient is renewing a product called `DefenderX Ultimate` under a McAfee-related subscription.

No reliable evidence was found connecting `DefenderX Ultimate` to a legitimate McAfee product.

This inconsistency further increases suspicion around the claimed renewal.

### Assessment

The exact match between the email's hotline and a publicly documented McAfee refund-scam number is a significant corroborating indicator.

Combined with the authentication failures, sender-domain inconsistency, payment request, and unsupported product claim, the evidence strongly supports treating the message as a phishing/billing-scam email.

## MITRE ATT&CK Mapping

### T1566 — Phishing

The email uses social engineering to induce the recipient to respond to a fraudulent subscription/payment notification.

The available evidence supports mapping the activity to the broader Phishing tactic.

### T1036 — Masquerading

The message presents Google Calendar infrastructure and branding while the visible sender and message content use different identities.

This identity mismatch is consistent with masquerading behavior.

### T1583 / T1584

No evidence was collected showing that the sender acquired infrastructure or domains specifically for this campaign.

These techniques are therefore not mapped.

### Unsupported Phishing Sub-techniques

The sample does not contain an actionable phishing URL or attachment.

Therefore:

- T1566.001 — Spearphishing Attachment: **Not supported**
- T1566.002 — Phishing: Spearphishing Link: **Not supported**

### ATT&CK Assessment

The strongest supported mappings are:

- T1566 — Phishing
- T1036 — Masquerading

The investigation does not provide sufficient evidence to map more specific phishing sub-techniques.

## Investigation Timeline

| Time | Event |
|---|---|
| 03 Feb 2026 21:51 UTC | Email generated according to the Date header |
| 04 Feb 2026 02:51 Pacific Time | Google Calendar event time displayed in the message |
| 04 Feb 2026 | Email claims USD 567.11 automatic renewal will be processed |
| Investigation | Header authentication failures identified |
| Investigation | Sender-domain and branding inconsistencies identified |
| Investigation | IOC extraction identified `209.85.210.74` and `gemalim.org` |
| Investigation | Support hotline `+1-865-489-7049` matched a publicly documented McAfee refund-scam report |

## Risk Assessment

### Severity
High

### Risk Factors
- Failed DKIM authentication
- Failed Microsoft composite authentication
- High spam-confidence score (SCL 8)
- Sender identity inconsistency
- High-value payment claim
- Urgent automatic-renewal message
- Unsupported product claim
- Support telephone number associated with a documented scam pattern

### Potential Impact
If a recipient follows the instructions in the message, they may disclose personal or financial information or interact with a fraudulent support operation.

## Analyst Conclusion

The evidence supports classifying Case 001 as a phishing/billing-scam email.

The assessment is based on the combination of authentication anomalies, identity inconsistencies, financial social engineering, unsupported product claims, and the match between the provided support hotline and a publicly documented McAfee refund-scam report.

The sending IP should not itself be classified as malicious because it belongs to shared Google infrastructure.

## Recommended Response

1. Do not contact the telephone numbers provided in the email.
2. Do not provide payment, account, or personal information.
3. Report the message to the organization's security or email-security team.
4. Quarantine or delete the message.
5. Search mail systems for other messages containing the identified sender address, domain, IP, and telephone numbers.
6. Add confirmed malicious indicators to appropriate email-security detections after validation.
7. If a recipient interacted with the scam, investigate possible credential or financial-information exposure.