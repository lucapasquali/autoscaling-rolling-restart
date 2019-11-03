import boto3
import sys
import time

kinesis_client = boto3.client('autoscaling')
autoscaling_group_name = sys.argv[1]

# describing the autoscaling group obtained in input
auto_scaling_group_response = client.describe_auto_scaling_groups(
    AutoScalingGroupNames=[
        autoscaling_group_name,
    ],
)

# iterate for each instance in the autoscaling group
for i in auto_scaling_group_response['AutoScalingGroups']['Instances']:
    printf("Destroying instance %s\n", auto_scaling_group_response['AutoScalingGroups']['Instances'][i]['InstanceId'])

    # destroying instance in autoscaling group
    # the destruction forces the replacement of the instance
    scaling_activity_response = client.terminate_instance_in_auto_scaling_group(
        InstanceId=auto_scaling_group_response['AutoScalingGroups']['Instances'][i]['InstanceId'],
        ShouldDecrementDesiredCapacity=False
    )

    # Checking the status of the auto scaling activity
    while true:
        scaling_activity_status_response = client.describe_scaling_activities(
            ActivityIds=[
                scaling_activity_response['Activity']['ActivityId'],
            ],
            AutoScalingGroupName=autoscaling_group_name,
            )
        if scaling_activity_status_response['Activities'][0]["StatusCode"] == 'Successful':
            print("Creation of Instance successful, proceeding with the next one\n")
            break
        elif scaling_activity_status_response['Activities'][0]["StatusCode"] == 'Failed':
            print("Creation of Instance failed, exiting\n")
            sys.exit(1)
        else:
            print("Creation of instance in %s status, waiting 10 seconds\n", scaling_activity_status_response['Activities'][0]["StatusCode"])
            time.sleep(10)
