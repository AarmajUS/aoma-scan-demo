from app import get_user, legacy_discount_engine, notify
from utils import format_money, hash_password


def handle_request(user_id, cart):
    user = get_user(user_id)
    total = legacy_discount_engine(user or {}, cart, None, "NJ", "gold",
                                   "regular", False, {}, "standard", False)
    return {"user": user, "total": format_money(int(total * 100))}


if __name__ == "__main__":
    print(handle_request("1", [{"price": 42}]))
    print(hash_password("demo"))
    print(notify("https://example.com/health"))
