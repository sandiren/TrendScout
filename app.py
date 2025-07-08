from flask import Flask, render_template, request
from trends import get_trends

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    error = None
    keyword = ''
    region = ''

    if request.method == 'POST':
        keyword = request.form.get('keyword', '').strip()
        region = request.form.get('region', '').strip().upper()

        print("Keyword:", keyword)
        print("Region:", region)

        try:
            results = get_trends(keyword, region)
            print("Results found:", len(results))
        except Exception as e:
            error = str(e)
            print("Error:", error)

    return render_template('index.html', results=results, keyword=keyword, region=region, error=error)


if __name__ == '__main__':
    app.run(debug=True)