"""New user registration validation and database logic."""

from __future__ import annotations

import asyncio
from typing import Any

import reflex as rx
from reflex.event import EventSpec

from sqlmodel import select

from .. import routes
from .local_auth_state import MyLocalAuthState
from ..models.user import LocalUser
from ..models.user_info import UserInfo

POST_REGISTRATION_DELAY = 0.5

class MyRegistrationState(MyLocalAuthState):
    """Handle registration form submission and redirect to login page after registration."""

    success: bool = False
    error_message: str = ""
    new_user_id: int = -1

    def _validate_fields(
        self, username, email, password, confirm_password
    ) -> EventSpec | list[EventSpec] | None:
        if not email:
            self.error_message = "Correo electrónico no valido"
            return rx.set_focus("email")
        if not username:
            self.error_message = "Nombre de usuario no puede estar vacio"
            return rx.set_focus("username")
        with rx.session() as session:
            existing_user = session.exec(
                select(LocalUser).where(LocalUser.username == username)
            ).one_or_none()
        if existing_user is not None:
            self.error_message = (
                f"Usuario {username} ya existe. Prueba otro"
            )
            return [rx.set_value("username", ""), rx.set_focus("username")]
        if not password:
            self.error_message = "Contraseña no puede estar vacía"
            return rx.set_focus("password")
        if password != confirm_password:
            self.error_message = "Contraseñas no coinciden"
            return [
                rx.set_value("confirm_password", ""),
                rx.set_focus("confirm_password"),
            ]

    def _register_user(self, username, password) -> None:
        with rx.session() as session:
            # Create the new user and add it to the database.
            new_user = LocalUser()  # type: ignore
            new_user.username = username
            new_user.password_hash = LocalUser.hash_password(password)
            new_user.enabled = False
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            if new_user.id is not None:
                self.new_user_id = new_user.id

    @rx.event
    def handle_registration(
        self,
        form_data: dict[str, Any],
    ):
        """Handle registration form on_submit.

        Set error_message appropriately based on validation results.

        Args:
            form_data: A dict of form fields and values.
        """
        username = form_data["username"]
        password = form_data["password"]
        email = form_data["email"]
        validation_errors = self._validate_fields(
            username, email, password, form_data["confirm_password"]
        )
        if validation_errors:
            self.new_user_id = -1
            return validation_errors
        self._register_user(username, password)
        return type(self).successful_registration
    # This event handler must be named something besides `handle_registration`!!!
    @rx.event
    def handle_registration_email(self, form_data):
        registration_result = self.handle_registration(form_data)
        if self.new_user_id >= 0:
            with rx.session() as session:
                session.add(
                    UserInfo(
                        email=form_data["email"],
                        created_from_ip=self.router.session.client_ip,
                        user_id=self.new_user_id,
                    )
                )
                session.commit()
        return registration_result
    

    @rx.event
    def set_success(self, success: bool):
        """Set the success flag.

        Args:
            success: Whether the registration was successful.
        """
        self.success = success

    @rx.event
    async def successful_registration(
        self,
    ):
        # Set success and redirect to login page after a brief delay.
        self.error_message = ""
        self.new_user_id = -1
        self.success = True
        yield
        await asyncio.sleep(POST_REGISTRATION_DELAY)
        yield [rx.redirect(routes.LOGIN_ROUTE), type(self).set_success(False)]

    @rx.event
    def redir(self):
        """Redirect to the registration form."""
        return rx.redirect(routes.REGISTER_ROUTE)
