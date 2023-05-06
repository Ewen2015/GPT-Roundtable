#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
author:     Ewen Wang
email:      wolfgangwong2012@gmail.com
license:    Apache License 2.0
"""
import json
import openai

def setup_openai(path_config):
    with open(path_config) as f:
        config = json.load(f)

    openai.organization = config["OPENAI_ORG_ID"]
    openai.api_key = config["OPENAI_API_KEY"]
    return None

def get_completion(prompt, model="gpt-3.5-turbo-0301", temperature=1):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def get_prompt(topic, person1, person2, person3):
    prompt = f"""
    写一个对话录，以“人名：对话内容”的形式。人名要加粗，Markdown格式。\
    分别用{person1}、{person2}、{person3}的口吻，就以下主题发表看法：{topic}。\
    发言者的讨论必须反应出自己的人生经历、哲学思想、身分，口吻要符合自己的特点。\
    发言不能重复别人和自己的发言。\
    参考以下例子：<芒格(实用主义投资家):我更看重教育的实际效益。\
    教育要培养具有创新精神与判断力的人才,让他们适应社会变化,解决各种复杂问题。\
    知识与技能要与时俱进,不断自我更新,以适应社会发展的需要。教育不应只注重理论知识,更要关注知识的运用与创新。\
    重要的不是知识本身,而是知识如何在实践中发挥作用,创造价值,实现自我与社会的进步。>
    """
    return prompt


def main():
    path_config = "/Users/ewang1/Documents/openai.json"
    
    topic = "教育的内核是获得自由"
    person1 = "康德"
    person2 = "芒格"
    person3 = "波伏娃"

    setup_openai(path_config)
    prompt = get_prompt(topic, person1, person2, person3)
    response = get_completion(prompt)
    
    return response


if __name__ == '__main__':
    main()