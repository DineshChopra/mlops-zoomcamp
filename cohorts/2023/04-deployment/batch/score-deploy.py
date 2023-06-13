from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule
from prefect.flow_runner import SubprocessFlowRunner
from datetime import timedelta

DeploymentSpec(
  flow_location='score-prefect.py',
  name='ride_duration_prediction',
  parameters={
    "taxi_type": "green",
    "run_id": "fe9c3b5aa055480fb3e605bce5be9b68"
  },
  schedule=CronSchedule(cron='30 11 * * *'), # 11:20 am everyday
  flow_runner=SubprocessFlowRunner(),
  tags=['ml']
)
