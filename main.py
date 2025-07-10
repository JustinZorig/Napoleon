import time 
from active_window import get_active_window_title
from url_extractor import get_url_if_browser
from distraction_checker import checker
from popup import show_popup
from logger import log_event

def main_loop():
    while True:
        window_title = get_active_window_title()
        url = get_url_if_browser(window_title)
        if url and checker(url):
            show_popup(url)
            log_event(url, "Blocked")
        else:
            log_event(window_title, "Allowed")
        time.sleep(1)
    
if __name__ == "__main__":
    main_loop()