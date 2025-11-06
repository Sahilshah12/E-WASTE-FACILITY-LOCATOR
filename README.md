# 🌍 E-Waste Facility Locator

<div align="center">

![Django](https://img.shields.io/badge/Django-5.2.4-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.11.9-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)
![Deployment](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render)

**Smart Automation for Responsible E-Waste Management**

🌐 **[View Live Application](https://e-waste-facility-locator-zy4a.onrender.com)** 🌐

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [About](#-about-the-project)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Screenshots](#-screenshots)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 About The Project

The **E-Waste Facility Locator** is a comprehensive Django-based web application designed to promote responsible e-waste management. With India generating over 3.2 million tonnes of e-waste annually and only 10% being formally recycled, this platform bridges the gap between consumers and certified recycling facilities.

### 🌟 Why This Project?

- **Environmental Impact**: Prevents toxic materials (lead, mercury, cadmium) from contaminating soil and water
- **User Education**: Interactive pop-ups educate users about harmful e-waste components
- **Gamification**: Rewards system encourages responsible recycling behavior
- **Smart Estimation**: AI-powered device value calculator incentivizes recycling
- **Accessibility**: Mobile-responsive design with interactive mapping

### 🎬 Demo

🔗 **Live Demo**: **[https://e-waste-facility-locator-zy4a.onrender.com](https://e-waste-facility-locator-zy4a.onrender.com)**

> **Note**: The app is hosted on Render's free tier. Initial load may take 30-60 seconds as the server spins up from sleep mode.

📹 **Video Walkthrough**: [YouTube Link]

---

## ✨ Key Features

### 🔐 **1. User Authentication System**
- Secure registration and login with Django's built-in authentication
- Password hashing and session management
- User profile creation with recycling statistics tracking

### 🗺️ **2. Interactive Facility Locator**
- **Leaflet.js** integration for real-time interactive maps
- Search and filter e-waste facilities by location
- Facility details: address, phone, working hours, accepted items
- Distance calculation from user location
- JSON API endpoint for dynamic data loading

### 📚 **3. Educational Pop-ups**
- Information cards about harmful e-waste components
- Details on **Lead**, **Mercury**, and **Cadmium** health impacts
- Dismissible modals with engaging visuals
- Raises awareness about proper disposal methods

### 💰 **4. Device Value Estimator**
- Database of 10+ common electronic devices
- Estimated recycling value calculation
- Categories: Smartphones, Laptops, Tablets, Smart Watches
- Helps users understand monetary benefits of recycling

### 🏆 **5. User Dashboard & Gamification**
- Personal recycling statistics and progress tracking
- **Points System**: Earn points for each device recycled
- **Leaderboard**: Community-wide rankings
- **Badges**: Achievements for recycling milestones
- Visual charts showing recycling impact

### 🛡️ **6. Admin Dashboard**
- Full CRUD operations for facilities, devices, and components
- User management and statistics
- Content moderation tools
- Built with Django Admin customization

---

## 🛠️ Technology Stack

### **Backend**
```
Django 5.2.4          - Web Framework
Python 3.13           - Programming Language
SQLite3               - Database (Development)
Django ORM            - Object-Relational Mapping
```

### **Frontend**
```
HTML5 & CSS3          - Markup & Styling
Bootstrap 5.3.2       - UI Framework
JavaScript (ES6+)     - Client-side Logic
jQuery 3.7.1          - DOM Manipulation
Leaflet.js 1.9.4      - Interactive Maps
Bootstrap Icons 1.11  - Icon Library
```

### **Development Tools**
```
Git                   - Version Control
VS Code               - Code Editor
Chrome DevTools       - Debugging
Virtual Environment   - Dependency Isolation
```

---

## 📸 Screenshots

<details>
<summary>Click to expand screenshots</summary>

### Home Page
![Home Page](screenshots/home.png)

### Facility Locator with Map
![Locator](screenshots/locator.png)

### Educational Pop-ups
![Learn](screenshots/learn.png)

### Device Value Estimator
![Estimator](screenshots/estimator.png)

### User Dashboard
![Dashboard](screenshots/dashboard.png)

### Admin Panel
![Admin](screenshots/admin.png)

</details>

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

```bash
Python 3.8+
pip (Python package manager)
Git
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sahilshah12/E-WASTE-FACILITY-LOCATOR.git
   cd E-WASTE-FACILITY-LOCATOR
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Load initial data (optional)**
   ```bash
   python manage.py loaddata core/fixtures/initial_data.json
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main App: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

---

## 📁 Project Structure

```
E-WASTE-FACILITY-LOCATOR/
│
├── blogs/                      # Project configuration
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py                # WSGI config
│   └── asgi.py                # ASGI config
│
├── core/                       # Main application
│   ├── migrations/            # Database migrations
│   ├── static/core/           # Static files (CSS, JS)
│   │   ├── css/style.css
│   │   └── js/main.js
│   ├── templates/core/        # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── locator.html
│   │   ├── learn.html
│   │   ├── estimate.html
│   │   ├── dashboard.html
│   │   ├── register.html
│   │   └── login.html
│   ├── fixtures/              # Initial data
│   │   └── initial_data.json
│   ├── admin.py               # Admin configuration
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── forms.py               # Form classes
│   ├── urls.py                # App URL patterns
│   └── tests.py               # Unit tests
│
├── contact/                    # Contact form app
│   ├── migrations/
│   ├── templates/contact/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── school/                     # Legacy app (optional)
│   └── ...
│
├── app/                        # Legacy app (optional)
│   └── ...
│
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── db.sqlite3                  # SQLite database (gitignored)
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
├── E_WASTE_PROJECT_REPORT.md  # Comprehensive documentation
└── PROJECT_ANALYSIS.md         # Technical analysis
```

---

## 🔌 API Endpoints

### Public Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/locator/` | Facility locator with map |
| GET | `/learn/` | Educational content |
| GET | `/estimate/` | Device value estimator |
| GET | `/register/` | User registration |
| GET | `/login/` | User login |

### Authenticated Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/dashboard/` | User dashboard (requires login) |
| POST | `/logout/` | User logout |

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/facilities-json/` | JSON data of all facilities |

### Admin Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin/` | Django admin panel |

---

## 🧪 Testing

### Run Unit Tests

```bash
python manage.py test
```

### Test Specific App

```bash
python manage.py test core
```

### Check Code Coverage

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Manual Testing Scenarios

1. **User Registration Flow**
   - Navigate to `/register/`
   - Fill form and submit
   - Verify profile creation

2. **Facility Search**
   - Go to `/locator/`
   - Test map interactions
   - Search for facilities

3. **Device Estimation**
   - Visit `/estimate/`
   - Select device and condition
   - Check estimated value

4. **Dashboard Gamification**
   - Log in and visit `/dashboard/`
   - Add recycled device
   - Verify points and leaderboard update

---

## 🌐 Deployment

### 🚀 Currently Deployed On

**Platform**: Render.com  
**Live URL**: [https://e-waste-facility-locator-zy4a.onrender.com](https://e-waste-facility-locator-zy4a.onrender.com)  
**Database**: PostgreSQL (Render-hosted)  
**Python Version**: 3.11.9  
**Status**: ✅ Live

### Production Checklist

- [x] Update `SECRET_KEY` in settings.py
- [x] Set `DEBUG = False`
- [x] Configure `ALLOWED_HOSTS`
- [x] Use PostgreSQL instead of SQLite
- [x] Set up static files with WhiteNoise
- [x] Configure environment variables
- [ ] Configure email backend for notifications
- [ ] Enable custom domain with HTTPS/SSL
- [ ] Set up logging and monitoring

### Deploy to Render (Your Own Instance)

See detailed step-by-step guide in `RENDER_DEPLOYMENT.md`.

**Quick Steps:**
1. Push your code to GitHub
2. Create new Web Service on Render
3. Connect your GitHub repository
4. Set build command: `./build.sh`
5. Set start command: `gunicorn blogs.wsgi:application`
6. Add environment variables (SECRET_KEY, DEBUG, DATABASE_URL)
7. Create PostgreSQL database and link it
8. Deploy!

### Deploy to Heroku

```bash
# Install Heroku CLI
heroku login
heroku create ewaste-locator

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Configure environment
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Deploy to Railway

See detailed deployment guide in `DEPLOYMENT_GUIDE.md`.

---

## 🗺️ Roadmap

### Phase 1: Core Features ✅
- [x] User authentication
- [x] Facility locator with maps
- [x] Educational content
- [x] Device value estimator
- [x] User dashboard
- [x] Admin panel

### Phase 2: Enhancements 🚧
- [ ] QR code generation for facilities
- [ ] Email notifications for recycling reminders
- [ ] Advanced search filters (distance, rating)
- [ ] Facility reviews and ratings
- [ ] SMS alerts for nearby facilities

### Phase 3: Advanced Features 🔮
- [ ] Mobile app (React Native)
- [ ] Social sharing of achievements
- [ ] Corporate bulk recycling module
- [ ] Integration with facility APIs
- [ ] Payment gateway for value redemption
- [ ] Multi-language support
- [ ] Dark mode UI

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write descriptive commit messages
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📜 License

Distributed under the MIT License. See `LICENSE` file for more information.

```
MIT License

Copyright (c) 2025 Sahil Shah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📞 Contact

**Sahil Shah**

- GitHub: [@Sahilshah12](https://github.com/Sahilshah12)
- Email: sahilshah@example.com
- LinkedIn: [Your LinkedIn Profile]
- Portfolio: [Your Portfolio Website]

**Project Link**: [https://github.com/Sahilshah12/E-WASTE-FACILITY-LOCATOR](https://github.com/Sahilshah12/E-WASTE-FACILITY-LOCATOR)

---

## 🙏 Acknowledgments

Special thanks to:

- **Django Documentation** - Excellent framework documentation
- **Leaflet.js** - For the amazing mapping library
- **Bootstrap Team** - Responsive UI framework
- **Stack Overflow Community** - Problem-solving support
- **GitHub** - Version control and hosting
- **Environmental Organizations** - E-waste awareness data
- **Open Source Contributors** - Inspiration and code references

### Resources Used

- [Django Official Docs](https://docs.djangoproject.com/)
- [Leaflet.js Documentation](https://leafletjs.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [E-Waste Statistics - CPCB India](http://cpcb.nic.in/)
- [WHO Guidelines on E-Waste](https://www.who.int/)

---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/Sahilshah12/E-WASTE-FACILITY-LOCATOR?style=social)
![GitHub forks](https://img.shields.io/github/forks/Sahilshah12/E-WASTE-FACILITY-LOCATOR?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Sahilshah12/E-WASTE-FACILITY-LOCATOR?style=social)

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

Made with ❤️ and ♻️ for a sustainable future

**[Back to Top](#-e-waste-facility-locator)**

</div>
