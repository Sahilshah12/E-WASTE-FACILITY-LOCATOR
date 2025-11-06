# E-Waste Facility Locator

## 🏷️ Project Overview
A Smart Automation Web App for Responsible E-Waste Management built with Django 5.x

## ✨ Features

### Main Functional Modules:
1. **User Authentication** - Register, Login, Logout
2. **Facility Locator** - Interactive map with OpenStreetMap and Leaflet.js
3. **Educational Pop-ups** - Learn about harmful e-waste components
4. **Device Value Estimator** - Calculate metal recovery value and credit points
5. **User Dashboard** - Track points, recycled items, and CO₂ saved
6. **Admin Dashboard** - Manage facilities, devices, users, and components

## 🚀 Quick Start

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Navigate to the project directory**
   ```powershell
   cd c:\Django\blogs
   ```

2. **Activate your virtual environment** (if using one)
   ```powershell
   # If you have a virtual environment
   .\env\Scripts\Activate.ps1
   ```

3. **Install required packages**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Make migrations for the core app**
   ```powershell
   python manage.py makemigrations core
   ```

5. **Apply database migrations**
   ```powershell
   python manage.py migrate
   ```

6. **Load demo data (facilities, devices, components)**
   ```powershell
   python manage.py loaddata core/fixtures/initial_data.json
   ```

7. **Create a superuser for admin access**
   ```powershell
   python manage.py createsuperuser
   ```
   Follow the prompts to set username, email, and password.

8. **Run the development server**
   ```powershell
   python manage.py runserver
   ```

9. **Access the application**
   - Main Site: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
blogs/
├── core/                          # E-Waste Locator App
│   ├── admin.py                   # Admin configurations
│   ├── models.py                  # Database models
│   ├── views.py                   # View functions
│   ├── urls.py                    # URL routing
│   ├── forms.py                   # Form classes
│   ├── fixtures/
│   │   └── initial_data.json      # Demo data
│   ├── static/core/
│   │   ├── css/
│   │   │   └── style.css          # Custom styles
│   │   └── js/
│   │       └── main.js            # Custom JavaScript
│   └── templates/core/
│       ├── base.html              # Base template
│       ├── home.html              # Landing page
│       ├── locator.html           # Facility map
│       ├── learn.html             # Educational content
│       ├── estimate.html          # Value estimator
│       ├── dashboard.html         # User dashboard
│       ├── login.html             # Login page
│       └── register.html          # Registration page
├── blogs/
│   ├── settings.py                # Project settings
│   └── urls.py                    # Main URL config
├── db.sqlite3                     # SQLite database
├── manage.py                      # Django management script
└── requirements.txt               # Python dependencies
```

## 🗄️ Database Models

### 1. Facility
Stores e-waste recycling facility information:
- Name, address, city, pincode
- Latitude, longitude (for maps)
- Contact information
- Accepted items list

### 2. ComponentInfo
Educational data about harmful components:
- Component name (Lead, Mercury, Cadmium)
- Devices where found
- Health effects
- Environmental impact

### 3. Device
Electronic device catalog:
- Brand and model name
- Device type (laptop, smartphone, etc.)
- Metal content (gold, silver, copper in mg)
- Estimated recovery value in ₹

### 4. UserProfile
Extended user profile with gamification:
- Points earned from recycling
- Total devices recycled
- CO₂ saved (calculated)
- Automatic creation via Django signals

## 🎮 Usage Guide

### For Users:

1. **Register an Account**
   - Click "Register" in the navbar
   - Fill in username, email, and password
   - You'll be automatically logged in

2. **Find Recycling Facilities**
   - Go to "Locator" page
   - View facilities on interactive map
   - Search by city or pincode
   - Click markers for facility details

3. **Learn About E-Waste**
   - Visit "Learn" page
   - Read about harmful components
   - Click "Show Another Fact" for more info

4. **Estimate Device Value**
   - Go to "Estimate" page
   - Enter device brand and model
   - See metal content and estimated value
   - View points you'll earn

5. **Track Your Progress**
   - Access "Dashboard" (login required)
   - View your points, recycled devices, CO₂ saved
   - Simulate recycling devices
   - Check leaderboard rankings

### For Administrators:

1. **Access Admin Panel**
   - Go to http://127.0.0.1:8000/admin/
   - Login with superuser credentials

2. **Manage Content**
   - Add/edit/delete facilities
   - Update device database
   - Add component information
   - View user statistics

## 🧪 Demo Data Included

### Facilities (3):
- Green E-Waste Recyclers Delhi
- EcoRecycle Mumbai Center
- Tech Waste Solutions Bangalore

### Devices (10):
- Apple iPhone 12, Samsung Galaxy S21
- Dell Latitude 5420, HP ProBook 450
- Apple iPad Pro 11, Lenovo ThinkPad X1
- OnePlus 9 Pro, Samsung Galaxy Tab S7
- Asus ROG Strix G15, Xiaomi Mi 11X Pro

### Components (3):
- Lead - Health and environmental effects
- Mercury - Neurotoxic impacts
- Cadmium - Cancer and pollution risks

## 🎨 Frontend Technologies

- **Bootstrap 5** - Responsive UI framework
- **Bootstrap Icons** - Icon library
- **Leaflet.js** - Interactive maps
- **OpenStreetMap** - Map tiles
- **jQuery** - JavaScript utilities
- **Custom CSS** - Additional styling

## 🔒 Security Features

- Django's built-in authentication system
- CSRF protection on all forms
- Password validation
- Login required decorators for protected views
- Secure session management

## 📊 Gamification System

### Points Calculation:
- Points = Device Value ÷ 10
- Example: ₹200 device = 20 points

### CO₂ Savings:
- CO₂ Saved = Points × 0.05 kg
- Example: 100 points = 5 kg CO₂ saved

### Leaderboard:
- Top 5 users by points
- Real-time ranking system
- User rank display on dashboard

## 🛠️ Customization Tips

### Adding New Facilities:
```powershell
python manage.py shell
```
```python
from core.models import Facility
f = Facility.objects.create(
    name="New Facility",
    address="123 Street",
    city="YourCity",
    pincode="123456",
    latitude=12.345678,
    longitude=77.123456,
    contact="+91-1234567890",
    accepted_items="All devices"
)
```

### Adding New Devices:
Use the admin panel or Django shell to add devices with metal content and estimated values.

## 🐛 Troubleshooting

### Common Issues:

1. **Import Error for 'core'**
   - Ensure 'core' is in INSTALLED_APPS in settings.py
   - Run migrations again

2. **Static Files Not Loading**
   - Check STATIC_URL in settings.py
   - Run `python manage.py collectstatic`

3. **Map Not Displaying**
   - Check internet connection (Leaflet CDN required)
   - Check browser console for JavaScript errors

4. **No Fixtures Loading**
   - Ensure migrations are applied first
   - Check JSON file syntax

## 📝 API Endpoints

- `/` - Home page
- `/locator/` - Facility locator with map
- `/learn/` - Educational content
- `/estimate/` - Device value estimator
- `/dashboard/` - User dashboard (auth required)
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/api/facilities/` - JSON API for facilities

## 🌟 Future Enhancements (Bonus Features)

- [ ] QR code generator for verified recyclers
- [ ] Dark/Light mode toggle
- [ ] Export dashboard data to PDF
- [ ] Email notifications for recycling reminders
- [ ] Mobile app integration
- [ ] Payment gateway for rewards redemption
- [ ] Social sharing features
- [ ] Multilingual support

## 📜 License

This project is created for educational purposes.

## 👨‍💻 Developer Notes

### Key Implementation Details:

1. **Django Signals**: Automatic UserProfile creation when User is created
2. **Model Methods**: `get_point_value()`, `add_recycled_device()`, `get_rank()`
3. **Template Inheritance**: All templates extend `base.html`
4. **Bootstrap Components**: Cards, forms, navbar, alerts, badges
5. **Leaflet Integration**: Custom markers, popups, clustering
6. **Responsive Design**: Mobile-first approach

### Code Organization:
- Models handle data structure and business logic
- Views manage request/response and user interactions
- Forms validate and clean user input
- Templates provide clean separation of presentation
- Static files enhance user experience

## 📞 Support

For issues or questions:
1. Check Django documentation: https://docs.djangoproject.com/
2. Review Leaflet.js docs: https://leafletjs.com/
3. Bootstrap 5 docs: https://getbootstrap.com/docs/5.3/

---

**Happy Recycling! 🌱♻️**

*Making the world greener, one device at a time.*
