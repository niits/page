from datetime import datetime, timedelta
import pandas as pd

from app import create_celery_app
from database import Request, DetectionTime, db
from detection.analyze import get_session_attributes

celery = create_celery_app()


def run_celery():
    celery.worker_main(['', '-B'])


@celery.task()
def detect_bots():
    print("Detection: ")
    df = pd.read_sql(Request.query.filter(Request.time > (
        datetime.now() - timedelta(hours=1))).statement, db.session.bind)

    aggregated_df = get_session_attributes(df)

    suspects = aggregated_df[
        (aggregated_df['std_dev_request_interarrival_time'] < 2)  |
        (aggregated_df['avg_request_interarrival_time'] < 2) |
        (aggregated_df['no_referrer_requests_ratio'] > 0.6)
    ]

    print(suspects['ip_address'].to_list())

    detetionTimes = [DetectionTime(host=ip_address)  for ip_address in suspects['ip_address'].to_list()]
    db.session.bulk_save_objects(detetionTimes)
    db.session.commit()
