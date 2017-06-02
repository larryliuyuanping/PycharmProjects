# -*- coding: utf-8 -*-

import datetime

from maiziserver.utils.logger import logger as log
from maiziserver.db.api.apiutils import APIResult, dec_make_conn_cursor

def list_career_can_use():

    @dec_make_conn_cursor
    def main(conn, cursor):

        sql = """
                select id,
                        name,
                        type,
                        case type
                        when 0 then '线上'
                        else '线下'
                        end as type_name,
                        remark,
                        is_delete
                from mz_server_career
                where is_delete = 0
                """

        try:
            cursor.execute(sql)
            info = cursor.fetchall()
            log.info("db execute: " + cursor._last_executed)
        except Exception as e:
            raise e

        result_dict = {
            "result": info,
        }

        return APIResult(result=result_dict)

    return main()

def list_career():

    @dec_make_conn_cursor
    def main(conn, cursor):

        sql = """
                select id,
                        name,
                        type,
                        case type
                        when 0 then '线上'
                        else '线下'
                        end as type_name,
                        remark,
                        is_delete,
                        case is_delete
                        when 0 then '正常'
                        else '禁用'
                        end as state
                from mz_server_career
                """

        try:
            cursor.execute(sql)
            info = cursor.fetchall()
            log.info("db execute: " + cursor._last_executed)
        except Exception as e:
            raise e

        result_dict = {
            "result": info,
        }

        return APIResult(result=result_dict)

    return main()

def get_career_by_id(career_id):

    @dec_make_conn_cursor
    def main(conn, cursor):
        sql = """
                select id,
                        name,
                        type,
                        case type
                        when 0 then '线上'
                        else '线下'
                        end as type_name,
                        remark,
                        is_delete
                from mz_server_career
                where id=%s
                """

        try:
            cursor.execute(sql, (career_id,))
            info = cursor.fetchone()
            log.info("db execute: " + cursor._last_executed)
        except Exception as e:
            raise e

        return APIResult(result=info)

    return main()


def start(career_id):

    @dec_make_conn_cursor
    def main(conn, cursor):
        sql = """
                update mz_server_career
                set is_delete = 0
                where id=%s
                """
        try:
            cursor.execute(sql, (career_id,))
            conn.commit()
            log.info("db execute: " + cursor._last_executed)
        except Exception as e:
            raise e

        return APIResult(result=True)

    return main()

def stop(career_id):

    @dec_make_conn_cursor
    def main(conn, cursor):
        sql = """
                update mz_server_career
                set is_delete = 1
                where id=%s
                """

        try:
            cursor.execute(sql, (career_id,))
            conn.commit()
            log.info("db execute: " + cursor._last_executed)
        except Exception as e:
            raise e

        return APIResult(result=True)

    return main()

def add(name,type,remark):

    @dec_make_conn_cursor
    def main(conn, cursor):
        sql = """
                insert into mz_server_career(name,
                            type,
                            remark)
                values (%s,%s,%s)
                """

        try:
            cursor.execute(sql, (name, type, remark,))
            conn.commit()
            log.info("db execute: " + cursor._last_executed)
        except Exception as e:
            raise e

        return APIResult(result=True)

    return main()

def update(career_id,name,type,remark):

    @dec_make_conn_cursor
    def main(conn, cursor):
        sql = """
                update mz_server_career set
                            name=%s,
                            type=%s,
                            remark=%s
                where id =%s
                """

        try:
            cursor.execute(sql, ( name, type, remark, career_id,))
            conn.commit()
            log.info("db execute: " + cursor._last_executed)
        except Exception as e:
            raise e

        return APIResult(result=True)

    return main()