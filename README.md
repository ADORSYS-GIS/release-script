# release-script

This documentation is a WIP (Work in Progress)...

## Local Development
- Setup a new venv (if not done already)
  ```shell
  python3 -m venv venv
  ```

- Source it
  ```shell
  source venv/bin/activate
  ```

- Install the project dependencies:
  ```shell
  pip install -r test.requirements.txt -r requirements.txt
  ```

- Run tests locally:
  ```shell
  pytest --cov=src
  ```

- Run code linting, to detect wrong code or bad practices
  ```shell
  flake8 ./src --count --show-source --statistics
  ```
  
- Run security tests
  ```shell
  bandit -r . --ll -ii -x ./test -x ./venv
  ```