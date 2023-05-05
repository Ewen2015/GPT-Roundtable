#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
author:     Ewen Wang
email:      wolfgangwong2012@gmail.com
license:    Apache License 2.0
"""

def get_prompt(topic, person1, person2, person3):
    prompt = f"\
    写一个对话录，以“人名：对话内容”的形式。\
    分别用{person1}、{person2}、{person3}的口吻，就以下主题发表看法：{topic}。\
    发言者的讨论要契合自己的哲学思想，观点和口吻要有自己的特点。\
    每个人讨论要尽可能深刻，有启发，发言要承接前一个人的发言，又有自己的思考，不能重复前面人的观点。\
    然后，他们相互讨论达成一个共识。\
    ".replace(" ", "")
    return prompt


def main():
    topic = "教育的内核是获得自由"
    person1 = "康德"
    person2 = "芒格"
    person3 = "波伏娃"

    prompt = get_prompt(topic, person1, person2, person3)


if __name__ == '__main__':
    main()