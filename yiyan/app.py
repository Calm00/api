from flask import Flask, jsonify
import random
import json
import os

app = Flask(__name__)

def load_sentences():
    """从JSON文件加载句子"""
    try:
        with open('sentences.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('sentences', [])
    except FileNotFoundError:
        # 如果文件不存在，创建一个包含默认句子的文件
        default_sentences = {
            "sentences": [
                "生命不止，奋斗不息",
                "人生就像一场马拉松，重要的不是比快，而是坚持到底",
                "没有人可以回到过去重新开始，但谁都可以从现在开始，书写一个全新的结局"
            ]
        }
        with open('sentences.json', 'w', encoding='utf-8') as f:
            json.dump(default_sentences, f, ensure_ascii=False, indent=4)
        return default_sentences['sentences']

@app.route('/yiyan')
def yiyan():
    return jsonify({"message": "欢迎使用一言API"})

@app.route('/yiyan/get')
def get_yiyan():
    sentences = load_sentences()
    random_sentence = random.choice(sentences)
    return jsonify({"sentence": random_sentence})

if __name__ == '__main__':
    app.run(debug=True)