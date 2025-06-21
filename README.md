# MBX-RE 🚗

MBX-RE is a modern web-based vehicle marketplace platform built with Django, allowing users to easily and efficiently post vehicle listings for buying and selling.

## 🌟 Key Features

- **Vehicle Listings**: Users can post listings with images, detailed descriptions, and pricing
- **Real-time Chat System**: Integrated chat functionality between buyers and sellers
- **Account Management**: Registration, login, password recovery, and password change
- **Post Management**: Users can edit and delete their own listings
- **Responsive Design**: Beautiful, user-friendly interface
- **Location-based Search**: Filter listings by province/city, district, and ward

## 🏗️ System Architecture

```
MBX-RE/
├── MBX/                    # Main Django configuration
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
├── home/                   # Home page application
│   ├── views.py           # Home page logic
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JS, Images
├── account/               # Account management
│   ├── views.py           # Registration and login logic
│   ├── forms.py           # Form validation
│   └── templates/         # Login/registration templates
├── post/                  # Post management
│   ├── models.py          # Post model
│   ├── views.py           # CRUD operations
│   ├── forms.py           # Create/edit post forms
│   └── templates/         # Post templates
├── chat/                  # Chat system
│   ├── models.py          # Message model
│   ├── views.py           # Chat API
│   └── context_processors.py
├── media/                 # File upload storage
├── templates/             # Common templates
└── manage.py             # Django management
```

## 🛠️ Technologies Used

### Backend
- **Django 5.1.4**: Main web framework
- **SQLite**: Database (can be migrated to PostgreSQL/MySQL)
- **Django ORM**: Database management

### Frontend
- **HTML5/CSS3**: User interface
- **JavaScript**: Client-side interactions
- **Bootstrap**: CSS framework (if applicable)

### Authentication & Security
- **Django Authentication**: Authentication system
- **CSRF Protection**: Form security
- **Email Integration**: Password reset email functionality

### File Handling
- **Pillow**: Image processing
- **Django Media**: File upload management

## 🚀 Installation and Setup

### System Requirements
- Python 3.8+
- pip
- Git

### Step 1: Clone repository
```bash
git clone <repository-url>
cd MBX-RE
```

### Step 2: Create virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create superuser (optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run server
```bash
python manage.py runserver
```

Access the application at: `http://localhost:8000`

## 📱 Usage Guide

### 1. Register Account
- Visit `/account/register/`
- Fill in personal information
- Confirm email (if applicable)

### 2. Post Vehicle Listing
- Login to the system
- Navigate to "Create Post" or `/post/create/`
- Upload vehicle images
- Fill in information: title, price, description, address
- Publish listing

### 3. Chat with Buyers/Sellers
- View listings on homepage
- Click on listing to see details
- Use chat feature to contact

### 4. Manage Listings
- Access profile to view your listings
- Edit or delete listings

## 🔧 Configuration

### Email Setup (Gmail)
In `MBX/settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### Database Setup
Default uses SQLite. To switch to PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mbx_db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 Models

### Post Model
```python
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    product = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    province = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    ward = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### Message Model
```python
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
```

## 🔌 API Endpoints

### Authentication
- `GET /account/register/`: Registration page
- `POST /account/register/`: Process registration
- `GET /account/login/`: Login page
- `POST /account/login/`: Process login
- `GET /account/forgot-password/`: Password recovery

### Posts
- `GET /`: Homepage displaying listings
- `GET /post/create/`: Create new listing
- `POST /post/create/`: Save listing
- `GET /post/<id>/`: View listing details
- `GET /post/<id>/edit/`: Edit listing
- `POST /post/<id>/delete/`: Delete listing

### Chat
- `GET /chat/messages/<username>/`: Get messages
- `POST /chat/send/`: Send message

## 🎨 User Interface

### UI/UX Features
- **Responsive Design**: Mobile and desktop compatible
- **Modern UI**: Clean, modern interface
- **Image Gallery**: Beautiful vehicle image display
- **Search & Filter**: Search and filter listings
- **Real-time Chat**: Live chat functionality

### Components
- Navigation bar with main menu
- Advertisement banners
- Product display grid
- Post creation form with validation
- Chat interface
- User profile management

## 🔒 Security

- **CSRF Protection**: Protection against Cross-Site Request Forgery
- **Authentication Required**: Login required for important features
- **File Upload Security**: File upload validation and checking
- **SQL Injection Protection**: Using Django ORM
- **XSS Protection**: Django template escaping

## 🚀 Deployment

### Production Settings
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
STATIC_ROOT = '/path/to/static/files/'
```

### Environment Variables
```bash
export SECRET_KEY='your-secret-key'
export DEBUG=False
export DATABASE_URL='postgresql://user:pass@localhost/db'
```

### Web Server
- **Gunicorn**: WSGI server
- **Nginx**: Reverse proxy
- **PostgreSQL**: Production database

## 🤝 Contributing

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## 📞 Contact

- **Email**: vodailuong2510@gmail.com
- **Project Link**: [https://github.com/your-username/MBX-RE](https://github.com/your-username/MBX-RE)

## 🙏 Acknowledgments

- Django team for the excellent framework
- Open source community
- All contributors to the project

---

**MBX-RE** - Modern and reliable vehicle marketplace platform! 🚗✨
