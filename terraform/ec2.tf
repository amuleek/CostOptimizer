resource "aws_instance" "app_server" {
  ami           = "ami-0fc5d935ebf8bc3bc" # Amazon Linux 2023
  instance_type = "t2.micro"

  iam_instance_profile = aws_iam_instance_profile.instance_profile.name

  tags = {
    Name = "${var.project_name}-server"
  }
}

resource "aws_iam_instance_profile" "instance_profile" {
  name = "${var.project_name}-instance-profile"
  role = aws_iam_role.cost_analyzer_role.name
}
