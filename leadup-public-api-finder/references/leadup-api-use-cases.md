# LeadUp API use cases

Common API needs across LeadUp projects. Use as a quick map from
project → likely categories → starting candidates. **Always verify
from official docs** before recommending.

## Hostendor (hosting / server / domain panel)

| Need | Category | Starting candidates (verify!) |
|---|---|---|
| IP geo + reverse DNS | Maps / Geo | ipinfo, ipapi, ipgeolocation |
| DNS lookup + propagation | Security / Data | Cloudflare DNS over HTTPS, Google DoH |
| WHOIS / domain age | Data | RDAP (free, IANA), domainsdb |
| SSL certificate inspection | Security | crt.sh API, ssl-checker |
| Uptime monitor | Reliability | UptimeRobot API, BetterStack |
| Email validation (MX/DMARC) | Validation | mailboxlayer, kickbox, abstractapi |
| Threat / IP reputation | Security | AbuseIPDB, VirusTotal (rate-limited free) |
| URL safety | Security | Google Safe Browsing, urlhaus |
| Breach check | Security | HaveIBeenPwned (paid) |

## LeadUp website (leadup.in marketing site)

| Need | Category | Starting candidates |
|---|---|---|
| Email validation on lead form | Validation | abstractapi, mailboxlayer |
| Phone validation (E.164, India) | Validation | numverify, abstractapi |
| Contact enrichment (B2B) | Data | clearbit, hunter, peopledatalabs |
| Chatbot inference | AI | Anthropic / OpenAI / Gemini (via `leadup-ai-feature-planner`) |
| Analytics events | Data | GA4 Measurement Protocol, PostHog, Plausible |
| Newsletter | Messaging | Resend, Postmark, Mailerlite |

## Jewellery SaaS (multi-tenant)

| Need | Category | Starting candidates |
|---|---|---|
| Live gold / silver rates | Data | metals-api, goldapi (paid), public RSS for India |
| Currency conversion INR↔USD↔AED | Data | exchangerate.host (key-less), open.er-api, ECB |
| GSTIN + PAN validation | Validation | sandbox.co.in, GST API providers |
| Invoice / GST report | Docs | Tally / Zoho connectors, custom generation |
| WhatsApp templates | Messaging | Gupshup / AiSensy / Wati / WhatsApp Cloud API (via `leadup-whatsapp-automation-planner`) |
| Payment | Payments | Razorpay (default India), Cashfree |
| Customer KYC | Identity | regulated; avoid storage; route to `leadup-pii-risk-reviewer` |

## Salon / clinic / school SaaS

| Need | Category | Starting candidates |
|---|---|---|
| WhatsApp reminders | Messaging | BSP options (see above) |
| SMS gateway | Messaging | MSG91, Twilio (India numbers), Gupshup |
| Transactional email | Messaging | Resend, Postmark, AWS SES |
| Calendar invites (.ics) | Docs | generate locally; Google Calendar API for sync |
| Local business listings | Local / business | Google Business Profile, Places |
| OTP send + verify | Identity | MSG91 OTP, Twilio Verify |
| Geocode address | Maps / Geo | Mapbox, Google Maps, OpenCage |
| Payment | Payments | Razorpay, Cashfree |

## INET CRM

| Need | Category | Starting candidates |
|---|---|---|
| Customer lookup (B2B) | Data | clearbit, hunter |
| Email + phone validation | Validation | abstractapi, numverify |
| Document / PDF generation | Docs | pdfshift, pdfco, ApyHub, generate locally |
| Geocoding / address validation | Maps / Geo | Mapbox, OpenCage |
| Lead enrichment | Data | clearbit, fullcontact, peopledatalabs |
| WhatsApp + email outbox | Messaging | BSP + Resend |

## Trivasia (travel)

| Need | Category | Starting candidates |
|---|---|---|
| Weather (forecast + current) | Weather | Open-Meteo (free, key-less), OpenWeather |
| Currency conversion | Data | exchangerate.host, ECB |
| Country / ISO codes | Data | restcountries (key-less), wikidata |
| Flight / airport schedules | Travel | aviationstack, FlightAware (limited free), OAG (paid) |
| Maps + routing | Maps / Geo | Mapbox, Google Maps, OpenStreetMap + OSRM |
| Hotel / fare | Travel | mostly paid; partner-only |

## Security suite

| Need | Category | Starting candidates |
|---|---|---|
| Malware / hash lookup | Security | VirusTotal, MalwareBazaar |
| Phishing / URL reputation | Security | Google Safe Browsing, PhishTank, urlhaus |
| IP reputation | Security | AbuseIPDB |
| Breach check | Security | HaveIBeenPwned (paid) |
| ASN / WHOIS / GeoIP | Data | RDAP, ipinfo, ipapi |
| DNS over HTTPS | Security | Cloudflare, Google |

## Reading this table

- Names are **starting candidates only**. Always run the verification
  checklist on each.
- "Free" tier sizes change. Re-read pricing pages.
- For payments / KYC / WhatsApp: route to the specialist LeadUp
  skills (`leadup-api-research-builder`,
  `leadup-whatsapp-automation-planner`, `leadup-pii-risk-reviewer`,
  `leadup-security-review`).
- For AI: route to `leadup-ai-feature-planner`.
