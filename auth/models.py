def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "password_hash": user["password_hash"],
        "created_at": user["created_at"]
    }
