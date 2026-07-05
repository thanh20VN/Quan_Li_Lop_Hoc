from gui.function import *
import flet as ft
import data
import logic
import config

id1 = 0
column = ["ID", "Lỗi vi phạm", "Điểm trừ / cộng", "Số lần"]
idclass=None
user=None

def set_user(uid):
    global id1, idclass
    id1 = uid
    user = data.find_user(id1)
    idclass = user.get('class_id', None) if isinstance(user, dict) else None


def _load_data():
    user_data = data.UserData()
    t3 = []
    for i in user_data.values():
        if i['role'] != config.roles[0]:
            t3.append(i['id'])
    return t3


def _make_rows(data_list):
    rows = []
    for i in data_list:
        rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(i["id"]))),
                    ft.DataCell(ft.Text(i["name"])),
                    ft.DataCell(ft.Text(str(i["point"]))),
                    ft.DataCell(ft.Text(str(i["count"]))),
                ]
            )
        )
    return rows


def _make_user_checkboxes():
    t3 = _load_data()
    row3 = []
    for i in t3:
        t8 = data.find_user(i)
        if isinstance(t8, dict):
            row3.append(ft.Checkbox(label=str(t8["id"]) + " ." + t8["name"], value=False))
    return row3


def build_home(page):
    try:
        t1 = list1("error", id1,idclass)
        t2 = list1("give", id1,idclass)
    except Exception:
        t1, t2 = [], []
    row1 = _make_rows(t1)
    row2 = _make_rows(t2)

    layout = get_layout(page)
    is_mobile = layout == "mobile"

    col_width = (page.width or 400) - 40 if is_mobile else 500

    error_table = ft.DataTable(
        vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE),
        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREEN),
        border=ft.border.all(1, ft.Colors.RED),
        border_radius=10,
        columns=[ft.DataColumn(ft.Text(col)) for col in column],
        rows=row1
    )

    give_table = ft.DataTable(
        vertical_lines=ft.border.BorderSide(1, ft.Colors.BLUE),
        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREEN),
        border=ft.border.all(1, ft.Colors.RED),
        border_radius=10,
        columns=[ft.DataColumn(ft.Text(col)) for col in column],
        rows=row2
    )

    error_col = ft.Column(
        controls=[
            ft.Text("Danh sách vi phạm:", size=16),
            error_table,
            ft.Text("Tổng điểm: -" + str(logic.student.my_error_give.cal_errors(id1,idclass)), size=20),
        ],
        scroll=ft.ScrollMode.ALWAYS,
        height=page.height - 120 if page.height else 570,
        width=col_width
    )

    give_col = ft.Column(
        controls=[
            ft.Text("Danh sách Cộng điểm:", size=16),
            give_table,
            ft.Text("Tổng điểm: +" + str(logic.student.my_error_give.cal_give(id1,idclass)), size=20),
        ],
        scroll=ft.ScrollMode.ALWAYS,
        height=page.height - 120 if page.height else 570,
        width=col_width
    )

    if is_mobile:
        tables = ft.Column(controls=[error_col, give_col], spacing=20)
    else:
        tables = ft.Row(controls=[error_col, give_col], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # user = data.find_user(id1)
    user_name = user.get('name', '') if isinstance(user, dict) else ''

    return ft.View(
        "/classmonitor",
        [
            ft.Row(
                controls=[ft.Text(f"Xin chào lớp trưởng {user_name}", size=20)],
                alignment=ft.MainAxisAlignment.START,
            ),
            tables,
            ft.Row(
                controls=[
                    ft.Button(text="Tổng kết", width=100, on_click=lambda e: page.go("/classmonitor/summary")),
                    ft.Button(text="Xoá lỗi", width=100, on_click=lambda e: page.go("/classmonitor/remove")),
                    ft.Button(text="Đăng xuất", width=110, on_click=lambda e: page.go("/logout"))
                ],
                alignment=ft.MainAxisAlignment.END
            ),
        ]
    )


def build_subroute(page, sub):
    if sub == "summary":
        return _build_summary(page)
    elif sub == "remove":
        return _build_remove(page)
    return None


def _build_summary(page):
    t15 = ft.Checkbox(label="Tuần")
    t16 = ft.Checkbox(label="Học kỳ")
    t17 = ft.Checkbox(label="Năm học")
    t18 = ft.Column(controls=[t15, t16, t17])
    row5 = []
    t21 = ft.Column(controls=row5, visible=True)
    t25 = ft.Column(controls=[], scroll=ft.ScrollMode.ALWAYS, expand=True)

    t23 = {'value': ''}

    def click(e):
        if t23['value'] == "Tuần":
            t24 = logic.summary.week.generate_weekly_summary(idclass).values()
            t26 = data.team.read_mainfile(idclass)
            for i in t24:
                week_num = i.pop("week", None)
                if week_num:
                    t25.controls.append(ft.Text(f"--- Tuần {week_num} ---", size=20, weight=ft.FontWeight.BOLD))
                for k in t26["idteam"]:
                    if str(k["id_team"]) == str(next(iter(i))):
                        t25.controls.append(ft.Text(f"Tên nhóm: {k['name']}", size=18))
                for j in i.values():
                    t25.controls.append(ft.Text(
                        f"Tên: {j['name']}, điểm cộng: {j['give']}, điểm trừ: {j['error']}, đánh giá: {j['ratings']}, Tổng điểm: {str(j['total'])}",
                        size=18
                    ))
            t22.disabled = True
            page.update()
        elif t23['value'] == "Học kỳ":
            result = logic.summary.semester.generate_weekly_summary(idclass)
            semester_num = result.get("semester", "")
            t24 = result.get("data", [])
            t26 = data.team.read_mainfile(idclass)
            if semester_num:
                t25.controls.append(ft.Text(f"--- Học kỳ {semester_num} ---", size=20, weight=ft.FontWeight.BOLD))
            for i in t24:
                for k in t26["idteam"]:
                    if str(k["id_team"]) == str(next(iter(i))):
                        t25.controls.append(ft.Text(f"Tên nhóm: {k['name']}", size=18))
                for j in i[1]:
                    t25.controls.append(ft.Text(
                        f"Tên: {j[0]}, đánh giá: {j[2]}, Tổng điểm: {j[1]}",
                        size=18
                    ))
            t22.disabled = True
            page.update()
        elif t23['value'] == "Năm học":
            t24 = logic.summary.year.generate_weekly_summary(idclass)
            t26 = data.team.read_mainfile(idclass)
            t25.controls.append(ft.Text(f"--- Năm học ---", size=20, weight=ft.FontWeight.BOLD))
            for i in t24:
                for k in t26["idteam"]:
                    if str(k["id_team"]) == str(next(iter(i))):
                        t25.controls.append(ft.Text(f"Tên nhóm: {k['name']}", size=18))
                for j in i[1]:
                    t25.controls.append(ft.Text(
                        f"Tên: {j[0]}, đánh giá: {j[2]}, Tổng điểm: {j[1]}",
                        size=18
                    ))
            t22.disabled = True
            page.update()

    t22 = ft.OutlinedButton(text="Xác nhận", width=130, height=40, on_click=click, disabled=False)

    def check3(e):
        is_valid = check_single_true([t15, t16, t17])
        if is_valid:
            t19 = find_selected_text([t15, t16, t17])
            tt = data.summary.read_main("week")
            if t19[-1] == "Tuần":
                t23['value'] = 'Tuần'
                row5.clear()
                if data.summary.read_main("semester")["num"] == 0 and tt["num"] >= config.semester_1:
                    row5.append(ft.Text("Tối đa tuần học kỳ 1", size=20))
                elif data.summary.read_main("semester")["num"] == 1 and tt["num"] == config.semester_total:
                    row5.append(ft.Text("Tối đa tuần học kỳ 2", size=20))
                elif data.summary.read_main("semester")["num"] == 2:
                    row5.append(ft.Text("Tối đa học kỳ", size=20))
                else:
                    row5.append(t22)
                t21.controls = row5
                page.update()
            elif t19[-1] == "Học kỳ":
                t23['value'] = 'Học kỳ'
                row5.clear()
                if data.summary.read_main("semester")["num"] == 0 and not tt["num"] <= config.semester_1:
                    row5.append(ft.Text("Tối đa tuần học kỳ 1", size=20))
                elif data.summary.read_main("semester")["num"] == 1 and not tt["num"] == config.semester_total:
                    row5.append(ft.Text("Tối đa tuần học kỳ 2", size=20))
                elif data.summary.read_main("semester")["num"] == 2:
                    row5.append(ft.Text("Tối đa học kỳ", size=20))
                else:
                    row5.append(t22)
                t21.controls = row5
                page.update()
            elif t19[-1] == "Năm học":
                t23['value'] = 'Năm học'
                row5.clear()
                if not data.summary.read_main("semester")["num"] <= 2:
                    row5.append(ft.Text("Không đủ học kỳ", size=20))
                else:
                    row5.append(t22)
                t21.controls = row5
                page.update()
        else:
            row5.clear()
            t21.controls = row5
            page.update()

    for i in [t15, t16, t17]:
        i.on_change = check3

    return ft.View(
        "/classmonitor/summary",
        [
            ft.AppBar(title=ft.Text("Tổng kết"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            ft.Row(controls=[t18, t21, t25])
        ]
    )


def _build_remove(page):
    row3 = _make_user_checkboxes()
    row4 = []
    t7 = ft.Column(controls=row4, scroll=ft.ScrollMode.ALWAYS, width=300, height=650, visible=False)

    def click1(e):
        t13 = find_selected_numbers(row3)
        t14 = data.team.read_mainfile(idclass)['idteam']
        t15_local = find_selected_numbers(row4)
        idt = 0
        for i in t14:
            team = data.team.read_teamfile(i['id_team'])
            if team and t13[-1] in team['members']:
                idt = team['teamleider_id']
        for i in range(int(text1.value)):
            t = logic.team.remove.remove_error(idt, t13[-1], t15_local[-1])
            if t:
                row4.clear()
                for checkbox in row3:
                    checkbox.value = False
                page.go("/classmonitor")

    text1 = ft.TextField(label="Mấy lần", width=300, height=100, text_align=ft.TextAlign.LEFT)
    buton = ft.Button(text="Xác nhận", width=100, height=50, on_click=click1, disabled=False)

    t9 = ft.Column(
        controls=[text1, buton],
        scroll=ft.ScrollMode.ALWAYS,
        width=200,
        height=650,
        visible=False
    )

    def check1(e):
        is_valid = check_single_true(row3)
        if is_valid:
            t4_local = find_selected_numbers(row3)
            t6_local = list2("error", int(t4_local[-1]),idclass)
            row4.clear()
            for i in t6_local:
                row4.append(
                    ft.Checkbox(label=str(i["id"]) + "." + i["name"] + ", Số lần: " + str(i["count"]), value=False)
                )
            if not row4:
                row4.append(ft.Text(value="Không có lỗi nào"))
            else:
                t9.visible = True
            t7.controls = row4
            t7.visible = True
        else:
            t7.visible = False
            t9.visible = False
        page.update()

    for checkbox in row3:
        checkbox.on_change = check1

    layout = get_layout(page)
    is_mobile = layout == "mobile"

    if is_mobile:
        content = ft.Column(
            controls=[
                ft.Column(controls=row3, scroll=ft.ScrollMode.ALWAYS, height=200),
                t7, t9
            ]
        )
    else:
        content = ft.Row(
            controls=[
                ft.Column(controls=row3, scroll=ft.ScrollMode.ALWAYS, width=200, height=650),
                t7, t9
            ]
        )

    return ft.View(
        "/classmonitor/remove",
        [
            ft.AppBar(title=ft.Text("Xoá lỗi"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            content
        ]
    )
