# Koop-KPMIM# Koperasi KPMIM Website

A comprehensive Django-based website for Koperasi Kolej Profesional MARA Indera Mahkota Kuantan Berhad (KPMIM Cooperative), serving as the official digital portal for the college community.

![System Status](https://img.shields.io/badge/Status-Active-green)
![Framework](https://img.shields.io/badge/Framework-Django-092E20)
![License](https://img.shields.io/badge/License-Educational-blue)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [URL Structure](#url-structure)
- [Database Models](#database-models)
- [Color Scheme](#color-scheme)
- [Usage](#usage)
- [Services Offered](#services-offered)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Koperasi KPMIM Website is designed to provide comprehensive information and services to the KPMIM college community, including students, lecturers, and staff. The platform showcases cooperative services, organizational structure, and facilitates online bookings for various facilities.

### Project Goals
- Provide centralized information about cooperative services
- Enable easy access to booking facilities
- Showcase organizational transparency through interactive charts
- Support the cooperative's mission of serving the college community
- Enhance digital presence and accessibility

## Features

### Public Information
- **Homepage**: Hero section with service highlights and testimonials
- **About Section**: Complete history, vision, and mission of KPMIM
- **Interactive Organization Chart**: Clickable member profiles with modal details
- **Service Directory**: Comprehensive listing of all cooperative services
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices

### About Section
- **Sejarah (History)**: Detailed timeline of KPMIM establishment and development
- **Visi (Vision)**: "Melahirkan Modal Insan Global dan Berintegriti"
- **Misi (Mission)**: "Memperkasa pendidikan tertiari yang holistik berteraskan ilmu, teknologi dan nilai keusahawanan"

### Organization Features
- **Interactive Org Chart**: Hierarchical display of cooperative leadership
- **Member Profiles**: Detailed information including contact details and bio
- **Modal Popups**: Enhanced user experience with member information display
- **Photo Gallery**: Professional portraits of key personnel

### Service Management
- **Service Catalog**: Complete listing of available services
- **Working Hours**: Clear display of operational schedules
- **Booking Integration**: Direct links to external booking systems
- **Service Details**: Comprehensive information for each offering

### Tourism Services
- **Student Packages**: Travel packages designed for students
- **Educational Trips**: Edutrip and CSR program offerings
- **Package Management**: Pricing and duration information display

## System Requirements

### Minimum Hardware Requirements
- **Processor**: Dual-core processor with 1GHz clock speed
- **Memory**: 4GB RAM minimum
- **Storage**: 1GB available space
- **Network**: Stable internet connection required
- **Display**: 1024x768 resolution minimum

### Software Requirements
- **Operating System**: Windows 10+, macOS 10.15+, or Ubuntu 18.04 LTS
- **Web Browser**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Python**: 3.8+ (for development)
- **Database**: SQLite (default) or PostgreSQL/MySQL for production

### Development Requirements
- **Python**: 3.8+
- **Django**: 4.0+
- **Bootstrap**: 5.3.2
- **Font Awesome**: 6.5.1
- **AOS**: 2.3.4 (Animate On Scroll)

## Installation

### Prerequisites
1. Install Python 3.8+
2. Install pip (Python package manager)
3. Install Git (optional, for version control)

### Setup Instructions

1. **Clone/Download the Project**
   ```bash
   git clone [repository-url]
   cd kpmimkoop
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -m requirements.txt
   pip install django
   pip install pillow  # For image handling
   pip install django-crispy-forms  # For form styling (if needed)
   ```

4. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser** (Optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Website**
   Open your browser and navigate to `http://localhost:8000`

## URL Structure

### Main Navigation Routes
```
/                           # Homepage
/tentang/                   # About main page
/tentang/sejarah/          # History page
/tentang/visi/             # Vision page
/tentang/misi/             # Mission page
```

### Organization Routes
```
/organisasi/               # Organization main page
/organisasi/carta/         # Interactive organization chart
```

### Service Routes
```
/perkhidmatan/                    # Services overview
/perkhidmatan/cafe-air/           # Cafe Air details
/perkhidmatan/koop-mart/          # Koop Mart details
/perkhidmatan/kios-aok-cafe/      # Kios "Aok Cafe" details
/perkhidmatan/dobi/               # Laundry services
/perkhidmatan/parcel/             # IM Parcel services
/perkhidmatan/bilik-acara/        # Event hall booking
/perkhidmatan/pakir-berbumbung/   # Covered parking
```

### Tourism Routes
```
/pelancongan/              # Tourism overview
/pelancongan/siswa/        # Student tourism packages
/pelancongan/edutrip-csr/  # Educational trips and CSR
```

### External Links
```
https://docs.google.com/forms/...  # Booking system (Google Forms)
```

## Database Models

### AboutContent
- **Fields**: title, content, page_type, last_updated
- **Purpose**: Manages content for About pages (History, Vision, Mission)
- **Choices**: HISTORY, VISION, MISSION

### OrganizationMember
- **Fields**: name, position, image, order
- **Purpose**: Stores organization chart member information
- **Features**: Image upload support, ordering capability

### Service
- **Fields**: name, description, image, is_active
- **Purpose**: Manages cooperative service listings
- **Features**: Image support, active/inactive status

### Booking
- **Fields**: name, email, phone, booking_type, dates, times, notes, status
- **Purpose**: Handles booking requests for various services
- **Types**: BILIK, DOBI, PARCEL, PAKIR
- **Status**: PENDING, APPROVED, REJECTED

### TourPackage
- **Fields**: name, description, price, duration, image, is_edutrip, is_csr
- **Purpose**: Manages tourism package offerings
- **Categories**: Student packages, Educational trips, CSR programs

### KoopMartOrder
- **Fields**: name, email, phone, order_details, status, created_at
- **Purpose**: Handles Koop Mart order processing
- **Status**: PENDING, PROCESSING, COMPLETED, CANCELLED

## Color Scheme

The website follows KPMIM's official color palette:

- **Primary Color**: `#0d47a1` (Dark Blue - Primary brand color)
- **Secondary Color**: `#2196f3` (Light Blue - Accent color)
- **Dark Color**: `#333` (Text and headers)
- **Light Color**: `#f8f9fa` (Background and light sections)
- **Success**: `#28a745` (Success messages)
- **Warning**: `#ffc107` (Warning messages)
- **Danger**: `#dc3545` (Error messages)

## Usage

### Navigation
- **Responsive Navbar**: Collapsible menu for mobile devices
- **Dropdown Menus**: Organized content sections
- **Breadcrumb Navigation**: Clear page hierarchy
- **Footer Links**: Quick access to important pages

### Interactive Features
- **Organization Chart**: Click on member cards to view detailed information
- **Modal Windows**: Enhanced user experience for member profiles
- **Hover Effects**: Visual feedback on interactive elements
- **Smooth Animations**: AOS library for scroll animations

### Booking System
- **External Integration**: Google Forms for booking requests
- **Multiple Services**: Support for various booking types
- **Contact Information**: Easy access to cooperative contact details

## Services Offered

### Food & Beverage
- **Cafe Air**: Main cafeteria with full meal service
- **Kios "Aok Cafe"**: Quick service kiosk for snacks and beverages

### Retail & Commerce
- **Koop Mart**: Daily necessities store for campus community
- **Operating Hours**: Mon-Fri: 8:00 AM - 10:00 PM, Sat: 9:00 AM - 6:00 PM

### Support Services
- **IM Parcel**: Package delivery and collection service
- **Dobi**: Professional laundry services for students and staff
- **Bilik Acara**: Event hall rental for meetings and celebrations
- **Pakir Berbumbung**: Covered parking facilities

### Tourism & Education
- **Unit Pelancongan Siswa**: Student travel packages and group tours
- **Edutrip dan CSR**: Educational trips and corporate social responsibility programs

## Technology Stack

### Backend Framework
- **Django**: Python web framework for robust backend development
- **SQLite**: Default database for development
- **Django ORM**: Object-relational mapping for database operations

### Frontend Technologies
- **HTML5**: Modern markup for semantic structure
- **CSS3**: Advanced styling with custom properties
- **JavaScript**: Interactive functionality and animations
- **Bootstrap 5.3.2**: Responsive grid system and components

### External Libraries
- **Font Awesome 6.5.1**: Icon library for visual elements
- **AOS 2.3.4**: Animate On Scroll library for smooth animations
- **jQuery 3.7.1**: JavaScript library for DOM manipulation

### Development Tools
- **Git**: Version control system
- **VS Code**: Recommended code editor
- **Chrome DevTools**: Browser debugging and testing

## Contributing

This project is maintained for KPMIM Cooperative educational purposes. For contributions or issues:

1. **Code Standards**: Follow PEP 8 for Python and web standards for frontend
2. **Documentation**: Update documentation for any new features
3. **Testing**: Test all functionality across different browsers
4. **Responsive Design**: Ensure mobile compatibility for all changes

## Support

For technical support or questions about the website:

- **KPMIM IT Department**: Contact through official channels
- **Email**: koperasi@kpmim.edu.my
- **Phone**: 09-573 3333
- **Address**: Jalan IM 9/40, Bandar Indera Mahkota, 25200 Kuantan, Pahang

## License

This project is developed for educational purposes at Kolej Profesional MARA Indera Mahkota. All rights reserved.

**© 2024 Koperasi KPMIM | All Rights Reserved**

---

### Project Information
- **Institution**: Kolej Profesional MARA Indera Mahkota
- **Department**: Koperasi KPMIM
- **Session**: 2024/2025
- **Purpose**: Official cooperative website and service portal
- **Target Users**: Students, lecturers, and staff of KPMIM

### Contact Information
- **Address**: Kolej Profesional MARA Indera Mahkota, Jalan IM 9/40, Bandar Indera Mahkota, 25200 Kuantan, Pahang
- **Phone**: 09-573 3333
- **Email**: koperasi@kpmim.edu.my
- **Website**: [Booking System](https://docs.google.com/forms/d/e/1FAIpQLSf8la-t-A2J8l9tWBujXqeYpLZylUQWVxGIjKx7N80jESsrrA/viewform?usp=dialog)

---

*This website serves as the digital gateway for KPMIM Cooperative, demonstrating modern web development practices while serving the educational community with comprehensive service information and booking capabilities.*