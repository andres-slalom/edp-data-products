from datetime import datetime


def build_dag_metadata():
    return {
        "dag_id": "sample_ingestion_dag_v2",
        "schedule": "@daily",
        "start_date": datetime(2026, 1, 1).isoformat(),
    }


if __name__ == "__main__":
    print(build_dag_metadata())
