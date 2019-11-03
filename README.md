# autoscaling-rolling-restart
script to implement rolling restart for an autoscaling group in AWS

### Prerequisites

- Python 3
- AWS CLI (the script will use the default profile and default region configured for the CLI)

### Usage

This script accepts in input the autoscaling group name and does a rolling replacement of the instances within the autoscaling group one by one.
This is just a prototype and there is not much error handling.

```
python rolling_restart.py <ASG name>
```
