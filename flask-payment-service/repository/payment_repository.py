from db_config import get_db_connection

def process_payment(user_id, merchant_id, amount):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        conn.start_transaction()

        # Check user balance
        cursor.execute("SELECT balance FROM users WHERE user_id = %s", (user_id,))
        user = cursor.fetchone()

        if not user:
            return "User not found"

        if user[0] < amount:
            return "Insufficient balance"

        # Check merchant
        cursor.execute("SELECT merchant_id FROM merchants WHERE merchant_id = %s", (merchant_id,))
        merchant = cursor.fetchone()

        if not merchant:
            return "Merchant not found"

        # Deduct from user
        cursor.execute(
            "UPDATE users SET balance = balance - %s WHERE user_id = %s",
            (amount, user_id)
        )

        # Add to merchant
        cursor.execute(
            "UPDATE merchants SET balance = balance + %s WHERE merchant_id = %s",
            (amount, merchant_id)
        )

        conn.commit()
        return "Payment successful"

    except Exception as e:
        conn.rollback()
        return f"Payment failed: {str(e)}"

    finally:
        cursor.close()
        conn.close()