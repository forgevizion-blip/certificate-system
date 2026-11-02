# Hackathon Certificate Portal

A lightweight, serverless portal for hackathon participants to search their registration number, download their personalized certificate (PDF), and verify certificate authenticity via URL.

---

## Deployment Steps (GitHub Pages)

### 1. Create a Repository
1. Go to [GitHub](https://github.com) and click **New repository**.
2. Name it (e.g., `hackathon-certificates` or `certificates`).
3. Set visibility to **Public** and click **Create repository**.

### 2. Upload Files
Upload or push these files to the root of your repository:
- `index.html`
- `certificate.png` (or `.jpg`)
- `.nojekyll`
- `README.md`

### 3. Set Configuration (`SITE_URL` & `APPS_SCRIPT_URL`)
Open `index.html` and update the `CONFIG` block at the top of the `<script>`:
```javascript
const CONFIG = {
  // 1. Your deployed Google Apps Script Web App URL:
  APPS_SCRIPT_URL: 'https://script.google.com/macros/s/YOUR_DEPLOYMENT_ID/exec',

  // 2. Your live GitHub Pages website URL:
  SITE_URL: 'https://<your-username>.github.io/<repo-name>/',

  // 3. Certificate background image (relative path):
  TEMPLATE_URL: 'certificate.png'
};
```

### 4. Enable GitHub Pages
1. In your repository on GitHub, go to **Settings** > **Pages** (in the left sidebar).
2. Under **Build and deployment** > **Branch**:
   - Branch: `main` (or `master`)
   - Folder: `/ (root)`
3. Click **Save**.
4. Within 1–2 minutes, your portal will be live at `https://<your-username>.github.io/<repo-name>/`!

---

## File Overview

| File | Purpose |
|---|---|
| `index.html` | Single-page certificate lookup, verification, and PDF generator |
| `certificate.png` | Background certificate template (replace with your custom design if desired) |
| `.nojekyll` | Instructs GitHub Pages to serve all static assets directly without Jekyll processing |
| `Code.gs` | Google Apps Script backend connected to your Google Sheet roster |
| `roster.csv` | Student roster template formatted for Google Sheets import |
