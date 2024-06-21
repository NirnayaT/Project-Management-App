from dotenv import load_dotenv
import os

load_dotenv()  # This line brings all environment variables from .env into os.environ
print(os.environ['SECRET_KEY'])