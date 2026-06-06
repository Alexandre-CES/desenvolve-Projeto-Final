from fastapi import FastAPI
from dotenv import load_dotenv

'''
  #?Using dotenv: 
    import os
    os.getenv("VARIABLE")
'''
load_dotenv()

app = FastAPI()

@app.get('/')
async def home():
  return {
    'message': 'Hello World!'
  }
