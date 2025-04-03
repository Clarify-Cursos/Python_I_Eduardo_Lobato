#importar os packages IPython e Image

# from PIL import Image, ImageDraw, ImageFont: Esta linha importa os componentes necessários da biblioteca Pillow (PIL).
# Imagem: Usado para criar e manipular imagens.
# ImageDraw: Usado para desenhar formas e texto em imagens.
# ImageFont: Usado para carregar e usar fontes de texto.
# from IPython.display import Image as imgx: Esta linha importa a classe Image de IPython.display e a renomeia para imgx.

from PIL import Image, ImageDraw, ImageFont
from IPython.display import Image as imgx

#declarando as variáveis
nomes = ['Jeferson', 'Vitor', 'Mariana']
evento = 'Formatura do curso de Python'
data = '28 de fevereiro de 2025'
local = 'Av. Paulista, 1439'


for nome in nomes:
    #criando uma imagem em rgb com fundo branco (600x400px)
    img = Image.new("RGB", (600,400), (255,255,255))
    
    #preparando a ferramenta para desenhar a imagem
    draw = ImageDraw.Draw(img)

    #fontes que serão usadas no texto:chamamos o arquivo de texto e configuramos o tamanho da fonte
    font_title = ImageFont. truetype("arial.ttf", 36)
    font_text = ImageFont.truetype("arial.ttf", 24)

    # draw.text(...): Esta linha é repetida várias vezes para adicionar texto à imagem nas coordenadas especificadas, usando a cor preta (0, 0, 0) e a fonte carregada. Ele usa uma string F para personalizar o convite com o nome atual.
    draw.text((50,50), f'Convite para {nome}', (0,0,0), font=font_title)
    draw.text((50,100), evento, (0,0,0), font=font_title)
    draw.text((50,150), data, (0,0,0), font=font_title)
    draw.text((50,200), local, (0,0,0), font=font_title)
    
    # Desenhando um retângulo e salvando a imgem
    draw.rectangle([(45,45), (555,355)], outline="black", width=2)
        
    img.save(f'{nome}.jpg')
    print('Criado com sucesso !')

   

        
    


