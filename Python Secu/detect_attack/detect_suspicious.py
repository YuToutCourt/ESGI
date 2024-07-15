import time
import re
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rich.console import Console
from rich.text import Text

console = Console()

class LogFileHandler(FileSystemEventHandler):
    """
    A handler class that monitors a specified log file for suspicious activity.

    Attributes:
        log_file_path (str): The path to the log file to be monitored.
        suspicious_patterns (list): A list of regex patterns to detect suspicious activity.
    """
    def __init__(self, log_file_path, suspicious_patterns):
        self.log_file_path = log_file_path
        self.suspicious_patterns = suspicious_patterns

    def on_modified(self, event):
        """
        Called when the monitored log file is modified.
        
        Args:
            event (FileSystemEvent): The event representing the file modification.
        """
        if event.src_path == self.log_file_path:
            self.check_log_for_suspicious_activity()    

    def check_log_for_suspicious_activity(self):
        """
        Checks the log file for suspicious activity based on predefined patterns.
        """
        with open(self.log_file_path, 'r') as log_file:
            lines = log_file.readlines()
            for line in lines[-10:]:  # Check the last 10 lines
                if any(re.search(pattern, line) for pattern in self.suspicious_patterns):
                    self.print_suspicious_activity(line)

    def print_suspicious_activity(self, line):
        """
        Prints a message indicating that suspicious activity has been detected.
        
        Args:
            line (str): The line from the log file that contains suspicious activity.
        """
        text = Text(f"Suspicious activity detected in {self.log_file_path}: {line.strip()}")
        text.stylize("bold red")
        console.print(text)

def main(log_files, rules):
    """
    Monitors specified log files for suspicious activity.

    Args:
        log_files (list): List of paths to the log files to be monitored.
        rules (str): Path to the file containing rules for suspicious activity detection.
    """

    with open(rules, 'r') as file:
        rules = file.read().split("\n")
        suspicious_patterns = [re.compile(rule) for rule in rules]

    observers = []
    for log_file in log_files:
        event_handler = LogFileHandler(log_file, suspicious_patterns)
        observer = Observer()
        observer.schedule(event_handler, path=log_file, recursive=False)
        observers.append(observer)
        console.print(f"Started monitoring {log_file} for suspicious activity...", style="bold green")

    for observer in observers:
        observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for observer in observers:
            observer.stop()
        for observer in observers:
            observer.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor log files for suspicious activity.")
    parser.add_argument("-l", '--log_files', type=str, nargs='+', help='Paths to the log files to be monitored\nExemple: python3 detect_suspicious.py /var/log/auth.log /path/to/other/logfile.log')     
    parser.add_argument("-r", '--rules', type=str, help='Rule file to be used for monitoring\nExemple: python3 detect_suspicious.py /var/log/auth.log /path/to/other/logfile.log -r rules.txt')
    args = parser.parse_args()
    main(args.log_files, args.rules)
