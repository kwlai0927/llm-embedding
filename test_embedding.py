import requests
import json
import sys

def test_embedding():
    # 測試健康檢查端點
    try:
        health_response = requests.get("http://localhost:8000/healthz")
        print("健康檢查結果:", health_response.json())
        if health_response.status_code != 200 or health_response.json().get("status") != "ok":
            print("健康檢查未通過，結束測試。")
            sys.exit(1)
    except Exception as e:
        print("健康檢查失敗:", str(e))
        sys.exit(1)
    
    # 測試 embedding 端點
    test_text = "這是一個測試句子"
    payload = {"text": test_text}
    
    response = requests.post(
        "http://localhost:8000/embed",
        json=payload
    )
    
    if response.status_code == 200:
        result = response.json()
        print("\n輸入文本:", test_text)
        print("向量維度:", len(result["embedding"]))
        print("向量前5個元素:", result["embedding"][:5])
    else:
        print("錯誤:", response.status_code, response.text)

if __name__ == "__main__":
    test_embedding() 