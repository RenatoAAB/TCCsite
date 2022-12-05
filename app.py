import streamlit as st

audio_file = open("./Pre-processamento/funk_22050.wav",'rb')
funk22050 = audio_file.read()
audio_file = open("./Pre-processamento/funk_11000.wav",'rb')
funk11000 = audio_file.read()
audio_file = open("./Pre-processamento/funk_7000.wav",'rb')
funk7000 = audio_file.read()
audio_file = open("./Pre-processamento/funk_5500.wav",'rb')
funk5500 = audio_file.read()
audio_file = open("./Pre-processamento/funk_4000.wav",'rb')
funk4000 = audio_file.read()
audio_file = open("./Pre-processamento/funk_256classes.wav",'rb')
funk256 = audio_file.read()
audio_file = open("./Pre-processamento/funk_64classes.wav",'rb')
funk64 = audio_file.read()
audio_file = open("./Pre-processamento/funk_32classes.wav",'rb')
funk32 = audio_file.read()
audio_file = open("./Pre-processamento/funk_16classes.wav",'rb')
funk16 = audio_file.read()



audio_file = open("./MusicasGeradas/sashimi_100_best.wav",'rb')
sashimi1 = audio_file.read()
audio_file = open("./MusicasGeradas/sashimi_erro.wav",'rb')
sashimi2 = audio_file.read()
audio_file = open("./MusicasGeradas/sashimi_kond_1.wav",'rb')
sashimi3 = audio_file.read()
audio_file = open("./MusicasGeradas/sashimi_kond_ruido.wav",'rb')
sashimi4 = audio_file.read()
audio_file = open("./MusicasGeradas/sashimi_kond_grave.wav",'rb')
sashimi5 = audio_file.read()
audio_file = open("./MusicasGeradas/sashimi_mandelao.wav",'rb')
sashimi6 = audio_file.read()
audio_file = open("./MusicasGeradas/sashimi_mandelao2.wav",'rb')
sashimi7 = audio_file.read()

audio_file = open("./MusicasPConsertar/jukebox_abusadamente_bom.wav",'rb')
jukebox1 = audio_file.read()
audio_file = open("./MusicasPConsertar/jukebox_absudamente_ruim_15.wav",'rb')
jukebox2 = audio_file.read()
audio_file = open("./MusicasPConsertar/jukebox_mandelao1_ruim_16.wav",'rb')
jukebox3 = audio_file.read()
audio_file = open("./MusicasPConsertar/jukebox_mandelao2_ruim_16.wav",'rb')
jukebox4 = audio_file.read()
audio_file = open("./MusicasPConsertar/jukebox_mandelao3_ruim_18.wav",'rb')
jukebox5 = audio_file.read()
audio_file = open("./MusicasPConsertar/jukebox_mandelao4_ruim_18.wav",'rb')
jukebox6 = audio_file.read()




st.set_page_config(page_title="IAnita TCC")


st.subheader("Esse site é dedicado a disponibilizar os resultados de meu projeto de conclusão de curso")
st.subheader("Escola Politécnica da Universidade de São Paulo")
st.subheader("Renato A. A. Battistin")
st.title("IAnita: Um estudo de inteligência artificial para geração de funk")



with st.container():
    st.write("---")
    st.header("Introdução")
    st.write("##")
    st.write("    O principal objetivo deste projeto é criar uma inteligência artificial que seja capaz de gerar músicas do gênero funk brasileiro a partir de uma entrada qualquer inicial. A ideia é analisar e comparar os resultados obtidos com outros resultados já consolidados da área de estudo de machine learning e deep learning aplicados à música. Como projeto focado em desenvolver uma tecnologia nova e de resultados avaliados primeiramente de forma qualitativa, prevê-se uma metodologia experimental que vai testar diversas técnicas de aprendizado em conjunto com outras diversas análises exploratórias dos dados. Com tal processo iterativo, espera-se entender e melhorar a qualidade das músicas produzidas com o tempo. Espera-se também gerar ideias e análises no âmbito cultural e musical sobre a complexidade e a produção atual do funk brasileiro, mostrando que a ideia de que o funk é um tipo de música fácil e simples não passa de um mito.")

with st.container():
    st.write("---")
    st.header("Como foi realizado este estudo?")
    st.write("##")
    st.write("Este estudo se inspirou na metodologia experimental iterativa empregada para pesquisas no campo de Machine Learning. Primeiro, definiu-se um objetivo - no caso, gerar funks novos a partir de um modelo de Deep Learning utilizando o formato de áudio cru. Depois, foram levantadas todas as dificuldades de se trabalhar com esse formato de áudio e pesquisados modelos que representem o estado da arte nessa área. Foram selecionados 2 modelos: SaShiMi - para ser treinado do zero, e a rede Jukebox como prova dde conceito. Em seguida, foram realizadas fases de composição da base de dados intercaladas com fases de treinamento, de forma a buscar os melhores hiperparâmetros da rede, a melhor base possível, e os melhores pré-processamentos dessas bases - filtrando trechos que não condiziam com o funk. Assim, espera-se melhorar as amostras geradas pela rede. Importante ressaltar também que o projeto foi desenvolvido com recursos limitados, uma assinatura Pro+ do ambiente de desenvolvimento virtual da Google Colab foi todo o poder de processamento utilizado.")

with st.container():
    st.write("---")
    st.header("Análise de parâmetros para o pré-processamento dos dados")
    st.write("##")
    st.write("A composição da base de dados foi realizada a partir de áudios em formato cru (.mp3, .wav, etc.). Esse formato, porém, contém muito informação, o que o torna difícil de se trabalhar. Com isso em mente, reduziu-se a quantidade de informações nos trechos por meio da redução da frequência de amostragem e da diminuição dos níveis de codificação sonora.")

    st.subheader("Frequência de amostragem")
    st.write("A frequência de amostragem original dos áudios é 44100 Hz. Diminuir esse valor pode ocasionar efeitos que prejudicam a qualidade sonora do áudio - frequências mais agudas passam a ser pior representadas. Uma análise informal com base nos áudios abaixo concluiu que 7000 Hz já resolvia o problema de alocação de memória do ambiente de desenvolvimento e perdia pouca qualidade.")
    st.write("Funk 22050 Hz:")
    st.audio(funk22050, format="audio/wav")
    st.write("Funk 11000 Hz:")
    st.audio(funk11000, format="audio/wav")
    st.write("Funk 7000 Hz - escolhido como melhor:")
    st.audio(funk7000, format="audio/wav")
    st.write("Funk 5500 Hz - bom, mas perde alguns detalhes:")
    st.audio(funk5500, format="audio/wav")
    st.write("Funk 4000 Hz - qualidade consideravelmente prejudicada:")
    st.audio(funk4000, format="audio/wav")

    st.subheader("Quantidade de níveis sonoros")
    st.write("A quantidade de níveis sonoros original dos áudios é 16 bits, resultando em 65356 níveis sonoros distintos. Isso se traduz em 65356 classes para o algoritmo classificar cada ponto, o que é uma tarefa muito difícil. Para auxiliar, foi realizado a redução através de uma transformação chamada 'mu-law', que diminui os níveis sonoros minizando a perda de informação para um ouvido humano. Abaixo as reduções experimentadas:")
    st.write("Funk original para comparação (65356 classes):")
    st.audio(funk7000, format="audio/wav")
    st.write("Funk com 256 classes:")
    st.audio(funk256, format="audio/wav")
    st.write("Funk com 64 classes - escolhido por conter a maior redução com a menor perda perceptível:")
    st.audio(funk64, format="audio/wav")
    st.write("Funk com 32 classes - começa a existir ruído moderado atrás do som")
    st.audio(funk32, format="audio/wav")
    st.write("Funk com 16 classes - colocado para melhor exemplificação de ruído forte causado pela diminuição dos níveis sonoros:")
    st.audio(funk16, format="audio/wav")




with st.container():
    st.write("---")
    st.header("Arquiteturas trabalhadas")
    st.write("##")
    st.subheader("SaShiMi")
    st.write("##")
    st.write("SaShiMi é uma arquitetura criada no ínicio de 2022 baseada na teoria de controle de estados de espaço. Ela cria uma nova parametrização dessa técnica de forma a aplicá-la no contexto de sequências com longas depêndencias, por exemplo para trabalhar com áudio em formato cru. O código utilizado foi adaptado do repositório: https://github.com/HazyResearch/state-spaces/tree/main/sashimi.")
    st.image("./sashimi.png", caption="Especificação da arquitetura SaShiMi. Retirada da publicação original.")
    st.write("##")
    st.subheader("Jukebox")
    st.write("##")
    st.write("Jukebox é uma rede treinada pelo grupo OpenAI que utiliza representações reduzidas dos dados de entrada para gerar novas amostras. Essa ideia é realizada por estruturas chamadas VQ-VAEs, um tipo específico de variational autoencoder. O código utilizado foi adaptado do repositório: https://github.com/openai/jukebox.")
    st.image("./vae.png", caption="Ilustração de um VAE, bloco fundamental da arquitetura Jukebox.")


with st.container():
    st.write("---")
    st.header("Áudios gerados")
    st.write("##")
    st.subheader("SaShiMi - base de dados 1")
    st.write("##")
    st.write("A primeira base foi composta por 100 funks muito escutados em 2021, de diversos gêneros e produtoras diferentes. As gerações realizadas não compreenderam corretamente o funk, elas contém desde sons não ritmados à ruídos. Uma das melhores geradas é mostrada abaixo. Todas as músicas do SaShiMi tem os 4 primeiros segundos provenientes de uma música real, e os 4 últimos gerados pela rede.")
    st.write("##")
    st.audio(sashimi1, format="audio/wav")
    st.write("##")
    st.write("Um caso peculiar foi a amostra gerada em que a música simplesmente acabou no início da geração. Supõe-se que pode ter sido efeito da falta de filtragem neste primeira base de dados, pois as outras bases de dados passaram por esse processo e esta foi a única amostra gerada assim.")
    st.write("##")
    st.audio(sashimi2, format="audio/wav")
    st.subheader("SaShiMi - base de dados 2")
    st.write("##")
    st.write("A segunda base de dados usada para treinamento contém apenas músicas da produtora Kondzilla, tentando reduzir a variância das amostras através de restringir o estilo de edição empregado nas músicas. Gerou áudios como o seguinte: ")
    st.audio(sashimi3, format="audio/wav")
    st.write("##")
    st.write("Ainda existem muitas amostras consideradas meio que ruídos: ")
    st.audio(sashimi4, format="audio/wav")
    st.write("##")
    st.write("Porém, com essa base, apesar das melhores métricas de treinamento, a rede parece ter percebido a grande presença de graves na música funk, e começou a acertar mais só criando graves sem nenhuma musicalidade: ")
    st.audio(sashimi5, format="audio/wav")
    st.write("##")
    st.subheader("SaShiMi - base de dados 3")
    st.write("##")
    st.write("A terceira base de dados usada para treinamento contém apenas músicas do subgênero Mandelão e tenta melhorar os resultados reduzindo a variabilidade oriunda dos gêneros presentes na base. Os resultados não diferem muito da primeira geração, provavelmente porque dentro das amostras ainda existe bastante variação, já que as músicas contém diferentes produtores. Algumas das músicas selecionadas aleatoriamente para a partição de teste são razoavelmente distintas do resto. Abaixo algumas das amostras geradas:")
    st.audio(sashimi6, format="audio/wav")
    st.audio(sashimi7, format="audio/wav")
    st.write("##")


    st.subheader("Jukebox")
    st.write("##")
    st.write("O modelo aqui utilizado '1b_lyrics' foi treinado pela OpenAI em uma base de 1,2 milhão de músicas de vários gêneros e utilizando uma capacidade computacional estimada em mais de 5 milhões de dólares. Ele gerou uma das únicas amostras condizentes com o gênero funk utilizando como condicionamento um trecho de 15 segundos da música 'Abusadamente'. Percebe-se um vocal inglês, mas o ritmo foi compreendido e continuado de forma natural pela rede.")
    st.write("##")
    st.audio(jukebox1, format="audio/wav")
    st.write("Com a mesma entrada também foram geradas amostras que falharam em seguir a proposta da música, provavelmente pela base de dados utilizada em seu treinamento, que contém outros gêneros e nenhum funk, além de 600 mil das 1.2 milhão de músicas serem da língua inglesa.")
    st.audio(jukebox2, format="audio/wav")
    st.write("Em outro teste com uma entrada menos regular, que transiciona de um ritmo para outro, a rede teve resultados piores. Abaixo a amostra foi condicionada em 16 segundos de música.")
    st.audio(jukebox3, format="audio/wav")
    st.audio(jukebox4, format="audio/wav")
    st.write("E mesmo aumentando esse tempo de condicionamento de 16 para 18 segundos, dando mais acesso ao novo ritmo sendo tocado, não foi suficiente para melhoras significativas: ")
    st.audio(jukebox5, format="audio/wav")
    st.audio(jukebox6, format="audio/wav")


    with st.container():
        st.write("---")
        st.header("Conclusões")
        st.write("##")
        st.write("Fica claro que o funk é como qualquer outro estilo, tem suas nuances, complexidades, mas também suas características marcantes que dão origem ao gênero. Sua importância cultural não deve ser subestimada, e ele pode ser sim objeto de estudos acadêmicos. Do ponto de vista técnico, é uma música ritmada que tem potencial para gerar novos insights na área do Deep learning. Contudo, essa área se mostra computacionalmente muito custosa, requerendo muito investimento em servidores especializados para o treinamento das redes. Só assim essas arquiteturas podem atingir seu verdadeiro potencial e de fato representar e reproduzir uma parte da arte, da subjetividade do ser humano por meio de um evento matemático-antropofágico.")
