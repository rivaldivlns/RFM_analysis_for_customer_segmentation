# Customer Segmentation using RFM Analysis & Clustering Techniques

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Data](#data)
4. [Methodology](#methodology)
    - [RFM Analysis](#rfm-analysis)
    - [Clustering Techniques](#clustering-techniques)
5. [Usage](#usage)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction
This repository is dedicated to customer segmentation using RFM (Recency, Frequency, Monetary) Analysis and various clustering techniques. By analyzing purchase history, we aim to identify distinct groups within the customer base to enable more targeted marketing, improve customer relationship management, and optimize resource allocation.

## Getting Started

### Prerequisites
To run the analysis, ensure you have the following software and libraries installed:
- Python (>= 3.7)
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/rivaldivlns/customer-segmentation-rfm.git
   ```

2. Navigate to the repository folder and install the required packages:
   ```sh
   cd customer-segmentation-rfm
   pip install -r requirements.txt
   ```

## Data
The dataset contains transaction records with the following columns:
- CustomerID
- TransactionDate
- PurchaseAmount

## Methodology

### RFM Analysis
RFM Analysis is a behavior-based segmentation technique based on three metrics:
- **Recency**: How recently a customer made a purchase.
- **Frequency**: How often a customer makes a purchase.
- **Monetary**: How much money a customer spends on purchases.

### Clustering Techniques
After computing RFM scores for each customer, clustering techniques (e.g., K-means, Agglomerative, DBSCAN) are applied to group customers into distinct segments.

## Usage
1. Load the dataset.
2. Run the RFM analysis to generate RFM scores for each customer.
3. Apply clustering techniques to segment customers.
4. Visualize and interpret the results.

## Results
The repository provides a Jupyter Notebook showcasing the entire analysis process, from data preprocessing to clustering and visualization. Insights and recommendations based on the identified segments are also discussed.

## Contributing
If you would like to contribute to the project, please fork the repository, make your changes, and create a pull request. Ensure your PR provides a detailed description of the changes made.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

---
