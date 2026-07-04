import flet as ft
import data_py
import logic
from gui.function import get_layout

id1 = 0
column = ["ID", "Lỗi vi phạm", "Điểm trừ / cộng", "Số lần"]
user=None
idclass=None

def set_user(uid):
    global id1, idclass
    id1 = uid
    user = data_py.find_user(id1)
    idclass = user.get('class_id', None) if isinstance(user, dict) else None


def _check_single_true(checkboxes):
    if isinstance(checkboxes[0], list):
        flat_list = [item for sublist in checkboxes for item in sublist]
        return sum(1 for cb in flat_list if cb.value) == 1
    return sum(1 for cb in checkboxes if cb.value) == 1


def _mutil1(checkboxes):
    if isinstance(checkboxes[0], list):
        flat_list = [item for sublist in checkboxes for item in sublist]
        return sum(1 for cb in flat_list if cb.value) > 0
    return sum(1 for cb in checkboxes if cb.value) > 0


def _find_checkbox(checkboxes):
    flat_checkboxes = []
    for item in checkboxes:
        if isinstance(item, list):
            flat_checkboxes.extend(item)
        else:
            flat_checkboxes.append(item)
    for checkbox in flat_checkboxes:
        if checkbox.value:
            return checkbox.label
    return None


def _list_data(type):
    a = []
    b = [[], []]
    if type == "error":
        tm = logic.student.my_error_give.my_errors(id1,idclass)
    elif type == "give":
        tm = logic.student.my_error_give.my_give(id1,idclass)
    if tm:
        for i in tm:
            a.append(i["id"])
        for i in a:
            if i not in b[0]:
                b[0].append(i)
                b[1].append(a.count(i))
        c = []
        for i in b[0]:
            for j in tm:
                if c == [] and i == j["id"]:
                    c.append({"id": i, "name": j["name"], "point": j["point"], "count": b[1][b[0].index(i)]})
                elif j["id"] != c[-1]["id"] and i == j["id"]:
                    c.append({"id": i, "name": j["name"], "point": j["point"], "count": b[1][b[0].index(i)]})
        return c
    else:
        return []


def _get_number_from_label(label):
    try:
        return int(label.split('.')[0].strip())
    except:
        return 0


def _find_selected_numbers(checkboxes):
    flat = []
    for item in checkboxes:
        if isinstance(item, list):
            flat.extend(item)
        else:
            flat.append(item)
    return [_get_number_from_label(cb.label) for cb in flat if cb.value]


def _make_rows(data_list):
    return [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(i["id"]))),
                ft.DataCell(ft.Text(i["name"])),
                ft.DataCell(ft.Text(str(i["point"]))),
                ft.DataCell(ft.Text(str(i["count"]))),
            ]
        )
        for i in data_list
    ]


def build_home(page):
    try:
        t1 = _list_data("give")
        t2 = _list_data("error")
    except Exception:
        t1, t2 = [], []
    row2 = _make_rows(t1)
    row1 = _make_rows(t2)

    row4 = []
    try:
        team = data_py.team.read_teamfile(id1)
        if team and team.get("members"):
            for i in team["members"]:
                t8 = data_py.find_user(i)
                if isinstance(t8, dict):
                    row4.append(ft.Checkbox(label=str(t8["id"]) + " ." + t8["name"], value=False))
    except Exception:
        pass

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

    # user = data_py.find_user(id1)
    # print(user)
    user_name = user.get('name', '') if isinstance(user, dict) else ''

    return ft.View(
        "/teamleider",
        [
            ft.Row(
                controls=[ft.Text(f"Xin chào Tổ trưởng {user_name}", size=20)],
                alignment=ft.MainAxisAlignment.START,
            ),
            tables,
            ft.Row(
                controls=[
                    ft.Button(text="Thêm vi phạm", width=150, height=50, on_click=lambda e: page.go("/teamleider/error")),
                    ft.Button(text="Thêm điểm cộng", width=150, height=50, on_click=lambda e: page.go("/teamleider/give")),
                    ft.Button(text="Đăng xuất", width=110, height=50, on_click=lambda e: page.go("/logout"))
                ],
                alignment=ft.MainAxisAlignment.END
            )
        ]
    )


def build_subroute(page, sub):
    if sub == "error":
        return _build_error(page)
    elif sub == "give":
        return _build_give(page)
    return None


def _build_error(page):
    row3 = []
    errors = data_py.eg.read_egfile("e")
    if errors and "errors" in errors:
        for i in errors["errors"]:
            row3.append(ft.Checkbox(label=str(i["id"]) + " ." + i["name"], value=False))
    elif errors:
        for i in errors:
            row3.append(ft.Checkbox(label=str(i["id"]) + " ." + i["name"], value=False))

    row4 = []
    team = data_py.team.read_teamfile(id1)
    if team and team.get("members"):
        for i in team["members"]:
            t8 = data_py.find_user(i)
            if isinstance(t8, dict):
                row4.append(ft.Checkbox(label=str(t8["id"]) + " ." + t8["name"], value=False))

    t0 = ft.TextField(label="Mấy lần", width=300, height=100, text_align=ft.TextAlign.LEFT)
    t3_btn = ft.Button(text="Xác nhận", on_click=lambda e: None, width=100, height=50, disabled=False)

    t4 = ft.Column(controls=row4, alignment=ft.MainAxisAlignment.START, visible=False)
    t5 = ft.Column(controls=[t0, t3_btn], alignment=ft.MainAxisAlignment.START, visible=False)

    def click(e):
        t6 = _find_checkbox(row3)
        t7 = _find_selected_numbers(row4)
        if t6:
            error_id = _get_number_from_label(t6)
            for i in t7:
                for j in range(int(t0.value)):
                    t9 = logic.team.add.add_error(id1, i, error_id)
                    if t9 == True:
                        page.go("/teamleider")

    t3_btn.on_click = click

    def on_checkbox_change(e):
        is_valid = _check_single_true(row3)
        t4.visible = is_valid
        t5.visible = _mutil1(row4) if is_valid else False
        page.update()

    for checkbox in row3:
        checkbox.on_change = on_checkbox_change

    def check_true(e):
        t5.visible = _mutil1(row4)
        page.update()

    for checkbox in row4:
        checkbox.on_change = check_true

    layout = get_layout(page)
    is_mobile = layout == "mobile"

    if is_mobile:
        content = ft.Column(controls=[ft.Column(controls=row3), t4, t5])
    else:
        content = ft.Row(controls=[ft.Column(controls=row3), t4, t5])

    return ft.View(
        "/teamleider/error",
        [
            ft.AppBar(title=ft.Text("Vi phạm"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            content,
        ],
    )


def _build_give(page):
    row3 = []
    gives = data_py.eg.read_egfile("g")
    if gives and "give" in gives:
        for i in gives["give"]:
            row3.append(ft.Checkbox(label=str(i["id"]) + " ." + i["name"], value=False))
    elif gives:
        for i in gives:
            row3.append(ft.Checkbox(label=str(i["id"]) + " ." + i["name"], value=False))

    row4 = []
    team = data_py.team.read_teamfile(id1)
    if team and team.get("members"):
        for i in team["members"]:
            t8 = data_py.find_user(i)
            if isinstance(t8, dict):
                row4.append(ft.Checkbox(label=str(t8["id"]) + " ." + t8["name"], value=False))

    t0 = ft.TextField(label="Mấy lần", width=300, height=100, text_align=ft.TextAlign.LEFT)
    t3_btn = ft.Button(text="Xác nhận", on_click=lambda e: None, width=100, height=50, disabled=False)

    t4 = ft.Column(controls=row4, alignment=ft.MainAxisAlignment.START, visible=False)
    t5 = ft.Column(controls=[t0, t3_btn], alignment=ft.MainAxisAlignment.START, visible=False)

    def click(e):
        t6 = _find_checkbox(row3)
        t7 = _find_selected_numbers(row4)
        if t6:
            give_id = _get_number_from_label(t6)
            for i in t7:
                for j in range(int(t0.value)):
                    t9 = logic.team.add.add_give(id1, i, give_id)
                    if t9 == True:
                        page.go("/teamleider")

    t3_btn.on_click = click

    def on_checkbox_change(e):
        is_valid = _check_single_true(row3)
        t4.visible = is_valid
        t5.visible = _mutil1(row4) if is_valid else False
        page.update()

    for checkbox in row3:
        checkbox.on_change = on_checkbox_change

    def check_true(e):
        t5.visible = _mutil1(row4)
        page.update()

    for checkbox in row4:
        checkbox.on_change = check_true

    layout = get_layout(page)
    is_mobile = layout == "mobile"

    if is_mobile:
        content = ft.Column(controls=[ft.Column(controls=row3), t4, t5])
    else:
        content = ft.Row(controls=[ft.Column(controls=row3), t4, t5])

    return ft.View(
        "/teamleider/give",
        [
            ft.AppBar(title=ft.Text("Điểm cộng"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
            content,
        ],
    )
