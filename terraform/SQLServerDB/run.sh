#!/usr/bin/env bash

# source: https://learn.hashicorp.com/terraform/development/running-terraform-in-automation

# To initialize the working directory. Turn of interactive mode  - is not neccesery.
terraform validate
terraform init -input=false
# To create a plan and save it to the local file tfplan.
terraform plan -out=tfplan -input=false
# Apply changes. The -refresh parametr validate plan vs source(for me at Azure)
# terraform apply -refresh=true -state-out=state/$(date +'%Y-%m-%d_%H_%M_%S'.ftstate)
