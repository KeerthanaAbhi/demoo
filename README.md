# OpenShift Pipeline Demo

A small Python HTTP application and CI/CD example for OpenShift Pipelines.

## Application

The application listens on port **8000** and prints the required startup marker:

`SERVICERUNNING`

Run locally:

```bash
python app.py
```

Check it:

```bash
curl http://localhost:8000/
```

## GitHub Actions

The workflow at `.github/workflows/workflow.yml` runs Python linting and unit tests on pushes and pull requests to `main`.

## OpenShift / Tekton

The Tekton definitions are in `.tekton/tasks.yml`. They define the pipeline stages:

1. cleanup
2. git-clone
3. flake8
4. nose
5. buildah
6. deploy (using `openshift-client`)

Apply the definitions to an OpenShift project with Tekton Pipelines installed:

```bash
oc apply -f .tekton/tasks.yml
```

The Buildah task pushes the image to the image reference supplied through the PipelineRun parameter `IMAGE`. The deploy task updates the deployment named `demoo` to use that image and exposes port 8000.

## Required environment

- OpenShift cluster with Pipelines (Tekton) installed
- A Git clone task named `git-clone` available in the namespace (commonly installed from the Tekton Catalog)
- A registry destination writable by the Buildah task, supplied as `IMAGE`
- Permission for the pipeline service account to build/push images and deploy workloads

## Repository layout

- `app.py` — HTTP service on port 8000
- `Dockerfile` — container image definition
- `tests/test_app.py` — unit test
- `.github/workflows/workflow.yml` — GitHub Actions workflow
- `.tekton/tasks.yml` — Tekton tasks and pipeline
