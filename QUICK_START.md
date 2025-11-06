# 🚀 E-WASTE LOCATOR - QUICK START GUIDE

## ✅ Project Status: **FULLY FUNCTIONAL & CORRECT**

---

## 🎯 How to Use Your Application

### 1. **Start the Server**
```powershell
cd c:\Django\blogs
python manage.py runserver
```
**URL:** http://127.0.0.1:8000/

---

## 📱 Features & How to Test Them

### 🏠 **Home Page** (/)
- **What to See:** Animated landing page with stats
- **Features:** Hero section, feature cards, statistics
- **Test:** Click "Find Facilities" or "Estimate Value"

### 🗺️ **Facility Locator** (/locator/)
- **What to See:** Interactive map with facility markers
- **How to Use:**
  1. View all 3 facilities on the map
  2. Search by City (e.g., "Delhi", "Mumbai")
  3. Search by Pincode (e.g., "110001")
  4. Click markers for facility details
- **Current Data:** Delhi, Mumbai, Bangalore facilities

### 💡 **Learn About E-Waste** (/learn/)
- **What to See:** Random harmful component info
- **Components:** Lead, Mercury, Cadmium
- **Shows:** Health effects, environmental impact
- **Test:** Refresh to see different components

### 💰 **Value Estimator** (/estimate/)
- **How to Use:**
  1. Enter Brand (e.g., "Apple", "Samsung")
  2. Enter Model (e.g., "iPhone 13", "Galaxy S21")
  3. Click "Estimate"
- **Shows:** Metal content, estimated value, points
- **Available Devices:**
  - Apple iPhone 13 Pro
  - Samsung Galaxy S21
  - Apple MacBook Pro M1
  - Dell XPS 15
  - iPad Pro 12.9
  - Samsung Galaxy Tab S7
  - And more...

### 👤 **User Registration** (/register/)
- **How to Register:**
  1. Enter username
  2. Enter email (optional)
  3. Enter password (twice)
  4. Click "Sign Up"
- **Auto-creates:** User profile with 0 points

### 🔐 **Login** (/login/)
- **Existing Users:**
  - Username: `sahil` (or any user you created)
  - Password: (your password)

### 📊 **Dashboard** (/dashboard/)
- **Must be logged in**
- **Shows:**
  - Your points
  - Devices recycled
  - CO2 saved
  - Your rank
  - Leaderboard (top 5 users)
- **Action:** Recycle a device to earn points
- **How to Recycle:**
  1. Select a device from dropdown
  2. Click "Recycle Device"
  3. See points added!

---

## 🔧 Admin Panel

### Access Admin: http://127.0.0.1:8000/admin/

### Create Superuser (if needed):
```powershell
python manage.py createsuperuser
```

### Admin Features:
- ✅ Manage Facilities (add, edit, delete)
- ✅ Manage Devices (add new devices to catalog)
- ✅ Manage Components (add educational content)
- ✅ View User Profiles (see all user stats)

---

## 📊 Current Database

### Facilities (3)
1. **GreenTech Recyclers** - Delhi
   - Address: 123 Green Park, New Delhi
   - Items: Laptops, Smartphones, Tablets, Monitors

2. **EcoWaste Solutions** - Mumbai
   - Address: 456 Marine Drive, Mumbai
   - Items: All electronic devices

3. **TechRecycle Hub** - Bangalore
   - Address: 789 MG Road, Bangalore
   - Items: Computers, Phones, Printers

### Devices (10)
- Apple iPhone 13 Pro (₹800)
- Samsung Galaxy S21 (₹650)
- Apple MacBook Pro M1 (₹1500)
- Dell XPS 15 (₹1200)
- iPad Pro 12.9 (₹950)
- Samsung Galaxy Tab S7 (₹700)
- HP Pavilion Laptop (₹600)
- Lenovo ThinkPad X1 (₹1100)
- Google Pixel 6 (₹720)
- OnePlus 9 Pro (₹680)

### Components (3)
1. **Lead** - Found in CRT monitors, batteries
2. **Mercury** - Found in LCD screens, batteries
3. **Cadmium** - Found in rechargeable batteries

### Users (2)
- User profiles with points and recycling stats

---

## 🎮 Test Scenarios

### Scenario 1: New User Journey
1. Visit home page → Click "Join Now"
2. Register new account
3. Login
4. Go to Dashboard
5. Recycle a device (select iPhone 13 Pro)
6. See points added (80 points)
7. Check leaderboard

### Scenario 2: Find Facility
1. Go to Locator
2. Search "Delhi"
3. Click facility marker on map
4. See facility details

### Scenario 3: Estimate Device
1. Go to Estimate
2. Brand: "Apple"
3. Model: "iPhone 13"
4. See: 15mg gold, 80mg copper, 5mg silver
5. Value: ₹800 = 80 points

### Scenario 4: Learn
1. Go to Learn
2. Read about harmful component
3. Refresh to see another component

---

## 🔍 Common Commands

### Run Server
```powershell
cd c:\Django\blogs
python manage.py runserver
```

### Check for Errors
```powershell
python manage.py check
```

### Apply Migrations
```powershell
python manage.py migrate
```

### Create Superuser
```powershell
python manage.py createsuperuser
```

### Load Demo Data (if needed again)
```powershell
python manage.py loaddata core/fixtures/initial_data.json
```

### Access Django Shell
```powershell
python manage.py shell
```

---

## 🎨 Pages Overview

| Page | URL | Login Required? | Purpose |
|------|-----|-----------------|---------|
| Home | / | No | Landing page |
| Locator | /locator/ | No | Find facilities |
| Learn | /learn/ | No | Educational content |
| Estimate | /estimate/ | No | Device value |
| Register | /register/ | No | Sign up |
| Login | /login/ | No | Authentication |
| Dashboard | /dashboard/ | Yes | User stats |
| Logout | /logout/ | Yes | End session |
| Admin | /admin/ | Yes (superuser) | Management |

---

## 💡 Tips

### For Testing:
1. **Create multiple users** to test leaderboard
2. **Add more facilities** via admin panel
3. **Add more devices** to expand catalog
4. **Test on mobile** - fully responsive!

### For Development:
1. **Debug toolbar** - Install django-debug-toolbar for insights
2. **Custom CSS** - Edit `core/static/core/css/style.css`
3. **Custom JS** - Edit `core/static/core/js/main.js`
4. **Templates** - Edit files in `core/templates/core/`

---

## 🐛 Troubleshooting

### Server won't start?
```powershell
# Make sure you're in the right directory
cd c:\Django\blogs
# Check Python version
python --version  # Should be 3.13
```

### Page not loading?
- Check if server is running
- Check URL is correct
- Clear browser cache
- Check terminal for errors

### Template errors?
- Check file exists in `core/templates/core/`
- Check template syntax (no duplicate blocks)
- Check base.html extends properly

### Database errors?
```powershell
# Reset database (CAREFUL - deletes data!)
del db.sqlite3
python manage.py migrate
python manage.py loaddata core/fixtures/initial_data.json
python manage.py createsuperuser
```

---

## 📞 Support & Documentation

### Files to Check:
- **PROJECT_ANALYSIS.md** - Complete analysis report
- **README_EWASTE.md** - Project overview
- **SETUP_COMPLETE.md** - Setup documentation

### Key Code Locations:
- **Models:** `core/models.py`
- **Views:** `core/views.py`
- **URLs:** `core/urls.py`
- **Forms:** `core/forms.py`
- **Templates:** `core/templates/core/`
- **Static:** `core/static/core/`

---

## 🎉 You're All Set!

Your E-Waste Locator is **100% functional and ready to use!**

Start the server and explore all the features. Everything is working perfectly! 🚀

---

*Quick Start Guide - E-Waste Facility Locator*  
*Version: 1.0 | Date: November 3, 2025*
