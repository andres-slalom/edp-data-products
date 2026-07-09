## Promotion Context

- Source branch:
- Target branch:
- Promotion stage: feature-to-develop | develop-to-qa | qa-to-main

## Changed Domains

- [ ] adsl
- [ ] adf
- [ ] airflow
- [ ] dbt
- [ ] databricks
- [ ] platform-common

## Validation Checklist

- [ ] I confirmed only required paths were changed.
- [ ] I verified CI runs only domain-specific validations/tests.
- [ ] I understand merge will trigger simulated deploy only for changed paths.
- [ ] I will merge this PR using Squash and merge.

## Optional Failure Simulation Tags

Add one tag only when you want to force a failing validation for demo purposes:

- [ ] [poc-fail-adsl]
- [ ] [poc-fail-adf]
- [ ] [poc-fail-airflow]
- [ ] [poc-fail-dbt]
- [ ] [poc-fail-databricks]
- [ ] [poc-fail-platform]