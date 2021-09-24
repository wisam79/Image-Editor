# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters


@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="اختر ما تريد فعله للصورة من القائمةㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="سطوع", callback_data="bright"),
                        InlineKeyboardButton(text="ميكس", callback_data="mix"),
                        InlineKeyboardButton(text="اسود وابيض", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="دائرة", callback_data="circle"),
                        InlineKeyboardButton(text="ضبابية", callback_data="blur"),
                        InlineKeyboardButton(text="اطار", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="ملصق", callback_data="stick"),
                        InlineKeyboardButton(text="تدوير", callback_data="rotate"),
                        InlineKeyboardButton(text="تباين", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="بني داكن", callback_data="sepia"),
                        InlineKeyboardButton(text="رسم", callback_data="pencil"),
                        InlineKeyboardButton(text="كارتون", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="عكسي", callback_data="inverted"),
                        InlineKeyboardButton(text="تشويه", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="ازالة الخلفية", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="غلق", callback_data="close_e"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("هناك شيء خاطئ!", quote=True)
            except Exception:
                return
