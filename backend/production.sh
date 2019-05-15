#!/bin/bash
gunicorn -b :5000 -w 4 app:create_app("Production")