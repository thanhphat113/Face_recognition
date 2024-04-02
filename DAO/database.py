import mysql.connector

def connect_to_database():
    # Thực hiện kết nối đến cơ sở dữ liệu MySQL
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="PhongKhamThuY"
        )
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to the database: {}".format(error))
        return None

def close_connection(connection):
    # Đóng kết nối đến cơ sở dữ liệu
    if connection:
        connection.close()
        print("Connection closed")

def execute_query(connection, query):
    # Thực thi truy vấn và trả về kết quả (nếu có)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as error:
        print("Error executing query: {}".format(error))
        return None
    
def insert_data(connection, query):
    # Thêm dữ liệu vào bảng
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as error:
        print("Error inserting data: {}".format(error))
