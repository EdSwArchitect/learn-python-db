import psycopg2
import psycopg2.extras
import json

from db_learning.configuration import get_db_config

def main():
    try:
        config = get_db_config('./data/config.json')

        conn = psycopg2.connect(f"dbname={config['dbName']} user={config['user']} password={config['token']} host={config['host']} port={config['port']}")

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            try:
                cursor.execute("SELECT version()")
                single_row = cursor.fetchone()

                print(f"{single_row}")

                cursor.execute("SELECT count(*) FROM edwin_table")

                single_row = cursor.fetchone()

                print(f"The current edwin_table count: {single_row}")

                cursor.execute("SELECT id, first_name, last_name, created_at, updated_at, data FROM edwin_table")

                many_rows = cursor.fetchall()

                print(f"The current edwin_table: {many_rows}")

                for row in many_rows:
                    print(f"Length: {len(row)}. Type of of row {type(row)}")
                    print(f"Keys are: {row.keys()}")

                    for key in row.keys():
                        print(f"Key: {key} Value: {row[key]}")

                    # print(f"{row}")
                    print("---------")

                upsert_stmt = """insert into edwin_table (id, first_name, last_name, created_at, updated_at, data)
                VALUES ('edwin.k.brown', 'Ed', 'Brown', current_timestamp, current_timestamp, 
                'This is the current way of how we do it') ON CONFLICT (id) DO UPDATE 
                SET first_name = EXCLUDED.first_name, updated_at = current_timestamp, 
                data = 'This is the current way of how we do it' 
                """

                cursor.execute(upsert_stmt)

                conn.commit()

            except psycopg2.OperationalError as err:
                print(f"I am unable to connect to the database. {err=}")
            except psycopg2.DatabaseError as err:
                print(f"Some database error. {err=}")

    except psycopg2.OperationalError as err:
        print(f"I am unable to connect to the database. {err=}")
    except psycopg2.DatabaseError as err:
        print(f"Some database error. {err=}")
    except json.decoder.JSONDecodeError as err:
        print(f"Error processing JSON config file. {err=}")
    except FileNotFoundError as err:
        print(f"Error file not found. {err=}")

if __name__ == "__main__":
    main()