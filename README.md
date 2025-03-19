
# **Hotel Booking Analytics & Q&A API**  

## 📌 **Overview**  
This project is an **AI-powered hotel booking analytics and Q&A system** built using **FastAPI**. It provides insights into hotel booking trends, cancellations, and lead times while also allowing users to ask **natural language questions** about the data.  

## 🚀 **Features**  
✅ **Hotel Booking Analytics** – Revenue trends, cancellation rates, and lead time statistics.  
✅ **AI-Powered Q&A System** – Uses FAISS and Sentence Transformers for natural language search.  
✅ **FastAPI Backend** – REST API for analytics & Q&A.  
✅ **Scalable Deployment** – Can be hosted on Render, AWS, or similar platforms.  

---

## 📂 **Project Structure**  
📁 `app.py` – The FastAPI application (API endpoints & Q&A system).  
📁 `cleaned_hotel_bookings.csv` – The cleaned dataset used for analysis.  
📁 `hotel_booking.py` – Data processing & visualization script.  
📁 `requirements.txt` – List of dependencies for easy installation.  

---

## 🔧 **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Soundaryar1008/hotel-booking-api.git
cd hotel-booking-api
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the API**  
```sh
uvicorn app:app --reload
```

### **4️⃣ Open API Documentation**  
Go to: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  

---

## 📊 **API Endpoints**  

| **Method** | **Endpoint**              | **Description**                 |
|-----------|-------------------------|--------------------------------|
| GET       | `/ask?query=your_question` | AI-powered Q&A system         |
| GET       | `/revenue-trends`         | Get revenue trends            |
| GET       | `/cancellation-rate`      | Get cancellation rate         |
| GET       | `/bookings-by-country`    | Get booking distribution      |
| GET       | `/lead-time-stats`        | Get lead time statistics      |

---

## 🎯 **Deployment Guide (Optional)**  

### **Deploy on Render**  
1. Push the project to GitHub.  
2. Go to **[Render](https://render.com/)**.  
3. Create a **New Web Service** → Connect GitHub repo.  
4. Use this **Start Command**:  
   ```sh
   uvicorn app:app --host 0.0.0.0 --port $PORT
   ```
5. Deploy! 🚀  

---

## 📌 **Conclusion**  
This project provides **useful insights** into hotel booking trends and enables AI-powered Q&A. It's built with **FastAPI, FAISS, and Sentence Transformers** for high performance.  

🔹 **Developer:** _Soundarya_  
🔹 **GitHub Repo:** [hotel-booking-api](https://github.com/Soundaryar1008/hotel-booking-api)  


