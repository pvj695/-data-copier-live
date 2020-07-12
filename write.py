
from utils import get_mysql_connection


def build_insert_query(table_name, column_names):
    column_values = tuple(map(lambda column:column.replace(column,'%s'),column_names))
    column_values_s = ','.join(column_values)
    column_names_s = ','.join(column_names)
    query = f'''INSERT INTO {table_name} ({column_names_s}) VALUES ({column_values_s})'''
    return query

def insert_data(db_details,query,data,batchsize=100):

    SOURCE_DB = db_details['SOURCE_DB']

    connection = get_mysql_connection(db_host=SOURCE_DB["DB_HOST"],
                                      db_name=SOURCE_DB["DB_NAME"],
                                      db_user=SOURCE_DB["DB_USER"],
                                      db_pass=SOURCE_DB["DB_PASS"],
                                      )
    cursor = connection.cursor()

    records = []
    count =1
    for record in data:
        records.append(record)
        if count % batchsize == 0:
            cursor.executemany(query,records)
            connection.commit()
            recs = []
        count = count+1

    cursor.executemany(query, records)

    connection.commit()

    print(cursor.rowcount, "record inserted.")

    connection.close()

    return