# It helps keep sensitive information separate from your codebase and allows you to easily switch
# configurations between development, testing, and production environments.
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')
debug_mode = os.getenv('DEBUG')

# Display the values
print(f"Database URL: {database_url}")
print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode}")


# Request modules and use
