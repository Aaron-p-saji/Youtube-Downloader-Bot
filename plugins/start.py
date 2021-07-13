from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Developer", url="https://t.me/achuz_z2004")],
        [InlineKeyboardButton(
            "Our Other Bots 😊", url="https://t.me/aaronsbotz")],
        [InlineKeyboardButton(
            "Need Our Repo Link 😊", url="https://t.me/achuz_z_2004")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info \n This Bot Developed By <b>Aaron</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
