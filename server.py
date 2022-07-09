from flask import Flask, render_template, url_for
from data_store import file_manager

app = Flask('Psychologist_Site')


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/introduction')
def introduction():
    return render_template("introduction.html")


@app.route('/service')
def service_and_price():
    return render_template("service_and_price.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


# data_store.file_manager("data/blog_article/flow_article")


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
