# Sri Tirumala Chemical Industries - Website Maintenance & Developer Guide

Welcome to the Developer Guide for the Sri Tirumala Chemical Industries website. This document contains everything you need to know to maintain, update, deploy, and extend the website yourself using **VS Code**, **GitHub**, and free static hosting services.

---

## 1. Project Structure

The website is a lightweight, high-performance static application. It has **no database servers** to maintain; all data is managed on your local computer via simple data configurations.

```
c:\Users\kavya\Desktop\Tirumala2/
├── index.html                  # Main homepage structure (Navigation, Hero, About, Products grid, Map, Footer)
├── gallery.html                # Product gallery page (Shows all categories and individual variants)
├── products-data.js            # PRODUCT CATALOG (Dynamic specs, highlights, sizes, and flavor images)
├── script.js                   # INTERACTIVE LOGIC (Navigation scroll tracking, sticky header, modal renderer)
├── style.css                   # STYLING SHEET (Navy/teal color tokens, responsive grid rules, animations)
└── assets/                     # IMAGE REPOSITORY
    ├── tirumala_bleach.png     # Bleaching powder image
    ├── tirumala_floor_*.png    # Tirumala floor cleaner flavor images (orange, green, pink, white)
    ├── cheetah_floor_*.png     # Cheetah floor cleaner flavor images (orange, green, pink, white)
    ├── liger_floor_*.png       # Liger floor cleaner flavor images (orange, green, pink, white, yellow)
    ├── home_doctor_*.png       # Home Doctor floor cleaner flavor images (orange, green, pink, white, yellow)
    ├── tirumala_acid_*.png     # Cleaning acid bottle images (green, yellow)
    ├── horpic_toilet_*.png     # Toilet cleaner bottle images (blue, white)
    ├── cheetah_ant_killer.png  # Ant killer packaging image
    ├── facility_*.jpg          # Facilities showcase photos (warehouse, production, floor area)
    └── ...                     # Other raw/archived assets
```

---

## 2. Decoupled Architecture (Scalability)

We have separated the website into three distinct layers to make future updates safe and easy:
1. **Markup Layer (`index.html` & `gallery.html`)**: Defines *what* sections exist and holds static card layouts.
2. **Configuration Data Layer (`products-data.js`)**: Holds the descriptions, specs, packaging sizes, and image filenames for the products.
3. **Execution Logic Layer (`script.js`)**: Automatically reads the configuration data and handles UI transitions, drawer open/close actions, and animations. **You do not need to modify this file.**

---

## 3. Product & Content Management

### How to Edit an Existing Product
All interactive product details (the popup specs modal, highlights, sizes, and swatches) are controlled by the `productModalData` object inside **`products-data.js`**.

For example, to update the specs or highlights of the **Tirumala Bleaching Powder**, open `products-data.js` and locate its entry:
```javascript
bleaching_powder: {
    title: "Tirumala Bleaching Powder",
    tag: "Disinfectant",
    brand: "TIRUMALA BRAND",
    desc: "...",
    image: "assets/tirumala_bleach.png",
    subProducts: [
        {
            name: "Tirumala Bleaching Powder",
            desc: "...",
            highlights: [
                "34.5% Minimum Active Chlorine content", // Change bullets here
                "High stability and long shelf life"
            ],
            sizes: ["25 Kg Bag", "50 Kg Drum"], // Edit packaging sizes here
            specs: {
                "Active Chlorine": "34.5% Min", // Edit specifications here
                "Appearance": "Free flowing white powder"
            }
        }
    ]
}
```
Simply edit the text inside the quotation marks, save the file, and refresh your browser.

---

### How to Add a New Product Category
To add a completely new product category:
1. **Define the Data in `products-data.js`**: Add a new key-value pair under `productModalData`. For example:
   ```javascript
   new_chemical: {
       title: "Tirumala Brand New Chemical",
       tag: "Industrial Strength",
       brand: "TIRUMALA BRAND",
       desc: "High-grade sanitization chemical.",
       image: "assets/new_chemical.png",
       subProducts: [
           {
               name: "New Chemical Premium",
               desc: "Details about the product...",
               highlights: ["Bullet 1", "Bullet 2"],
               sizes: ["5L Can", "50L Drum"],
               specs: {
                   "Active Matter": "90%",
                   "pH Level": "8.5"
               }
           }
       ]
   }
   ```
2. **Add a Product Card in `index.html`**: Open `index.html`, locate the `#products` section, and add a card inside `<div class="products-grid">`:
   ```html
   <div class="product-card animate-on-scroll fade-up stagger-delay-11">
       <div class="product-img-wrapper">
           <span class="product-tag">Industrial Strength</span>
           <img src="assets/new_chemical.png" alt="New Chemical" class="product-img">
       </div>
       <div class="product-body">
           <h3>Tirumala Brand New Chemical</h3>
           <p>High-grade sanitization chemical description here.</p>
           <button onclick="openProductModal('new_chemical')" class="btn btn-primary full-width">
               <i class="fa-solid fa-eye"></i> View Details
           </button>
       </div>
   </div>
   ```
3. **Extend Stagger Delay (If Needed)**: If you exceed 12 products, open `style.css` at the bottom and add a new transition delay class matching your new stagger delay index (e.g. `.stagger-delay-13 { transition-delay: 1.3s; }`).

---

### How to Update General Website Information (`index.html`)
* **Google Maps Location**:
  Locate the `<iframe>` in `index.html` (around line 398) inside the `<div class="map-card-wrapper">` and swap the `src` attribute with your new Google Maps Embed URL.
* **WhatsApp Contact Number**:
  Locate all links containing `https://wa.me/919908914524` and update `919908914524` to your new mobile number (including the country code `91` at the beginning, without `+` or spaces).
* **Phone Numbers**:
  Locate `tel:+919908914524` or `tel:+919030444291` and update the value in both the `href` attribute and the visible text.
* **Email Address**:
  Locate `mailto:k.pr9908914522@gmail.com` and replace the email address.

---

## 4. Product Image Management Guidelines

To maintain a professional look and avoid visual misalignment on cards or modal drawer pages, follow these standard formatting guidelines:
1. **Background**: Always use images with **pure white background (`#ffffff`)** or a **transparent background (`.png` format)**. Do not use busy household background photos.
2. **Aspect Ratio & Canvas Size**: Save images as square canvas dimensions (**$800 \times 800$ pixels**).
3. **Centering & Margins**: Center the product bottle inside the square frame, leaving a **10% transparent safety margin** on all four edges so the bottle neck or base is never cut off by card borders.

---

## 5. Pushing to GitHub using VS Code (GUI Method)

You do not need to memorize terminal commands to push your changes. VS Code has a built-in visual Git client.

### Step 1: Open Folder in VS Code
Open VS Code, click **File** > **Open Folder...**, select **`c:\Users\kavya\Desktop\Tirumala2`**, and click **Select Folder**.

### Step 2: Initialize your Git Repository (First Time Only)
1. Click the **Source Control** icon in the left sidebar (looks like a branch with three nodes, or press `Ctrl` + `Shift` + `G`).
2. Click the blue **"Initialize Repository"** button.

### Step 3: Write your Commit Message & Commit
1. Type a short description of the changes you made in the **"Message"** text box at the top of the Source Control panel (e.g. `Added new products`).
2. Click the **Commit** checkmark button (or press `Ctrl` + `Enter`). 
3. If prompted to stage all files, click **Yes**.

### Step 4: Publish to GitHub
1. In the Source Control panel, click the blue **"Publish Branch"** button.
2. Select either **"Publish to GitHub public repository"** or **"Publish to GitHub private repository"**.
3. If you haven't authorized VS Code on GitHub before, a browser window will open asking you to sign in.
4. VS Code will automatically create a repository on your GitHub account, configure the remote origin, and push your code.

### Step 5: Push Future Updates
Once initialized, whenever you change any files:
1. Go to the Source Control panel.
2. Type a message and click **Commit**.
3. Click the **"Sync Changes"** (or **"Push"**) button at the bottom left or top of the panel. Your live website will automatically redeploy!

---

## 6. Free Hosting Deployment Workflow

Once your code is pushed to GitHub, you can host the website completely free.

### Deployment Method A: GitHub Pages
1. Go to your repository page on GitHub.
2. Click on the **Settings** tab at the top.
3. Scroll down and click **Pages** in the left-hand menu.
4. Under the **Build and deployment** section, select **Deploy from a branch**.
5. Set the branch selection dropdown to `main` (and folder to `/ (root)`) and click **Save**.
6. Wait 1 minute, and your site will be live at `https://your-github-username.github.io/your-repository-name/`.

### Deployment Method B: Netlify (Recommended for Instant Updates)
1. Go to [Netlify](https://www.netlify.com/) and log in using your GitHub account.
2. Click **Add new site** > **Import an existing project**.
3. Select **GitHub** and authorize.
4. Choose your `tirumala-chemicals` repository.
5. Leave all build settings blank (as it is a static site) and click **Deploy Site**.
6. Netlify will deploy your site instantly and provide a URL (which you can rename or connect to a custom domain). Every time you push a change to GitHub, Netlify updates the live site in under 10 seconds.

---

## 7. Backing Up & Restoring Your Files

### The Backup Process
* **Method 1 (Git Tags - Recommended)**:
  Before making major changes, create a stable checkpoint version in Git. In the VS Code terminal (or standard terminal), run:
  ```bash
  git tag -a v1.0.0 -m "Stable version before editing catalog"
  git push origin v1.0.0
  ```
* **Method 2 (Manual Archive)**:
  Right-click the `Tirumala2` folder on your desktop, select **Send to** > **Compressed (zipped) folder** (or **Compress to ZIP** on Windows 11). Rename the zip with the current date (e.g. `Tirumala_Backup_2026-06-16.zip`).

### The Restore Process
* **Method 1 (Discarding Uncommitted Changes)**:
  If you made a mistake and want to discard all changes since your last commit, open the Source Control panel in VS Code, click the `...` menu icon at the top of the panel, and select **Checkout** > **Discard All Changes**.
* **Method 2 (Restoring from ZIP)**:
  Rename the corrupted folder `Tirumala2` to `Tirumala2_corrupted`. Extract your backup zip file to your desktop, and rename the extracted folder back to `Tirumala2`.
