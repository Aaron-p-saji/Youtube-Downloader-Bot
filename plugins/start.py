from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/achuz_z2004")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/achuz_z2004")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info \n This Bot Developed By Aaron"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
