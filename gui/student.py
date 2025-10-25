import flet as ft
import data_py
import logic

id1=0
column=["ID","Lỗi vi phạm","Điểm trừ / cộng","Số lần"]

def list1(type):
    a=[]
    b=[[],[]]
    if type=="error":
        tm=logic.student.my_error_give.my_errors(id1)
    elif type=="give":
        tm=logic.student.my_error_give.my_give(id1)
    if tm != ["None found"]:
        for i in tm:a.append(i["id"])
        for i in a:
            if i not in b[0]: b[0].append(i); b[1].append(a.count(i))
        c=[]
        for i in b[0]:
            for j in tm:
                if c==[] and i==j["id"]:
                    c.append({"id":i,"name":j["name"],"point":j["point"], "count":b[1][b[0].index(i)]})
                elif j["id"] != c[-1]["id"] and i==j["id"]:
                    c.append({"id":i,"name":j["name"],"point":j["point"], "count":b[1][b[0].index(i)]})
    else:c=[]
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

    page.title = "Học sinh"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1100
    page.window.height = 770
    # page.window.full_screen=True
    page.window.resizable = False
    page.window.maximizable=False
    page.window.center()

    page.add(
        ft.Row(
            controls=[
                ft.Text(f"Xin chào học sinh {data_py.find_user(id1).get('name')}", size=20)
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
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    height=600,
                    width=500
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
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    height=600,
                    width=500
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.Row(
            controls=[
                ft.Button(text="Thoát", width=100, on_click=lambda e: page.window.destroy())
            ],
            alignment=ft.MainAxisAlignment.END
        ),
    )

def __init__(page1,id):
    global id1
    id1=id
    # ft.app(target=gui)
    gui(page1)