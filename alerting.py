import smtplib
import json

class Alerting:
    def __init__(self):
        # Load alert settings from config.json
        with open("config.json", "r") as config_file:
            self.config = json.load(config_file)

    def send_alert(self, message):
        # Implement alerting methods (e.g., email, SMS, Slack) based on your requirements
        if self.config.get("email_alert"):
            self.send_email_alert(message)
        
        if self.config.get("console_alert"):
            print(message)

    def send_email_alert(self, message):
        email_settings = self.config.get("email_settings")
        # Implement email alerting using SMTP

    # Implement other alerting methods as needed
