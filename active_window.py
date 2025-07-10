import pygetwindow as gw

def get_active_window_title():
    try:
        window = gw.getActiveWindow()
        return window.title if window else None
    except Exception as e:
        print("Error getting active window:", e)
        return None