variable "aws_region" {
  description = "AWS region where the staging environment will be created"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type for the staging server"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "Name of the AWS key pair"
  type        = string
  default     = "todo-devops-key"
}

variable "public_key" {
  description = "Public SSH key used to access the EC2 server"
  type        = string
}

variable "allowed_ip" {
  description = "IP range allowed to access the staging server"
  type        = string
  default     = "0.0.0.0/0"
}