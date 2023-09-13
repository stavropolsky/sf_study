variable "instance_family_image" {
  description = "Instance image"
  type        = string
  default     = "lamp"
}

variable "vpc_subnet_id" {
  description = "VPC subnet network id"
  type        = string
}

variable "vpc_subnet_zone" {
  description = "Zone of the VPC subnet"
  type        = string
}

variable "token" {
  description = "Token"
  type        = string
}

variable "cloud_id" {
  description = "Cloud id"
  type        = string
}


variable "folder_id" {
  description = "Folder id"
  type        = string
}
