import mysql.connector


class DatabaseConnection:
    def __init__(self):
        self.db_connector_obj = None
        self.connection_cursor = None
        try:
            self.db_connector_obj = mysql.connector.connect(
                host='localhost',
                port="3307",
                user="root",
                password="password",
                database="db"
            )
            self.connection_cursor = self.db_connector_obj.cursor()
        except mysql.connector.Error as error:
            print(f"Error while connecting to mysql: {error}")

    # def get_connection(self):
    #     # get the connection
    #     connection = DatabaseConnection()
    #     return connection

    def execute_query(self, query, values=None):
        if self.db_connector_obj.is_connected() and self.connection_cursor:
            try:
                self.connection_cursor.execute(query, values)

                # self.db_connector_obj.commit()
                print(self.connection_cursor)
                # in order to get the result / results from curser
                return [True, ""]
            except mysql.connector.Error as err:
                print(f"Error while executing : {err}")
                return [False, f"Error while executing : {err}"]

    def commit_query(self):
        self.db_connector_obj.commit()

    def get_result_rows(self):
        return self.connection_cursor.fetchall()

    def close_connection(self):
        if self.db_connector_obj.is_connected():
            self.connection_cursor.close()
            self.db_connector_obj.close()
