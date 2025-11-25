def estimate_ec2_cost(instance_type):
    pricing = {
        "t2.micro": 0.0116,
        "t3.medium": 0.0416,
        "m5.large": 0.096
    }
    return pricing.get(instance_type, 0.05)


def analyze_instances(instances):
    results = []
    total_cost = 0

    for inst in instances:
        cost = estimate_ec2_cost(inst['type'])
        total_cost += cost

        results.append({
            "InstanceId": inst["id"],
            "Type": inst["type"],
            "State": inst["state"],
            "EstimatedCostPerHour": cost
        })

    return results, total_cost
