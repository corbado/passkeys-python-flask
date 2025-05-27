<img width="1070" alt="GitHub Repo Cover" src="https://github.com/corbado/corbado-php/assets/18458907/aa4f9df6-980b-4b24-bb2f-d71c0f480971">

# Python Flask Passkeys Example Application

This is a sample implementation of the [Corbado passkeys-first authentication solution](https://www.corbado.com) using
Python with Flask. The following packages are being used:

- [Corbado web-js](https://github.com/corbado/javascript/tree/develop/packages/web-js)
- [Corbado Python](https://github.com/corbado/corbado-python)

[![integration-guides](https://github.com/user-attachments/assets/7859201b-a345-4b68-b336-6e2edcc6577b)](https://app.corbado.com/integration-guides/python-flask)

## File structure

- `app`: The Flask project
- `app/__init__.py`: The initialization file for the Flask app
- `app/models.py`: Defines our custom user model
- `app/config.py`: Flask configuration that should be available throughout our app
- `app/decorators.py`: Decorators to force authentication on API routes
- `app/routes.py`: Contains the routes for our application
- `app/project.db`: The sqlite database instance
- `templates/`: The Flask project templates

## Setup

### Prerequisites

Please follow the steps in [Getting started](https://docs.corbado.com/overview/getting-started) to create and configure
a project in the [Corbado developer panel](https://app.corbado.com/).

You need to have [Python](https://www.python.org/downloads/) and `pip` installed to run it.

### Configure environment variables

Use the values you obtained in [Prerequisites](#prerequisites) to configure the following variables inside a `.env`
file you create in the root folder of this project:

```sh
CORBADO_PROJECT_ID=pro-XXX
CORBADO_API_SECRET=corbado1_XXX
CORBADO_FRONTEND_API=https://${CORBADO_PROJECT_ID}.frontendapi.cloud.corbado.io
CORBADO_BACKEND_API=https://backendapi.cloud.corbado.io
```

## Usage

### Run the project locally

Run

```bash
python -m venv venv
```

to create a virtual environment.

Then, activate the virtual environment with

```bash
source venv/bin/activate
```

or

```bash
venv\Scripts\activate
```

on Windows.

To install all dependencies, run

```bash
pip install -r requirements.txt
```

Migrate your database by running

```bash
flask db upgrade
```

Now you can start the server by running

```bash
python run.py
```

## Passkeys support

- Community for Developer Support: https://bit.ly/passkeys-community
- Passkeys Debugger: https://www.passkeys-debugger.io/
- Passkey Subreddit: https://www.reddit.com/r/passkey/

## Telemetry

This example application uses telemetry. By gathering telemetry data, we gain a more comprehensive understanding of how our SDKs, components, and example applications are utilized across various scenarios. This information is crucial in helping us prioritize features that are beneficial and impactful for the majority of our users. Read our [official documentation](https://docs.corbado.com/corbado-complete/other/telemetry) for more details.

To disable telemetry, add the following line to your `.env` file:

```sh
CORBADO_TELEMETRY_DISABLED=true
```
