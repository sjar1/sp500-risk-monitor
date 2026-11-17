# S&P 500 Investigative Risk Monitor

Research-only S&P 500 SEC filing review-priority monitor.

## Dashboard
When GitHub Pages is enabled from **main / (root)**, the site is:
https://sjar1.github.io/sp500-risk-monitor/

## Automated scanner
[Daily SEC scan](https://github.com/sjar1/sp500-risk-monitor/actions/workflows/daily-scan.yml)

**Required setup:** GitHub repository **Settings → Secrets and variables → Actions → New repository secret** named `SEC_USER_AGENT`. Set it to an app identifier with your genuine contact email, for example `SP500RiskMonitor contact@yourdomain.com`. SEC requests need an identifying user agent; do not use a made-up email. The migrated report is an initial snapshot; it is not evidence that the new repository has scanned successfully.

To publish, visit **Settings → Pages**, choose **Deploy from a branch**, select **main** and **/(root)**, then save. Run **Daily S&P 500 SEC Scan** manually once and confirm a green run and updated `report.json`. The scheduled workflow runs weekdays at 12:20 UTC (GitHub scheduling may be delayed).

## Data and interpretation
The bot scores SEC filing items and certain text matches as *research priorities*, not adjudications, misconduct claims, or estimates of a stock price decline. The probabilities in the dashboard remain **Pending** until a forecasting model is calibrated. Verify all source filings before forming conclusions.

## Provenance
Migrated from `sjar1/sp500-investigative-monitor` on 2026-11-17, including the prior scanner, dashboard, and last published report.
