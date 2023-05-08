import pyautogui

botao_fechar = 'imagens/botaofechar.png'
botao_fechar_red = 'imagens/botaofechar-red.png'
botaook = 'imagens/botaook.png'

# Enquanto a condição for verdadeira, tente encontrar o botão de fechar na tela.
while True:
    try:
        if pyautogui.locateOnScreen(botaook, confidence=0.8):
            img = pyautogui.locateOnScreen(botaook, confidence=0.8)
            pyautogui.click(img.left + img.width/2, img.top + img.height/2)
            break
    except:
        try:
            # Procura o botão de fechar na tela.
            img = pyautogui.locateOnScreen(botao_fechar, confidence=0.8)
            # Clica na imagem encontrada.
            pyautogui.click(img.left + img.width/2, img.top + img.height/2)
            break
        except:
            try:
                # Procura o botão de fechar na tela.
                img = pyautogui.locateOnScreen(
                    botao_fechar_red, confidence=0.8)
                # Clica na imagem encontrada.
                pyautogui.click(img.left + img.width/2, img.top + img.height/2)
                break
            except:
                pass
