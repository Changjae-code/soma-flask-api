from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        print("✅ 요청 도착, 데이터:", data)

        # 필드가 없으면 에러
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400

        # 응답 테스트용 더미 데이터
        result = {
            "이름": "홍길동",
            "생년월일": "900101",
            "성별": "남",
            "연락처": "010-1234-5678",
            "직업": "개발자",
            "운동목적": "체력증진",
            "특이사항": "무릎 통증",
        }

        return jsonify(result)

    except Exception as e:
        print("❌ 서버 오류:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
