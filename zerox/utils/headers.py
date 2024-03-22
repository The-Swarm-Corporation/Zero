import os
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Define API header model
class APIHeaderModel(BaseModel):
    Authorization: str = f"Bearer {os.environ.get('NOTION_API_KEY')}"
    NotionVersion: dict = {"Notion-Version": "2021-05-13"}
    ContentType: str = "application/json"
