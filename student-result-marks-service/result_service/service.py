from db.connection import get_connection
from exceptions import ResultCalculationException


def get_result(student_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT SUM(marks) as total_marks, AVG(marks) as average_marks FROM marks WHERE student_id=%s",
        (student_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result["average_marks"] is None:
        raise ResultCalculationException("No marks available")

    # decide pass or fail
    result_status = "Pass" if result["average_marks"] >= 40 else "Fail"

    return {
        "student_id": student_id,
        "total_marks": result["total_marks"],
        "average_marks": result["average_marks"],
        "result": result_status
    }