from flask import Flask

import logging

import main
app = Flask(__name__)

@app.route("/")
def site_index():
    app.logger.info('Testing info logger!!')
    main.main()
    return "<p>Welcome!!</p>"