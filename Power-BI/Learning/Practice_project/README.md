Power BI Portfolio Project: Sales Performance & DAX Mastery
Project Overview
This project was created to practice and demonstrate my proficiency in Power BI, specifically focusing on DAX (Data Analysis Expressions), data modeling, and performance optimization. Instead of using a pre-made dataset, I structured a 20-row sales dataset covering multiple categories (Mobile, Laptop, Tablet, Accessory) to simulate a real-world retail environment.

How I Loaded the Data
To keep the project lightweight and easily accessible within the .pbix file, I used the "Enter Data" feature in Power BI Desktop rather than importing an external Excel or CSV file. This ensures the project is self-contained and ready for immediate interaction.

DAX Implementation & Problem Solving
I implemented 10 specific DAX calculations to solve common business questions. I focused on the two core concepts of Power BI: Row Context (Calculated Columns) and Filter Context (Measures).

1. Fundamental Aggregations
Total Sales & Quantity: Built basic measures to aggregate revenue and units. I opted for explicit measures over implicit sums to ensure the model stays scalable.

Average Transaction: Calculated the mean value per sale to track customer spending behavior.

2. Advanced Logic & Filtering
Mobile Category Sales: Used the CALCULATE function to create a filtered measure specifically for the Mobile segment.

All-Time Sales: Leveraged the ALL function to bypass visual filters—a crucial step for calculating "Percentage of Total" metrics.

3. Data Categorization (Row Context)
Sales Segmentation: Created a calculated column using an IF statement to categorize transactions as "High Volume" or "Standard." This allows for better filtering via Slicers.

4. Time Intelligence & Iterators
Sales MTD (Month-to-Date): Used TOTALMTD to track cumulative growth throughout the month.

Iterator Logic (SUMX): Implemented SUMX to calculate total revenue without needing a helper column, demonstrating an understanding of memory-efficient DAX.

Key Learnings from this Project
Measure vs. Column: I learned that while Calculated Columns are great for Slicers and grouping, Measures are the "gold standard" for calculations because they respond dynamically to user filters and keep the file size small.

Context Troubleshooting: During development, I handled "context" errors by ensuring that column-based logic stayed in Calculated Columns and aggregate-based logic stayed in Measures.

Visual Storytelling: I mapped each DAX result to its most effective visual—using KPI Cards for big numbers, Line Charts for trends, and Donut Charts for categorical breakdowns.

How to use this repository
Download the .pbix file.

Open it in Power BI Desktop.

Interact with the Sales Segment Slicer to see how the Measures dynamically recalculate across the dashboard.
