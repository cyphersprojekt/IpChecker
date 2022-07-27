# IpChecker

### Depends on:
    * wget (pip install wget)
    * dotenv (pip install python-dotenv)
    
### Setup:
    * Load the .env values as plain text. No single or double quotes required
    
### Usage:
* The first time you run it, the script will create a permanent file called 'old_ip' with your current public IP address. After that, and every time you run it, it will create a new, temporary file, called 'current_ip'. If 'old_ip' and 'current_ip' are the same, it will do nothing. But if they're not the same, it will notify you via email with the values you set up in the .env file, and update old_ip.
