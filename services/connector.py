import pypyodbc


class connector:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pypyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-HEDK6J9\MSSQLSERVER01;'
                              'Database=my_db;'
                              'Trusted_Connection=yes;')

        self.cursor = self.conn.cursor()

    def get_channels(self):
        list_channels = []
        channels = self.cursor.execute('SELECT * FROM channels')
        for i in channels:
            list_channels.append(i)
        return list_channels

    def get_packages(self):
        list_channels = []
        packages = self.cursor.execute('SELECT * FROM package')
        for i in packages:
            list_channels.append(i)
        return list_channels

    def put_package(self, type, price, channels_list):
        put_pack = self.cursor.execute(f"insert into package (subscription_type, price, channels_list) values ('{type}', {price}, '{channels_list}');")
        self.conn.commit()
        return put_pack

