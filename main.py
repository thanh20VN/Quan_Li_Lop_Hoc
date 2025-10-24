import data_py
import logic
import getpass
import cli
import flet as ft
import gui

logined = False
id = 0
data_py.load_users(),data_py.UserData


choose = "u"  # Set default to GUI mode

if not data_py.UserData == {}:
    def Login(page: ft.Page):
        page.title = "Đăng nhập"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.width = 400
        page.window.height = 400
        # page.window.full_screen=True
        page.window.resizable = False

        user_field = ft.TextField(label="Tên", width=300, text_align=ft.TextAlign.LEFT)
        pass1 = ft.TextField(label="Mật khẩu", width=300, password=True, text_align=ft.TextAlign.LEFT)
        button = ft.ElevatedButton(text="Đăng nhập", width=100, disabled=True)
        error_text = ft.Text(value="", color="red")
        cli= ft.Checkbox(label="Cửa sổ dòng lệnh", value=False)
        gui= ft.Checkbox(label="Chế độ GUI", value=True)

        def on_login_click(e):
            username = user_field.value 
            password = pass1.value
            t = logic.login.login(username, password)
            if t == "Login successful.":
                global id
                id = data_py.find_user_name(username).get("id")
                page.window.destroy()
            else:
                error_text.value = t
                page.update()

        def check(e): 
            if all([user_field.value, pass1.value]):
                button.disabled = False
            else:
                button.disabled = True
            page.update()

        def on_cli_change(e):
            global choose
            if e.control == cli and cli.value:
                gui.value = False
                choose = "c"
            elif e.control == gui and gui.value:
                cli.value = False
                choose = "u"
            page.update()

        user_field.on_change = check
        pass1.on_change = check
        button.on_click = on_login_click
        cli.on_change = on_cli_change
        gui.on_change = on_cli_change

        page.add(
            ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Text("Vui lòng đăng nhập", size=20),
                            user_field,
                            pass1,
                            button,
                            ft.Row(
                                controls=[
                                    cli,
                                    gui
                                ]
                            ),
                            error_text
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        page.update()
    ft.app(target=Login)
else:
    def Register(page: ft.Page):
        page.title = "Đăng ký"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.width = 400
        page.window.height = 400
        # page.window.full_screen=True
        page.window.resizable = False

        user_field = ft.TextField(label="Tên", width=300, text_align=ft.TextAlign.LEFT)
        pass1 = ft.TextField(label="Mật khẩu", width=300, password=True, text_align=ft.TextAlign.LEFT)
        button = ft.ElevatedButton(text="Đăng Ký", width=100, disabled=True)
        error_text = ft.Text(value="", color="red")
        cli= ft.Checkbox(label="Cửa sổ dòng lệnh", value=False)
        gui= ft.Checkbox(label="Chế độ GUI", value=True)

        def on_login_click(e):
            username = user_field.value 
            password = pass1.value
            t = logic.reg.register(username, password, len(data_py.UserData)+1, "teacher")
            if t == "Tạo tài khoản thành công.":
                global id
                id = len(data_py.UserData)
                page.window.destroy()
            else:
                error_text.value = t
                page.update()

        def check(e): 
            if all([user_field.value, pass1.value]):
                button.disabled = False
            else:
                button.disabled = True
            page.update()

        def on_cli_change(e):
            global choose
            if e.control == cli and cli.value:
                gui.value = False
                choose = "c"
            elif e.control == gui and gui.value:
                cli.value = False
                choose = "u"
            page.update()

        user_field.on_change = check
        pass1.on_change = check
        button.on_click = on_login_click
        cli.on_change = on_cli_change
        gui.on_change = on_cli_change

        page.add(
            ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Text("Vui lòng đăng ký tài khoản \ngiáo viên đầu tiên.", size=20),
                            user_field,
                            pass1,
                            button,
                            ft.Row(
                                controls=[
                                    cli,
                                    gui
                                ]
                            ),
                            error_text
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        page.update()
    ft.app(target=Register)
# id=2
print(choose)
if choose=="c": 
    if data_py.find_user(id).get("role") == "teacher":
        cli.teacher(id)

    elif data_py.find_user(id).get("role") == "class monitor":
        cli.class_monitor(id)

    elif data_py.find_user(id).get("role") == "teamleider":
        cli.teamleider(id)

    elif data_py.find_user(id).get("role") == "student":
        cli.student(id)
if choose=="u":
    if data_py.find_user(id).get("role") == "teacher":
        gui.teacher.__init__(id)

    elif data_py.find_user(id).get("role") == "class monitor":
        gui.class_monitor.__init__(id)

    elif data_py.find_user(id).get("role") == "teamleider":
        gui.teamleider.__init__(id)

    elif data_py.find_user(id).get("role") == "student":
        gui.student.__init__(id)