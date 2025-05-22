#!/usr/bin/env bash
set -euo pipefail

# ─── CONFIGURE THESE (or set as env vars before calling) ────────────────────
AWS_REGION=${AWS_REGION:-us-east-1}
ECR_REPO=${ECR_REPO:-my-portfolio-streamlit}
IMAGE_TAG=${IMAGE_TAG:-latest}
# ──────────────────────────────────────────────────────────────────────────────

# 1. Get your AWS account ID
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# 2. Full ECR URI
ECR_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO"

echo "Using:"
echo "  AWS_REGION   = $AWS_REGION"
echo "  ECR_REPO     = $ECR_REPO"
echo "  IMAGE_TAG    = $IMAGE_TAG"
echo "  ECR_URI      = $ECR_URI"
echo

# 3. (Optional) Create the ECR repo if it doesn't exist
if ! aws ecr describe-repositories --repository-names "$ECR_REPO" --region "$AWS_REGION" &> /dev/null; then
  echo "Creating ECR repository: $ECR_REPO"
  aws ecr create-repository \
    --repository-name "$ECR_REPO" \
    --region "$AWS_REGION"
  echo
fi

# 4. Build the Docker image
echo "Building Docker image: $ECR_REPO:$IMAGE_TAG"
docker build -t "$ECR_REPO:$IMAGE_TAG" .

# 5. Authenticate Docker to ECR
echo "Logging in to ECR"
aws ecr get-login-password --region "$AWS_REGION" \
  | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
echo

# 6. Tag & push
echo "Tagging image as $ECR_URI:$IMAGE_TAG"
docker tag "$ECR_REPO:$IMAGE_TAG" "$ECR_URI:$IMAGE_TAG"

echo "Pushing image to ECR"
docker push "$ECR_URI:$IMAGE_TAG"
echo

echo "✅ Done! Image available at:"
echo "   $ECR_URI:$IMAGE_TAG"
