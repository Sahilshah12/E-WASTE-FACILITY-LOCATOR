# E-WASTE LOCATOR - QUICK COMMAND REFERENCE

## 🚀 Essential Commands

### Start the Server
```powershell
cd c:\Django\blogs
python manage.py runserver
```
Access at: http://127.0.0.1:8000/

### Create Admin User
```powershell
python manage.py createsuperuser
```

### Database Operations
```powershell
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Load demo data
python manage.py loaddata core/fixtures/initial_data.json
```

### Django Shell
```powershell
python manage.py shell
```

## 📍 URL Routes

| Page | URL | Description |
|------|-----|-------------|
| Home | http://127.0.0.1:8000/ | Landing page |
| Locator | http://127.0.0.1:8000/locator/ | Facility map |
| Learn | http://127.0.0.1:8000/learn/ | E-waste education |
| Estimate | http://127.0.0.1:8000/estimate/ | Device value calculator |
| Dashboard | http://127.0.0.1:8000/dashboard/ | User stats (login required) |
| Register | http://127.0.0.1:8000/register/ | New account |
| Login | http://127.0.0.1:8000/login/ | User login |
| Admin | http://127.0.0.1:8000/admin/ | Admin panel |

## 🧪 Test Data

### Sample Devices to Search:
- Apple iPhone 12
- Samsung Galaxy S21
- Dell Latitude 5420
- HP ProBook 450
- Lenovo ThinkPad X1 Carbon

### Facilities by City:
- **Delhi**: Green E-Waste Recyclers
- **Mumbai**: EcoRecycle Center
- **Bangalore**: Tech Waste Solutions

## 💡 Quick Tips

1. **Register first** to access the dashboard
2. **Try the estimator** with demo device models
3. **Check the map** to see all facility locations
4. **Visit learn page** to see harmful components
5. **Use admin panel** to add more data

## 📊 Statistics

- **3 Facilities** loaded
- **10 Devices** in database
- **3 Components** documented
- **All features** fully functional

## 🛠️ Project Files

```
blogs/core/
├── models.py        # Database models
├── views.py         # Business logic
├── forms.py         # Form classes
├── urls.py          # URL routing
├── admin.py         # Admin config
├── templates/       # HTML files
├── static/          # CSS/JS
└── fixtures/        # Demo data
```

## 🎯 Next Steps

1. ✅ Create superuser
2. ✅ Login to admin panel
3. ✅ Add more facilities
4. ✅ Register a test user
5. ✅ Try recycling devices
6. ✅ Check leaderboard

---

**Happy Recycling! 🌱**
