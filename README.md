# Customer-Segmentation-Project
Developed a customer segmentation model using the Mall Customers dataset. Applied K-Means clustering to group customers based on annual income and spending score. Used Python, Pandas, Matplotlib, and Scikit-learn to analyze customer behavior and visualize meaningful customer segments for targeted marketing insights.
# Customer Segmentation using K-Means Clustering

## 📌 Project Overview
This project focuses on customer segmentation using the **K-Means Clustering** algorithm. By analyzing customer demographics and spending behavior, the project groups customers into different segments that can help businesses understand customer preferences and design targeted marketing strategies.

---

## 🎯 Objective
- Segment customers based on their purchasing behavior.
- Identify customer groups with similar characteristics.
- Provide business insights using data visualization and clustering.

---

## 📂 Dataset
**Dataset:** Mall Customers Dataset

### Features
- CustomerID
- Genre
- Age
- Annual Income (k$)
- Spending Score (1-100)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- KaggleHub
- VS Code

---

## 📊 Project Workflow

1. Download the dataset using KaggleHub.
2. Load and inspect the dataset.
3. Perform data preprocessing.
4. Visualize customer distribution.
5. Determine the optimal number of clusters using the Elbow Method.
6. Apply K-Means Clustering.
7. Visualize customer segments.
8. Analyze the characteristics of each customer segment.

---

## 📈 Visualizations

The project includes:

- Customer Distribution Scatter Plot
- Elbow Method Graph
- Customer Segmentation Plot
- Cluster Centroids Visualization

---

## 🤖 Machine Learning Algorithm

**K-Means Clustering**

K-Means is an unsupervised machine learning algorithm used to divide data into clusters based on similarity. In this project, customers are grouped according to:

- Annual Income
- Spending Score

---

## 📁 Project Structure

```
Customer-Segmentation-Project/
│
├── customer_segmentation.py
├── Mall_Customers.csv
├── customer_distribution.png
├── elbow_method.png
├── customer_segments.png
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run the Project

### Install the required libraries

```bash
pip install kagglehub pandas matplotlib scikit-learn
```

### Run the project

```bash
python customer_segmentation.py
```

---

## 📌 Results

The K-Means algorithm successfully grouped customers into five distinct clusters based on their annual income and spending score. These segments can help businesses:

- Identify high-value customers
- Recognize low-spending customers
- Develop personalized marketing campaigns
- Improve customer retention strategies

---

## 🚀 Future Improvements

- Add Age and Genre as clustering features.
- Build an interactive dashboard using Power BI or Streamlit.
- Compare K-Means with Hierarchical Clustering and DBSCAN.
- Deploy the project as a web application.

---

## 👩‍💻 Author

**SruthiKeerthana Chilakala**

Computer Science and Data Science Student

---

## 📜 License

This project is created for educational and internship purposes.
