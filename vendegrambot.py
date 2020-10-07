#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def productos(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Los productos disponibles son:')

def servicios(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Los servicios disponibles son:')


def buscar(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Para que encuentres lo que necesites')

def zonas(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Aqui podras ver las zonas cercana de nuestros suscriptores')

def vendedores(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Pronto podras visualizar una lista de todos nuestros suscriptores')

def vendedoresinfo(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Pronto podras visualizar los detalles de nuestros suscriptores')


def informacion(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Bienvenidos Somo VendeGram Donde esperemos que encuentres lo que buscas recuerda que puedes encontrarnos en www.vendegram.com. Puedes seleccionar los diferentes opciones en el menu /')

def quienessomos(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Somos un grupos de jovenes aficionados a la programacion por lo que nos unimos para llevarles este proyecto al beneficio de todos, para que los emprendedores y pequeños comerciantes tenga un espacio en la web y ustedes como sus clientes puedan disponer de sus productos actualizados mediente este bot')

def contactanos(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Puedes contactarnos al correo telegram@gmail.com. Donde atenderemos tu duda, consulta o requerimiento')


# def bop(bot, update):
#     url = get_image_url()
#     chat_id = update.message.chat_id
#     bot.send_photo(chat_id=chat_id, photo=url)

# def p(update, context):
#     """Send a message when the command /start is issued."""
#     update.message.reply_text('Hi!')

def iduser(update, context):
    
    chat_id=update.effective_chat.id
    if (chat_id == 643117404):
        msj = "hola Oscar"
    else:
        msj =f"Bienvenido {chat_id}"
    update.message.reply_text(msj)



def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def start(update, context):
    chat_id=update.effective_chat.id
    bien = "En que podemos ayudarte hoy. \n Recuerda seleccionar el boton / para ver las opciones disponibles"
    if (chat_id == 643117404):
        msj = f"Bienvenido Oscar. {bien}"
    else:
        msj =f"Bienvenido {chat_id}. {bien}"
    update.message.reply_text(msj)


def vendegramb():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1191654751:AAHKJSDfYup7YKpW5ZyLbt-caGEs5PA8qig", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("productos", productos))
    dp.add_handler(CommandHandler("servicios", servicios))
    dp.add_handler(CommandHandler("buscar", buscar))
    dp.add_handler(CommandHandler("zonas", zonas))
    dp.add_handler(CommandHandler("vendedores", vendedores))
    dp.add_handler(CommandHandler("vendedoresinfo", vendedoresinfo))
    dp.add_handler(CommandHandler("informacion", informacion))
    dp.add_handler(CommandHandler("quienessomos", quienessomos))
    dp.add_handler(CommandHandler("contactanos", contactanos))
    dp.add_handler(CommandHandler("idtelegram", iduser))
    dp.add_handler(CommandHandler("ayuda", help_command))
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    vendegramb()
