# Power BI Portfolio Project: Sales Performance & DAX Mastery

### 📊 Project Overview
This project was designed to demonstrate proficiency in **Power BI**, specifically focusing on **DAX (Data Analysis Expressions)**, data modeling, and performance optimization. 

To simulate a real-world business environment, I structured a specialized dataset covering multiple product categories including Mobile, Laptop, Tablet, and Accessories. This allowed me to practice complex logic that mirrors actual retail analytics requirements.

### 💾 Data Source & Loading
* **Data Entry:** To keep the project lightweight and self-contained, I used the **"Enter Data"** feature within Power BI Desktop rather than importing external files. 
* **Structure:** The dataset consists of 5 columns and 20 rows, carefully designed to test both **Row Context** and **Filter Context**.

---

### 🧠 DAX Implementation & Problem Solving
I implemented 10 specific DAX calculations to solve common business questions. Below is a breakdown of the logic used:

#### 1. Fundamental Aggregations
* **Total Sales & Quantity:** Created explicit measures to aggregate revenue. I opted for measures over implicit sums to ensure the model remains scalable.
* **Average Transaction:** Calculated the mean value per sale to track customer spending behavior.

#### 2. Advanced Logic & Filtering
* **Mobile Category Sales:** Leveraged the `CALCULATE` function to create a filtered measure specific to one segment.
* **All-Time Sales:** Used the `ALL` function to bypass visual filters, which is essential for "Percentage of Total" calculations.

#### 3. Data Categorization (Row Context)
* **Sales Segmentation:** Created a **Calculated Column** using an `IF` statement to categorize transactions as "High Volume" or "Standard." This was used specifically to enable **Slicer** functionality.

#### 4. Time Intelligence & Iterators
* **Sales MTD (Month-to-Date):** Used `TOTALMTD` to track cumulative growth throughout the month.
* **Iterator Logic (SUMX):** Implemented `SUMX` to calculate total revenue without needing a helper column, demonstrating memory-efficient DAX practices.

---

### 💡 Key Technical Learnings
* **Measure vs. Column:** I prioritized Measures for dynamic calculations to keep the file size optimized and only used Calculated Columns for grouping/slicing.
* **Context Mastery:** Successfully managed the transition between Row Context and Filter Context, ensuring calculations remained accurate even when multiple filters were applied.
* **Visualization Strategy:** Mapped each metric to its most effective visual—KPI Cards for big numbers, Line Charts for trends, and Donut Charts for categorical breakdowns.

---

### 🚀 How to Explore this Project
1.  Download the `.pbix` file from this repository.
2.  Open it in **Power BI Desktop**.
3.  Interact with the **Sales Segment Slicer** to see how the measures dynamically recalculate across the dashboard.
