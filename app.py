from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({'error': 'No image data provided'}), 400

    # 실제 OCR 대신 더미 데이터 반환
    return jsonify({
        "이름": "박혜영",
        "생년월일": "830827",
        "성별": "여",
        "연락처": "010-9161-8109",
        "직업": "사무직",
        "운동목적": "체중감량, 통증개선",
        "특이사항": "통증 부위: 어깨, 팔꿈치, 골반",
        "선호 요일": "월, 목, 토 오후",
        "요청 사항": "근력 + 유연성 향상, 등록제안"
    })
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
