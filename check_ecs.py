import boto3

import sys

import argparse

def check_ecs_running_tasks(cluster_name):

    ecs_client = boto3.client("ecs")

    response = ecs_client.list_tasks(

        cluster=cluster_name,

        desiredStatus="RUNNING"

    )

    running_tasks = response.get("taskArns", [])

    if running_tasks:

        print(f"Running tasks found: {running_tasks}")

        sys.exit(1)

    else:

        print("No running tasks found.")




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Check ECS running tasks")

    parser.add_argument("--cluster_name", type=str, help="The name of the ECS cluster")

    args = parser.parse_args()

    check_ecs_running_tasks(args.cluster_name)
