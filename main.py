import openai

model_engine = "gpt-3.5-turbo"  # ChatGPT 模型
conversation_history = []

# 定义获取聊天响应的函数
def get_chat_response(prompt):
    # 将用户消息压入暂存区
    entry_user = {"role": "user", "content": prompt}
    conversation_history.append(entry_user)

    try:
        # 调用 ChatCompletion API 生成聊天响应
        completions = openai.ChatCompletion.create(
            model=model_engine,
            messages=conversation_history,
            temperature=0.7,
            max_tokens=50,
            n=1,
            stop=None
        )

        # 保存聊天历史和响应结果
        v_response = completions.choices[0].message.content.strip()
        entry_assistant = {"role": "assistant", "content": v_response}
        conversation_history.append(entry_assistant)

        return v_response
    except Exception as e:
        # 如果报错，则移除本次用户prompt
        conversation_history.pop()
        return "OpenAI：网络响应异常，请尝试重试。（如无法解决，请键入 quit 退出程序）\n {}".format(str(e))


if __name__ == '__main__':
    openai.api_key = input("API_KEY(https://platform.openai.com/account/api-keys): ")

    # 测试聊天功能
    while True:
        user_input = input("Question: ")
        if user_input == "quit":
            print("AI: 再见！")
            break
        response = get_chat_response(user_input)
        print("AI: ", response)
