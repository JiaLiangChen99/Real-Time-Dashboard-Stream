import reflex as rx


class AuthState(rx.State):
    users: dict[str, str] = {"admin": "admin123"}
    in_session: bool = False
    error_message: str = ""

    @rx.event
    def sign_in(self, form_data: dict):
        username = form_data.get("username", "")
        password = form_data.get("password", "")
        if self.users.get(username) == password:
            self.in_session = True
            self.error_message = ""
            return rx.redirect("/admin/dashboard")
        else:
            self.in_session = False
            self.error_message = (
                "Invalid username or password"
            )
            yield

    @rx.event
    def sign_out(self):
        self.in_session = False
        return rx.redirect("/admin/login")

    @rx.event
    def check_session(self):
        if not self.in_session:
            return rx.redirect("/admin/login")