import argparse
import boto3
import sys
def scale_ecs_service(cluster_name, service_name, desired_count):
    ecs_client = boto3.client("ecs")
    try:
        response = ecs_client.update_service(
            cluster=cluster_name,
            service=service_name,
            desiredCount=desired_count
        )
        print(f"Successfully scaled service {service_name} to {desired_count}.")
    except Exception as e:
        print(f"Failed to scale service: {str(e)}")
        sys.exit(1)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scale ECS service")
    parser.add_argument("--cluster_name", type=str, required=True, help="The name of the ECS cluster")
    parser.add_argument("--service_name", type=str, required=True, help="The name of the ECS service")
    parser.add_argument("--desired_count", type=int, required=True, help="The desired count of tasks")
    args = parser.parse_args()
    scale_ecs_service(args.cluster_name, args.service_name, args.desired_count)
