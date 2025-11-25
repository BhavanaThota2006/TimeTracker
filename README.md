**<h2>Automatic Time Tracker</h2>**<br>
**<h3>Track how much time you spend on each window or application — automatically.</h3>**<br>
This Python-based Automatic Time Tracker monitors the currently active window on a Windows system and logs how long each window remains focused. It helps you analyze your productivity patterns by generating a pie chart summary of time spent per window.
<br><br>

**<h2>Features</h2>**<br>
Real-time active window tracking<br>
Cleans window titles by removing hidden Unicode characters<br>
Ignores empty or system/tab pages (e.g., Chrome/Edge new tabs, settings pages)<br>
Logs usage with timestamps in time_log.txt<br>
Automatically generates a pie chart showing window-wise time distribution<br>
Built specifically for Windows OS (uses win32gui, win32process)<br><br>

**<h2>Requirements</h2>**<br>
Install all dependencies:<br>
pip install psutil pywin32 matplotlib<br>
You must also have scipy and pywin32 properly installed.<br><br>

**<h2>Project Structure</h2>**<br>
time-tracker/<br>
│── time_tracker.py<br>
│── time_log.txt<br>
│── requirements.md<br>

**<h2>How to Run</h2>**<br>
Clone the repository or download the script<br>
Install dependencies<br>
Run:python time_tracker.py<br>
The script will immediately start tracking:<br>
Logs appear in the console<br>
A detailed log is written to time_log.txt<br>
Press Ctrl + C anytime to stop tracking<br>
A pie chart is generated automatically on exit<br><br>

**<h2>Sample Output (Log Format)</h2>**<br>
2025-11-25 18:23:10 | Visual Studio Code — index.js | 65 seconds<br>
2025-11-25 18:24:15 | Chrome — YouTube | 32 seconds<br>
2025-11-25 18:25:20 | WhatsApp | 14 seconds<br><br>

**<h2>Visual Summary</h2>**<br>
When you stop the script, you get a pie chart:<br>
Each slice = a window title<br>
Displays total time spent in percentage<br>
Windows with less than 3 seconds are filtered out<br><br>

 **<h2>How It Works</h2>**<br>
The script:<br>
Detects the foreground window using win32gui.<br>
Extracts the process name using win32process and psutil.<br>
Tracks how long each window stays active.<br>
Logs data to a file.<br>
Generates a pie chart using matplotlib.<br><br>

**<h2>Ignored Windows</h2>**<br>
Certain windows are intentionally ignored to reduce noise:<br>
Chrome or Edge new tabs<br>
Chrome/Edge internal pages (chrome://, edge://)<br>
Empty titles<br><br>

**<h2>Use Cases</h2>**<br>
Productivity monitoring<br>
Work-from-home reporting<br>
Application usage analytics<br>
Screen time insights<br>
Developer activity tracking<br><br>


**<h2>License</h2>**<br>
This project is open-source and free to use under the MIT License.<br>
