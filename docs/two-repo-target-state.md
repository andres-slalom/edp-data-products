# Two-Repo Target State

This document explains how the PoC maps to the real repository model.

## Repository 1: edp-foundation-platform

Purpose:

- shared GitHub workflows
- templates and guardrails
- engineering standards
- common governance assets

Typical path filtering examples:

- `.github/**`
- `standards/**`
- `templates/**`
- `policies/**`

## Repository 2: edp-data-products

Purpose:

- raw ingestion contracts from ADSL
- Azure Data Factory pipelines
- Airflow DAGs
- dbt models and metrics
- Databricks medallion transformations

Typical path filtering examples:

- `adsl/**`
- `adf/**`
- `airflow/**`
- `dbt/**`
- `databricks/bronze/**`
- `databricks/silver/**`
- `databricks/gold-core/**`
- `databricks/gold-semantic/**`
- `databricks/staging/**`

## Recommended Operational Model

Use `edp-foundation-platform` to centralize reusable workflows and standards.

Use `edp-data-products` to host domain delivery assets and trigger checks only for the changed product areas.

If you want to standardize CI behavior across both repositories, define reusable workflows in `edp-foundation-platform` and call them from `edp-data-products` with `workflow_call`.