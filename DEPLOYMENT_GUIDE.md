# 🚀 Deployment Guide - E-Waste Facility Locator

Complete guide to deploy your Django application to production environments.

---

## 📋 Table of Contents

1. [Pre-Deployment Checklist](#-pre-deployment-checklist)
2. [Local Production Testing](#-local-production-testing)
3. [Deploy to Heroku](#-deploy-to-heroku)
4. [Deploy to Railway](#-deploy-to-railway)
5. [Deploy to Render](#-deploy-to-render)
6. [Deploy to PythonAnywhere](#-deploy-to-pythonanywhere)
7. [Deploy to AWS EC2](#-deploy-to-aws-ec2)
8. [Deploy to DigitalOcean](#-deploy-to-digitalocean)
9. [Post-Deployment Tasks](#-post-deployment-tasks)
10. [Troubleshooting](#-troubleshooting)

---

## ✅ Pre-Deployment Checklist

### 1. Update `requirements.txt`

```bash
pip freeze > requirements.txt
```

Add these production dependencies:

```txt
Django==5.2.4
gunicorn==21.2.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
python-decouple==3.8
dj-database-url==2.1.0
```

### 2. Create `Procfile` (for Heroku/Railway/Render)

Create a file named `Procfile` (no extension) in project root:

```procfile
web: gunicorn blogs.wsgi --log-file -
```

### 3. Create `runtime.txt` (for Heroku)

```txt
python-3.13.0
```

### 4. Update `blogs/settings.py`

#### Install python-decouple

```bash
pip install python-decouple
```

#### Modify settings.py

```python
from decouple import config
import dj_database_url
import os

# Security Settings
SECRET_KEY = config('SECRET_KEY', default='your-secret-key-here')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# Database Configuration
if config('DATABASE_URL', default=None):
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL'),
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static Files Configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static'),
]

# WhiteNoise for serving static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... rest of middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security Settings for Production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
```

### 5. Create `.env` file (DO NOT COMMIT THIS)

```env
SECRET_KEY=your-very-long-random-secret-key-here
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### 6. Update `.gitignore`

```gitignore
# Environment variables
.env
.env.local
.env.production

# Static files
staticfiles/
/static/

# Database
*.sqlite3
db.sqlite3
```

### 7. Install Production Dependencies

```bash
pip install gunicorn whitenoise psycopg2-binary python-decouple dj-database-url
pip freeze > requirements.txt
```

---

## 🧪 Local Production Testing

Test your production configuration locally before deploying:

### 1. Set Debug to False

```bash
# In .env file
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 2. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 3. Run with Gunicorn

```bash
gunicorn blogs.wsgi:application
```

### 4. Test the Application

Visit `http://127.0.0.1:8000` and verify:
- ✅ Static files load correctly
- ✅ All pages render properly
- ✅ Forms submit without errors
- ✅ Authentication works

---

## 🟪 Deploy to Heroku

### Prerequisites
- Heroku account: https://signup.heroku.com/
- Heroku CLI installed

### Step 1: Install Heroku CLI

**Windows (PowerShell):**
```powershell
winget install Heroku.HerokuCLI
```

**macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### Step 2: Login to Heroku

```bash
heroku login
```

### Step 3: Create Heroku App

```bash
cd C:\Django\blogs
heroku create ewaste-facility-locator

# Or with custom name
heroku create your-custom-name
```

### Step 4: Add PostgreSQL Database

```bash
heroku addons:create heroku-postgresql:mini
```

### Step 5: Set Environment Variables

```bash
heroku config:set SECRET_KEY="your-secret-key-generate-new-one"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=".herokuapp.com"
```

### Step 6: Deploy to Heroku

```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main
```

### Step 7: Run Migrations

```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py loaddata core/fixtures/initial_data.json
```

### Step 8: Open Your App

```bash
heroku open
```

### Heroku Useful Commands

```bash
# View logs
heroku logs --tail

# Check app info
heroku info

# Open database console
heroku pg:psql

# Restart app
heroku restart

# Scale dynos
heroku ps:scale web=1
```

---

## 🚂 Deploy to Railway

Railway offers free hosting with generous limits.

### Step 1: Sign Up

Visit https://railway.app/ and sign up with GitHub

### Step 2: Create New Project

1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your repository: `E-WASTE-FACILITY-LOCATOR`

### Step 3: Add PostgreSQL Database

1. Click "New" → "Database" → "PostgreSQL"
2. Railway automatically provides `DATABASE_URL`

### Step 4: Configure Environment Variables

In Railway dashboard, go to Variables tab:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=*.up.railway.app
DISABLE_COLLECTSTATIC=1
```

### Step 5: Add Start Command

In Settings tab, set custom start command:

```bash
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn blogs.wsgi
```

### Step 6: Deploy

Railway automatically deploys on every git push to main branch.

```bash
git push origin main
```

### Step 7: Generate Domain

In Settings → Domains, click "Generate Domain"

Your app will be live at: `https://your-app.up.railway.app`

---

## 🎨 Deploy to Render

Render provides free tier with automatic deployments.

### Step 1: Sign Up

Visit https://render.com/ and create account

### Step 2: Create Web Service

1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - **Name**: ewaste-facility-locator
   - **Environment**: Python 3
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```bash
     gunicorn blogs.wsgi:application
     ```

### Step 3: Add Environment Variables

```
SECRET_KEY=your-secret-key-here
DEBUG=False
PYTHON_VERSION=3.13.0
ALLOWED_HOSTS=.onrender.com
```

### Step 4: Create PostgreSQL Database

1. Click "New +" → "PostgreSQL"
2. Name: ewaste-db
3. Copy internal database URL

### Step 5: Link Database

Add to environment variables:
```
DATABASE_URL=postgresql://user:password@host/database
```

### Step 6: Deploy

Click "Create Web Service" - Render will automatically deploy

### Step 7: Run Migrations

In Render dashboard → Shell:

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 🐍 Deploy to PythonAnywhere

Great for beginners, free tier available.

### Step 1: Sign Up

Visit https://www.pythonanywhere.com/ and create free account

### Step 2: Upload Your Code

**Option A: Upload via Dashboard**
1. Go to Files tab
2. Upload your project zip file
3. Extract it

**Option B: Clone from Git**
```bash
cd ~
git clone https://github.com/Sahilshah12/E-WASTE-FACILITY-LOCATOR.git
cd E-WASTE-FACILITY-LOCATOR
```

### Step 3: Create Virtual Environment

In Bash console:

```bash
mkvirtualenv --python=/usr/bin/python3.10 ewaste-env
pip install -r requirements.txt
```

### Step 4: Configure Web App

1. Go to Web tab
2. Click "Add a new web app"
3. Select "Manual configuration"
4. Choose Python 3.10

### Step 5: Configure WSGI File

Edit `/var/www/yourusername_pythonanywhere_com_wsgi.py`:

```python
import os
import sys

path = '/home/yourusername/E-WASTE-FACILITY-LOCATOR'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'blogs.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 6: Set Environment Variables

In Web tab → Environment variables:

```
SECRET_KEY=your-secret-key
DEBUG=False
```

### Step 7: Configure Static Files

In Web tab → Static files section:

```
URL: /static/
Directory: /home/yourusername/E-WASTE-FACILITY-LOCATOR/staticfiles
```

### Step 8: Collect Static Files & Migrate

In Bash console:

```bash
cd ~/E-WASTE-FACILITY-LOCATOR
workon ewaste-env
python manage.py collectstatic
python manage.py migrate
python manage.py createsuperuser
```

### Step 9: Reload Web App

Click "Reload" button in Web tab

Your app is live at: `https://yourusername.pythonanywhere.com`

---

## ☁️ Deploy to AWS EC2

For production-grade deployment with full control.

### Step 1: Launch EC2 Instance

1. Go to AWS Console → EC2
2. Click "Launch Instance"
3. Choose Ubuntu Server 22.04 LTS
4. Select t2.micro (free tier)
5. Configure security group:
   - SSH (22) - Your IP
   - HTTP (80) - 0.0.0.0/0
   - HTTPS (443) - 0.0.0.0/0
6. Create/download key pair

### Step 2: Connect to EC2

```bash
# Windows (PowerShell)
ssh -i "your-key.pem" ubuntu@your-ec2-public-ip

# Change permissions first
icacls "your-key.pem" /inheritance:r
icacls "your-key.pem" /grant:r "%username%:R"
```

### Step 3: Update System & Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv nginx postgresql postgresql-contrib -y
```

### Step 4: Clone Repository

```bash
cd /var/www
sudo git clone https://github.com/Sahilshah12/E-WASTE-FACILITY-LOCATOR.git
sudo chown -R ubuntu:ubuntu E-WASTE-FACILITY-LOCATOR
cd E-WASTE-FACILITY-LOCATOR
```

### Step 5: Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

### Step 6: Configure PostgreSQL

```bash
sudo -u postgres psql

# In PostgreSQL console:
CREATE DATABASE ewaste_db;
CREATE USER ewaste_user WITH PASSWORD 'strong_password';
ALTER ROLE ewaste_user SET client_encoding TO 'utf8';
ALTER ROLE ewaste_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ewaste_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ewaste_db TO ewaste_user;
\q
```

### Step 7: Create .env File

```bash
nano .env
```

Add:
```env
SECRET_KEY=generate-new-secret-key
DEBUG=False
DATABASE_URL=postgresql://ewaste_user:strong_password@localhost/ewaste_db
ALLOWED_HOSTS=your-ec2-ip,yourdomain.com
```

### Step 8: Run Migrations

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### Step 9: Configure Gunicorn Service

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add:
```ini
[Unit]
Description=gunicorn daemon for E-Waste Locator
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/E-WASTE-FACILITY-LOCATOR
Environment="PATH=/var/www/E-WASTE-FACILITY-LOCATOR/venv/bin"
ExecStart=/var/www/E-WASTE-FACILITY-LOCATOR/venv/bin/gunicorn --workers 3 --bind unix:/var/www/E-WASTE-FACILITY-LOCATOR/gunicorn.sock blogs.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start service:
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

### Step 10: Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/ewaste
```

Add:
```nginx
server {
    listen 80;
    server_name your-ec2-ip yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/E-WASTE-FACILITY-LOCATOR;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/E-WASTE-FACILITY-LOCATOR/gunicorn.sock;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/ewaste /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### Step 11: Configure Firewall

```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

### Step 12: Setup SSL (Optional but Recommended)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Your app is live at: `http://your-ec2-ip` or `https://yourdomain.com`

---

## 🌊 Deploy to DigitalOcean

Similar to AWS but simpler interface.

### Step 1: Create Droplet

1. Go to DigitalOcean → Create → Droplets
2. Choose Ubuntu 22.04 LTS
3. Select Basic plan ($4/month)
4. Add SSH key
5. Create Droplet

### Step 2: Follow AWS EC2 Steps 2-12

The process is identical to AWS EC2 deployment from Step 2 onwards.

---

## ✅ Post-Deployment Tasks

### 1. Test All Features

- [ ] Homepage loads correctly
- [ ] User registration works
- [ ] Login/Logout functional
- [ ] Facility locator map displays
- [ ] Device estimator calculates values
- [ ] Dashboard shows user data
- [ ] Admin panel accessible
- [ ] Static files load (CSS, JS, images)

### 2. Setup Monitoring

**Sentry for Error Tracking:**
```bash
pip install sentry-sdk
```

Add to settings.py:
```python
import sentry_sdk
sentry_sdk.init(
    dsn="your-sentry-dsn",
    traces_sample_rate=1.0,
)
```

### 3. Setup Backups

**Heroku:**
```bash
heroku pg:backups:schedule DATABASE_URL --at '02:00 America/Los_Angeles'
```

**AWS/DigitalOcean:**
```bash
# Create backup script
sudo nano /usr/local/bin/backup-db.sh
```

```bash
#!/bin/bash
pg_dump ewaste_db > /backups/ewaste_$(date +%Y%m%d).sql
```

```bash
sudo chmod +x /usr/local/bin/backup-db.sh
# Add to crontab
crontab -e
# Add: 0 2 * * * /usr/local/bin/backup-db.sh
```

### 4. Setup Custom Domain

1. Purchase domain (Namecheap, GoDaddy, etc.)
2. Add DNS records:
   - A Record: `@` → Your server IP
   - A Record: `www` → Your server IP
3. Update `ALLOWED_HOSTS` in settings.py

### 5. Enable HTTPS

For production, always use HTTPS:
```bash
# Let's Encrypt (Free SSL)
sudo certbot --nginx -d yourdomain.com
```

---

## 🔧 Troubleshooting

### Issue: Static Files Not Loading

**Solution:**
```bash
python manage.py collectstatic --noinput
# Check STATIC_ROOT in settings.py
# Verify WhiteNoise is in MIDDLEWARE
```

### Issue: Database Connection Error

**Solution:**
```bash
# Check DATABASE_URL
heroku config:get DATABASE_URL
# Verify PostgreSQL is running
sudo systemctl status postgresql
```

### Issue: 500 Internal Server Error

**Solution:**
```bash
# Check logs
heroku logs --tail  # Heroku
sudo tail -f /var/log/nginx/error.log  # AWS/DO

# Enable DEBUG temporarily
heroku config:set DEBUG=True
```

### Issue: CSS/JS Not Updating

**Solution:**
```bash
# Clear static files and recollect
rm -rf staticfiles/
python manage.py collectstatic --clear --noinput
# Hard refresh browser (Ctrl+Shift+R)
```

### Issue: Gunicorn Won't Start

**Solution:**
```bash
# Check service status
sudo systemctl status gunicorn
# View logs
sudo journalctl -u gunicorn
# Restart service
sudo systemctl restart gunicorn
```

---

## 📚 Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Heroku Django Guide](https://devcenter.heroku.com/articles/django-app-configuration)
- [Railway Documentation](https://docs.railway.app/)
- [Render Django Guide](https://render.com/docs/deploy-django)
- [DigitalOcean Tutorials](https://www.digitalocean.com/community/tutorials)

---

## 🎯 Recommended Deployment Path

**For Beginners:**
1. ✅ **PythonAnywhere** - Easiest, free tier available
2. ✅ **Heroku** - Simple, good documentation

**For Production:**
1. ✅ **Railway** - Modern, generous free tier
2. ✅ **Render** - Easy to use, good performance
3. ✅ **AWS EC2** - Full control, scalable

**For Learning:**
1. ✅ **DigitalOcean** - Good tutorials, affordable

---

<div align="center">

### 🚀 Ready to Deploy!

Choose your platform and follow the steps above.

Need help? Open an issue on [GitHub](https://github.com/Sahilshah12/E-WASTE-FACILITY-LOCATOR/issues)

**Good luck with your deployment! 🎉**

</div>
