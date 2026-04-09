from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import aiohttp



@register("astrbot_plugin_setuv0_1", "czx233", "一个简单的涩图插件", "0.0.1")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.api_url = "https://api.waifu.pics/sfw/waifu"

    @filter.command("setu")
    async def setu(self, event: AstrMessageEvent):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    image_url = data.get("url")
                    if image_url:
                        yield event.image_result(image_url)
                        logger.info(f"发送图片: {image_url}")
                    else:
                        yield event.plain_result("获取图片失败")
                else:
                    yield event.plain_result(f"请求失败，状态码: {resp.status}")
    async def terminate(self):
        pass



