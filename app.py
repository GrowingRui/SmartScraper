from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)


@app.route('/scrape', methods=['POST'])
def run_scraper():
    data = request.json
    target_url = data.get('url')

    base_dir = os.path.abspath(os.path.dirname(__file__))
    scrapy_project_path = os.path.join(base_dir, "scrapy_app")

    if target_url:
        # 使用 -O (大写) 覆盖旧文件，确保数据不重叠
        cmd = f'scrapy crawl universal_spider -a url="{target_url}" -O result.json'

        # 启动子进程
        subprocess.Popen(cmd, shell=True, cwd=scrapy_project_path)
        return jsonify({"message": "多页爬取任务启动，请在 PyCharm 控制台监控进度"}), 200

    return jsonify({"message": "URL无效"}), 400


if __name__ == '__main__':
    app.run(port=5000, debug=True)


#负责接收插件指令并启动 Scrapy。