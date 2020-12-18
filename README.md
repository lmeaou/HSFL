# HYPER SPEED FILE LIFT (HSFL)

some file sharing util

# dev environnement setup

1. clone repo
2. `sudo apt install python3-venv`
3. `python3 -m venv venv`
4. `. venv/bin/activate`
5. `pip3 install -r requirements.txt`

# dev environnement activation
1. `. venv/bin/activate`
2. `flask run`

If adding dependencies with `pip3`, add them to `requirements.txt` with `pip-freeze.sh`.

# run flask in dev mode
`export FLASK_ENV=development` then `flask run`.
