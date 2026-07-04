from .supabase_client import supabase

def read_egfile(t):
    if t == "g":
        response = (
            supabase.table("give")
            .select("*")
            .execute()
        )
        return response.data
    if t == "e":
        response = (
            supabase.table("error")
            .select("*")
            .execute()
        )
        return response.data