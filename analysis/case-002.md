# Case 002 — Initial Triage

## Subject

CAN I TRUST YOU?

## Sender

Capt William [33124@dlit.mtt.ac.th](mailto:33124@dlit.mtt.ac.th)

## Reply-To

[fdy3215@gmail.com](mailto:fdy3215@gmail.com)

## Claimed Identity

Capt William D Swenson, US Army

## Initial Indicators

* Sender domain: dlit.mtt.ac.th
* Reply-To domain: gmail.com
* Sender and Reply-To identities: Mismatched
* Sender header: None
* Military identity claim: Yes
* Claimed location: Syria
* Financial opportunity: Yes
* Large fund claim: Yes
* Request for assistance: Yes
* Attachment: None observed
* URL: None observed

## Initial Assessment

The email claims to originate from a US Army officer deployed in Syria and asks the recipient to assist with the safekeeping of a large amount of money stored in military trunk boxes.

The message requests that the recipient establish trust and respond to a private email address before additional details are provided.

The sender address uses the `mtt.ac.th` domain while the Reply-To address uses Gmail, creating an identity mismatch.

The combination of an impersonated authority/military identity, a large-fund claim, secrecy, and a promise of substantial financial reward is consistent with an advance-fee or confidence-based social engineering scam.

Further header and content analysis is required.

## Header Authentication Analysis

### SPF

No SPF result was observed in the parsed header information.

### DKIM

No DKIM result was observed in the parsed header information.

### DMARC

No DMARC result was observed in the parsed header information.

### Sender Header

No `Sender` header was present.

### Reply-To

The message uses:

`fdy3215@gmail.com`

This differs from the visible sender address:

`33124@dlit.mtt.ac.th`

The mismatch is an important investigation indicator because replies would be directed to a different email identity.

### Header Assessment

The available header information does not establish sender authenticity. The mismatch between the visible sender and Reply-To addresses warrants further investigation alongside the social-engineering indicators in the message body.

# Case 002 — Content Analysis

## Authority Impersonation

The sender identifies himself as:

`Capt William D Swenson`

and claims to be a U.S. Army officer serving with the 82nd Airborne Division in a peacekeeping deployment.

William D. Swenson is a real former U.S. Army officer. However, publicly documented information about his military service does not match the service history described in the email.

The use of a real person's identity is therefore a significant impersonation indicator. However, the available evidence does not establish whether the legitimate individual or the legitimate institutional email account was directly compromised.

## Financial Pretext

The sender claims to possess a large amount of money stored in two military trunk boxes and asks the recipient to assist with keeping the funds safe.

The message also promises that the recipient will be "rewarded handsomely" for providing assistance.

This combination of a large undisclosed fund, a promised financial reward, and a request for assistance is consistent with an advance-fee or confidence-based scam.

## Trust and Secrecy

The subject asks:

`CAN I TRUST YOU?`

The body repeatedly emphasizes trust and asks the recipient to respond before further details are provided.

This establishes an emotional and trust-based approach rather than providing a legitimate business or operational reason for the requested communication.

## Contact Redirection

The message contains multiple identities:

* Visible sender: `33124@dlit.mtt.ac.th`
* Reply-To: `fdy3215@gmail.com`
* Body contact: `captwilliamsdswensom@gmail.com`

The use of separate Gmail addresses instead of continuing communication through the apparent institutional sender is a significant social-engineering indicator.

## Content Assessment

The overall message is consistent with a social-engineering / advance-fee scam. The primary behavioral indicators are authority impersonation, financial pretext, secrecy, trust-building, and redirection to private email accounts.

No malicious URL or attachment was identified. Therefore, the case should not be mapped to attachment- or link-specific phishing sub-techniques solely on the basis of the email.

# Case 002 — Scam Pattern Analysis

## Historical Scam Pattern

A public 419-scam archive contains an earlier fraudulent email using the name "Capt. William D. Swenson" and substantially the same narrative found in this case.

The archived message claims that the sender is a U.S. Army officer and West Point graduate serving with the 82nd Airborne Division's peacekeeping force after deployment from Iraq. It also describes military trunk boxes containing funds, asks whether the recipient can be trusted, promises a reward, and directs the recipient to a private email address. These elements closely correspond to the content of Case 002.

This provides strong evidence that the Case 002 message is part of a known advance-fee / confidence-scam narrative rather than an isolated legitimate request.

## Identity Verification

William D. Swenson is a real former U.S. Army officer and Medal of Honor recipient. Publicly documented records associate him with the 10th Mountain Division and deployments to Iraq and Afghanistan.

The archived scam message demonstrates that his name has previously been used in fraudulent correspondence. The existence of the real individual therefore does not authenticate the sender of Case 002.

## Narrative Discrepancies

The email claims that the sender is serving with the 82nd Airborne Division and has been moved from Iraq to Syria as part of a peacekeeping force.

Publicly documented information about William D. Swenson instead identifies his documented combat service with the 10th Mountain Division and deployments to Iraq and Afghanistan.

The discrepancy between the documented biography and the narrative in the email further supports impersonation.

## Assessment

The combination of a real person's identity, a previously documented scam narrative, a fabricated financial opportunity, trust-building language, and requests to communicate through private email addresses provides strong evidence of a social-engineering / advance-fee scam.

The evidence does not establish whether the `dlit.mtt.ac.th` account was compromised, spoofed, or otherwise abused. The institutional domain should therefore not be classified as malicious solely on the basis of this message.

# IOC Enrichment

## IP Address: 209.85.160.194

The IP address `209.85.160.194` was extracted from the email headers.

The address belongs to Google's infrastructure and is associated with Google mail services. Its presence in the message therefore does not independently indicate malicious activity.

The IP should be retained as a contextual IOC because it identifies the apparent mail-delivery infrastructure, but it should not be classified as malicious based solely on this investigation.

**Assessment:** Legitimate/shared mail infrastructure — no direct malicious attribution.

## Email Address: [33124@dlit.mtt.ac.th](mailto:33124@dlit.mtt.ac.th)

The sender address uses the `dlit.mtt.ac.th` subdomain, which is legitimate institutional infrastructure associated with Matthayom Wat That Thong School in Thailand.

Independent public reports have documented other `@dlit.mtt.ac.th` addresses being used in scam messages. However, no reliable public evidence was identified specifically associating `33124@dlit.mtt.ac.th` with malicious activity.

The address is therefore retained as a suspicious sender indicator because of its use in this fraudulent message and its relationship with the other social-engineering indicators.

The available evidence does not establish whether the mailbox was compromised, spoofed, or otherwise abused.

**Assessment:** Suspicious sender indicator — maliciousness of the specific mailbox not independently confirmed.

## Email Address: [captwilliamsdswensom@gmail.com](mailto:captwilliamsdswensom@gmail.com)

The address `captwilliamsdswensom@gmail.com` is explicitly provided in the message body as a private contact address for the claimed sender.

The use of a separate Gmail address is significant because it differs from the visible sender address `33124@dlit.mtt.ac.th` and the Reply-To address `fdy3215@gmail.com`.

No reliable independent evidence was identified that would allow the specific Gmail account to be classified as malicious on its own.

Its significance therefore comes primarily from its role in the message's social-engineering workflow rather than from independent reputation data.

**Assessment:** Suspicious contact indicator — no independent malicious attribution confirmed.

## Email Address: [fdy3215@gmail.com](mailto:fdy3215@gmail.com)

The address `fdy3215@gmail.com` is specified in the `Reply-To` header.

This differs from the visible sender address `33124@dlit.mtt.ac.th`, meaning that a direct reply to the message would be routed to a separate Gmail account.

The address therefore plays an important role in the apparent social-engineering workflow by redirecting communication away from the institutional sender identity.

No reliable independent evidence was identified that would allow the specific Gmail account to be classified as malicious based solely on its address.

**Assessment:** Suspicious communication endpoint — no independent malicious attribution confirmed.

## Remaining Extracted Artifacts

The IOC extraction script identified additional email addresses and domains associated with message headers and infrastructure.

The `mail.gmail.com` and `gmail.com` domains are associated with legitimate Google mail infrastructure and do not provide evidence of malicious activity by themselves.

The `CAJFivM9tEoOui_gqYF7yva2PUtBjBDvcJsgkwcV-3H3fYb4qjg@mail.gmail.com` address appears to be a system-generated Google mail address rather than an attacker-controlled contact address.

The `redacted.com` domain and `redacted@redacted.com` address are anonymized artifacts in the sample and cannot be meaningfully investigated.

These artifacts are therefore not treated as malicious IOCs.

**IOC disposition:** Retained for completeness in raw extraction output but excluded from malicious-indicator attribution.

# MITRE ATT&CK Mapping

## T1036 — Masquerading

The sender uses the identity of a real U.S. Army officer, William D. Swenson, to establish credibility.

The message presents the sender as Capt. William D. Swenson and provides a military background that does not match the documented history of the real individual.

This is consistent with identity impersonation and masquerading.

## T1566 — Phishing

The fraudulent email is used as the initial delivery mechanism for the social-engineering attempt.

The message attempts to establish trust and persuade the recipient to continue communication with the sender.

The case is primarily classified as social engineering / advance-fee fraud, but the email delivery mechanism is consistent with the broader Phishing technique.

## Techniques Not Mapped

### T1566.001 — Spearphishing Attachment

Not mapped because no attachment was observed.

### T1566.002 — Spearphishing Link

Not mapped because no URL or actionable link was observed.

## ATT&CK Assessment

The strongest supported ATT&CK mappings are:

* T1036 — Masquerading
* T1566 — Phishing

The investigation does not provide sufficient evidence to map additional techniques related to malicious attachments, links, infrastructure acquisition, credential theft, or malware execution.

# Investigation Timeline

## 1. Email Received

The message was received with the subject:

`CAN I TRUST YOU?`

The apparent sender was:

`33124@dlit.mtt.ac.th`

The message identifies the sender as Capt. William D. Swenson, a U.S. Army officer.

## 2. Initial Social Engineering Attempt

The sender establishes an authority-based identity and claims to be deployed in Syria with the 82nd Airborne Division.

The message introduces a story involving large amounts of money stored in military trunk boxes.

## 3. Trust Establishment

The sender asks whether the recipient can be trusted and states that further information will be provided after receiving a response.

This establishes a trust-based communication channel before revealing additional details.

## 4. Financial Incentive

The sender promises that the recipient will be rewarded handsomely for assisting with the safekeeping of the funds.

## 5. Communication Redirection

The message provides private Gmail addresses and uses `fdy3215@gmail.com` as the Reply-To address.

This redirects subsequent communication away from the visible institutional sender address.

## 6. Historical Corroboration

Publicly available scam records contain an earlier message using substantially the same William D. Swenson identity and military-fund narrative.

This provides additional evidence that the message follows a known advance-fee / confidence-scam pattern.

## 7. Investigation Outcome

No attachment or actionable URL was identified.

The investigation therefore focused on sender identity, header inconsistencies, social-engineering characteristics, communication redirection, and historical scam-pattern matching.

# Risk Assessment

**Severity:** High

**Classification:** Social Engineering / Advance-Fee Scam

**Confidence:** High

The message presents multiple independent indicators of fraudulent activity, including authority impersonation, a fabricated financial opportunity, trust and secrecy language, sender/Reply-To mismatch, redirection to private email addresses, and strong similarity to a previously documented scam narrative.

No malicious attachment or actionable URL was identified. The primary threat is therefore social engineering and potential financial fraud rather than malware delivery through the analyzed message.

# Analyst Conclusion

Case 002 is assessed as a high-confidence social-engineering / advance-fee scam.

The sender claims to be Capt. William D. Swenson, a real former U.S. Army officer, but the message uses a documented scam narrative involving military service, a large hidden fund, military trunk boxes, trust-building, and promised financial reward.

The visible sender address uses a legitimate institutional domain, while the Reply-To and body contact addresses use Gmail accounts. The legitimate nature of the institutional domain does not establish the authenticity of the sender or the legitimacy of the message.

A historical scam report containing substantially the same identity and narrative provides additional corroboration that the message follows a known fraud pattern.

The available evidence does not establish whether the institutional mailbox was compromised, spoofed, or otherwise abused. Therefore, the investigation does not attribute the activity to the institution or classify its domain as malicious.

# Recommended Response

* Do not reply to the sender or the provided Gmail addresses.
* Do not provide personal, financial, banking, identity, or account information.
* Preserve the original `.eml` file and associated header evidence.
* Block or quarantine the identified sender addresses according to organizational policy.
* Report the message as suspected fraud or social engineering.
* Monitor for additional messages using the same sender identity, narrative, or contact addresses.
* If similar messages are received, correlate their headers, sender addresses, Reply-To addresses, and message content.
* Consider creating detections for recurring impersonation and advance-fee scam patterns rather than blocking legitimate institutional domains solely because they appeared in this case.
