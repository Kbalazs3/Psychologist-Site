from flask import Flask, render_template

app = Flask('Psychologist_Site')


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/introduction')
def introduction():
    return render_template("introduction.html")


@app.route('/service')
def service_and_price():
    pass



@app.route('/contact')
def contact_page():
    return render_template("contact.html")


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
