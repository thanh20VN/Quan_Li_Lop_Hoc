import flet as ft
import data
import logic
from gui.function import get_layout

id1 = 0
column = ["ID", "Lỗi vi phạm", "Điểm trừ / cộng", "Số lần"]
user=None
idclass=None

def set_user(uid):
    global id1, idclass
    id1 = uid
    user = data.find_user(id1)
    idclass = user.get('class_id', None) if isinstance(user, dict) else None


def _list_data(type):
    a = []
    b = [[], []]
    if type == "error":
        tm = logic.student.my_error_give.my_errors(id1,idclass)
    elif type == "give":
        tm = logic.student.my_error_give.my_give(id1,idclass)
    if tm != ["None found"]:
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
    else:
        c = []
    return c


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


def build_home(page):
    try:
        t1 = _list_data("error")
        t2 = _list_data("give")
    except Exception:
        t1, t2 = [], []
    row1 = _make_rows(t1)
    row2 = _make_rows(t2)

    layout = get_layout(page)
    is_mobile = layout == "mobile"

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

    col_width = (page.width or 400) - 40 if is_mobile else 500

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
        tables = ft.Column(
            controls=[error_col, give_col],
            spacing=20,
        )
    else:
        tables = ft.Row(
            controls=[error_col, give_col],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

    # user = data.find_user(id1)
    user_name = user.get('name', '') if isinstance(user, dict) else ''

    return ft.View(
        "/student",
        [
            ft.Row(
                controls=[ft.Text(f"Xin chào học sinh {user_name}", size=20)],
                alignment=ft.MainAxisAlignment.START,
            ),
            tables,
            ft.Row(
                controls=[
                    ft.Button(text="Đăng xuất", width=110, on_click=lambda e: page.go("/logout"))
                ],
                alignment=ft.MainAxisAlignment.END
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
    )
