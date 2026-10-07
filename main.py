name: Run Headless Camoufox

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  workflow_dispatch: # Allows manual trigger from the GitHub Actions tab

jobs:
  run-camoufox:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository code
        uses: actions/checkout@v4

      - name: Set up Python Environment
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install Camoufox Python Package
        run: |
          python -m pip install --upgrade pip
          pip install -U "camoufox[geoip]"

      - name: Cache Camoufox Browser Binaries
        id: cache-camoufox
        uses: actions/cache@v4
        with:
          path: ~/.cache/camoufox
          key: ${{ runner.os }}-camoufox-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-camoufox-

      - name: Install Missing Ubuntu System GUI Libraries
        run: |
          sudo apt-get update
          sudo apt-get install -y --no-install-recommends \
            libgtk-3-0 \
            libx11-xcb1 \
            libasound2 \
            libdbus-glib-1-2 \
            libxt6

      - name: Fetch Camoufox Browser
        if: steps.cache-camoufox.outputs.cache-hit != 'true'
        run: python3 -m camoufox fetch

      - name: Verify Installation Versions
        run: python3 -m camoufox version

      - name: Run Script
        run: python main.py
