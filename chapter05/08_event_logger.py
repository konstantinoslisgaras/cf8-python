from datetime import datetime

def log_event(event_type: str, **kwargs: dict) -> None:
    """
    Logs and event with a specified type and additional keyword arguments.

    Params:
        event_type (str): The type of event that is logged.
        kwargs (dict): Additional information about the event.
    """
    timestamp = datetime.now().isoformat()
    print(f"Event type: {event_type}")
    print(f"Timestamp: {timestamp}")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print("="*50)

def main():
    log_event("UserLogin", user="KappaLambda", status="Success", ip="192.168.1.1")
    log_event("FileUpload", user="AlphaAlpha", status="Failure", filename="report.xlsx", ip="192.168.1.1")

if __name__ == "__main__":
    main()