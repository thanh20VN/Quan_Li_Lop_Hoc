import flet as ft
import data
import logic
import config


def build_register_view(page: ft.Page):
    user_field = ft.TextField(label="Tên", width=300, text_align=ft.TextAlign.LEFT)
    pass1 = ft.TextField(label="Mật khẩu", width=300, password=True, text_align=ft.TextAlign.LEFT)
    button = ft.ElevatedButton(text="Đăng Ký", width=100, disabled=True)
    login_button = ft.ElevatedButton(text="Đăng nhập", width=100)
    error_text = ft.Text(value="", color="red")

    def on_register_click(e):
        username = user_field.value
        password = pass1.value
        t = logic.reg.register(username, password)
        if t[0] == "Tạo tài khoản thành công.":
            page.user_id = t[1]
            page.go("/teacher")
        else:
            error_text.value = t[0]
            page.update()

    def check(e):
        button.disabled = not (user_field.value and pass1.value)
        page.update()

    user_field.on_change = check
    pass1.on_change = check
    button.on_click = on_register_click
    login_button.on_click = lambda _: page.go("/")

    return ft.View(
        "/register",
        [
            ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Text("Vui lòng đăng ký tài khoản \ndành cho giáo viên.", size=20),
                            user_field,
                            pass1,
                            ft.Row(
                                controls=[button, login_button]
                            ),
                            error_text
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )


def build_login_view(page: ft.Page):
    user_field = ft.TextField(label="Tên", width=300, text_align=ft.TextAlign.LEFT)
    pass1 = ft.TextField(label="Mật khẩu", width=300, password=True, text_align=ft.TextAlign.LEFT)
    button = ft.ElevatedButton(text="Đăng nhập", width=100, disabled=True)
    register_button = ft.ElevatedButton(text="Đăng ký", width=100)
    error_text = ft.Text(value="", color="red")

    def on_login_click(e):
        username = user_field.value
        password = pass1.value
        t = logic.login.login(username, password)
        if t == "Login successful.":
            user_id = data.find_user_name(username).get("id")
            role = data.find_user(user_id).get("role")
            route_map = {
                config.roles[0]: "/teacher",
                config.roles[1]: "/classmonitor",
                config.roles[2]: "/teamleider",
                config.roles[3]: "/student",
            }
            target = route_map.get(role)
            if target:
                page.user_id = user_id
                page.go(target)
            else:
                error_text.value = "Vai trò không hợp lệ"
                page.update()
        else:
            error_text.value = t
            page.update()

    def check(e):
        button.disabled = not (user_field.value and pass1.value)
        page.update()

    user_field.on_change = check
    pass1.on_change = check
    button.on_click = on_login_click
    register_button.on_click = lambda _: page.go("/register")

    return ft.View(
        "/",
        [
            ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Text("Vui lòng đăng nhập", size=20),
                            user_field,
                            pass1,
                            ft.Row(
                                controls=[button, register_button]
                            ),
                            error_text
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )
