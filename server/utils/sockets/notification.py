from datetime import datetime
from tzlocal import get_localzone


def get_greeting():
    """
    Returns a greeting message based on the current local time.
    
    Returns:
        str: A greeting message, either "Good Morning!", "Good Afternoon!", or "Good Evening!"
    """
        
    timezone = get_localzone()
    now = datetime.now(timezone)
    hours = now.hour

    if hours < 12:
        return "Good Morning!"
    elif hours < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"
