from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import base64
import io
import traceback

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400

        # base64 디코딩
        image_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(image_data))

        # OCR 분석 (kor+eng 언어팩이 설치되어 있어야 함)
        extracted_text = pytesseract.image_to_string(image, lang='kor+eng')

        # 추출된 텍스트를 콘솔에도 출력해보기
        print("🔍 OCR 결과:\n", extracted_text)

        # 텍스트에서 주요 정보 추출 (예시)
        result = {
            "이름": extract_field(extracted_text, ["이름"]),
            "생년월일": extract_field(extracted_text, ["생년월일", "생일"]),
            "성별": extract_field(extracted_text, ["성별"]),
            "연락처": extract_field(extracted_text, ["연락처", "전화"]),
            "직업": extract_field(extracted_text, ["직업"]),
            "운동목적": extract_field(extracted_text, ["운동 목적", "운동목적"]),
            "특이사항": extract_field(extracted_text, ["특별 요청", "특이사항", "요청 사항"]),
        }

        return jsonify(result)

    except Exception as e:
        print("🔥 에러 발생:", str(e))
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


def extract_field(text, keywords):
    """
    키워드 기반으로 OCR 텍스트에서 줄을 추출해주는 함수
    """
    for line in text.split('\n'):
        for keyword in keywords:
            if keyword in line:
                return line.replace(keyword, '').strip()
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)