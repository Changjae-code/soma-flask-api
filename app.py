from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import base64
import io
import os
import traceback

app = Flask(__name__)

# ✅ Tesseract 경로 (Windows용)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400

        # base64 디코딩
        image_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(image_data))

        # OCR 분석
        extracted_text = pytesseract.image_to_string(image, lang='kor+eng')

        # 텍스트에서 정보 추출
        result = {
            "이름": extract_field(extracted_text, ["이름"]),
            "생년월일": extract_field(extracted_text, ["생년월일", "생년월", "생일"]),
            "성별": extract_field(extracted_text, ["성별"]),
            "연락처": extract_field(extracted_text, ["연락처", "전화"]),
            "직업": extract_field(extracted_text, ["직업"]),
            "운동목적": extract_field(extracted_text, ["운동 목적", "운동목적"]),
            "특이사항": extract_field(extracted_text, ["특별 요청", "특별사항", "요청 사항"]),
            "전체텍스트": extracted_text.strip()
        }

        return jsonify(result)


    except Exception as e:
        print("🔥 에러 발생:", str(e))
        traceback.print_exc()  # 전체 스택트레이스 출력
        return jsonify({'error': str(e)}), 500

def extract_field(text, keywords):
    for keyword in keywords:
        for line in text.split('\n'):
            if keyword in line:
                return line.replace(keyword, '').replace(':', '').strip()
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
