import reflex as rx
import sqlmodel

class UserInfo(rx.Model, table=True):
    email: str
    is_admin: bool = False
    created_from_ip: str
    user_id: int = sqlmodel.Field(foreign_key="localuser.id")
