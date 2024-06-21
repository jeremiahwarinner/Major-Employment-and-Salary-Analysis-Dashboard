# Major Employment and Salary Analysis Dashboard

This project provides an interactive dashboard to analyze the employment and salary data of different majors. It is built using Python, Dash, and Plotly, allowing users to explore insights on employment rates, salary distributions, and full-time year-round employment rates by major.

## Features

- **Data Visualization**: Interactive charts showing employment rates, salary distributions, and full-time year-round employment rates.
- **Data Filtering**: Dropdown menu to select major categories and view relevant data.
- **Comprehensive Insights**: Visual representation of key statistics and trends across different majors.

## Technologies Used

- **Python**: Programming language used for data processing and backend logic.
- **Dash**: Web framework for building interactive web applications.
- **Plotly**: Graphing library for creating interactive charts.
- **Pandas**: Data manipulation and analysis library.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jeremiahwarinner/Major-Employment-and-Salary-Analysis-Dashboard.git
    cd major-employment-salary-analysis
    ```

2. Install the required packages:
    ```bash
    pip install dash plotly pandas
    ```

3. Ensure your dataset (`all-ages.csv`) is in the root directory of the project.

### Running the Dashboard

1. Start the Dash application:
    ```bash
    python dashboard.py
    ```

2. Open your web browser and go to `http://127.0.0.1:8050` to view the dashboard.

## Usage

- **Dropdown Menu**: Select a major category from the dropdown to filter the charts.
- **Charts**:
  - **Employment Rate Chart**: Displays the employment rate by major.
  - **Salary Distribution Chart**: Shows the median, 25th percentile, and 75th percentile salaries by major.
  - **Full-Time Year-Round Employment Rate Chart**: Illustrates the full-time year-round employment rate by major.

## Key Insights

1. **Top Majors by Employment Rate**:
   - Majors in "Computers & Mathematics" have the highest average employment rate at 80.17%.
   - "Interdisciplinary" and "Communications & Journalism" also have high employment rates, close to 79%.

2. **Salary Insights**:
   - Majors in "Engineering" have the highest average median salary at $77,759, with the 75th percentile salary reaching up to $108,534.
   - "Computers & Mathematics" and "Physical Sciences" also offer high median salaries, above $60,000.
   - The majors with the lowest average median salaries are in "Interdisciplinary" and "Arts", around $43,000.

3. **Full-Time Year-Round Employment**:
   - Majors like "Management Information Systems and Statistics" and "Computer and Information Systems" have the highest full-time year-round employment rates at 75.48% and 74.85%, respectively.

4. **Correlation Insights**:
   - There is a strong positive correlation between the number of individuals employed full-time year-round and the total number of employed individuals.
   - Majors with higher median salaries also tend to have higher salaries at both the lower (25th percentile) and upper (75th percentile) ends.

## Example Screenshots

![employmentrate](https://github.com/jeremiahwarinner/Major-Employment-and-Salary-Analysis-Dashboard/assets/158241209/896e651a-52bb-455e-bf6e-f354ed6acb5e)
![fulltimeyearroundemployment](https://github.com/jeremiahwarinner/Major-Employment-and-Salary-Analysis-Dashboard/assets/158241209/82f5c2ae-dca1-4428-a716-9784925284e6)
![salary distribution](https://github.com/jeremiahwarinner/Major-Employment-and-Salary-Analysis-Dashboard/assets/158241209/53b05727-bee0-4f8b-8ccb-a5df69fb1455)


## Interactive Demo


https://github.com/jeremiahwarinner/Major-Employment-and-Salary-Analysis-Dashboard/assets/158241209/b6869c04-d212-466f-96ca-3c3aade7e3dd


