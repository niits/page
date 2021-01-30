from datetime import datetime
import re
import pandas as pd


def get_session_attributes(df, aggregation_level="hour"):
    aggregation_levels = {"day": ["host", "date"],
                          "hour": ["host", "date", "hour"]}

    aggregation_columns = aggregation_levels[aggregation_level]

    df = df.sort_values(by=aggregation_columns + ["timestamp"], ascending=True)
    df["timestamp_previous"] = df.groupby(aggregation_columns)[
        "timestamp"].shift(1)

    df["timestamp_previous"] = df["timestamp_previous"].fillna(df["timestamp"])

    df["timestamp_previous"] = pd.to_datetime(df["timestamp_previous"])
    df["request_time_delta"] = (
        df["timestamp"] - df["timestamp_previous"]
    ).dt.total_seconds()

    aggregated_df = (
        df.groupby(aggregation_columns)
        .agg(
            number_requests_GET=pd.NamedAgg(
                column="request",
                aggfunc=(lambda req: (req.str.startswith("GET")).sum()),
            ),
            number_requests_HEAD=pd.NamedAgg(
                column="request",
                aggfunc=(lambda req: (req.str.startswith("HEAD")).sum()),
            ),
            number_requests_POST=pd.NamedAgg(
                column="request",
                aggfunc=(lambda req: (req.str.startswith("POST")).sum()),
            ),
            number_requests_no_referrer=pd.NamedAgg(
                column="referrer",
                aggfunc=(lambda req: (req.str.startswith("-")).sum()),
            ),
            number_requests_no_user_agent=pd.NamedAgg(
                column="user_agent",
                aggfunc=(lambda req: (req.str.startswith("-")).sum()),
            ),
            number_requests_has_user_agent_contains_phantom=pd.NamedAgg(
                column="user_agent",
                aggfunc=(lambda req: (req.str.contains("PhantomJS")).sum()),
            ),
            number_requests_total=pd.NamedAgg(
                column="request", aggfunc="count"),
            avg_request_interarrival_time=pd.NamedAgg(
                column="request_time_delta", aggfunc="mean"
            ),
        )
        .reset_index()
    )

    aggregated_df["HEAD_requests_ratio"] = (
        aggregated_df["number_requests_HEAD"] /
        aggregated_df["number_requests_total"]
    )
    aggregated_df["GET_requests_ratio"] = (
        aggregated_df["number_requests_GET"] /
        aggregated_df["number_requests_total"]
    )
    aggregated_df["POST_requests_ratio"] = (
        aggregated_df["number_requests_POST"] /
        aggregated_df["number_requests_total"]
    )
    aggregated_df["no_referrer_requests_ratio"] = (
        aggregated_df["number_requests_no_referrer"]
        / aggregated_df["number_requests_total"]
    )
    aggregated_df["no_user_agent_requests_ratio"] = (
        aggregated_df["number_requests_no_user_agent"]
        / aggregated_df["number_requests_total"]
    )
    aggregated_df["requests_has_user_agent_contains_phantom_ratio"] = (
        aggregated_df["number_requests_has_user_agent_contains_phantom"]
        / aggregated_df["number_requests_total"]
    )

    return aggregated_df
