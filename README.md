# PoC: GitHub Promotion Flow With Path-Based CI/CD

This proof of concept is focused completely on GitHub flow.

The repository keeps the current folders as-is, but the CI/CD behavior is now centered on branch promotion and selective execution by path.

## Promotion Model 

The PoC uses three long-lived branches:

- `develop`
- `qa`
- `main`

Expected promotion path:

1. Feature branch -> `develop`
2. `develop` -> `qa`
3. `qa` -> `main`

Required merge strategy for this PoC:

- `Squash and merge`

## Objective

Show an end-to-end promotion process with pull requests and simulated deployments where validations, tests, and deployments run only for changed paths, not the full repository.

## Path Domains

- `adsl/**`
- `adf/**`
- `airflow/**`
- `dbt/**`
- `databricks/**`
- `.github/**` and `docs/**` as platform/common

## Workflows

- `pr-validation-by-path.yml`
    - Trigger: pull requests targeting `develop`, `qa`, or `main`
    - Validates allowed promotion route
    - Detects changed paths
    - Runs only domain-specific validations/tests for changed domains
    - For dbt changes, simulates a dbt Cloud CI API trigger after dbt validation passes
    - Publishes workflow evidence: route, changed files by domain, and executed scopes

- `deploy-by-path-after-merge.yml`
    - Trigger: PR merged into `develop`, `qa`, or `main`
    - Maps target branch to environment (`dev`, `qa`, `prod`)
    - Simulates deployments only for changed domains
    - Publishes workflow evidence: environment, changed files by domain, and executed deploy scopes

## Repository Layout

```text
.
├── .github/workflows/
├── adsl/raw/
├── adf/pipelines/
├── airflow/dags/
├── dbt/models/
└── databricks/
        ├── bronze/
        ├── silver/
        ├── gold-core/
        ├── gold-semantic/
        └── staging/
```

## How To Run The Full Example

1. Create branches `develop`, `qa`, and `main` in GitHub.
2. In repository settings, enable only `Squash and merge` and disable other merge methods.
3. Create a feature branch from `develop`.
4. Change only one domain file, for example `dbt/models/core/customer_metrics.sql`.
5. Open PR `feature/...` -> `develop` and verify only `dbt` validation/test jobs run.
6. Merge PR using `Squash and merge`.
7. Open PR `develop` -> `qa` and verify path-based validations run again.
8. Merge PR using `Squash and merge` and verify simulated deploy to `qa` runs only for changed domains.
9. Open PR `qa` -> `main`.
10. Merge PR using `Squash and merge` and verify simulated deploy to `prod` runs only for changed domains.

## Notes

- This PoC simulates deployments using echo/log steps.
- Branch protection rules (required checks, reviewers) should be configured in GitHub settings.

## Demo Proof Points

Use each workflow run summary as objective evidence:

1. Promotion route is validated.
2. Changed files are listed by domain.
3. Only matching validation and test jobs execute.
4. Only matching deployment jobs execute after merge.
