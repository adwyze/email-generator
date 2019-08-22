## Getting Started

#### install pipenv
- run `pip install pipenv`


#### install dependencies
- run `cd email-generator`
- run `pipenv install --dev`


#### activate the virtual environment
- run `pipenv shell`


#### publish the new built templates
- run `python mandrill_operations.py --key your-mandrill-key --operation update --email acb.xyz@fff.com --template_name anomaly-alert --file_name anomalyAlert.html`

