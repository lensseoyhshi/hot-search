import os
from openai import OpenAI

# 构造 client
client = OpenAI(
    api_key="sk-dZbQUPMPpqV7rBGdCh3XZkesP52ZuqFpT12vSSI6qyckkazw",  # 混元 APIKey
    base_url="https://api.hunyuan.cloud.tencent.com/v1",  # 混元 endpoint
)

completion = client.chat.completions.create(
    model="hunyuan-large",
    messages=[
        {
            "role": "user",
            "content": "查询2025年4月3日明星新闻，每个新闻的标题跟着详情"
        }
    ],
    extra_body={
        "enable_enhancement": True,  # <- 自定义参数
        "force_search_enhancement": True,  # <- 自定义参数
        # "enable_deep_read": True,  # <- 自定义参数
        "search_info": True,  # <- 自定义参数
    },
)
print(completion.choices[0].message.content)