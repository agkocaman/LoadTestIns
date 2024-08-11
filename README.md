
---

# Search Module Load Test

This repository contains a simple load test for the search module on the n11.com website. The test is written using [Locust](https://locust.io/), a Python-based load testing tool.

## Description

This test script sends search requests to the n11.com website using different search terms to see how the search module responds. The script checks whether the search results are correctly displayed for each term.

## Test Scenarios

The test script performs the following tasks:
1. Sends search requests using the following terms:
   - `ayakkabı`
   - `bilgisayar`
   - `defter`
   - `kumanda`
   - `buzdolabı`
2. Checks if the search was successful and if the results contain the expected content.
3. Logs success or failure for each search term.

## Requirements

- Python 3.7+
- Locust

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/agkocaman/LoadTestIns.git
   cd LoadTestIns
   ```

2. Install the required Python packages:
   ```sh
   pip install locust
   ```

## Usage

To run the load test, use the following command:

```sh
locust -f search_load.py
```

Then, open your browser and go to `http://localhost:8089` to start the test.
