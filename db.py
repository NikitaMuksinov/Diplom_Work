import psycopg2
from Diplom_Work.config import DB_CONFIG


def get_system_data():
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM system_info ORDER BY timestamp DESC")
            rows = cursor.fetchall()
    return rows


def save_system_info(system_info):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO system_info (computer_name, user_name, os_version, ip_addresses, running_processes, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
                system_info['computer_name'],
                system_info['user_name'],
                system_info['os_version'],
                ", ".join(system_info['ip_addresses']),
                ", ".join(system_info['running_processes']),
                system_info['timestamp']
            ))
        conn.commit()
