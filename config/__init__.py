import os
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

RETRY_CONFIG = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

GEMINI_MODEL = "gemini-2.5-flash-lite"

# Get API key from environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("⚠️  WARNING: GOOGLE_API_KEY not found in .env file")
    print("   Get free API key from: https://aistudio.google.com/")