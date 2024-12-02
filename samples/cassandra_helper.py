from cassandra.cluster import Cluster

class CassandraHelper:
    def __init__(self, contact_points, keyspace):
        self.contact_points = contact_points
        self.keyspace = keyspace
        self.cluster = None
        self.session = None

    def connect(self):
        self.cluster = Cluster(self.contact_points)
        self.session = self.cluster.connect(self.keyspace)

    def disconnect(self):
        if self.session:
            self.session.shutdown()
        if self.cluster:
            self.cluster.shutdown()

    def create(self, table, data):
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.session.execute(query)

    def read(self, table, columns='*', condition=None):
        query = f"SELECT {columns} FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        return self.session.execute(query)

    def update(self, table, updates, condition):
        set_clause = ', '.join(f"{k}='{v}'" for k, v in updates.items())
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        self.session.execute(query)

    def delete(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        self.session.execute(query)