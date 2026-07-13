# 🔗 Serverless URL Shortener on AWS

A simple serverless URL shortener built on AWS using **API Gateway**, **AWS Lambda**, and **Amazon DynamoDB**. The application generates a short URL for any valid long URL and redirects users back to the original website using HTTP 301 redirects.

This project was built to get hands-on experience with AWS serverless services and understand how API Gateway, Lambda, IAM, and DynamoDB work together in a real-world application.

---

## 🚀 Architecture

```
                 Create Short URL

          POST /shorten
                │
                ▼
          API Gateway
                │
                ▼
      shorten-url Lambda
                │
                ▼
           DynamoDB
                │
      Store URL Mapping
                │
                ▼
      Return Short URL



--------------------------------------------



          Open Short URL

      GET /{shortCode}
                │
                ▼
          API Gateway
                │
                ▼
      redirect-url Lambda
                │
                ▼
           DynamoDB
                │
      Fetch Original URL
                │
                ▼
      HTTP 301 Redirect
                │
                ▼
      Original Website Opens
```

---

## 🏗️ AWS Services Used

- Amazon API Gateway (HTTP API)
- AWS Lambda (Python 3.12)
- Amazon DynamoDB
- IAM
- CloudWatch Logs

---

## 📌 Features

- Generate short URLs from long URLs
- Redirect using HTTP 301
- Serverless architecture
- No EC2 instances or server management
- On-demand DynamoDB
- CloudWatch logging for debugging
- IAM execution role for secure access

---

## 📂 Project Structure

```
.
├── shorten-url/
│   └── lambda_function.py
│
├── redirect-url/
│   └── lambda_function.py
│
└── README.md
```

---

## ⚙️ How It Works

### 1. Create Short URL

- User sends a POST request containing a long URL.
- API Gateway forwards the request to the **shorten-url** Lambda.
- Lambda generates a random 6-character short code.
- The mapping is stored in DynamoDB.
- Lambda returns the generated short URL.

Example request

```json
{
    "url":"https://www.google.com/search?q=aws+devops+projects"
}
```

Example response

```json
{
    "shortUrl":"https://abc123xyz.execute-api.ap-south-1.amazonaws.com/aB3kRz",
    "shortCode":"aB3kRz"
}
```

---

### 2. Redirect

- User opens the generated short URL.
- API Gateway extracts the short code.
- The request is sent to the **redirect-url** Lambda.
- Lambda looks up the short code in DynamoDB.
- If found, Lambda returns an HTTP 301 redirect.
- The browser automatically opens the original URL.

---

## 🗄️ DynamoDB Schema

**Table Name**

```
url-shortener
```

| Attribute | Type |
|-----------|------|
| shortCode | String (Partition Key) |
| longUrl | String |

Example

| shortCode | longUrl |
|------------|---------|
| aB3kRz | https://www.google.com |

---

## 🔐 IAM Role

The Lambda execution role was configured with:

- AmazonDynamoDBFullAccess
- AWSLambdaBasicExecutionRole

---

## 🌐 API Endpoints

### Create Short URL

```
POST /shorten
```

Request

```json
{
    "url":"https://example.com"
}
```

Response

```json
{
    "shortUrl":"https://your-api.execute-api.region.amazonaws.com/Xy12Ab",
    "shortCode":"Xy12Ab"
}
```

---

### Redirect

```
GET /{shortCode}
```

Example

```
GET /Xy12Ab
```

Response

```
301 Moved Permanently
```

Browser redirects to

```
https://example.com
```

---

## 🧪 Testing

### Using Postman

#### Create Short URL

Method

```
POST
```

URL

```
https://<api-id>.execute-api.<region>.amazonaws.com/shorten
```

Headers

```
Content-Type : application/json
```

Body

```json
{
    "url":"https://www.google.com"
}
```

---

#### Redirect

Method

```
GET
```

URL

```
https://<api-id>.execute-api.<region>.amazonaws.com/<shortCode>
```

---

## 💻 Testing with PowerShell

```powershell
$body = '{"url":"https://www.google.com"}'

Invoke-RestMethod `
-Uri "https://<api-id>.execute-api.ap-south-1.amazonaws.com/shorten" `
-Method POST `
-ContentType "application/json" `
-Body $body
```

---

## 📖 What I Learned

Through this project I learned:

- Building serverless applications on AWS
- Creating HTTP APIs using API Gateway
- Writing Lambda functions in Python
- Reading and writing data in DynamoDB
- Using IAM execution roles
- Handling HTTP status codes like 301 redirects
- Passing path parameters from API Gateway to Lambda
- Monitoring Lambda logs using CloudWatch

---

## ⚠️ Common Issues

### 500 Internal Server Error

- Verify Lambda logs in CloudWatch.
- Check IAM permissions.
- Verify DynamoDB table name.

---

### 404 Not Found

- Verify the API Gateway route exists.
- Check the invoke URL.

---

### DynamoDB ResourceNotFoundException

- Ensure the table name matches the code.
- Make sure Lambda and DynamoDB are in the same AWS Region.

---

### Redirect Not Working

- Verify the short code exists in DynamoDB.
- Check the GET route is configured as:

```
GET /{shortCode}
```

---

## 🔮 Future Improvements

- Generate QR codes for shortened URLs
- Custom aliases for short URLs
- URL expiration
- Click analytics
- User authentication
- Custom domain with Route 53
- Infrastructure as Code using Terraform
- CI/CD using GitHub Actions

---

## 📷 Demo

You can add screenshots here:

- API Gateway routes
- Lambda functions
- DynamoDB table
- Postman requests
- CloudWatch logs

---

## 📚 Key Concepts Demonstrated

- Serverless Computing
- Event-Driven Architecture
- REST APIs
- HTTP Status Codes
- DynamoDB CRUD Operations
- IAM Roles and Permissions
- CloudWatch Logging
- AWS Managed Services

---

## 👨‍💻 Author

**Bhavith Reddy**

Aspiring DevOps & Cloud Engineer

Building hands-on projects with AWS, Docker, Kubernetes, Terraform, Jenkins, and GitHub Actions.

---

## ⭐ If you found this project helpful, consider giving it a star!
