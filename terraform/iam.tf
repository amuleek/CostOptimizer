resource "aws_iam_role" "cost_analyzer_role" {
  name = "${var.project_name}-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_policy" "cost_analyzer_policy" {
  name        = "${var.project_name}-policy"
  description = "Read-only policy for Cloud Cost Analyzer"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow",
      Action = [
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes",
        "ec2:DescribeRegions",
        "s3:ListAllMyBuckets",
        "cloudwatch:GetMetricData",
        "cloudwatch:ListMetrics",
        "rds:DescribeDBInstances",
        "lambda:ListFunctions"
      ],
      Resource = "*"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "attach_policy" {
  role       = aws_iam_role.cost_analyzer_role.name
  policy_arn = aws_iam_policy.cost_analyzer_policy.arn
}
