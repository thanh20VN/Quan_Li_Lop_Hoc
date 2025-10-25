import flet as ft
import data_py
import logic

# from ..data import data_py
# from ..logic import logic

# from data_py as data_py
# from logic as logic

id1=0
column=["ID","Lỗi vi phạm","Điểm trừ / cộng","Số lần"]
y123=0

def check_single_true(checkboxes): 
    if isinstance(checkboxes[0], list):
        flat_list = [item for sublist in checkboxes for item in sublist]
        return sum(1 for cb in flat_list if cb.value) == 1
    return sum(1 for cb in checkboxes if cb.value) == 1

def mutil1(checkboxes): 
    if isinstance(checkboxes[0], list):
        flat_list = [item for sublist in checkboxes for item in sublist]
        return sum(1 for cb in flat_list if cb.value) >0
    return sum(1 for cb in checkboxes if cb.value) >0

def find_checkbox(checkboxes):
    flat_checkboxes = []
    for item in checkboxes:
        if isinstance(item, list):
            flat_checkboxes.extend(item)
        else:
            flat_checkboxes.append(item)
    
    # Tìm checkbox được chọn và trả về label
    for checkbox in flat_checkboxes:
        if checkbox.value:
            return checkbox.label
    
    return None

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

t1=[]
t2=[]
row1=[]
row2=[]
def gui(page: ft.Page):
    def up2():
        global t1
        global t2
        t2=[]
        t1=[]
        return [list1("give"),list1("error")]
    def up3():
        tt=up2()
        global t1, t2
        for i in tt:
            if t1==[]:t2=i
            else:t1=i
        # print(t1,t2)
    up3()
    def up1():
        global row1, row2
        row1=[]
        row2=[]
        for i in t1:
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
        for i in t2:
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
    up1()
    # print(row1)
    # print(row2)
    def up(): global row2; row2=[]; up3(); up1(); page.update()
    row4=[]
    for i in data_py.team.read_teamfile(id1)["members"]:
        t8=data_py.find_user(i)
        row4.append(
            ft.Checkbox(label=str(t8["id"])+" ."+t8["name"], value=False)
        )
    page.title = "Tổ trưởng"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1100
    page.window.height = 770
    page.scroll = ft.ScrollMode.AUTO
    page.window.maximizable=False
    page.window.resizable=False
    page.window.center()

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
                            ft.Button(text="Thêm vi phạm", width=150, height=50, on_click=lambda e: page.go("/error")),
                            ft.Button(text="Thêm điểm cộng", width=150, height=50, on_click=lambda e: page.go("/give")),
                            ft.Button(text="Thoát", width=100, height=50, on_click=lambda e: page.window.destroy())
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ])
        )
        if page.route == "/error":
            def click(e):
                t6=find_checkbox(row3)
                t7=find_selected_numbers(row4)
                for i in t7:
                    for j in range(int(t0.value)):
                        # print(id1, i, int(t6[0:2]))
                        t9=logic.team.add.add_error(id1, i, int(t6[0:2]))
                        if t9==True: up(); page.go("/")
                        
            row3=[]
            for i in data_py.eg.read_egfile("e")["errors"]:
                row3.append(
                    ft.Checkbox(label=str(i["id"])+" ."+i["name"], value=False)
                )
            row5=[]
            page.window.resizable = False
            t0=ft.TextField(label="Mấy lần", width=300, height=100, text_align=ft.TextAlign.LEFT)
            t3=ft.Button(text="Xác nhận", on_click=click, width=100, height=50, disabled=False)
            row5.append(t0)
            row5.append(t3)

            t4=ft.Column(
                controls=row4,
                alignment=ft.MainAxisAlignment.START,
                visible=False
            )

            t5=ft.Column(
                controls=row5,
                alignment=ft.MainAxisAlignment.START,
                visible=False
            )
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
                                t4,
                                t5
                            ]
                        ),
                    ],
                )
            )
            def on_checkbox_change(e):
                global y123
                is_valid = check_single_true(row3) 
                if t4.visible or y123!=0:
                    t5.visible = is_valid; y123=1
                if not t4.visible:
                    y123=0
                t4.visible = is_valid
                
                page.update()
            



            for checkbox in row3:
                checkbox.on_change = on_checkbox_change
            def check_true(e):
                # print(mutil1(row4))
                if mutil1(row4): t5.visible=True
                else: t5.visible=False
                page.update()
            page.update()
            for checkbox in row4:
                checkbox.on_change = check_true
            page.update()
        if page.route == "/give":
            def click(e):
                t6=find_checkbox(row3)
                t7=find_selected_numbers(row4)
                for i in t7:
                    for j in range(int(t0.value)):
                        # print(id1, i, int(t6[0:2]))
                        t9=logic.team.add.add_give(id1, i, int(t6[0:2]))
                        if t9==True: up(); page.go("/")
                        
            row3=[]
            for i in data_py.eg.read_egfile("g")["give"]:
                row3.append(
                    ft.Checkbox(label=str(i["id"])+" ."+i["name"], value=False)
                )
            row5=[]
            page.window.resizable = False
            t0=ft.TextField(label="Mấy lần", width=300, height=100, text_align=ft.TextAlign.LEFT)
            t3=ft.Button(text="Xác nhận", on_click=click, width=100, height=50, disabled=False)
            row5.append(t0)
            row5.append(t3)

            t4=ft.Column(
                controls=row4,
                alignment=ft.MainAxisAlignment.START,
                visible=False
            )

            t5=ft.Column(
                controls=row5,
                alignment=ft.MainAxisAlignment.START,
                visible=False
            )
            def on_checkbox_change(e):
                global y123
                is_valid = check_single_true(row3) 
                if t4.visible or y123!=0:
                    t5.visible = is_valid; y123=1
                if not t4.visible:
                    y123=0
                t4.visible = is_valid
                
                page.update()
            

            page.views.append(
                ft.View(
                    "/give",
                    [
                        ft.AppBar(title=ft.Text("Điểm cộng"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=row3
                                ),
                                t4,
                                t5
                            ]
                        ),
                    ],
                )
            )


            for checkbox in row3:
                checkbox.on_change = on_checkbox_change
            def check_true(e):
                # print(mutil1(row4))
                if mutil1(row4): t5.visible=True
                else: t5.visible=False
                page.update()
            page.update()
            for checkbox in row4:
                checkbox.on_change = check_true
            page.update()
        page.update()
    # def view_pop(view):
    #     # print(page.views)
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)

    def view_pop(view):
        # Chỉ pop nếu còn view
        if page.views:
            page.views.pop()
        # Chỉ truy cập nếu còn view
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            # Nếu không còn view, có thể về trang chủ hoặc thoát
            page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    # print(row4[0:2],row3)
    
def __init__(page1,id):
    global id1
    id1=id
    gui(page1)

