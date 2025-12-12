# main.py

# Chol_Minjun/main.py

# 파인튜닝된 모델을 쉽게 사용하기 위해 pipeline을 사용합니다.
from transformers import pipeline

# ✨ 문체 변환에 최적화된 파인튜닝된 모델 (heegyu/kobart-text-style-transfer) 사용
MODEL_NAME = "heegyu/kobart-text-style-transfer" 

# Model 로드 (최초 실행 시 다운로드 필요)
# pipeline은 모델 로드 시 발생했던 경고(num_labels) 문제도 자동으로 처리합니다.
style_transfer_pipe = pipeline(
    "text2text-generation", 
    model=MODEL_NAME
)

def convert_style(input_text: str, target_style: str) -> str:
    """
    입력 텍스트를 지정된 스타일로 변환합니다.
    """
    # 모델이 인식하도록 입력 형식을 '목표 말투로 변환: [원문]' 형태로 포맷합니다.
    prompt = f"{target_style} 말투로 변환:{input_text}"
    
    # 텍스트 생성 (generate)
    # max_length와 기타 옵션은 모델 카드에서 권장하는 값을 사용합니다.
    # 이 모델은 반복 문제에 대한 저항력이 강합니다.
    result = style_transfer_pipe(
        prompt, 
        max_length=64, 
        num_beams=5, 
        early_stopping=True
    )
    
    # 결과 추출
    converted_text = result[0]['generated_text']
    return converted_text

if __name__ == "__main__":
    
    # 1. 원문 (딱딱한 문체)
    hard_text = "본 프로젝트는 기한 내에 완료되어야 하며, 모든 팀원은 지침을 엄수해야 합니다."
    print("=" * 60)
    print(f"**원문 (딱딱):** {hard_text}")
    
    # 2. '친근하게' 변환 요청
    friendly_text = convert_style(hard_text, "친근한")
    print(f"**변환 (친근):** {friendly_text}")
    
    # 3. 다른 스타일로 변환 요청 (예: '아재' 말투)
    hard_text_2 = "보고서에 결과값이 누락되었습니다. 수정하시기 바랍니다."
    ajae_text = convert_style(hard_text_2, "아재")
    print("\n" + "-" * 60)
    print(f"**원문 (딱딱):** {hard_text_2}")
    print(f"**변환 (아재):** {ajae_text}")
    print("=" * 60)