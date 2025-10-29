import data_py
import logic
import getpass
import cli
import flet as ft
import gui
import subprocess
import sys

logined = False
id = 0
data_py.load_users()


choose = "c"  # Set default to GUI mode

import config

def h():
    if choose == "c":
        # CLI mode thì gọi trực tiếp
        role = data_py.find_user(id).get("role")
        if role == config.roles[0]:
            cli.teacher(id)
        elif role == config.roles[1]:
            cli.class_monitor(id)
        elif role == config.roles[2]:
            cli.teamleider(id)
        elif role = config.roles[3]:
            cli.student(id)

#     elif choose == "u":
#         # GUI mode thì mở app mới (để Flet chạy trong main thread riêng)
#         role = data_py.find_user(id).get("role")
#         if role == config.roles[0]:
#             subprocess.Popen([sys.executable, "-m", "gui.teacher", str(id)])
#         elif role == config.roles[1]:
#             subprocess.Popen([sys.executable, "-m", "gui.class_monitor", str(id)])
#         elif role == config.roles[2]:
#             subprocess.Popen([sys.executable, "-m", "gui.teamleider", str(id)])
#         elif role == config.roles[3]:
#             subprocess.Popen([sys.executable, "-m", "gui.student", str(id)])

#if not data_py.UserData == {} and logined == False:
#    def Login(page: ft.Page):
#        page.title = "Đăng nhập"
#        page.vertical_alignment = ft.MainAxisAlignment.CENTER
#        page.theme_mode = ft.ThemeMode.LIGHT
#        page.window.width = 400
#         page.window.height = 400
#         # page.window.full_screen=True
#         page.window.resizable = False
#         page.window.maximizable=False
#         page.window.center()

#         user_field = ft.TextField(label="Tên", width=300, text_align=ft.TextAlign.LEFT)
#         pass1 = ft.TextField(label="Mật khẩu", width=300, password=True, text_align=ft.TextAlign.LEFT)
#         button = ft.ElevatedButton(text="Đăng nhập", width=100, disabled=True)
#         error_text = ft.Text(value="", color="red")
#         # cli= ft.Checkbox(label="Cửa sổ dòng lệnh", value=False)
#         # gui= ft.Checkbox(label="Chế độ GUI", value=True)

#         def on_login_click(e):
#             username = user_field.value 
#             password = pass1.value
#             t = logic.login.login(username, password)
#             if t == "Login successful.":
#                 global id
#                 id = data_py.find_user_name(username).get("id")
#                 page.clean()  # xoá toàn bộ control cũ
#                 role = data_py.find_user(id).get("role")

#                 if role == config.roles[0]:
#                     import gui.teacher as teacher
#                     teacher.__init__(page,id)
#                 elif role == config.roles[1]:
#                     import gui.class_monitor as cm
#                     cm.__init__(page,id)
#                 elif role == config.roles[2]:
#                     import gui.teamleider as tl
#                     tl.__init__(page,id)
#                 elif role == config.roles[3]:
#                     import gui.student as st
#                     st.__init__(page,id)
#             else:
#                 error_text.value = t
#                 page.update()

#         def check(e): 
#             if all([user_field.value, pass1.value]):
#                 button.disabled = False
#             else:
#                 button.disabled = True
#             page.update()

#         # def on_cli_change(e):
#         #     global choose
#         #     if e.control == cli and cli.value:
#         #         gui.value = False
#         #         choose = "c"
#         #     elif e.control == gui and gui.value:
#         #         cli.value = False
#         #         choose = "u"
#         #     page.update()

#         user_field.on_change = check
#         pass1.on_change = check
#         button.on_click = on_login_click
#         # cli.on_change = on_cli_change
#         # gui.on_change = on_cli_change

#         page.add(
#             ft.Row(
#                 controls=[
#                     ft.Column(
#                         [
#                             ft.Text("Vui lòng đăng nhập", size=20),
#                             user_field,
#                             pass1,
#                             button,
#                             # ft.Row(
#                             #     controls=[
#                             #         cli,
#                             #         gui
#                             #     ]
#                             # ),
#                             error_text
#                         ]
#                     )
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#             )
#         )
#         page.update()
#     ft.app(target=Login)
# elif logined == False:
#     def Register(page: ft.Page):
#         page.title = "Đăng ký"
#         page.vertical_alignment = ft.MainAxisAlignment.CENTER
#         page.theme_mode = ft.ThemeMode.LIGHT
#         page.window.width = 400
#         page.window.height = 400
#         # page.window.full_screen=True
#         page.window.resizable = False
#         page.window.maximizable=False
#         page.window.center()

#         user_field = ft.TextField(label="Tên", width=300, text_align=ft.TextAlign.LEFT)
#         pass1 = ft.TextField(label="Mật khẩu", width=300, password=True, text_align=ft.TextAlign.LEFT)
#         button = ft.ElevatedButton(text="Đăng Ký", width=100, disabled=True)
#         error_text = ft.Text(value="", color="red")
#         # cli= ft.Checkbox(label="Cửa sổ dòng lệnh", value=False)
#         # gui= ft.Checkbox(label="Chế độ GUI", value=True)

#         def on_login_click(e):
#             username = user_field.value 
#             password = pass1.value
#             t = logic.reg.register(username, password, len(data_py.UserData)+1, config.roles[0])
#             if t == "Tạo tài khoản thành công.":
#                 global id
#                 id = data_py.find_user_name(username).get("id")
#                 page.clean()  # xoá toàn bộ control cũ
#                 role = data_py.find_user(id).get("role")

#                 if role == config.roles[0]:
#                     import gui.teacher as teacher
#                     teacher.__init__(page,id)
#                 elif role == config.roles[1]:
#                     import gui.class_monitor as cm
#                     cm.__init__(page,id)
#                 elif role == config.roles[2]:
#                     import gui.teamleider as tl
#                     tl.__init__(page,id)
#                 elif role == config.roles[3]:
#                     import gui.student as st
#                     st.__init__(page,id)
#             else:
#                 error_text.value = t
#                 page.update()

#         def check(e): 
#             if all([user_field.value, pass1.value]):
#                 button.disabled = False
#             else:
#                 button.disabled = True
#             page.update()

#         # def on_cli_change(e):
#         #     global choose
#         #     if e.control == cli and cli.value:
#         #         gui.value = False
#         #         choose = "c"
#         #     elif e.control == gui and gui.value:
#         #         cli.value = False
#         #         choose = "u"
#             # page.update()

#         user_field.on_change = check
#         pass1.on_change = check
#         button.on_click = on_login_click
#         # cli.on_change = on_cli_change
#         # gui.on_change = on_cli_change

#         page.add(
#             ft.Row(
#                 controls=[
#                     ft.Column(
#                         [
#                             ft.Text("Vui lòng đăng ký tài khoản \ngiáo viên đầu tiên.", size=20),
#                             user_field,
#                             pass1,
#                             button,
#                             # ft.Row(
#                             #     controls=[
#                             #         cli,
#                             #         gui
#                             #     ]
#                             # ),
#                             error_text
#                         ]
#                     )
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#             )
#         )
#         page.update()
#     ft.app(target=Register)
# # id=2
# # print(choose)


h()