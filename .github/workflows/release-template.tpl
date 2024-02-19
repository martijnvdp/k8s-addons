---
name: release-APP_NAME
on:
  push:
    branches:
      - main
    paths:
      - deployments/APP_NAME/**
  workflow_call:

jobs:
  call-release-workflow:
    uses: ./.github/workflows/release.yaml
    with:
      appname: APP_NAME
    needs: [changes]