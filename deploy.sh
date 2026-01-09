#!/bin/bash

# MindCare AI Deployment Script
# Updates AWS Lambda function with latest code

echo "🧠 MindCare AI - Deployment Script"
echo "=================================="

# Create deployment package
echo "📦 Creating deployment package..."
zip -r mindcare-lambda.zip lambda_function.py src/ -x "*.pyc" "__pycache__/*"

# Update Lambda function
echo "🚀 Updating Lambda function..."
aws lambda update-function-code \
  --function-name MindCare-AI-Platform \
  --zip-file fileb://mindcare-lambda.zip

# Get function URL
echo "🌐 Getting function URL..."
FUNCTION_URL=$(aws lambda get-function-url-config --function-name MindCare-AI-Platform --query 'FunctionUrl' --output text)

echo ""
echo "✅ Deployment Complete!"
echo "🌍 Website URL: $FUNCTION_URL"
echo ""
echo "🎯 Features Updated:"
echo "   • Real-time facial emotion detection"
echo "   • AWS Rekognition integration"
echo "   • Camera capture functionality"
echo "   • Enhanced therapeutic recommendations"
echo ""
echo "📱 Test the emotion detection:"
echo "   1. Go to: $FUNCTION_URL"
echo "   2. Click 'Emotion AI' in navigation"
echo "   3. Allow camera access"
echo "   4. Click 'Analyze Emotion'"
echo ""

# Clean up
rm mindcare-lambda.zip

echo "🎉 Ready to help improve mental health!"