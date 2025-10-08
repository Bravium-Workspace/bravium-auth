def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "password_hash": user["password_hash"],
        "created_at": user["created_at"]
    }
