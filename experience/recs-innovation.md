---
type: experience
company: Recs Innovation
location: Naju, South Korea
start: 2024-03
end: 2024-11
roles:
  - title: AI Team Lead
    start: 2024-07
    end: 2024-11
  - title: AI Engineer
    start: 2024-06
    end: 2024-07
  - title: Data Science Intern
    start: 2024-03
    end: 2024-06
skills: [Python, PyTorch, FastAPI, Docker, Docker Compose, GitHub Actions, PostgreSQL, Prometheus, Grafana, MLflow, pandas, NumPy]
tags: [mlops, anomaly-detection, time-series, solar-forecasting, vpp, gnn, leadership, renewable-energy]
website: https://azizjonkasimov.github.io/work/solar-mlops/
---

# Recs Innovation

**March 2024 – November 2024 | Naju, South Korea**

Career progression at the same company: Data Science Intern → AI Engineer → AI Team Lead.

Titles decided by Azizjon on 2026-10-05: Data Science Intern, AI Engineer, AI Team Lead (the
middle role was called AI Developer before). LinkedIn matches since the same day, when the intern
entry was renamed from Data Scientist Intern (`profile/linkedin.md`). The public case study is
https://azizjonkasimov.github.io/work/solar-mlops/.

## AI Team Lead
**July 2024 – November 2024**

- Productionized solar power prediction and anomaly detection systems for solar power plants,
  with their inference services integrated into a commercial Virtual Power Plant (VPP) platform.
- Managed ML, backend, and frontend teams, ensuring seamless integration into Virtual Power
  Plant (VPP) platforms.
- Improved predictive model accuracy by 22% (error rate: 9% → 7%), enabling revenue from Korean
  Power Exchange (KPX) power brokerage.
- Built end-to-end MLOps infrastructure (Docker Compose, GitHub Actions, PostgreSQL, Prometheus,
  Grafana), reducing manual operations by 80%, saving $48K annually.

### Anomaly Detection Optimization
- Worked on multivariate time-series anomaly detection using a graph-based model (GNNAD).
  Extensively refactored the open-source codebase.
- Implemented comprehensive visualizations comparing model predictions against actual data for
  each time series feature.
- Developed an enhanced error calculation methodology, increasing model precision by 5% and
  recall by 7%.
- Introduced a dynamic hourly threshold system (24 thresholds vs. 1 global), improving recall by
  10% by accounting for daily error rate fluctuations.
- Optimized the training pipeline by filtering out anomalous data points from training data,
  resulting in 30% precision improvement and 20% recall improvement.
- Production-aligned cross-validation using 16-point inference windows, hourly thresholds, and
  nightly retraining.
- **Cumulative impact:** Improved anomaly detection precision by ~35% and recall by ~37% through
  multiple optimization strategies.
- The gains above are percentage points, not relative improvements (user, 2026-09-27). Do not
  print them next to the intern-stage 70% precision / 50% recall as if they added up; the
  portfolio website dropped the 70%/50% figures from its anomaly-detection paragraph for that
  reason on 2026-09-27.

## AI Engineer
**June 2024 – July 2024**

- Deployed a containerized anomaly detection system, automating deployments with GitHub Actions
  (deployment time reduced from 3 hours to 15 minutes).
- Developed a PyTorch-based solar generation forecasting model achieving <10% average error,
  qualifying the company for KPX business.

## Data Science Intern
**March 2024 – June 2024**

- Created RESTful APIs with FastAPI to integrate the solar power-plant anomaly detection system
  into a VPP platform.
- Optimized a Graph Neural Network (GNN) model, achieving 70% precision and 50% recall; managed
  experiments using MLflow.
- Built comprehensive ML pipelines (PyTorch, pandas, NumPy) for data processing and model
  inference.

## LinkedIn Media / Proof Artifacts

LinkedIn lists the following proof/media artifacts for the Recs Innovation experience:

- Power generation prediction system — bar chart where yellow bars represent hourly generated
  power and green bars represent predicted generation.
- Power generation prediction system — another week of predictions and true values visualized.
- Power generation prediction system — system page showing true values, predicted values, and
  a visible average error rate of 3.53% in the screenshot.
- Solar Today article: "Recs Innovation Launches Microgrid-Linked ESS to Lead Innovation in
  VPP" — article summary on LinkedIn describes Recs Innovation's AI-integrated ESS product line,
  anomaly detection, SCADA control, predictive maintenance, and VPP support.
- Anomaly detection system screenshots: detected anomalous points with red/yellow anomaly
  classification and continuous monitoring with no anomalies detected.

The screenshot files are described under "Screenshots of the Recs systems" below.

KPX thresholds (resolved 2026-10-05): KPX's renewable generation forecasting program
(재생에너지 발전량 예측제도) has two separate bars, and both statements above are right.
To register, a broker passes a one-month test with a forecast error of 10% or less; that is
what the first model (<10% average error) cleared. KPX then pays an incentive only for days
forecast within 8% (3 KRW/kWh for 6-8%, 4 KRW/kWh at 6% or less, the rules until June 2025,
when solar tightened). Cutting the error from 9% to 7% crossed that 8% line, which is the
revenue the resumes mention. Azizjon also recalled "under 8%". Sources: NewDaily, 2023-09-21
(registration test); Haezoom's notes on the forecasting program and its 2025 rule change.

## Screenshots of the Recs systems

On 2026-09-26 the user shared the original screenshots (1196 to 1536 px wide). They replaced the
800 px copies saved from LinkedIn's media viewer earlier that day, and they include four screens that
are not on LinkedIn. All are in `media/recs-innovation/`. The platform is branded Sun-Q. The Korean
screens show its own interface; the English ones appear to be the same interface translated in the
browser, so some labels read oddly ("Today's development status" for 오늘의 발전 현황).

| File | What it shows | On LinkedIn | On the website |
|---|---|---|---|
| `forecast-bars.jpg` | Korean forecast page, Oct 25-31, 2024: hourly output and forecast as bars | yes | yes |
| `forecast-week.jpg` | The same page and week as a line chart | yes | yes |
| `forecast-page.jpg` | Korean forecast page, Oct 16-24, 2024, with a 3.53% average error for the selected period (not the 9% → 7% figure used in resumes) | yes | yes |
| `anomaly-detected.png` | Abnormal-symptoms page, Inverter 1, Oct 21-25, 2024: the affected features listed and anomalies marked red or yellow on the power chart | yes | yes |
| `anomaly-detected-voltage.png` | The same inverter and period on the voltage chart | no | yes |
| `anomaly-none.png` | Inverter 2, Nov 18-22, 2024: no anomalies (current chart) | yes | yes |
| `dashboard.png` | The platform's home screen, Nov 28, 2024: weather, equipment status, SMP and REC sales, battery charge, generation, and transmission | no | yes |
| `forecast-page-en.png` | English forecast page, Nov 4-8, 2024, with actual output only and no forecast values | no | no: a forecast page without forecasts proves little |
| `anomaly-none-inverter-3.png` | Inverter 3, Nov 28, 2024: no anomalies, but the table shows an impossible vertical irradiance of −2,977,985 | no | no: the glitch next to "no abnormal symptoms" invites questions |

The screens name the customer plant in the header and subtitle, and the home screen also shows
the plant's town and its SMP and REC sales. Each screenshot on the website has
a `-covered` copy (same format as the original) with those covered by slate boxes, and the website's
images are made from the covered copies.

## LinkedIn Skill Associations

- AI Team Lead: Project Management and Team Leadership.
- AI Engineer: MLOps and Data Analysis.
- Data Science Intern: Data Analysis and Research Skills.
