from flask import Flask

import main
app = Flask(__name__)

@app.route("/")
def site_index():
    return "<p>Welcome!!</p>"
    print(2 + 2)
    main.main()