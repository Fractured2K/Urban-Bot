import os

if not os.getenv('PRODUCTION'):
    from dotenv import load_dotenv
    load_dotenv()
