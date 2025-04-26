from dotenv import load_dotenv;
import os;
load_dotenv();

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY");
JWT_ACCESS_TOKEN_EXPIRES = os.environ.get("JWT_ACCESS_TOKEN_EXPIRES");
