# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script  # pylint:disable=import-error


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("مساعدة", url= "https://t.me/wsh22"),
                        InlineKeyboardButton("قناتي", url= "https://t.me/wsh23"),
                    ],
                    [
                        InlineKeyboardButton(
                            "تحميل من اليوتيوب",
                            url="https://t.me/YouTwisam_bot",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("رجوع", callback_data="start_data"),
                        InlineKeyboardButton("كلمني", "https://t.me/wsh22"),
                    ],
                    [
                        InlineKeyboardButton(
                            "تحميل من اليوتيوب",
                            url="https://t.me/YouTwisam_bot",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("عودة", callback_data="help_data"),
                        InlineKeyboardButton("ابدأ", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "تحميل من اليوتيوب",
                            url="https://t.me/youtwisam_bot",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass
