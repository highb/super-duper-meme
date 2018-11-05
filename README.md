# super-duper-meme

Super Duper Meme Generator

## Components

* frontend - The user-facing website
* api - The backend API that powers the website, as well as integrators.

## Setup

Use `docker-compose build && docker-compose up` to build and run.

If you want to do the builds manually:

```bash
pushd api; docker build -t super-duper-meme_api .; popd
pushd frontend; docker build -t super-duper-meme_frontend .; popd
```