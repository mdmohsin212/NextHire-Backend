# **NextHire - Job Portal System**  

Welcome to **NextHire**, a feature-rich job portal designed to bridge the gap between job seekers and employers. The platform offers an intuitive experience for users to explore job opportunities, apply seamlessly, and track their progress in real time.  

---

## **Features**  

### **User Authentication & Security**  
- **User Registration**: Both job seekers and employers can sign up with their details. A confirmation email is sent for verification before accessing the platform.  
- **JWT-Based Authentication**: Secure login system using JSON Web Tokens (JWT) to maintain user sessions.  
- **Role-Based Access Control**: Employers and job seekers have different levels of access to ensure a smooth workflow.  

### **Employer Functionality**  
- **Job Management**: Employers can create and delete job listings effortlessly.  
- **Candidate Tracking**: Employers get a detailed view of applicants for each job post.  
- **Task Assignments**: Additional tasks can be assigned to job seekers upon application approval.  
- **Application Review**: Employers have control over approving or rejecting job applications.  

### **Job Seeker Features**  
- **Job Search & Applications**: Users can explore job listings and apply with a single click.  
- **Real-Time Application Tracking**: View the status of submitted applications and receive updates.
- **Submit Details**: Once their application is approved, job seekers can submit additional details as required by the employer. 

---
## **Technology Stack**  
<div style="display: flex; gap: 10px;">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL (Supabase)">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT Authentication">
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel">
  <img src="https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white" alt="Cloudinary">
</div>

---

## **Installation & Setup**  

1. **Clone the repository**  
    ```bash
   git clone https://github.com/mdmohsin212/NextHire-Backend.git
    ```
2. **Install dependencies**
    ```
    cd NextHire-backend
    ```
3. **Environment Configuration**
    Create a .env file and set up the required credentials

4. **Run Database Migrations**
    ```
    python manage.py migrate
    ```
5. **Start the Server**
    ```
    python manage.py runserver
    ```

## **API Endpoints**  

### **Authentication**  
- `https://nexthire-backend.vercel.app/user/register/` → Register new users (Employers & Job Seekers)  
- `https://nexthire-backend.vercel.app/user/login/` → Authenticate users and return a JWT token  
- `https://nexthire-backend.vercel.app/user/profile/` → Retrieve user profile details  
- `https://nexthire-backend.vercel.app/user/logout/` → Logout user  

### **Job Management**  
- `https://nexthire-backend.vercel.app/job/list/` → Retrieve all job postings  
- `https://nexthire-backend.vercel.app/job/company/` → Retrieve all companies  
- `https://nexthire-backend.vercel.app/job/applied_job/` → Retrieve job applications  

### **User Profiles**  
- `https://nexthire-backend.vercel.app/user/profile/?id=<user_id>` → Retrieve a specific user profile 


## **Live Deployment**  

- **Backend API**: Hosted on Vercel  
- **Frontend Application**: [NextHire Frontend](https://nexthire-frontend.vercel.app/)  

---

## **Authentication Workflow**  

1. **User Sign-Up**: Registration request is submitted → Email confirmation is sent.  
2. **Email Verification**: User confirms email → Account gets activated.  
3. **JWT Login**: User logs in → JWT token is generated & stored for session management.  
4. **Secure Access**: User accesses platform features based on role (Employer/Job Seeker).  
