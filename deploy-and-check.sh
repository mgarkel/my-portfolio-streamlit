#!/usr/bin/env bash
set -euo pipefail

# ─── CONFIG ──────────────────────────────────────────────────────────────────
AWS_REGION=${AWS_REGION:-us-east-1}
CLUSTER_NAME=${CLUSTER_NAME:-streamlit-cluster}
SERVICE_NAME=${SERVICE_NAME:-streamlit-service}
TARGET_GROUP_ARN=${TARGET_GROUP_ARN:-}

if [ -z "$TARGET_GROUP_ARN" ]; then
  echo "Error: TARGET_GROUP_ARN must be set (export TARGET_GROUP_ARN=arn:...)."
  exit 1
fi
# ─────────────────────────────────────────────────────────────────────────────

echo "🔄 Triggering new deployment for $SERVICE_NAME in cluster $CLUSTER_NAME..."
aws ecs update-service \
  --cluster "$CLUSTER_NAME" \
  --service "$SERVICE_NAME" \
  --force-new-deployment \
  --region "$AWS_REGION"

echo "⏳ Waiting for service to become stable..."
aws ecs wait services-stable \
  --cluster "$CLUSTER_NAME" \
  --services "$SERVICE_NAME" \
  --region "$AWS_REGION"

echo
echo "✅ Service is now stable. Current deployments:"
aws ecs describe-services \
  --cluster "$CLUSTER_NAME" \
  --services "$SERVICE_NAME" \
  --region "$AWS_REGION" \
  --query "services[0].deployments" \
  --output table

echo
echo "🔍 Target group health for $TARGET_GROUP_ARN:"
aws elbv2 describe-target-health \
  --target-group-arn "$TARGET_GROUP_ARN" \
  --region "$AWS_REGION" \
  --query "TargetHealthDescriptions[*].TargetHealth.State" \
  --output table

echo
echo "🌐 Your app should be live at your ALB DNS name (no port needed)."
