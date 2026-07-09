# Dungeon Crawler

A turn-based combat game built as a full-stack web api, a Python game engine, a Flask REST API, and a JavaScript frontend.




## Skills Applied

- Object-oriented design —> Hero/Monster inherit from a shared base class, each overriding combat behavior independently
- REST API design (Flask) —> defined endpoints and response formats before building the frontend
- Frontend integration —>  JavaScript consuming the API / fetch()
- JSON-based data loading and save/load persistence

## What I Learned

- How to design a REST API and build a frontend that consumes it
- Managing state across stateless HTTP requests
- Debugging across a full stack — Python tracebacks and the browser console
- How inheritance and polymorphism replace repetitive conditional logic making code reusable and easy to spot a error

## Tech Stack

Python, Flask, JavaScript, HTML/CSS, JSON

## Run it locally

```bash
git clone https://github.com/Jrogers30/dungeon-crawler.git
cd dungeon-crawler
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

