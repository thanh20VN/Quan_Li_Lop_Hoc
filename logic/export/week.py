from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import data_py

def __init__(data1):
    t=data_py.team.read_mainfile()
    wb = Workbook()
    # Remove default sheet
    wb.remove(wb.active)

    # Process each team in a separate sheet
    for team_id, team_data in data1.items():
        name=""
        for i in t["idteam"]:
            # print(i)
            if str(i["id_team"]) == team_id:
                name=str(i["name"])[0].upper()+str(i["name"])[1:]
        # Create new sheet for team
        # print(name)
        ws = wb.create_sheet(name)
        
        # Styles
        header_font = Font(bold=True)
        header_fill = PatternFill(fill_type='solid', start_color='CCE5FF')
        center_align = Alignment(horizontal='center')
        border = Border(left=Side(style='thin'), right=Side(style='thin'),
                       top=Side(style='thin'), bottom=Side(style='thin'))

        # Headers
        headers = ['Mã học sinh', 'Họ và tên', 'Điểm cộng', 'Điểm trừ', 'Tổng điểm', 'Xếp loại', 'Hạng']
        
        # Sort students by total points for ranking
        sorted_students = sorted(
            [(student_id, student) for student_id, student in team_data.items()],
            key=lambda x: x[1]['total'],
            reverse=True
        )
        
        # Assign ranks
        base_rank = 1
        prev_total = None
        ranks = {}
        for student_id, student in sorted_students:
            if prev_total is None or student['total'] != prev_total:
                ranks[student_id] = base_rank
            else:
                ranks[student_id] = ranks[prev_student_id]
            base_rank += 1
            prev_total = student['total']
            prev_student_id = student_id

        # Write headers
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col)
            cell.value = header
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = center_align
            cell.border = border
            
        # Write student data
        current_row = 2
        for idx, (student_id, student) in enumerate(team_data.items(), 1):
            # Mã học sinh
            ws.cell(row=current_row, column=1, value=student_id)
            # Student data
            ws.cell(row=current_row, column=2, value=student['name'])
            ws.cell(row=current_row, column=3, value=student['give'])
            ws.cell(row=current_row, column=4, value=student['error'])
            ws.cell(row=current_row, column=5, value=student['total'])
            ws.cell(row=current_row, column=6, value=student['ratings'])
            ws.cell(row=current_row, column=7, value=ranks[student_id])
            
            # Style cells
            for col in range(1, 8):
                cell = ws.cell(row=current_row, column=col)
                cell.alignment = center_align
                cell.border = border
            
            current_row += 1

        # Auto-adjust columns for this sheet
        for col in range(1, 8):
            max_length = 0
            column_letter = get_column_letter(col)
            for row in ws.rows:
                cell = row[col-1]
                try:
                    if cell.value:
                        max_length = max(len(str(cell.value)), max_length)
                except:
                    pass
            ws.column_dimensions[column_letter].width = max_length + 2

    wb.save('week.xlsx')
    return 'week.xlsx'
