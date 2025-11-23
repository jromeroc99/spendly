"""Login state and authentication logic."""

from __future__ import annotations

from typing import Any

import reflex as rx
from sqlmodel import select

from .. import routes
from .local_auth_state import MyLocalAuthState
from ..models.user import LocalUser


class MyLoginState(MyLocalAuthState):
    """Handle login form submission and redirect to proper routes after authentication."""

    error_message: str = ""
    redirect_to: str = ""

    @rx.event
    def on_submit(self, form_data: dict[str, Any]):
        """Handle login form on_submit.

        Args:
            form_data: A dict of form fields and values.
        """
        self.error_message = ""
        username = form_data["username"]
        password = form_data["password"]
        with rx.session() as session:
            user = session.exec(
                select(LocalUser).where(LocalUser.username == username)
            ).one_or_none()
        if user is not None and not user.enabled:
            self.error_message = "Cuenta deshabilitada. Espera a ser confirmado"
            return rx.set_value("password", "")
        if (
            user is not None
            and user.id is not None
            and user.enabled
            and password
            and user.verify(password)
        ):
            # mark the user as logged in
            self._login(user.id)
        else:
            self.error_message = "Fallo al iniciar sesión, intentalo de nuevo"
            return rx.set_value("password", "")
        self.error_message = ""
        return MyLoginState.redir()  # type: ignore

    @rx.event
    def redir(self):
        """Redirect to the redirect_to route if logged in, or to the login page if not."""
        if not self.is_hydrated:
            # wait until after hydration to ensure auth_token is known
            return MyLoginState.redir()  # type: ignore
        page = self.router.url.path
        if not self.is_authenticated and page != routes.LOGIN_ROUTE:
            self.redirect_to = self.router.url.path
            return rx.redirect(routes.LOGIN_ROUTE)
        elif self.is_authenticated and page == routes.LOGIN_ROUTE:
            return rx.redirect(self.redirect_to or "/")


def my_require_login(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:
    """Decorator to require authentication before rendering a page.

    If the user is not authenticated, then redirect to the login page.

    Args:
        page: The page to wrap.

    Returns:
        The wrapped page component.
    """

    def protected_page():
        return rx.fragment(
            rx.cond(
                MyLoginState.is_hydrated & MyLoginState.is_authenticated,  # type: ignore
                page(),
                rx.center(
                    # When this text mounts, it will redirect to the login page
                    rx.text("Cargando...", on_mount=MyLoginState.redir),
                ),
            )
        )

    protected_page.__name__ = page.__name__
    return protected_page
