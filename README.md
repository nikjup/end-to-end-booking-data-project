# end-to-end-booking-data-project
# Booking.com Data Analysis Project

This project simulates a real-world analytics workflow at a company like Booking.com. It involves building a lightweight data pipeline, cleaning raw data, storing it in a MySQL database, and generating business insights with SQL and Power BI.

---

## Objective

To create a complete data analytics pipeline from raw data to dashboard using real-world tools and simulate the responsibilities of a data analyst and data engineer in a professional environment.

---

## Project Workflow

1. **Raw Data Collection**  
   - Source: Excel/CSV files (Booking data)
   - Initial inspection and manual cleaning in Excel

2. **ETL Pipeline (Python + MySQL)**  
   - Extracted and cleaned data using Python (`pandas`)
   - Loaded cleaned data into MySQL database tables
   - Scripts used: `nik3.py,nik4.py,nk.py,nk2.py`, `hk.py,n1.py`

3. **SQL Analysis**  
   - Wrote SQL queries to extract key metrics such as:
     - Booking rates
     - Cancellations by country
     - Revenue by customer type
     - Average booking duration
     - denormalize the normalized table


4. **Data Export & Reporting**  
   - Queried data exported from MySQL to Excel using Python
   - Structured reports generated for business review

5. **Visualization in Power BI**  
   - Built dashboards showing:
     - Top booking countries
     - Booking trends over time
     - Cancellation heatmaps
     - Revenue breakdown

---

## Tools & Technologies Used

- **Python**: pandas, openpyxl, MySQL Connector
- **MySQL**: database storage and queries
- **Excel**: raw data source and report formatting
- **Power BI**: data visualization and dashboards
- **SQL**: data extraction and transformation

---

## Folder Structure

```
booking-data-analysis/
│
├── dataset to excel/             # Raw and cleaned data files (Excel, CSV)
├──python code sql to excel /           # Python scripts for ETL and exports
├── powerbi report/         # Power BI .pbix file or screenshots
└── README.md          # Project overview
```

---

## Key Insights
- You might find that bookings with longer lead times have higher cancellation rates, especially in specific segments (e.g., online travel agents), suggesting a need for stricter cancellation policies for early bookings.
- july shows a dip, possibly due to seasonality. Identifying the customer type involved (e.g., transient or contract) can help tailor marketing for that segment in low seasons.
- If Transient customers dominate, the focus should be on short-term promotions, while Contract-heavy business suggests stability and potential for corporate partnerships.
- Higher-star hotels in specific countries (e.g., USA or France) may command premium ADRs, guiding location-based pricing optimization.
-  Higher-star hotels in specific countries (e.g., USA or France) may command premium ADRs, guiding location-based pricing optimization.
-  Some mid-range priced hotels may have higher ratings, revealing value performers that can be promoted more aggressively.

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/nikjup/end-to-end-booking-data-project.git
   ```
2. Ensure MySQL is installed and running.
3. Run the ETL script:
   ```bash
   python code sql to excel/hk.py,n1.py
   python code excel to sql/nik3.py,nik4.py,nk.py,nik2.py
   ```
4. Query the database using scripts using join function.
5. Export results using `dataframename_to_excel.py` and load into Power BI.

---

## Credits

This project is part of a data analytics case study to simulate a professional environment for practicing both analysis and data engineering.


![MySQL 8 0 Command Line Client 16-05-2025 07_54_34](https://github.com/user-attachments/assets/5a595cc8-c2e3-4473-af65-8098c74c6601)
![Power BI Desktop 16-05-2025 05_31_39](https://github.com/user-attachments/assets/447196e5-11b2-49b6-bd3d-9e5cab0b5741)
![Power BI Desktop 16-05-2025 07_58_30](https://github.com/user-attachments/assets/1dc125c6-c0d6-4613-bdd4-b50adcdc5251)
![Power BI Desktop 16-05-2025 07_58_42](https://github.com/user-attachments/assets/d25c1b44-72bc-47c2-af9a-dc4ce553683b)
