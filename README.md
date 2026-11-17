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

## Daily historical monitoring and alerts
Each successful weekday scan updates `report.json` and `history.json`. The latter retains up to 180 daily snapshots of **all scanned companies' scores**, Top 10 membership, and SEC evidence URLs. The dashboard shows risk score trends, watchlist entrants/exits, newly qualifying filings and source links.

**Early warning criteria:** a company enters the Top 10, its review score increases by 15 or more points since the previous day, or it has a newly qualifying filing scored at least 45. These are screening heuristics, **not allegations or calibrated probabilities**. New warnings generate a GitHub Issue titled `SEC early warnings — YYYY-MM-DD` in this repository. Enable GitHub notifications for Issues (Watch → Custom → Issues) to receive GitHub notifications.

The initial history baseline is from the first successful report, containing only the original Top 10. Full-universe historical scores start after the next scanner run. Same-day reruns overwrite that day's snapshot; comparisons are made to the prior UTC day.

The older `sp500-investigative-monitor` repository should only be deleted after the replacement dashboard, daily scan and alert issues are confirmed working. Deletion is not performed automatically.
