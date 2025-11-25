resource "aws_s3_bucket" "logs" {
  bucket = "${var.project_name}-logs-${random_id.suffix.hex}"

  tags = {
    Project = var.project_name
  }
}

resource "random_id" "suffix" {
  byte_length = 4
}
