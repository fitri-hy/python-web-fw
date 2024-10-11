# Py-Framework

Py-Framework is a simple web framework using the Python language to make it easier for users to build websites

```
my_mvc_framework/
│
├── app/
│   ├── controllers/
│   │   ├── home_controller.py
│   │   └── about_controller.py
│   ├── public/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   ├── layout.html
│   │   ├── about.html
│   │   └── home.html
│   ├── components/
│   │   ├── navbar.py
│   │   └── footer.py
│   ├── routes.py
│   └── app.py
├── requirements.txt
└── run.py
```

## Install
```
python -m venv venv
source venv/bin/activate  # for macOS/Linux
venv\Scripts\activate  # for Windows
pip install -r requirements.txt
python run.py
```