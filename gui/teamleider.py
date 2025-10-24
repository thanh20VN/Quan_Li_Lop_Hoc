import flet as ft
import data_py
import logic

id1=2
column=["ID","Lỗi vi phạm","Điểm trừ / cộng","Số lần"]


def check_single_true(checkboxes): 
    if isinstance(checkboxes[0], list):
        flat_list = [item for sublist in checkboxes for item in sublist]
        return sum(1 for cb in flat_list if cb.value) == 1
    return sum(1 for cb in checkboxes if cb.value) == 1
def list1(type):
    a=[]
    b=[[],[]]
    if type=="error":
        t=logic.student.my_error_give.my_errors(id1)
    elif type=="give":
        t=logic.student.my_error_give.my_give(id1)
    for i in t:a.append(i["id"])
    for i in a:
        if i not in b[0]: b[0].append(i); b[1].append(a.count(i))
    c=[]
    for i in b[0]:
        for j in t:
            if c==[] and i==j["id"]:
                c.append({"id":i,"name":j["name"],"point":j["point"], "count":b[1][b[0].index(i)]})
            elif j["id"] != c[-1]["id"] and i==j["id"]:
                c.append({"id":i,"name":j["name"],"point":j["point"], "count":b[1][b[0].index(i)]})
    return c

def gui(page: ft.Page):
    t1=list1("error")
    t2=list1("give")
    row1=[]
    for i in t1:
        row1.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(i["id"]))),
                    ft.DataCell(ft.Text(i["name"])),
                    ft.DataCell(ft.Text(str(i["point"]))),
                    ft.DataCell(ft.Text(str(i["count"]))),
                ]
            )
        )
    
    row2=[]
    for i in t2:
        row2.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(i["id"]))),
                    ft.DataCell(ft.Text(i["name"])),
                    ft.DataCell(ft.Text(str(i["point"]))),
                    ft.DataCell(ft.Text(str(i["count"]))),
                ]
            )
        )

    row3=[]
    for i in data_py.eg.read_egfile("e")["errors"]:
        row3.append(
            ft.Checkbox(label=i["name"], value=False)
        )
    
    row4=[]
    for i in data_py.team.read_teamfile(id1)["members"]:
        row4.append(
            ft.Checkbox(label=data_py.find_user(i)["name"], value=False)
        )
    page.title = "Học sinh"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1100
    page.window.height = 770
    # page.window.full_screen=True
    page.window.resizable = False
    t5=ft.TextField(label="Mấy lần", width=300, height=100, text_align=ft.TextAlign.LEFT)
    t3=ft.Button(text="Xác nhận", width=100, height=50, disabled=False)
    row4.append(t5)
    row4.append(t3)

    t4=ft.Column(
        controls=row4,
        alignment=ft.MainAxisAlignment.START,
        visible=False
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        controls=[
                            ft.Text(f"Xin chào Tổ trưởng {data_py.find_user(id1).get('name')}", size=20)
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text("Danh sách vi phạm:", size=16),
                                    ft.DataTable(
                                        vertical_lines=ft.border.BorderSide(3, ft.Colors.BLUE),
                                        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREEN),
                                        border=ft.border.all(2, ft.Colors.RED),
                                        border_radius=10,
                                        columns=[
                                            ft.DataColumn(ft.Text(col)) for col in column
                                        ],
                                        rows=row1
                                    ),
                                    ft.Text("Tổng điểm: -"+str(logic.student.my_error_give.cal_errors(id1)), size=20),
                                ]
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text("Danh sách Cộng điểm:", size=16),
                                    ft.DataTable(
                                        vertical_lines=ft.border.BorderSide(3, ft.Colors.BLUE),
                                        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREEN),
                                        border=ft.border.all(2, ft.Colors.RED),
                                        border_radius=10,
                                        columns=[
                                            ft.DataColumn(ft.Text(col)) for col in column
                                        ],
                                        rows=row2
                                    ),
                                    ft.Text("Tổng điểm: +" + str(logic.student.my_error_give.cal_give(id1)), size=20),
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        controls=[
                            ft.Button(text="Thêm vi phạm", width=150, height=50, on_click=lambda e: page.go("/error")),
                            ft.Button(text="Thêm điểm cộng", width=150, height=50, on_click=lambda e: page.go("/give")),
                            ft.Button(text="Thoát", width=100, height=50, on_click=lambda e: page.window.destroy())
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ])
        )
        if page.route == "/error":
            page.views.append(
                ft.View(
                    "/error",
                    [
                        ft.AppBar(title=ft.Text("Vi phạm"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=row3
                                ),
                                t4
                            ]
                        ),
                    ],
                )
            )
        if page.route == "/give":
            page.views.append(
                ft.View(
                    "/give",
                    [
                        ft.AppBar(title=ft.Text("Điểm cộng"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                    ],
                )
            )
        page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    # print(row4[0:2],row3)
    def on_checkbox_change(e):
        is_valid = check_single_true(row3) 
        t4.visible = is_valid
        page.update()
    

    for checkbox in row3:
        checkbox.on_change = on_checkbox_change
def __init__(id):
    global id1
    id1=id
    ft.app(target=gui)

