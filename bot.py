from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "SEU_TOKEN_AQUI"

menu = [
    ["Gerador de Copy", "Ideias de Anúncio"],
    ["Roteiro de Vídeo", "Ideias de Gancho"],
    ["Biblioteca de Anúncios"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text(
        "🚀 Painel de Marketing para Afiliados\n\nEscolha uma ferramenta:",
        reply_markup=keyboard
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if texto == "Gerador de Copy":
        resposta = """
🔥 COPY DE ANÚNCIO

Você sabia que muitas pessoas estão usando
um método simples para aumentar suas vendas online?

Descubra como começar hoje mesmo.

👉 Clique e veja o método completo.
"""
    elif texto == "Ideias de Anúncio":
        resposta = """
💡 IDEIAS DE ANÚNCIO

1. Antes e depois do resultado
2. História de transformação
3. 3 erros que iniciantes cometem
4. Demonstração do produto
"""
    elif texto == "Roteiro de Vídeo":
        resposta = """
🎬 ROTEIRO

Cena 1
Mostre o problema.

Cena 2
Explique rapidamente a solução.

Cena 3
Mostre o resultado.

Cena 4
Convide para clicar no link.
"""
    elif texto == "Ideias de Gancho":
        resposta = """
⚡ GANCHOS

• "Pouca gente sabe disso..."
• "Eu descobri algo incrível..."
• "3 erros que você precisa evitar..."
"""
    elif texto == "Biblioteca de Anúncios":
        resposta = """
📚 ANÚNCIOS

1. "Descubra o método que está ajudando iniciantes."
2. "Aprenda passo a passo mesmo começando do zero."
"""
    else:
        resposta = "Escolha uma opção do painel."

    await update.message.reply_text(resposta)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, responder))

app.run_polling()
