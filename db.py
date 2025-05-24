from supabase import create_client, Client

# Supabase config
url = "https://bryvofhvnlgvxrweqqxs.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJyeXZvZmh2bmxndnhyd2VxcXhzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc5MDcwNjIsImV4cCI6MjA2MzQ4MzA2Mn0.suR1EQyOs9mG5_CNcKWPjRLQVNFx2a0y2szKMGn48WE"

supabase: Client = create_client(url, key)

def save_product(link: str, caption: str):
    data = {
        "link": link,
        "caption": caption
    }
    try:
        response = supabase.table("products").insert(data).execute()
        return response
    except Exception as e:
        return f"❌ DB error: {str(e)}"

def get_all_products():
    try:
        response = supabase.table("products").select("*").execute()
        return response.data
    except Exception as e:
        return f"❌ Fetch error: {str(e)}"

