from flask import Flask

import main
app = Flask(__name__)

@app.route("/")
def site_index():
    return "<p>Hmm, that's not what I'd expected!</p>"
    main.main()