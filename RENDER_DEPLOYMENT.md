# 🎨 Deploy E-Waste Locator to Render - Step by Step

Complete guide to deploy your Django application to Render (Free Tier Available).

---

## 📋 What You'll Need

- GitHub account with your project repository
- Render account (free): https://render.com/
- 15-20 minutes

---

## 🚀 Deployment Steps

### Step 1: Prepare Your Project for Deployment

#### 1.1 Update `blogs/settings.py`

Open `blogs/settings.py` and make these changes:

```python
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-temporary-key-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # Render will provide the domain

# Database
# For PostgreSQL on Render
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE'),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'HOST': os.environ.get('PGHOST'),
        'PORT': os.environ.get('PGPORT', '5432'),
    }
}

# Fallback to SQLite for local development
if not os.environ.get('PGDATABASE'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static'),
]

# WhiteNoise configuration for serving static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line AFTER SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# WhiteNoise storage backend
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### 1.2 Verify `requirements.txt`

Your `requirements.txt` should include:

```txt
Django==5.2.6
asgiref==3.9.2
sqlparse==0.5.3
tzdata==2025.2
gunicorn==21.2.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
python-decouple==3.8
dj-database-url==2.1.0
```

#### 1.3 Create `build.sh` Script

Create a file named `build.sh` in your project root:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
```

#### 1.4 Make `build.sh` Executable

```bash
# In Git Bash or PowerShell
git update-index --chmod=+x build.sh
```

#### 1.5 Update `.gitignore`

Ensure your `.gitignore` includes:

```gitignore
# Database
*.sqlite3
db.sqlite3

# Static files
staticfiles/
/static/

# Environment
.env
```

#### 1.6 Commit Changes to GitHub

```bash
git add .
git commit -m "Configure for Render deployment"
git push origin main
```

---

### Step 2: Create Render Account

1. Go to **https://render.com/**
2. Click **"Get Started for Free"**
3. Sign up with **GitHub** (recommended)
4. Authorize Render to access your repositories

---

### Step 3: Create PostgreSQL Database

#### 3.1 Create New PostgreSQL Instance

1. From Render Dashboard, click **"New +"**
2. Select **"PostgreSQL"**

#### 3.2 Configure Database

- **Name**: `ewaste-db` (or any name you prefer)
- **Database**: `ewaste_db`
- **User**: `ewaste_user` (auto-generated)
- **Region**: Choose closest to your location
- **Plan**: **Free** (sufficient for testing)

#### 3.3 Create Database

1. Click **"Create Database"**
2. Wait 1-2 minutes for database to be provisioned
3. **Important**: Copy the **Internal Database URL** (you'll need this later)
   - It looks like: `postgresql://user:password@host/database`

---

### Step 4: Create Web Service

#### 4.1 Create New Web Service

1. From Dashboard, click **"New +"**
2. Select **"Web Service"**

#### 4.2 Connect Repository

1. Connect to your GitHub account if not already connected
2. Find and select **"E-WASTE-FACILITY-LOCATOR"** repository
3. Click **"Connect"**

#### 4.3 Configure Web Service

Fill in the following settings:

**Basic Settings:**
- **Name**: `ewaste-facility-locator` (or your preferred name)
- **Region**: Same as your database (e.g., Oregon, Singapore)
- **Branch**: `main`
- **Root Directory**: Leave blank
- **Environment**: `Python 3`
- **Build Command**: 
  ```bash
  ./build.sh
  ```
- **Start Command**: 
  ```bash
  gunicorn blogs.wsgi:application
  ```

**Instance Type:**
- Select **"Free"** (sufficient for testing and small projects)

---

### Step 5: Configure Environment Variables

Scroll down to **"Environment Variables"** section:

#### 5.1 Add These Variables

Click **"Add Environment Variable"** and add each one:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | `your-secret-key-generate-new-one-here` |
| `DEBUG` | `False` |
| `PYTHON_VERSION` | `3.13.0` |
| `DATABASE_URL` | Paste your Internal Database URL from Step 3.3 |
| `PGDATABASE` | `ewaste_db` (from your database) |
| `PGHOST` | (extract from Database URL) |
| `PGUSER` | (extract from Database URL) |
| `PGPASSWORD` | (extract from Database URL) |
| `PGPORT` | `5432` |

#### 5.2 Generate Secret Key

To generate a secure SECRET_KEY, run locally:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and use it as your SECRET_KEY value.

**Alternative Method**: Use Render's built-in Database URL:

Instead of adding individual PG variables, you can modify `settings.py` to use:

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}
```

Then just add:
- `SECRET_KEY`
- `DEBUG=False`
- `PYTHON_VERSION=3.13.0`
- `DATABASE_URL` (from your Render PostgreSQL)

---

### Step 6: Deploy Your Application

#### 6.1 Create Web Service

1. Click **"Create Web Service"** at the bottom
2. Render will automatically:
   - Clone your repository
   - Install dependencies from `requirements.txt`
   - Run `build.sh` (collect static files, migrate database)
   - Start your application with Gunicorn

#### 6.2 Monitor Deployment

Watch the **Logs** in real-time:
- You'll see installation progress
- Static files collection
- Database migrations
- Server startup

**Expected log output:**
```
==> Cloning from https://github.com/Sahilshah12/E-WASTE-FACILITY-LOCATOR...
==> Downloading cache...
==> Installing dependencies...
==> Running build command: ./build.sh
Collecting static files...
Running migrations...
==> Starting service with: gunicorn blogs.wsgi:application
[INFO] Starting gunicorn 21.2.0
[INFO] Listening at: http://0.0.0.0:10000
```

#### 6.3 Deployment Complete

When you see **"Live"** with a green dot, your app is deployed! 🎉

---

### Step 7: Access Your Application

#### 7.1 Get Your URL

Render automatically provides a URL:
```
https://ewaste-facility-locator.onrender.com
```

Click the URL or find it at the top of your service dashboard.

#### 7.2 Test Your Application

Visit your site and verify:
- ✅ Homepage loads
- ✅ Static files (CSS/JS) work
- ✅ Navigation works
- ✅ Registration page accessible
- ✅ Login page accessible

---

### Step 8: Create Superuser (Admin Access)

#### 8.1 Open Shell

1. In your Web Service dashboard
2. Click **"Shell"** tab (top right)
3. This opens a terminal to your running application

#### 8.2 Create Superuser

In the shell, run:

```bash
python manage.py createsuperuser
```

Follow the prompts:
- **Username**: admin (or your choice)
- **Email**: your-email@example.com
- **Password**: (enter secure password)
- **Password (again)**: (confirm)

#### 8.3 Access Admin Panel

Visit: `https://your-app.onrender.com/admin/`

Login with the credentials you just created.

---

### Step 9: Load Initial Data (Optional)

If you have fixtures with sample data:

#### 9.1 Open Shell Again

Click **"Shell"** in your service dashboard

#### 9.2 Load Data

```bash
python manage.py loaddata core/fixtures/initial_data.json
```

This will populate your database with:
- Sample facilities
- Sample devices
- Sample component information

---

### Step 10: Configure Custom Domain (Optional)

#### 10.1 Add Custom Domain

1. In your Web Service, go to **"Settings"**
2. Scroll to **"Custom Domain"** section
3. Click **"Add Custom Domain"**
4. Enter your domain: `www.yoursite.com`

#### 10.2 Update DNS Records

In your domain registrar (Namecheap, GoDaddy, etc.):

Add a CNAME record:
- **Type**: CNAME
- **Name**: www
- **Value**: `your-app.onrender.com`
- **TTL**: 3600

#### 10.3 Verify Domain

Back in Render, click **"Verify"**. Once DNS propagates (5-60 minutes), your custom domain will work!

---

## 🔄 Continuous Deployment

### Automatic Deploys

Render automatically redeploys when you push to GitHub:

```bash
# Make changes locally
git add .
git commit -m "Update feature"
git push origin main

# Render automatically detects the push and redeploys
```

### Manual Deploy

If needed, you can trigger manual deployment:
1. Go to your Web Service dashboard
2. Click **"Manual Deploy"**
3. Select **"Deploy latest commit"**

---

## 🛠️ Common Issues & Solutions

### Issue 1: Build Failed - Missing Dependencies

**Error**: `ModuleNotFoundError: No module named 'psycopg2'`

**Solution**:
```bash
# Add to requirements.txt
psycopg2-binary==2.9.9
gunicorn==21.2.0
whitenoise==6.6.0

# Commit and push
git add requirements.txt
git commit -m "Add deployment dependencies"
git push origin main
```

---

### Issue 2: Static Files Not Loading

**Error**: CSS/JS not loading, site looks unstyled

**Solution**:

1. Verify `whitenoise` in `MIDDLEWARE` (settings.py)
2. Check `STATIC_ROOT` is set correctly
3. Ensure `build.sh` runs `collectstatic`
4. Check logs for collectstatic errors

---

### Issue 3: Database Connection Error

**Error**: `could not connect to server: Connection refused`

**Solution**:

1. Verify `DATABASE_URL` environment variable is set
2. Check PostgreSQL database is running (Render dashboard)
3. Ensure `psycopg2-binary` is in requirements.txt
4. Verify database credentials match

---

### Issue 4: 500 Internal Server Error

**Error**: Site shows "Application Error"

**Solution**:

1. Check **Logs** tab in Render dashboard
2. Look for Python errors/tracebacks
3. Temporarily set `DEBUG=True` to see detailed error
4. Check allowed hosts in settings.py

---

### Issue 5: Build Takes Too Long / Times Out

**Solution**:

1. Optimize `requirements.txt` (remove unused packages)
2. Use `--no-cache-dir` in build command:
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

---

## 📊 Monitor Your Application

### View Logs

1. Go to your Web Service dashboard
2. Click **"Logs"** tab
3. See real-time application logs

### Check Metrics

1. Click **"Metrics"** tab
2. View:
   - CPU usage
   - Memory usage
   - Response times
   - HTTP status codes

---

## 💡 Render Free Tier Limitations

### What You Get (Free)

- ✅ 750 hours/month of runtime
- ✅ Automatic HTTPS/SSL
- ✅ Continuous deployment from Git
- ✅ 512 MB RAM
- ✅ PostgreSQL database (90 days, then expires)

### Limitations

- ⚠️ Service spins down after 15 minutes of inactivity
- ⚠️ First request after spin-down takes 30-60 seconds
- ⚠️ Database data expires after 90 days (free tier)
- ⚠️ Limited bandwidth

### Upgrade to Paid ($7/month)

For production use, consider upgrading:
- No spin-down (always running)
- More RAM (1-2 GB)
- Persistent database
- Better performance

---

## 🎯 Production Checklist

Before going live with real users:

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY` (never commit to Git)
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Enable HTTPS (Render provides free SSL)
- [ ] Set up database backups
- [ ] Monitor error logs regularly
- [ ] Test all features thoroughly
- [ ] Set up error tracking (Sentry)
- [ ] Configure email backend
- [ ] Add custom domain
- [ ] Upgrade to paid plan (avoid spin-down)

---

## 🚀 Quick Reference Commands

### Generate Secret Key
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Test Locally with Production Settings
```bash
python manage.py collectstatic --noinput
python manage.py check --deploy
gunicorn blogs.wsgi:application
```

### Access Render Shell
```
Dashboard → Your Service → Shell Tab
```

### View Logs
```
Dashboard → Your Service → Logs Tab
```

### Manual Deploy
```
Dashboard → Your Service → Manual Deploy → Deploy Latest Commit
```

---

## 📚 Additional Resources

- **Render Docs**: https://render.com/docs
- **Django Deployment**: https://docs.djangoproject.com/en/5.0/howto/deployment/
- **Render Community**: https://community.render.com/

---

## ✅ Your App is Live!

Congratulations! Your E-Waste Facility Locator is now deployed on Render.

**Your URLs:**
- **Application**: `https://your-app.onrender.com`
- **Admin Panel**: `https://your-app.onrender.com/admin/`

**Share your project:**
- Add the URL to your GitHub README
- Share on social media
- Add to your portfolio
- Show to potential employers/clients

---

<div align="center">

### 🎉 Deployment Successful!

**Need help?** Open an issue on [GitHub](https://github.com/Sahilshah12/E-WASTE-FACILITY-LOCATOR/issues)

**Enjoying Render?** Consider upgrading to support the platform and get better performance!

</div>
