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
        # 使用 -O 覆盖模式，文件名保持 result.json
        cmd = f'scrapy crawl universal_spider -a url="{target_url}" -O result.json'

        # 异步启动
        subprocess.Popen(cmd, shell=True, cwd=scrapy_project_path)
        return jsonify({"message": "多页抓取任务已启动，请观察 PyCharm 控制台"}), 200

    return jsonify({"message": "无效 URL"}), 400


if __name__ == '__main__':
    app.run(port=5000, debug=True)


#负责接收插件指令并启动 Scrapy。