# Career Portal

A simple full-stack career portal application with:
- 🌐 Angular frontend
- ⚙️ FastAPI backend
- 💼 Post and view job openings

---

## 📁 Project Structure

career-portal/
├── backend/ # FastAPI backend
│ ├── main.py
│ └── data.py
├── frontend/ # Angular frontend (job-post, job-list)
├── .gitignore
└── README.md



---

## 🚀 Getting Started

### 🛠 Backend Setup (FastAPI)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
python main.py

The backend will run at: http://<your-ec2-ip>:5000


** Frontend Setup (Angular)**
cd frontend
npm install
ng serve --host 0.0.0.0

The frontend will be accessible via: http://<your-ec2-ip>:4200


**API Endpoints**
GET /api/jobs — List all jobs
POST /api/jobs — Add a new job


** Features**
Post new jobs via a form

View job listings dynamically
Angular standalone components (job-post, job-list)
FastAPI REST backend with CORS


** Future Plans**
Dockerize frontend & backend
Deploy to AWS ECS with Terraform
Store jobs in DynamoDB
CI/CD with GitHub Actions
