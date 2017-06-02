# -*- coding: utf-8 -*-

import datetime

from maiziserver.utils.logger import logger as log
from maiziserver.db.api.apiutils import APIResult, dec_make_conn_cursor

def list_exercise_type(exercise_type):

    @dec_make_conn_cursor
    def main(conn, cursor):

        sql = """
                select id,
                        exercise_type
                from mz_server_exercise_type
                where (exercise_type like  %s or %s ='')
                """

        try:
            cursor.execute(sql,('%' + exercise_type + '%',
                                exercise_type,))
            info = cursor.fetchall()
            print(cursor._last_executed)
        except Exception as e:
            print (e)
            raise e

        result_dict = {
            "result": info,
        }

        return APIResult(result=result_dict)

    return main()

def get_exercise_type_by_id(exercise_type_id):

    @dec_make_conn_cursor
    def main(conn, cursor):
        sql = """
                select id,
                        exercise_type
                from mz_server_exercise_type
                where id=%s
                """

        try:
            cursor.execute(sql, (exercise_type_id,))
            info = cursor.fetchone()
        except Exception as e:
            raise e

        return APIResult(result=info)

    return main()


def add(exercise_type):

    @dec_make_conn_cursor
    def main(conn, cursor):
        sql = """
                insert into mz_server_exercise_type(exercise_type)
                values (%s)
                """

        try:
            cursor.execute(sql, (exercise_type,))
            conn.commit()

        except Exception as e:
            raise e

        return APIResult(result=True)

    return main()

def update(exercise_type_id,exercise_type):

    @dec_make_conn_cursor
    def main(conn, cursor):
        sql = """
                update mz_server_exercise_type set
                            exercise_type=%s
                where id =%s
                """

        try:
            cursor.execute(sql, (exercise_type, exercise_type_id,))
            conn.commit()
        except Exception as e:
            raise e

        return APIResult(result=True)

    return main()