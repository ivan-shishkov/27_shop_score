from datetime import datetime, timedelta, time

from pytz import timezone, utc

from db import db_session, Order


def get_local_datetime_now(timezone_name='Europe/Moscow'):
    return utc.localize(datetime.utcnow()).astimezone(
        timezone(timezone_name),
    ).replace(tzinfo=None)


def get_unprocessed_orders_info(shop_datetime_now):
    unprocessed_orders_query = db_session.query(Order).filter(
        Order.confirmed.is_(None),
    ).order_by(Order.id)

    unprocessed_orders_count = unprocessed_orders_query.count()

    if unprocessed_orders_count > 0:
        most_waited_order = unprocessed_orders_query.first()
        max_wait_time = shop_datetime_now - most_waited_order.created
    else:
        max_wait_time = timedelta()

    return {
        'max_wait_time': round(max_wait_time.total_seconds()),
        'unprocessed_orders_count': unprocessed_orders_count,
    }


def get_today_processed_orders_count(shop_datetime_now):
    shop_datetime_today_begin = datetime.combine(
        shop_datetime_now.date(),
        time.min,
    )
    return db_session.query(Order).filter(
        Order.confirmed >= shop_datetime_today_begin,
    ).count()


def get_processed_orders_info(shop_datetime_now):
    today_processed_orders_count = get_today_processed_orders_count(
        shop_datetime_now,
    )
    return {
        'today_processed_orders_count': today_processed_orders_count
    }


def get_orders_processing_info():
    shop_datetime_now = get_local_datetime_now()

    orders_processing_info = get_unprocessed_orders_info(shop_datetime_now)
    orders_processing_info.update(get_processed_orders_info(shop_datetime_now))

    return orders_processing_info
