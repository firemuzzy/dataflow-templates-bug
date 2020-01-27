#!/bin/bash -eu

# PROJECT="lablablab"
# STAGING_BUCKET="dataflow-templates"

# define with your project and bucket for staging the template
PROJECT= # DEFINE with your project id
STAGING_BUCKET= # DEFINE with your bucket

REGION="us-central1"
ZONE="us-west1-c"

# Working directories for dataflow
STAGING_BUCKET_PATH="gs://${STAGING_BUCKET}"

STAGING_LOCATION="$STAGING_BUCKET_PATH/staging"
TEMP_LOCATION="$STAGING_BUCKET_PATH/temp"

# Running Config for Dataflow
RUNNER=DataflowRunner

TEMPLATE_LOCATION="${STAGING_BUCKET_PATH}/templates/test"

python2 run_pipeline.py \
  --project=$PROJECT \
  --runner=$RUNNER \
  --staging_location=$STAGING_LOCATION \
  --temp_location=$TEMP_LOCATION \
  --template_location=$TEMPLATE_LOCATION \
  --requirements_file=requirements.txt \
  --region=REGION \
  --experiments=shuffle_mode=service
  
  # --experiments=shuffle_mode=service \