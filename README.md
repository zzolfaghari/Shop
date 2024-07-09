# Online Shop Serve

------------
## Clone The Project

To clone with https
```bash
git clone https://github.com/zzolfaghari/Shop.git
```

Checkout to products-api
```bash
git checkout products-api
```

## Create a Virtual Environment


#### Using Terminal Manually (Ubuntu)
- Install `python3-venv` package
  ```bash
  sudo apt install python3.11-venv
  ```
- Go to `Shop/` directory

- Create virtual environment
    ```bash
    python3.11 -m venv your-env-name
    ```
- Activate the environment
  ```bash
  source your-env-name/bin/activate
  ```

## Install Requirements


```bash
pip install -r requirements.txt
```

## Setting Environmental Variables
A `.env` file which contains environmental variables of the project has to be placed at the
root directory of the project, next to `manage.py` file.


## Running The Service

#### Using Terminal
In the root directory `Shop/OnlineShop` run
```bash
python3 manage.py runserver
```

## Running Tests

```bash
python3 manage.py test main.tests
```

