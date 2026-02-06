# 🤖 Lazy Living: Workflow Automation Suite
### Desktop & Web Automation Pythonic Scripts*

![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/selenium-%2343B02A.svg?style=for-the-badge&logo=selenium&logoColor=white)
![Automation](https://img.shields.io/badge/Focus-Efficiency-red?style=for-the-badge)

## 🚀 Overview
**Lazy Living** is a collection of high-impact Python scripts designed to automate repetitive, high-volume tasks in both business and personal environments. 

The project focuses on two primary automation domains:
1.  **Desktop Automation:** Using `PyAutoGUI` to handle complex multi-merge data tasks within legacy ERP systems.
2.  **Web Intelligence:** Using `Selenium` for automated market research and competitor price monitoring.



## 📈 Proven Impact
These scripts were developed to solve specific bottleneck issues, resulting in measurable time savings:
* **ERP Data Merging:** Reduced average per-task session time from **3 minutes to 48 seconds**.
* **Market Monitoring:** Saved **2+ hours per week** by automating competitor site snapshots and data gathering.

## 🛠️ Key Technical Features
* **GUI Wrapper:** Implemented a `Tkinter` interface to allow non-technical users to trigger complex automation sequences with a single click.
* **Intelligent Web Scraping:** Developed Selenium scripts with custom wait conditions and headless execution modes for efficient data collection.
* **Robust Error Handling:** Integrated fail-safe mechanisms to ensure desktop automation terminates safely if unexpected system pop-ups occur.
* **Binary Distribution:** Scripts are packaged as standalone `.exe` files using **PyInstaller**, removing the need for end-users to have a Python environment installed.

## 🏗️ Technical Stack
* **Language:** Python 3.x
* **Web Drivers:** Selenium (Chrome/Edge)
* **GUI & Control:** PyAutoGUI, Tkinter
* **Distribution:** PyInstaller

---

## 🔧 Getting Started

### Prerequisites
* Python 3.10+
* Chrome or Edge WebDriver (for Selenium scripts)

### Installation
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/Jaycuppp/Lazy_Living.git](https://github.com/Jaycuppp/Lazy_Living.git)
   cd Lazy_Living
Install Dependencies:

Bash
pip install selenium pyautogui
Running the Suite
To launch the automation dashboard:

Bash
python main_gui.py
🧬 Engineering Challenges
Coordinate Calibration: Desktop automation varies by screen resolution. I implemented relative coordinate logic to ensure PyAutoGUI clicks remained accurate across different monitor setups.

Rate Limiting: To avoid being flagged during web monitoring, I implemented randomized sleep intervals and user-agent rotation within the Selenium scripts.

👤 Author
Hakob Keshishyan

GitHub: @Jaycuppp

LinkedIn: [Your LinkedIn Link]

[!WARNING] Safety Note: Desktop automation scripts take control of your mouse and keyboard. Always ensure the "Fail-Safe" (moving the mouse to a corner) is enabled before running.
