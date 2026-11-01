# 🖥️ Linux System Dashboard

A simple web-based system monitoring dashboard built with Python Flask. Shows real-time CPU, RAM, and disk usage with color-coded progress bars.

![Dashboard Preview](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1+-green.svg)

---

## Features

- 📊 **Real-time system stats** — CPU, RAM, and disk usage
- 🎨 **Color-coded bars** — Green (healthy), Yellow (warning), Red (critical)
- 🌙 **Dark theme** — Easy on the eyes
- ⚡ **Lightweight** — Only 2 dependencies (Flask + psutil)

---

## Screenshots

The dashboard displays three main metrics:
- **CPU Usage** — Processor load percentage
- **RAM Usage** — Memory used vs total
- **Disk Usage** — Storage used vs total (root partition)

---

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/linux-system-dashboard.git
   cd linux-system-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python app.py
   ```

4. **Open in browser**
   
   Go to: http://127.0.0.1:5000

---

## Usage

- The dashboard shows current system stats when you load the page
- **Refresh the page** to update the stats
- Press **Ctrl + C** in the terminal to stop the server

---

## Project Structure

```
linux-system-dashboard/
├── app.py                 # Flask server + system stats logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── dashboard.html     # HTML template
└── static/
    └── style.css          # Stylesheet
```

---

## Technologies Used

- **Python 3** — Programming language
- **Flask** — Web framework
- **psutil** — System monitoring library
- **HTML/CSS** — Frontend

---

## Color Coding

The progress bars change color based on usage:

| Usage Level | Color | Meaning |
|------------|-------|---------|
| 0–59% | 🟢 Green | Healthy |
| 60–84% | 🟡 Yellow | Watch it |
| 85–100% | 🔴 Red | Critical |

---

## License

This project is open source and available under the MIT License.

---

## Author

Built as a beginner-friendly Python Flask project.

---

## Contributing

Feel free to fork this project and submit pull requests for improvements!
