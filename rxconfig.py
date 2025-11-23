import os
from dotenv import load_dotenv
import reflex as rx

load_dotenv()

config = rx.Config(
    app_name="spendly",
    db_url=os.getenv('DB_URL'),
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)