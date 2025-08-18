# 🌊 Deep Sales Analysis of Olist Marketplace

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://github.com/PavelGrigoryevDS/olist-deep-dive/blob/main/pyproject.toml)
[![Web Report](https://img.shields.io/badge/📚_Web_Report-2563EB?logoColor=white)](https://pavelgrigoryevds.github.io/olist-deep-dive/)
[![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/pavelgrigoryev/deep-sales-analysis-eda-viz-rfm-nlp-geo)
[![Presentation](https://img.shields.io/badge/Slides-Google%20Slides-red)](https://docs.google.com/presentation/d/1sOYi3MWXedIEnuSn41H8lBeZ9aGnnTi5iV-DEMbfCvc/present)
[![Jupyter Notebook](https://img.shields.io/badge/-Notebook-F37626?logo=jupyter&logoColor=white)](https://github.com/PavelGrigoryevDS/olist-deep-dive/blob/main/olist_deep_dive/olist_deep_dive.ipynb)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Comprehensive analysis of Brazilian e-commerce data, uncovering key insights and actionable business recommendations.

## 📑 Contents

- [🔗 Project Resources](#-project-resources)
- [🛠️ Tech Stack \& Methods](#️-tech-stack--methods)
- [📌 Project Overview](#-project-overview)
- [🗃️ Data Source](#️-data-source)
- [🎯 Main Conclusions](#-main-conclusions)
- [✨ Key Recommendations](#-key-recommendations)
- [🚀 How to Run This Project](#-how-to-run-this-project)

---

## 🔗 Project Resources

- **[Web Report](https://pavelgrigoryevds.github.io/olist-deep-dive/)** - Best for comfortable reading  
- **[Presentation Slides](https://docs.google.com/presentation/d/1sOYi3MWXedIEnuSn41H8lBeZ9aGnnTi5iV-DEMbfCvc/present)** - Key findings summary  
- **[Kaggle Notebook](https://www.kaggle.com/code/pavelgrigoryev/deep-sales-analysis-eda-viz-rfm-nlp-geo)** - Kaggle-integrated version
- **[Source Notebook](https://github.com/PavelGrigoryevDS/olist-deep-dive/blob/main/olist_deep_dive/olist_deep_dive.ipynb)** - Raw Jupyter notebook *(code only, no outputs)*  

[⬆ back to top](#-contents)

---

## 🛠️ Tech Stack & Methods

**Stack:**

`Python` | `Pandas` | `Plotly` | `StatsModels` | `SciPy` | `NLTK` | `TextBlob` | `Sklearn` | `Pingouin`

**Methods**:

- **Exploratory Data Analysis (EDA)**: Statistical summaries, missing value analysis, and outlier detection
- **Data Preprocessing**: Feature engineering, missing value handling, and creation of new metrics and dimensions
- **Time Series Analysis**: Revenue/order trends, seasonality decomposition
- **RFM Segmentation**: Customer value clustering (Recency, Frequency, Monetary)
- **Clustering**: sklearn-based customer behavior segmentation  
- **Geospatial Analysis**: Sales heatmaps and delivery performance by region
- **NLP Sentiment Analysis**: Review text processing with NLTK and TextBlob
- **Statistical Testing**: correlation analysis and hypothesis testing
  
[⬆ back to top](#-contents)

---

## 📌 Project Overview

Olist is a Brazilian e-commerce platform that connects sellers and buyers, offering a wide range of products and convenient conditions for online sales. Olist also acts as an intermediary, allowing sellers to connect to multiple marketplaces simultaneously, thereby increasing their reach.

This analysis aims to:  

- **Evaluate sales performance**  
   - Identify geographical trends and seasonal patterns  
   - Analyze revenue fluctuations and growth metrics  

- **Understand customer behavior**  
   - Examine purchasing frequency and retention drivers  
   - Segment buyers by value and payment preferences  

- **Assess operational efficiency**  
   - Map delivery timelines and bottleneck correlations  
   - Evaluate carrier performance across regions  

- **Optimize payment systems**  
   - Compare payment method success rates  
   - Identify risk factors for cancellations  

- **Generate actionable insights**  
   - Develop data-backed recommendations for business growth  
   - Propose customer experience improvements  

[⬆ back to top](#-contents)

---

## 🗃️ Data Source

The analysis uses the **Olist Brazilian E-Commerce Dataset** ([Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)) 

[⬆ back to top](#-contents)

---

## 🎯 Main Conclusions

### Sales Trends:
  - **Growth & Stabilization**: Sales volume and revenue grew until 2018, then stabilized at 6–7K orders and 1–1.2M R$ per month.
  - **Black Friday (11/24/2017)**: Record spikes in orders, revenue, and buyers.
  - **Geography**: Sao Paulo dominates (42% of sales), with steady growth in 2018, unlike other regions.

### Customer Behavior:

  - **Low Retention**: 97% of buyers made only one purchase; repeat buyers are rare.
  - **High-Value Buyers**: Clients using installment plans (50%) spend 2x more (higher average order value/weight).
  - **Loyalty**: Promoters (58% of buyers) leave positive reviews but rarely return. Critics (13%) spend more but churn faster due to delivery delays.

### Operational Insights:

  - Delayed orders correlate with lower ratings (avg. rating: 1–2 vs. 4–5 for on-time).
  - Heavy/expensive orders take longer to deliver and are more likely to be delayed.
  - Orders with installments process faster, have higher AOV, and show better retention.

### Payment & Risk:

  - **Credit cards dominate**: 74% of transactions, with 35% higher AOV vs. other methods.
  - **Installments boost value**: Orders with installments have 2x higher AOV (premium/heavy items).
  - **Voucher Payments**: Orders paid with vouchers have 3x higher cancellation rates (16% vs. 5% for credit cards).

### Product & Logistics:

  - **Top Categories**: Electronics (27% of sales) and furniture (18%) drive revenue.
  - Northern states take 2x longer delivery.
  - Heavy orders (+40% delivery time) and premium items face delays.
  - **Delivery Bottlenecks**: 70% of total delivery time is spent with carriers, notably slower in Rio de Janeiro and Salvador.

### Critical Challenges:

  - **Declining Ratings**: Average review scores dropped from 4.5 (2017) to 3.9 (2018), linked to delivery delays.
  - **Peak Season Failures**: Black Friday 2017 caused a surge in delayed deliveries, with complaints tied to carrier handoff bottlenecks.
  - **Abandoned Carts**: Canceled orders spike in February/August 2018, often for high-value items paid via vouchers.

### Customer Feedback & Ratings:

  - **Majority of reviews are positive**: 58% of reviews received a rating of 5. Only 12% of reviews received a rating of 1, while a mere 3% received a rating of 2.
  - **Negative Reviews**: 15% of review text mentions "slow delivery" or "missing items," heavily impacting NPS.

### Data Highlights:

  - **Negative Feedback Drivers**: Low ratings correlate with longer delivery times, higher order value, and heavier items.
  - **Success Factors**: Fast carrier handoff (≤3 days) and installment options boost ratings and repeat purchases.

[⬆ back to top](#-contents)

---

## ✨ Key Recommendations

### Boost Customer Retention & Repeat Purchases:

  - Launch a loyalty program targeting one-time buyers (97% of customers), offering discounts on second purchases or bonus points.
  - Personalized win-back campaigns for high-value clients (top 1% driving 15% of revenue) with exclusive offers.
  - Reduce time between purchases (currently 29+ days for 50% of repeat buyers) via time-bound promotions (e.g., "7-day discount").
  
### Improve Product & Pricing Strategy:

  - Expand "Beauty & Health" and "Home & Garden" (18% YoY growth categories) with curated bundles or subscriptions.
  - Reprice problem categories (e.g., "Watches & Gifts") to offset delivery costs or offer guaranteed faster shipping.

### Enhance High-Value Segments:

  - Premium installment plans for big spenders (avg. 3+ orders) with perks like free shipping or priority support.
  - Target voucher users (3x higher cancellation risk) with limited-time combo deals to convert abandoned carts.

### Fix Delivery Pain Points:

  - Prioritize carrier performance in critical regions (e.g., Rio de Janeiro, Salvador), where delays are 30% longer than average.
  - Expedite high-value/heavy orders (>500 R$ or >10kg), which face 2x more 1-star ratings due to delays.
  - Optimize Black Friday logistics to prevent repeat of 2017’s 4x surge in delays (pre-stock inventory, add temporary carriers).

### Regional Growth Tactics:

  - Hyper-local campaigns in São Paulo (42% of sales): Leverage its 20% faster delivery and 30% higher retention to test scalable models.
  - Fix underperformers (e.g., Maranhão, Ceará) with subsidized shipping or partner pickup points.

### Mitigate Negative Reviews:

  - Automate compensation for delayed orders (e.g., 10% off next purchase if delivery exceeds 15 days).
  - Sunday support surge: Add staff to cut response times, reducing low weekend ratings.

[⬆ back to top](#-contents)

---

## 🚀 How to Run This Project

### Prerequisites

- Python 3.11+ installed
- Git (for cloning)

### Clone the Repository

```bash
git clone https://github.com/PavelGrigoryevDS/olist-deep-dive.git
cd olist-deep-dive
```

### Install and Run

- If Poetry is NOT installed on your system, use Option 1
- If Poetry IS installed, use Option 2

#### Option 1: Using pip + virtualenv

```bash
python -m venv .venv
source .venv/bin/activate  
pip install poetry
poetry config virtualenvs.in-project true --local
poetry install
jupyter lab olist_deep_dive/olist_deep_dive.ipynb
```

#### Option 2: Poetry

```bash
poetry config virtualenvs.in-project true --local
poetry install
poetry run jupyter lab olist_deep_dive/olist_deep_dive.ipynb
```

[⬆ back to top](#-contents)

## 📜 License  

This analysis is shared under [MIT License](LICENSE).  
Original data from Olist remains under its [Kaggle license](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
