from gui.function import *
import flet as ft
import json
import data
import logic
import config
import logic.student.my_error_give

id1 = 0
column = ["STT", "Tên học sinh", "Tổ", "Điểm cộng", "Điểm trừ", "Tổng điểm cộng"]


def set_user(uid):
    global id1
    id1 = uid


def _load_data():
    from data.supabase_client import retry_query
    t2 = []
    try:
        user_data = retry_query(lambda: data.UserData())
        # print(user_data)
    except Exception:
        return t2
    for i in user_data.values():
        if i['role'] != config.roles[0] and i['role'] == config.roles[2]:
            team_name = ''
            try:
                for j in retry_query(lambda: data.team.read_mainfile(id1))['idteam']:
                    if j['id_team'] == i['id']:
                        team_name = j['name']
            except Exception:
                pass
            t2.append([
                i['id'], i['name'], team_name,
                logic.student.my_error_give.cal_give(i['id'],id1),
                logic.student.my_error_give.cal_errors(i['id'],id1),
                logic.student.my_error_give.cal_total(i['id'],id1)
            ])
        elif i['role'] != config.roles[0]:
            team_name = ''
            try:
                for j in retry_query(lambda: data.team.read_mainfile(id1))['idteam']:
                    t4 = retry_query(lambda: data.team.read_teamfile(j['id_team']))
                    if t4:
                        for h in t4['members']:
                            if h == i['id']:
                                team_name = j['name']
                                break
            except Exception:
                pass
            t2.append([
                i['id'], i['name'], team_name,
                logic.student.my_error_give.cal_give(i['id']),
                logic.student.my_error_give.cal_errors(i['id']),
                logic.student.my_error_give.cal_total(i['id'])
            ])
    return t2


def _make_row(cells):
    return ft.DataRow(cells=[ft.DataCell(ft.Text(str(c))) for c in cells])


def build_home(page):
    try:
        t2 = _load_data()
    except Exception:
        t2 = []
    layout = get_layout(page)
    is_mobile = layout == "mobile"
    is_tablet = layout == "tablet"
    # print(t2)
    row1 = [_make_row(i) for i in t2]
    # print(row1)
    table_width = page.width - 40 if is_mobile else None
    col_width = min(500, (page.width or 1100) // 2 - 20) if not is_mobile else (page.width or 400) - 40
    font_big = 16 if is_mobile else 20
    font_small = 14 if is_mobile else 16
    user = data.find_user(id1)
    id_class = user.get('class_id', None) if isinstance(user, dict) else None
    data_table = ft.DataTable(
        vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE),
        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREEN),
        border=ft.border.all(1, ft.Colors.RED),
        column_spacing=140 if not is_mobile else 40,
        heading_row_height=50,
        border_radius=10,
        columns=[ft.DataColumn(ft.Text(col)) for col in column],
        rows=row1
    )

    if is_mobile:
        table_content = ft.Column(
            controls=[data_table],
            scroll=ft.ScrollMode.ALWAYS,
            height=300,
            width=col_width
        )
    else:
        table_content = ft.Column(
            controls=[data_table],
            scroll=ft.ScrollMode.ALWAYS,
            height=page.height - 250 if page.height else 570,
            width=page.width - 40 if page.width else 1060
        )

    summary_container = _build_summary_box(page, is_mobile, font_small)
    export_container = _build_export_box(page, is_mobile, font_small)
    account_container = _build_account_box(page, is_mobile, font_small)

    if is_mobile:
        action_row = ft.Column(
            controls=[summary_container, export_container, account_container],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    else:
        action_row = ft.Row(
            controls=[summary_container, export_container, account_container],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

    logout_btn = ft.OutlinedButton(
        text="Đăng xuất", width=120,
        on_click=lambda e: page.go("/logout")
    )

    # print()
    user_name = user.get('name', '') if isinstance(user, dict) else ''

    return ft.View(
        "/teacher",
        [
            ft.Row(
                controls=[ft.Text(f"Xin chào Giáo viên {user_name}", size=font_big)],
                alignment=ft.MainAxisAlignment.START,
            ),
            table_content,
            action_row,
            ft.Row(
                controls=[logout_btn],
                alignment=ft.MainAxisAlignment.END
            )
        ]
    )


def _build_summary_box(page, is_mobile, font_size):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[ft.Text(value="Tổng kết", size=font_size)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.OutlinedButton(text="Tuần", width=85, on_click=lambda e: page.go("/teacher/summary/week")),
                        ft.OutlinedButton(text="Học kỳ", width=95, on_click=lambda e: page.go("/teacher/summary/semester"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.OutlinedButton(text="Năm học", width=110, on_click=lambda e: page.go("/teacher/summary/year"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        border=ft.border.all(1, ft.Colors.RED),
        border_radius=10,
        height=130,
        width=200 if not is_mobile else (page.width or 400) - 40,
    )


def _build_export_box(page, is_mobile, font_size):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[ft.Text(value="Xuất file excel", size=font_size)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.OutlinedButton(text="Tuần", width=85, on_click=lambda e: page.go("/teacher/export/week")),
                        ft.OutlinedButton(text="Học kỳ", width=95, on_click=lambda e: page.go("/teacher/export/semester"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.OutlinedButton(text="Năm học", width=110, on_click=lambda e: page.go("/teacher/export/year"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        border=ft.border.all(1, ft.Colors.RED),
        border_radius=10,
        height=130,
        width=200 if not is_mobile else (page.width or 400) - 40,
    )


def _build_account_box(page, is_mobile, font_size):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[ft.Text(value="Tài khoản", size=font_size)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.OutlinedButton(text="Thêm tài khoản", width=150, on_click=lambda e: page.go("/teacher/createAccount"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        border=ft.border.all(1, ft.Colors.RED),
        border_radius=10,
        height=130,
        width=200 if not is_mobile else (page.width or 400) - 40,
    )


def build_subroute(page, sub):
    if sub == "summary/week":
        return _build_summary_week(page)
    elif sub == "summary/semester":
        return _build_summary_semester(page)
    elif sub == "summary/year":
        return _build_summary_year(page)
    elif sub == "export/week":
        return _build_export_week(page)
    elif sub == "export/semester":
        return _build_export_semester(page)
    elif sub == "export/year":
        return _build_export_year(page)
    elif sub == "createAccount":
        return _build_create_account(page)
    return None


def _build_summary_week(page):
    t4 = ft.Column(controls=[], scroll=ft.ScrollMode.ALWAYS, expand=True)

    def click(e):
        t7 = logic.summary.week.generate_weekly_summary(id1).values()
        t8 = data.team.read_mainfile(id1)
        for i in t7:
            for k in t8["idteam"]:
                if str(k["id_team"]) == str(next(iter(i))):
                    t4.controls.append(ft.Text(f"Tên nhóm: {k['name']}", size=18))
            for j in i.values():
                t4.controls.append(ft.Text(
                    f"Tên: {j['name']}, điểm cộng: {j['give']}, điểm trừ: {j['error']}, đánh giá: {j['ratings']}, Tổng điểm: {str(j['total'])}",
                    size=18
                ))
        t5.disabled = True
        page.update()

    t5 = ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)

    row2 = []
    tt = data.summary.read_main("week")
    if data.summary.read_main("semester")["num"] == 0 and tt["num"] >= config.semester_1:
        row2.append(ft.Text("Tối đa tuần học kỳ 1", size=20))
        t5.disabled = True
    elif data.summary.read_main("semester")["num"] == 1 and tt["num"] == config.semester_total:
        row2.append(ft.Text("Tối đa tuần học kỳ 2", size=20))
        t5.disabled = True
    elif data.summary.read_main("semester")["num"] == 2:
        row2.append(ft.Text("Tối đa học kỳ", size=20))
        t5.disabled = True

    return ft.View(
        "/teacher/summary/week",
        [
            ft.AppBar(title=ft.Text("Tổng kết - Tuần"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            t5, ft.Column(controls=row2), t4
        ]
    )


def _build_summary_semester(page):
    t4 = ft.Column(controls=[], scroll=ft.ScrollMode.ALWAYS, expand=True)

    def click(e):
        t7 = logic.summary.semester.generate_weekly_summary(id1)
        t8 = data.team.read_mainfile(id1)
        for i in t7:
            for k in t8["idteam"]:
                if str(k["id_team"]) == str(next(iter(i))):
                    t4.controls.append(ft.Text(f"Tên nhóm: {k['name']}", size=18))
            for j in i[1]:
                t4.controls.append(ft.Text(
                    f"Tên: {j[0]}, đánh giá: {j[2]}, Tổng điểm: {j[1]}",
                    size=18
                ))
        t5.disabled = True
        page.update()

    t5 = ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)

    row2 = []
    tt = data.summary.read_main("week")
    if data.summary.read_main("semester")["num"] == 0 and not tt["num"] <= config.semester_1:
        row2.append(ft.Text("Tối đa tuần học kỳ 1", size=20))
        t5.disabled = True
    elif data.summary.read_main("semester")["num"] == 1 and not tt["num"] == config.semester_total:
        row2.append(ft.Text("Tối đa tuần học kỳ 2", size=20))
        t5.disabled = True
    elif data.summary.read_main("semester")["num"] == 2:
        row2.append(ft.Text("Tối đa học kỳ", size=20))
        t5.disabled = True

    return ft.View(
        "/teacher/summary/semester",
        [
            ft.AppBar(title=ft.Text("Tổng kết - Học kỳ"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            t5, ft.Column(controls=row2), t4
        ]
    )


def _build_summary_year(page):
    t4 = ft.Column(controls=[], scroll=ft.ScrollMode.ALWAYS, expand=True)

    def click(e):
        t7 = logic.summary.year.generate_weekly_summary(id1)
        t8 = data.team.read_mainfile(id1)
        for i in t7:
            for k in t8["idteam"]:
                if str(k["id_team"]) == str(next(iter(i))):
                    t4.controls.append(ft.Text(f"Tên nhóm: {k['name']}", size=18))
            for j in i[1]:
                t4.controls.append(ft.Text(
                    f"Tên: {j[0]}, đánh giá: {j[2]}, Tổng điểm: {j[1]}",
                    size=18
                ))
        t5.disabled = True
        page.update()

    t5 = ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)

    row2 = []
    if not data.summary.read_main("semester")["num"] <= 2:
        row2.append(ft.Text("Không đủ học kỳ", size=20))

    return ft.View(
        "/teacher/summary/year",
        [
            ft.AppBar(title=ft.Text("Tổng kết - Năm học"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            t5, ft.Column(controls=row2), t4
        ]
    )


def _build_export_week(page):
    t4 = data.summary.read_main("week")
    row3 = []
    for i in range(1, t4["num"] + 1):
        label = f"Tuần 0{i}" if i <= 9 else f"Tuần {i}"
        row3.append(ft.Checkbox(label=label))

    t5 = [i["id_team"] for i in data.team.read_mainfile(id1)["idteam"]]
    t6 = {}

    def check(e):
        t8 = find_selected_numbers_end(row3)
        if t8:
            t10.disabled = False
            page.update()
            for i in t5:
                t7 = data.summary.read(i, "week", int(t8[-1]))
                t6[str(i)] = t7
        else:
            t10.disabled = True
            page.update()

    for i in row3:
        i.on_change = check

    download_btn = ft.OutlinedButton(text="Tải file", width=120, visible=False)
    t9 = ft.Text(value="", size=20)

    def click(e):
        excel_bytes = logic.export.week.export_week(t6, id1)
        download_btn.url = excel_to_download_link(excel_bytes)
        download_btn.visible = True
        t9.value = "Xuất file thành công!"
        page.update()

    t10 = ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=True)

    return ft.View(
        "/teacher/export/week",
        [
            ft.AppBar(title=ft.Text("Xuất ra file excel - Tuần"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            ft.Row(
                controls=[
                    ft.Column(controls=row3, scroll=ft.ScrollMode.ALWAYS, height=650, width=100),
                    ft.Column(controls=[t10, download_btn, t9], spacing=10)
                ]
            )
        ]
    )


def _build_export_semester(page):
    t4 = data.summary.read_main("semester")
    row3 = []
    for i in range(1, t4["num"] + 1):
        label = f"Học kỳ 0{i}" if i <= 9 else f"Học kỳ {i}"
        row3.append(ft.Checkbox(label=label))

    t5 = [i["id_team"] for i in data.team.read_mainfile(id1)["idteam"]]
    t6 = {}

    def check(e):
        t8 = find_selected_numbers_end(row3)
        if t8:
            t10.disabled = False
            page.update()
            for i in t5:
                t7 = data.summary.read(i, "semester", int(t8[-1]))
                if t7 and isinstance(t7, dict):
                    t6[str(i)] = t7.get('students', [])
        else:
            t10.disabled = True
            page.update()

    for i in row3:
        i.on_change = check

    download_btn = ft.OutlinedButton(text="Tải file", width=120, visible=False)
    t9 = ft.Text(value="", size=20)

    def click(e):
        excel_bytes = logic.export.semester.export_semester(t6, id1)
        download_btn.url = excel_to_download_link(excel_bytes)
        download_btn.visible = True
        t9.value = "Xuất file thành công!"
        page.update()

    t10 = ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=True)

    return ft.View(
        "/teacher/export/semester",
        [
            ft.AppBar(title=ft.Text("Xuất ra file excel - Học kỳ"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            ft.Row(
                controls=[
                    ft.Column(controls=row3, scroll=ft.ScrollMode.ALWAYS, height=100, width=100),
                    ft.Column(controls=[t10, download_btn, t9], spacing=10)
                ]
            )
        ]
    )


def _build_export_year(page):
    download_btn = ft.OutlinedButton(text="Tải file", width=120, visible=False)
    t9 = ft.Text(value="", size=20)

    def click(e):
        t5 = data.summary.read(1, "year", 1)
        excel_bytes = logic.export.year.export_year(t5, id1)
        download_btn.url = excel_to_download_link(excel_bytes)
        download_btn.visible = True
        t9.value = "Xuất file thành công!"
        page.update()

    t10 = ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)

    return ft.View(
        "/teacher/export/year",
        [
            ft.AppBar(title=ft.Text("Xuất ra file excel - Năm học"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            ft.Row(controls=[t10, download_btn, t9])
        ]
    )


def _build_create_account(page):
    t3 = ft.TextField(label="Tên", width=300, text_align=ft.TextAlign.LEFT)
    t4 = ft.TextField(label="Mật khẩu", width=300, password=True, text_align=ft.TextAlign.LEFT)
    t5 = ft.Text(value=config.roles[3], size=20)
    t6 = ft.TextField(label="Tên tổ", width=300, text_align=ft.TextAlign.LEFT, visible=False)
    t7 = ft.ListView(spacing=10, padding=20, width=300, visible=True)

    class State1:
        def __init__(self):
            self.selected_role = ''
    state1 = State1()

    def click1(e):
        state1.selected_role = e.control.text
        page.update()

    for i in data.team.read_mainfile(id1)['idteam']:
        t7.controls.append(ft.Button(i['name'], on_click=click1))

    class State:
        def __init__(self):
            self.selected_role = config.roles[3]
    state = State()

    def click(e):
        state.selected_role = e.control.text
        t5.value = e.control.text
        if e.control.text == config.roles[2]:
            t6.visible = True
            t7.visible = False
        else:
            t7.visible = True
            t6.visible = False
        page.update()

    def click2(e):
        if not t3.value or not t4.value:
            page.open(ft.SnackBar(content=ft.Text("Vui lòng nhập tên và mật khẩu")))
            return
        if not state.selected_role:
            page.open(ft.SnackBar(content=ft.Text("Vui lòng chọn vai trò")))
            return
        t10 = logic.reg.register(t3.value, t4.value, state.selected_role, id1)
        if isinstance(t10, tuple) and t10[0] == "Tạo tài khoản thành công.":
            if state.selected_role == config.roles[2]:
                logic.team.create_team(t6.value, t10[1], id1)
            elif state.selected_role in [config.roles[1], config.roles[3]]:
                if not state1.selected_role:
                    page.open(ft.SnackBar(content=ft.Text("Vui lòng chọn tổ")))
                    return
                team_id = data.team.find_team(state1.selected_role, id1)
                if team_id:
                    logic.team.add_member(team_id, t10[1])
                else:
                    page.open(ft.SnackBar(content=ft.Text("Không tìm thấy tổ")))
                    return
        page.go("/teacher")

    return ft.View(
        "/teacher/createAccount",
        [
            ft.AppBar(title=ft.Text("Tạo tài khoản"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            ft.Container(
                content=ft.Column(
                    controls=[
                        t3, t4,
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.PopupMenuButton(
                                        icon=ft.Icons.VIEW_LIST,
                                        items=[
                                            ft.PopupMenuItem(text=config.roles[1], on_click=click),
                                            ft.PopupMenuItem(text=config.roles[2], on_click=click),
                                            ft.PopupMenuItem(text=config.roles[3], on_click=click),
                                        ]
                                    ),
                                    t5
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            alignment=ft.alignment.center,
                        ),
                        t6, t7,
                        ft.ElevatedButton(
                            text="Tạo tài khoản", width=200, height=40, on_click=click2
                        )
                    ],
                    spacing=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]
    )
