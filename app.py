import sys
from config import DB_DETAILS
from utils import get_tables
from read import read_table
from write import build_insert_query,insert_data

def main():
    """Program takes atleast one argument"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    tables = get_tables('table_list')

    for table_name in tables['table_name']:
        print(table_name)

        data,column_names = read_table(db_details,table_name,10)

        query = build_insert_query('film_actor_target', column_names)

        insert_data(db_details, query, data, batchsize=100)


if __name__=='__main__':
    main()





