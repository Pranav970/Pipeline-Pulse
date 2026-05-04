import os
from dotenv import load_dotenv
load_dotenv()

def analyze_log(log_text:str):
    if not os.getenv('OPENAI_API_KEY'):
        return {'root_cause':'Missing API key','fix':'Add OPENAI_API_KEY'}
    return {'root_cause':'Simulated analysis','fix':'Scale cluster or validate schema'}
