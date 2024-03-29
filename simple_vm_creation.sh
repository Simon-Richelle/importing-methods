#!/usr/bin/env bash

# create VM instance

gcloud beta compute --project=cryptocurrencies-248218 instances create datalab-vm --zone=europe-west1-b --machine-type=n1-standard-1 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=374390190878-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/cloud-platform --image=debian-9-stretch-v20190813 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=datalab-vm --reservation-affinity=any
