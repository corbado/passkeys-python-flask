import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    CORBADO_PROJECT_ID = os.environ.get('CORBADO_PROJECT_ID')
    CORBADO_API_SECRET = os.environ.get('CORBADO_API_SECRET')
    CORBADO_FRONTEND_API = os.environ.get('CORBADO_FRONTEND_API')
    CORBADO_BACKEND_API = os.environ.get('CORBADO_BACKEND_API')
    CORBADO_TELEMETRY_DISABLED = os.environ.get('CORBADO_TELEMETRY_DISABLED', "false")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "project.db")}'
    # Add other configuration variables as needed

