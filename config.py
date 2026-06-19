import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = 'harshaimages1759'
    BLOB_CONTAINER = 'images'
    BLOB_STORAGE_KEY = 'b6m9NIlhLzrme6wpAALMgSiS6bJwfNrXKNPQDOMucBMB0rZYmtoxoMC1OiadSc8UrGQSSfOEgQQs+AStRdYBkw=='

    SQL_SERVER = 'harsha1759.database.windows.net'
    SQL_DATABASE = 'cms'
    SQL_USER_NAME = 'cmsadmin'
    SQL_PASSWORD = 'admin@123'

    encoded_password = quote_plus(SQL_PASSWORD)

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{encoded_password}"
        f"@{SQL_SERVER}:1433/{SQL_DATABASE}"
        f"?driver=ODBC+Driver+18+for+SQL+Server"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    CLIENT_SECRET = "CmC8Q~IsISAOe_pH4JzWO5nG-l.VnNtZI0IYEb0f"

    AUTHORITY = "https://login.microsoftonline.com/common"

    CLIENT_ID = "2f799ca9-7588-4fe1-afea-dfe39e38542c"

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"