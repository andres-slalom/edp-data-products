# GitHub Promotion Flow PoC

This document describes the complete promotion path used in this PoC.

## Branches

- `develop`
- `qa`
- `main`

## Merge Strategy

- `Squash and merge` is required for all PR promotions in this PoC.

## Allowed PR Routes

- Feature branch -> `develop`
- `develop` -> `qa`
- `qa` -> `main`

In this PoC, route validation is enforced for all promotion targets:

- Target `develop`: source branch must start with `feature/`, `bugfix/`, or `chore/`
- Target `qa`: source branch must be `develop`
- Target `main`: source branch must be `qa`

## Workflow Sequence

1. Open PR.
2. `pr-validation-by-path.yml` runs:
   - checks promotion route
   - detects changed domains by path
   - runs validation/tests only for changed domains
   - for dbt path changes, simulates a dbt Cloud CI trigger after dbt validation succeeds
   - publishes evidence summary with changed files by domain
3. Merge PR.
4. `deploy-by-path-after-merge.yml` runs:
   - maps branch to environment (`develop=dev`, `qa=qa`, `main=prod`)
   - deploys only changed domains
   - publishes evidence summary with changed files and deployed domains

## Example End-To-End

1. Create `feature/add-dbt-metric` from `develop`.
2. Edit only `dbt/models/core/customer_metrics.sql`.
3. Open PR to `develop`.
4. Confirm only dbt validation/test jobs run.
5. Merge with `Squash and merge`.
6. Open PR `develop` -> `qa` and merge with `Squash and merge`.
7. Confirm simulated deploy only for dbt to `qa`.
8. Open PR `qa` -> `main` and merge with `Squash and merge`.
9. Confirm simulated deploy only for dbt to `prod`.

## What To Show In The Demo

For each PR and merge event, open the workflow summary and show:

1. Source and target branches.
2. Changed files grouped by domain.
3. Path flags per domain (`true` or `false`).
4. Only matching validation jobs executed.
5. Only matching deployment jobs executed.

## How To Simulate Success And Failure

You can force a validation failure without changing test code by adding a control tag in the PR body:

- `[poc-fail-adsl]`
- `[poc-fail-adf]`
- `[poc-fail-airflow]`
- `[poc-fail-dbt]`
- `[poc-fail-databricks]`
- `[poc-fail-platform]`

Examples:

1. dbt failure demo:
   - Change a file in `dbt/**`
   - Add `[poc-fail-dbt]` to PR body
   - `validate-dbt` fails, and dbt Cloud CI simulation is not triggered

2. dbt success demo:
   - Change a file in `dbt/**`
   - Do not include `[poc-fail-dbt]`
   - `validate-dbt` passes, and dbt Cloud CI simulation runs