import flet as ft
import data_py
import config


def main(page: ft.Page):
    page.title = "Quản lý lớp học"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1100
    page.window.height = 770
    page.window.resizable = True
    page.window.maximizable = True
    page.window.center()
    page.user_id = None

    def route_change(e):
        page.views.clear()
        target = e.route if hasattr(e, 'route') else str(e)

        if target == "/" or target == "":
            page.user_id = None
            from gui.auth import build_login_view
            page.views.append(build_login_view(page))

        elif target == "/register":
            from gui.auth import build_register_view
            page.views.append(build_register_view(page))

        elif target == "/logout":
            page.user_id = None
            from gui.auth import build_login_view
            page.views.append(build_login_view(page))

        elif target == "/teacher":
            import gui.teacher as teacher_module
            teacher_module.set_user(page.user_id)
            page.views.append(teacher_module.build_home(page))

        elif target.startswith("/teacher/"):
            import gui.teacher as teacher_module
            teacher_module.set_user(page.user_id)
            sub = target[len("/teacher/"):]
            page.views.append(teacher_module.build_home(page))
            sub_view = teacher_module.build_subroute(page, sub)
            if sub_view:
                page.views.append(sub_view)

        elif target == "/classmonitor":
            import gui.class_monitor as cm_module
            cm_module.set_user(page.user_id)
            page.views.append(cm_module.build_home(page))

        elif target.startswith("/classmonitor/"):
            import gui.class_monitor as cm_module
            cm_module.set_user(page.user_id)
            sub = target[len("/classmonitor/"):]
            page.views.append(cm_module.build_home(page))
            sub_view = cm_module.build_subroute(page, sub)
            if sub_view:
                page.views.append(sub_view)

        elif target == "/teamleider":
            import gui.teamleider as tl_module
            tl_module.set_user(page.user_id)
            page.views.append(tl_module.build_home(page))

        elif target.startswith("/teamleider/"):
            import gui.teamleider as tl_module
            tl_module.set_user(page.user_id)
            sub = target[len("/teamleider/"):]
            page.views.append(tl_module.build_home(page))
            sub_view = tl_module.build_subroute(page, sub)
            if sub_view:
                page.views.append(sub_view)

        elif target == "/student":
            import gui.student as st_module
            st_module.set_user(page.user_id)
            page.views.append(st_module.build_home(page))

        page.update()

    def view_pop(view):
        if page.views:
            page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route or "/")


if __name__ == "__main__":
    ft.app(target=main)
