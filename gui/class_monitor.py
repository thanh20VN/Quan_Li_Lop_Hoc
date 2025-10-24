import flet as ft
import data_py
import logic
import config

id1=0
column=["ID","Lỗi vi phạm","Điểm trừ / cộng","Số lần"]
data_py.load_users()
# print(data_py.UserData)
t3=[]
for i in data_py.UserData.values():
    # print(i)
    if i['role'] != config.roles[0]:
        t3.append(i['id'])
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

def check_single_true(checkboxes): 
    if isinstance(checkboxes[0], list):
        flat_list = [item for sublist in checkboxes for item in sublist]
        return sum(1 for cb in flat_list if cb.value) == 1
    return sum(1 for cb in checkboxes if cb.value) == 1

def list2(type,id2):
    a=[]
    b=[[],[]]
    if type=="error":
        tm=logic.student.my_error_give.my_errors(id2)
    elif type=="give":
        tm=logic.student.my_error_give.my_give(id2)
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

def get_number_from_label(label):
    # Tách chuỗi và lấy phần đầu tiên
    try:
        number = int(label.split('.')[0].strip())
        return number
    except:
        return 0

def find_selected_numbers(checkboxes):
    # Làm phẳng list nếu cần
    flat_checkboxes = []
    for item in checkboxes:
        if isinstance(item, list):
            flat_checkboxes.extend(item)
        else:
            flat_checkboxes.append(item)
    
    # Tìm và chuyển đổi số từ các label được chọn
    numbers = []
    for checkbox in flat_checkboxes:
        if checkbox.value:
            num = get_number_from_label(checkbox.label)
            numbers.append(num)
    
    return numbers

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
    for i in t3:
        t8=data_py.find_user(i)
        row3.append(
            ft.Checkbox(label=str(t8["id"])+" ."+t8["name"], value=False)
        )

    page.title = "Lớp trưởng"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1100
    page.window.height = 770
    # page.window.full_screen=True
    page.window.resizable = False
    page.window.maximizable=False
    page.window.center()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        controls=[
                            ft.Text(f"Xin chào lớp trưởng {data_py.find_user(id1).get('name')}", size=20)
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
                            ft.Button(text="Tổng kết", width=100, on_click=lambda e: page.go("/summary")),
                            ft.Button(text="Xoá lỗi / điểm cộng", width=100, on_click=lambda e: page.go("/remove")),
                            ft.Button(text="Thoát", width=100, on_click=lambda e: page.window.destroy())
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                ]
            ))
        if page.route == "/remove":
            row4 = []
            t7 = ft.Column(
                controls=row4,
                scroll=ft.ScrollMode.ALWAYS,
                width=300,
                height=650,
                visible=False
            )

            def click1(e):
                t13=find_selected_numbers(row3)
                t14=data_py.team.read_mainfile()['idteam']
                t15=find_selected_numbers(row4)
                idt=0
                for i in t14:
                    if t13[-1] in data_py.team.read_teamfile(i['id_team'])['members']:
                        idt=data_py.team.read_teamfile(i['id_team'])['teamleider_id']
                # print(text1['textField'])
                for i in range(int(text1.value)):
                    t=logic.team.remove.remove_error(idt, t13[-1], t15[-1])
                    print(t)

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
                    t4 = find_selected_numbers(row3)
                    t6 = list2("error", int(t4[-1]))
                    row4.clear()
                    for i in t6:
                        row4.append(
                            ft.Checkbox(label=str(i["id"]) + "." + i["name"] + ", Số lần: " + str(i["count"]), value=False)
                        )
                    if not row4:  # Nếu không có lỗi nào
                        row4.append(ft.Text(value="Không có lỗi nào / Điểm cộng"))
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



            page.views.append(
                ft.View(
                    "/remove",
                    [
                        ft.AppBar(title=ft.Text("Xoá lỗi / điểm cộng"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=row3,
                                    scroll=ft.ScrollMode.ALWAYS,
                                    width=200,
                                    height=650
                                ),
                                t7,
                                t9
                            ],
                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ]
                )
            )
        if page.route == "/summary":
            page.views.append(
                ft.View(
                    "/summary",
                    [
                        ft.AppBar(title=ft.Text("Tổng kết"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Text(value="Hello, World!")
                    ]
                )
            )
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
    page.go(page.route)
def __init__(id):
    global id1
    id1=id
    ft.app(target=gui)