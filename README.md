<div align="center">
  <h1><img src="https://img.icons8.com/color/48/000000/rocket.png"/> CKumar Django Project</h1>
  <p><em>A modern Django web application with dashboard and email functionality</em></p>
</div>

<h2><img src="https://img.icons8.com/color/28/000000/star.png"/> Features</h2>

<ul>
  <li>🔐 <strong>User Authentication System</strong></li>
  <li>📊 <strong>Interactive Dashboard</strong></li>
  <li>📧 <strong>Email Integration</strong></li>
  <li>🎨 <strong>Bootstrap Icons Integration</strong></li>
  <li>📱 <strong>Responsive Design</strong></li>
  <li>📑 <strong>Dynamic Content Management</strong></li>
  <li>🔒 <strong>Privacy & Policy Pages</strong></li>
</ul>

<h2><img src="https://img.icons8.com/color/28/000000/maintenance.png"/> Tech Stack</h2>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
</p>

<h2>🚀 Quick Start</h2>

<ol>
  <li><strong>Set up Virtual Environment</strong></li>
</ol>

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

<ol start="2">
  <li><strong>Install Dependencies</strong></li>
</ol>

```bash
pip install django
pip install -r requirements.txt
```

<ol start="3">
  <li><strong>Configure Environment</strong></li>
</ol>

<p>Create <code>.env</code> file in root directory:</p>

```python
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

<h2><img src="https://img.icons8.com/color/28/000000/folder-tree.png"/> Project Structure</h2>

<pre>
ckumar/
├── app/                  # Main application
├── dashboard/            # Dashboard functionality
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   └── ...
├── static/              # Static files
│   ├── css/
│   ├── js/
│   └── icons/
└── ckumar/              # Project settings
    ├── settings.py
    ├── urls.py
    └── wsgi.py
</pre>

<h2>📨 Email Configuration</h2>

<p>The project uses Gmail SMTP. Configure in settings.py:</p>

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

<h2><img src="https://img.icons8.com/color/28/000000/security-checked.png"/> Security Features</h2>

<ul>
  <li>🛡️ CSRF Protection</li>
  <li>🔒 XSS Prevention</li>
  <li>🔑 Secure Password Hashing</li>
  <li>📍 Session Security</li>
</ul>

<h2>📄 Available Pages</h2>

<ul>
    <li>🏠 Home</li>
    <li>💼 Services</li>
    <li>ℹ️ About</li>
    <li>📞 Contact</li>
    <li>🔒 Privacy Policy</li>
    <li>🌍 GDPR</li>
    <li>📜 Terms</li>
    <li>💰 Refund</li>
</ul>

<h2><img src="https://img.icons8.com/color/28/000000/rocket.png"/> Production Deployment</h2>

<ol>
  <li>Set <code>DEBUG=False</code> in settings</li>
  <li>Configure proper <code>ALLOWED_HOSTS</code></li>
  <li>Use secure <code>SECRET_KEY</code></li>
  <li>Set up proper database (PostgreSQL recommended)</li>
  <li>Configure static files serving</li>
  <li>Set up proper email credentials</li>
</ol>

<h2><img src="https://img.icons8.com/color/28/000000/collaboration.png"/> Contributing</h2>

<p>Contributions are welcome! Please feel free to submit a Pull Request.</p>


