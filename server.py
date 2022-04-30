from flask import Flask, render_template

app = Flask('Psychologist_Site')




@app.route('/')
def index_page():
    return render_template("index.html")


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
