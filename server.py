from flask import Flask, render_template

app = Flask('Psychologist_Site')


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
