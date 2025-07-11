import logging
from flask import Flask, render_template, request
from trends import get_trends

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

        logger.info('Keyword: %s', keyword)
        logger.info('Region: %s', region)

        try:
            results = get_trends(keyword, region)
            logger.info('Results found: %s', len(results))
        except Exception as e:
            error = str(e)
            logger.error('Error: %s', error)

    return render_template('index.html', results=results, keyword=keyword, region=region, error=error)


if __name__ == '__main__':
    app.run(debug=True)
