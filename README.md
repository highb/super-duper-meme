# super-duper-meme
Super Duper Meme Generator

## Components

* frontend - The user-facing website
* api - The backend API that powers the website, as well as integrators.

## Manual Setup

Here are the steps to setup/deploy these services:

* Install Python3

* Setup a virtualenv for each component/deployment, activate, and install requirements

```bash
./app.sh frontend deps
./app.sh api deps
```

* Start each service

```bash
./app.sh frontend run
./app.sh api run
```