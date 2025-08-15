import streamlit as st
import pandas as pd

st.title("🎈 Make App great again")
st.write(
    "Let's start building!"
)


# st.title("1️⃣ ✅ 공개 Google Sheet 읽기")
# st.info("📘 누구나 볼 수 있도록 공개된 시트를 Pandas로 직접 불러오는 가장 간단한 방법입니다.\n📎 링크는 반드시 `export?format=csv` 형태로 설정하세요.")

# csv_url1 = "https://docs.google.com/spreadsheets/d/15BkUWph9nhKtNPrZylDKNYVs9xl3xGKUxfJLY749fuo/export?format=csv"
# df1 = pd.read_csv(csv_url1)
# st.dataframe(df1[['question_id', 'nickname']])

st.title("2️⃣ 🔐 공개 Google Sheet 읽기")
st.info("📘 Sheet는 여전히 공개 상태입니다. URL만 안전하게 숨기기 위해 `secrets.toml`에 저장합니다.")

csv_url2 = st.secrets["link"]["gsheet_public_csv_url"]
df2 = pd.read_csv(csv_url2)

# 📄 시트 전체 미리보기
st.dataframe(df2, use_container_width=True)

# 🔍 활성화된 질문 필터링
active_rows = df2[df2["is_active"] == True]

if active_rows.empty:
    st.warning("⚠️ 현재 활성화된 질문이 없습니다.")
else:
    for i, row in active_rows.iterrows():
        st.divider()
        st.subheader(f"📌 질문: {row['question_text']}")
        
        # 선택지 opt_a, opt_b, opt_c, ... 자동 추출
        options = [row[col] for col in df2.columns if col.startswith("opt_") and pd.notna(row[col])]
        
        # 사용자 응답 입력
        selected = st.radio(
            f"답을 골라주세요 (질문 ID: {row['question_id']})",
            options,
            key=f"question_{i}"
        )

        # ✅ 정답 확인
        correct = row["answer"]
        if selected:
            if selected == correct:
                st.success("✅ 정답입니다!")
            else:
                st.error(f"❌ 오답입니다. 정답은 **{correct}** 입니다.")



