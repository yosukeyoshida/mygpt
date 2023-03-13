import os

import openai
import streamlit as st

openai.api_key = os.environ["OPENAI_API_KEY"]


def main():
    system_text = st.text_area("AIアシスタントの設定", value="あなたはアシスタントAIです。")
    user_text = st.text_area(
        "質問文",
        value="うどんの茹で方教えて",
    )
    is_generate_clicked = st.button("文章生成")

    if is_generate_clicked:
        message = [{"role": "system", "content": system_text}, {"role": "user", "content": user_text}]
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message, max_tokens=2000, temperature=0, stream=True)

        partial_words = ""
        answer = st.empty()

        for chunk in response:
            if chunk and "delta" in chunk["choices"][0] and "content" in chunk["choices"][0]["delta"]:
                partial_words += chunk["choices"][0]["delta"]["content"]
                answer.write(partial_words)


if __name__ == "__main__":
    main()
