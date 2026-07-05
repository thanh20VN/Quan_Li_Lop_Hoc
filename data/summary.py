import json
from .supabase_client import supabase


def write(teamleider_id, data, type, class_id=None):
    if type not in ["week", "semester", "year"]:
        return "Invalid type. Must be 'week', 'semester', or 'year'."

    payload = json.dumps(data, ensure_ascii=False) if isinstance(data, dict) else data

    if type == "week":
        supabase.table("summary").insert({
            "team_id": teamleider_id,
            "type": type,
            "payload": payload,
            "class_id": class_id
        }).execute()
    else:
        existing = (
            supabase.table("summary")
            .select("id")
            .eq("team_id", teamleider_id)
            .eq("type", type)
            .execute()
        )
        if existing.data:
            supabase.table("summary").update({
                "payload": payload,
                "class_id": class_id
            }).eq("id", existing.data[0]["id"]).execute()
        else:
            supabase.table("summary").insert({
                "team_id": teamleider_id,
                "type": type,
                "payload": payload,
                "class_id": class_id
            }).execute()


def read(teamleider_id, type, summary_num=None):
    if type not in ["week", "semester", "year"]:
        return "Invalid type. Must be 'week', 'semester', or 'year'."

    if type == "year":
        response = (
            supabase.table("summary")
            .select("payload")
            .eq("type", "year")
            .limit(1)
            .execute()
        )
        if not response.data:
            return None
        payload = response.data[0]["payload"]
        return json.loads(payload) if isinstance(payload, str) else payload

    response = (
        supabase.table("summary")
        .select("payload")
        .eq("team_id", teamleider_id)
        .eq("type", type)
        .execute()
    )

    if not response.data:
        return None

    if summary_num is not None:
        for item in response.data:
            payload = item["payload"]
            if isinstance(payload, str):
                payload = json.loads(payload)
            if isinstance(payload, dict) and payload.get(type) == summary_num:
                return payload

    payload = response.data[-1]["payload"]
    return json.loads(payload) if isinstance(payload, str) else payload


def read_main(type):
    counter_type = f"{type}_counter"
    response = (
        supabase.table("summary")
        .select("payload")
        .eq("type", counter_type)
        .limit(1)
        .execute()
    )
    if response.data:
        payload = response.data[0]["payload"]
        if isinstance(payload, str):
            try:
                return json.loads(payload)
            except Exception:
                pass
        if isinstance(payload, dict):
            return payload
    return {"num": 0}


def create(type, id_class=None):
    if type not in ["week", "semester", "year"]:
        return "Invalid type. Must be 'week', 'semester', or 'year'."

    counter_type = f"{type}_counter"
    main = read_main(type)
    new_num = main.get("num", 0) + 1

    counter_data = {"num": new_num}

    existing = (
        supabase.table("summary")
        .select("id")
        .eq("type", counter_type)
        .limit(1)
        .execute()
    )
    if existing.data:
        supabase.table("summary").update({
            "payload": counter_data,
            "class_id": id_class
        }).eq("id", existing.data[0]["id"]).execute()
    else:
        supabase.table("summary").insert({
            "type": counter_type,
            "payload": counter_data,
            "class_id": id_class
        }).execute()

    return new_num


def list_summaries(teamleider_id, type):
    response = (
        supabase.table("summary")
        .select("payload")
        .eq("team_id", teamleider_id)
        .eq("type", type)
        .execute()
    )
    result = {}
    if response.data:
        for idx, item in enumerate(response.data, 1):
            payload = item["payload"]
            if isinstance(payload, str):
                payload = json.loads(payload)
            result[idx] = payload
    return result


def check(teamleider_id, type, summary_id):
    if type not in ["week", "semester", "year"]:
        return False

    response = (
        supabase.table("summary")
        .select("id")
        .eq("team_id", teamleider_id)
        .eq("type", type)
        .execute()
    )
    return len(response.data) > 0


def remove(teamleider_id, type):
    if type not in ["week", "semester", "year"]:
        return "Invalid type. Must be 'week', 'semester', or 'year'."
    supabase.table("summary").delete().eq("team_id", teamleider_id).eq("type", type).execute()
    return "Xoá thành công."
