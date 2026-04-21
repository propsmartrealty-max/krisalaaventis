# 🚀 Google Indexing API: Sovereign Setup Guide

Activate high-velocity indexing for **Krisala Aventis** by deploying your Google Service Account key.

---

### Step 1: Create a Google Cloud Project
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project called **"Krisala-Aventis-Indexing"**.
3. Go to **APIs & Services** > **Library**.
4. Search for **"Indexing API"** and click **Enable**.

### Step 2: Generate Service Account Key
1. Go to **APIs & Services** > **Credentials**.
2. Click **Create Credentials** > **Service Account**.
3. Name it `indexing-relay` and give it the **Owner** role (or Editor).
4. Once created, click on the service account email.
5. Go to the **Keys** tab > **Add Key** > **Create New Key**.
6. Select **JSON** and download the file.

### Step 3: Deployment
1. Rename the downloaded file to `service-account.json`.
2. Move it to the `indexing-automation/` folder in your project.
   > [!CAUTION]
   > Never commit this file to a public repository. It should remain in your local environment.

### Step 4: Link to Search Console
1. Copy the **Service Account Email** (e.g., `indexing-relay@...iam.gserviceaccount.com`).
2. Go to [Google Search Console](https://search.google.com/search-console).
3. Select your property: `https://krisalaventis.in`.
4. Go to **Settings** > **Users and Permissions**.
5. Click **Add User** and paste the Service Account Email.
6. Set the Permission to **Owner**.

---

### Step 5: Trigger Indexing
Once the file is in place, run the following command in your terminal:
```bash
cd indexing-automation
npm run push
```

**Your site will now be indexed by Google within hours instead of days.**
