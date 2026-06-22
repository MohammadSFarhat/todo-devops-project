output "staging_public_ip" {
  description = "Public IP address of the staging EC2 server"
  value       = aws_instance.staging_server.public_ip
}

output "ssh_command" {
  description = "SSH command to connect to the staging server"
  value       = "ssh -i todo-devops-key.pem ubuntu@${aws_instance.staging_server.public_ip}"
}

output "frontend_url" {
  description = "Frontend application URL"
  value       = "http://${aws_instance.staging_server.public_ip}"
}

output "backend_url" {
  description = "Backend API URL"
  value       = "http://${aws_instance.staging_server.public_ip}:5000"
}

output "jenkins_url" {
  description = "Jenkins URL"
  value       = "http://${aws_instance.staging_server.public_ip}:8080"
}