import json

with open("config.json", "r", encoding="utf-8") as f:
    config_data = json.load(f)

semester_1=config_data["semester_1"]
semester_2=config_data["semester_2"]
semester_total=semester_1+semester_2
roles = config_data["roles"]
default_point=config_data["default_point"]
not_achieved=config_data["Not achieved"]
achieved=config_data["Achieved"]
medium=config_data["Medium"]
rather=config_data["Rather"]
good=config_data["Good"]
very_good=config_data["Very good"]
super_good=config_data["Super good"]