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
            "생년월일": "1990-01-01",
            "성별": "남성",
            "연락처": "010-1234-5678",
            "직업": "소프트웨어 엔지니어",
            "운동목적": "장시간 앉아 있는 직업 특성으로 인한 근골격계 질환 예방 및 체력 증진",
            "특이사항": (
                "최근 6개월간 오른쪽 무릎에 간헐적 통증이 있으며, 특히 계단을 오르내릴 때 통증이 심해짐.\n"
                "과거 요추디스크 수술 이력이 있으며, 현재는 장시간 앉은 자세 후 허리 통증이 재발함.\n"
                "평소 오른쪽 어깨가 올라가 있으며, 좌측 골반이 내려가 있는 자세 불균형이 관찰됨.\n"
                "스트레스 수준이 높고 수면 시간이 부족하여 전반적인 회복력이 낮은 상태."
            ),
            "AI 분석 요약": (
                "1. **운동 기능 평가 결과**, 자세 불균형(상체 우측 경사, 하체 좌측 기울어짐)이 지속적으로 관찰되며, "
                "오른쪽 무릎 주변 근육의 긴장도 증가로 인한 통증 유발 가능성이 높음.\n"
                "2. **직업 특성상 앉은 자세가 많아**, 대퇴근·햄스트링·요방형근의 유연성 저하와 요추 과신전 패턴이 동반됨.\n"
                "3. **회복 및 휴식 상태가 좋지 않아**, 고강도 프로그램보다는 점진적인 기능 향상 중심의 맞춤 운동이 권장됨.\n"
                "4. 스트레스와 관련된 신체 반응(복부 긴장, 상부 승모근 활성화)도 확인됨.\n"
            ),
            "추천 운동 프로그램": (
                "- 코어 안정화 운동 (Dead Bug, Bird Dog)\n"
                "- 고관절 가동성 향상 (90/90 Hip Mobility, Hip CARs)\n"
                "- 무릎 안정화 운동 (Step Down, Terminal Knee Extension)\n"
                "- 자세교정 스트레칭 (Upper Trap Stretch, Piriformis Stretch)\n"
                "- 회복 강화를 위한 저강도 호흡 운동 및 명상 5분 포함\n"
            )
        }

        return jsonify(result)

    except Exception as e:
        print("❌ 서버 오류:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
