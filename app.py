import time
from datetime import datetime
import win32gui
import win32process
import psutil
import matplotlib.pyplot as plt
import re


def get_active_window_title():
    """Get the active window's process name and title."""
    window = win32gui.GetForegroundWindow()
    tid, pid = win32process.GetWindowThreadProcessId(window)
    process = psutil.Process(pid)
    name = process.name()
    window_title = win32gui.GetWindowText(window)
    return name, sanitize_title(window_title)


def sanitize_title(title: str) -> str:
    """Remove invisible characters like zero-width spaces from titles."""
    return re.sub(r"[\u200b-\u200f\u202a-\u202e]", "", title).strip()


def is_ignorable_window(app_name, title):
    """Ignore system/browser blank windows like new tabs or settings pages."""
    title_lower = title.strip().lower()
    app_name_lower = app_name.lower()
    return (
        app_name_lower in ["chrome.exe", "msedge.exe"]
        and (
            title_lower == ""
            or "new tab" in title_lower
            or title_lower.startswith("chrome://")
            or title_lower.startswith("edge://")
        )
    )


def plot_pie_chart(data_dict):
    """Generate a pie chart of time spent per window."""
    labels = list(data_dict.keys())
    durations = list(data_dict.values())

    # Filter out very short durations (optional)
    labels, durations = zip(*[
        (label, duration) for label, duration in zip(labels, durations)
        if duration > 2
    ]) if durations else ([], [])

    plt.figure(figsize=(7, 7))
    plt.pie(durations, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Time Spent Per Window")
    plt.axis('equal')
    plt.show()


def main():
    # Clear log file at start
    with open("time_log.txt", "w", encoding="utf-8") as f:
        f.write("")

    last_title = None
    start_time = time.time()
    window_time_data = {}

    while True:
        try:
            app_name, title = get_active_window_title()

            if is_ignorable_window(app_name, title):
                time.sleep(1)
                continue

            if title != last_title and title.strip():
                end_time = time.time()
                if last_title is not None:
                    duration = int(end_time - start_time)
                    log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {last_title} | {duration} seconds\n"
                    with open("time_log.txt", "a", encoding="utf-8") as f:
                        f.write(log)
                    print(log.strip())

                    # Add duration to dictionary
                    window_time_data[last_title] = window_time_data.get(last_title, 0) + duration

                last_title = title
                start_time = time.time()

            time.sleep(1)

        except KeyboardInterrupt:
            print("\nTracking stopped by user.")
            # Log the current window before exiting
            if last_title is not None:
                duration = int(time.time() - start_time)
                window_time_data[last_title] = window_time_data.get(last_title, 0) + duration
                log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {last_title} | {duration} seconds\n"
                with open("time_log.txt", "a", encoding="utf-8") as f:
                    f.write(log)
                print(log.strip())

            # Show pie chart
            print("\nGenerating pie chart...")
            plot_pie_chart(window_time_data)
            break


if __name__ == "__main__":
    main()

