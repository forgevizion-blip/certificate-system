# Code Fuzion — 24-Hour Hackathon Certificate Portal & Mailing System

A lightweight, serverless portal for hackathon participants to search their registration number, download a complete set of **5 personalized official certificates (PDF)**, and have them **emailed directly to their inbox**, with instant certificate authenticity verification via unique URLs.

---

## Key Features

- **5 Certificates Per Participant**: Each participant receives 5 distinct certificates (Certificate 1 through Certificate 5) for the event.
- **Direct Email Delivery**: Participants can enter or confirm their email on the portal and click **"Email All 5 Certificates"** (or email individual certificates). Google Apps Script packages the high-res PDFs and mails them directly to the participant's inbox.
- **Auto-Sync to Google Sheets**: When a participant sends certificates to their email, their email is recorded in the roster and their status is marked as `Emailed`.
- **Individual PDF Downloads**: One-click download for all 5 certificates sequentially, or download any single certificate.
- **Tamper-Proof Verification**: Each certificate carries its own unique Certificate ID (e.g. `CF-XXXXXXXX-C1`). Scanning or visiting `?id=CF-XXXXXXXX-C1` displays authentic verification details and allows instant PDF download.
- **Auto-Migrating Backend**: Google Apps Script automatically ensures and updates the 10-column roster schema.

---

## Google Sheet Roster Schema

The `Roster` tab contains 10 columns:

| Column | Header | Description |
|---|---|---|
| **A** | `Registration No.` | Participant's ID (e.g. `00101`, `101`) |
| **B** | `Name` | Participant's Full Name |
| **C** | `Team` | Hackathon Team Name |
| **D** | `Email` | Participant's email (pre-filled or populated on mail) |
| **E** | `Certificate ID 1` | Unique ID for Certificate 1 |
| **F** | `Certificate ID 2` | Unique ID for Certificate 2 |
| **G** | `Certificate ID 3` | Unique ID for Certificate 3 |
| **H** | `Certificate ID 4` | Unique ID for Certificate 4 |
| **I** | `Certificate ID 5` | Unique ID for Certificate 5 |
| **J** | `Status` | `Claimed`, `Downloaded`, or `Emailed` |

---

## Setup & Deployment Instructions

### 1. Google Sheets & Apps Script Setup

1. Open your Google Sheet (named `LPU Hackathon Certificates` or similar).
2. Go to **Extensions > Apps Script**.
3. Replace all existing script code in `Code.gs` with the content of [`Code.gs`](file:///Users/sakura/projects/club/certificate_system/Code.gs).
4. Save the project (`Cmd+S` / `Ctrl+S`).
5. **Create the Claim Form (Automated)**:
   - In the Apps Script function dropdown, select `createClaimForm` and click **Run**.
   - Grant the requested permissions.
   - The script creates the Google Form with *Registration No.*, *Full Name*, *Team Name*, and *Email Address*, and links responses directly to the spreadsheet.
6. **Install the Form Submit Trigger**:
   - In the function dropdown, select `setupTrigger` and click **Run**.
7. **Deploy the Web App**:
   - Click **Deploy > New deployment** (or **Manage deployments > Edit > New version**).
   - Click the gear icon next to "Select type" and choose **Web app**.
   - Description: `v2.0 - 5 Certificates & Email System`
   - **Execute as**: `Me`
   - **Who has access**: `Anyone`
   - Click **Deploy** and copy your **Web App URL**.

---

### 2. Configure Frontend (`index.html`)

Open [`index.html`](file:///Users/sakura/projects/club/certificate_system/index.html) and locate the `CONFIG` object near line 400:

```javascript
const CONFIG = {
  // 1. Paste your deployed Google Apps Script Web App URL:
  APPS_SCRIPT_URL: 'https://script.google.com/macros/s/YOUR_DEPLOYMENT_ID/exec',

  // 2. Your live GitHub Pages website URL:
  SITE_URL: 'https://<your-username>.github.io/<repo-name>/',

  // 3. Certificate background image (relative path):
  TEMPLATE_URL: 'certificate.png',

  // 4. Custom certificate names (if you wish to rename Certificate 1..5):
  CERTIFICATES: [
    { number: 1, title: 'Certificate 1' },
    { number: 2, title: 'Certificate 2' },
    { number: 3, title: 'Certificate 3' },
    { number: 4, title: 'Certificate 4' },
    { number: 5, title: 'Certificate 5' }
  ]
};
```

---

### 3. Deploy to GitHub Pages

1. Push the files to your GitHub repository:
   - `index.html`
   - `certificate.png`
   - `Code.gs`
   - `roster.csv`
   - `.nojekyll`
   - `README.md`
2. In your GitHub repo, go to **Settings > Pages**.
3. Under **Build and deployment > Branch**, select `main` and root `/`, then click **Save**.
4. Your portal will be live in 1–2 minutes!

---

## File Overview

| File | Purpose |
|---|---|
| [`index.html`](file:///Users/sakura/projects/club/certificate_system/index.html) | Single-page responsive certificate search, 5-certificate dashboard, PDF generator, email dispatcher, and verification interface |
| [`Code.gs`](file:///Users/sakura/projects/club/certificate_system/Code.gs) | Google Apps Script backend handling lookups, multi-cert ID verification, automated form responses, and email delivery via `MailApp` |
| [`certificate.png`](file:///Users/sakura/projects/club/certificate_system/certificate.png) | High-resolution background certificate template |
| [`generate_roster.py`](file:///Users/sakura/projects/club/certificate_system/generate_roster.py) | Python helper to generate sample CSV rosters matching the 10-column schema |
| [`roster.csv`](file:///Users/sakura/projects/club/certificate_system/roster.csv) | Roster template formatted for Google Sheets import (with formula strings to preserve leading zeros) |
| [`roster_standard.csv`](file:///Users/sakura/projects/club/certificate_system/roster_standard.csv) | Standard CSV export of the 10-column roster |
