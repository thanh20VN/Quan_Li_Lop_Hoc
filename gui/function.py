import data_py
import logic
import config

def list1(type,id1):
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

def find_selected_text(checkboxes):
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
            num = checkbox.label
            numbers.append(num)
    
    return numbers

def get_number_from_week_label(label):
    try:
        # Tách chuỗi theo khoảng trắng và lấy phần số
        week_num = label.split()[-1]  # Lấy phần cuối "01" hoặc "10"
        return int(week_num)  # Chuyển thành số
    except:
        return 0

def find_selected_numbers_end(checkboxes):
    # Làm phẳng list nếu cần
    flat_checkboxes = []
    for item in checkboxes:
        if isinstance(item, list):
            flat_checkboxes.extend(item)
        else:
            flat_checkboxes.append(item)
    
    # Tìm và lấy số tuần từ label của các checkbox được chọn
    numbers = []
    for checkbox in flat_checkboxes:
        if checkbox.value:
            week_num = get_number_from_week_label(checkbox.label)
            numbers.append(week_num)
    
    return numbers