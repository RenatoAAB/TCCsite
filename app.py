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


st.subheader("Esse site ?? dedicado a disponibilizar os resultados de meu projeto de conclus??o de curso")
st.subheader("Escola Polit??cnica da Universidade de S??o Paulo")
st.subheader("Renato A. A. Battistin")
st.title("IAnita: Um estudo de intelig??ncia artificial para gera????o de funk")



with st.container():
    st.write("---")
    st.header("Introdu????o")
    st.write("##")
    st.write("    O principal objetivo deste projeto ?? criar uma intelig??ncia artificial que seja capaz de gerar m??sicas do g??nero funk brasileiro a partir de uma entrada qualquer inicial. A ideia ?? analisar e comparar os resultados obtidos com outros resultados j?? consolidados da ??rea de estudo de machine learning e deep learning aplicados ?? m??sica. Como projeto focado em desenvolver uma tecnologia nova e de resultados avaliados primeiramente de forma qualitativa, prev??-se uma metodologia experimental que vai testar diversas t??cnicas de aprendizado em conjunto com outras diversas an??lises explorat??rias dos dados. Com tal processo iterativo, espera-se entender e melhorar a qualidade das m??sicas produzidas com o tempo. Espera-se tamb??m gerar ideias e an??lises no ??mbito cultural e musical sobre a complexidade e a produ????o atual do funk brasileiro, mostrando que a ideia de que o funk ?? um tipo de m??sica f??cil e simples n??o passa de um mito.")

with st.container():
    st.write("---")
    st.header("Como foi realizado este estudo?")
    st.write("##")
    st.write("Este estudo se inspirou na metodologia experimental iterativa empregada para pesquisas no campo de Machine Learning. Primeiro, definiu-se um objetivo - no caso, gerar funks novos a partir de um modelo de Deep Learning utilizando o formato de ??udio cru. Depois, foram levantadas todas as dificuldades de se trabalhar com esse formato de ??udio e pesquisados modelos que representem o estado da arte nessa ??rea. Foram selecionados 2 modelos: SaShiMi - para ser treinado do zero, e a rede Jukebox como prova dde conceito. Em seguida, foram realizadas fases de composi????o da base de dados intercaladas com fases de treinamento, de forma a buscar os melhores hiperpar??metros da rede, a melhor base poss??vel, e os melhores pr??-processamentos dessas bases - filtrando trechos que n??o condiziam com o funk. Assim, espera-se melhorar as amostras geradas pela rede. Importante ressaltar tamb??m que o projeto foi desenvolvido com recursos limitados, uma assinatura Pro+ do ambiente de desenvolvimento virtual da Google Colab foi todo o poder de processamento utilizado.")

with st.container():
    st.write("---")
    st.header("An??lise de par??metros para o pr??-processamento dos dados")
    st.write("##")
    st.write("A composi????o da base de dados foi realizada a partir de ??udios em formato cru (.mp3, .wav, etc.). Esse formato, por??m, cont??m muito informa????o, o que o torna dif??cil de se trabalhar. Com isso em mente, reduziu-se a quantidade de informa????es nos trechos por meio da redu????o da frequ??ncia de amostragem e da diminui????o dos n??veis de codifica????o sonora.")

    st.subheader("Frequ??ncia de amostragem")
    st.write("A frequ??ncia de amostragem original dos ??udios ?? 44100 Hz. Diminuir esse valor pode ocasionar efeitos que prejudicam a qualidade sonora do ??udio - frequ??ncias mais agudas passam a ser pior representadas. Uma an??lise informal com base nos ??udios abaixo concluiu que 7000 Hz j?? resolvia o problema de aloca????o de mem??ria do ambiente de desenvolvimento e perdia pouca qualidade.")
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

    st.subheader("Quantidade de n??veis sonoros")
    st.write("A quantidade de n??veis sonoros original dos ??udios ?? 16 bits, resultando em 65356 n??veis sonoros distintos. Isso se traduz em 65356 classes para o algoritmo classificar cada ponto, o que ?? uma tarefa muito dif??cil. Para auxiliar, foi realizado a redu????o atrav??s de uma transforma????o chamada 'mu-law', que diminui os n??veis sonoros minizando a perda de informa????o para um ouvido humano. Abaixo as redu????es experimentadas:")
    st.write("Funk original para compara????o (65356 classes):")
    st.audio(funk7000, format="audio/wav")
    st.write("Funk com 256 classes:")
    st.audio(funk256, format="audio/wav")
    st.write("Funk com 64 classes - escolhido por conter a maior redu????o com a menor perda percept??vel:")
    st.audio(funk64, format="audio/wav")
    st.write("Funk com 32 classes - come??a a existir ru??do moderado atr??s do som")
    st.audio(funk32, format="audio/wav")
    st.write("Funk com 16 classes - colocado para melhor exemplifica????o de ru??do forte causado pela diminui????o dos n??veis sonoros:")
    st.audio(funk16, format="audio/wav")




with st.container():
    st.write("---")
    st.header("Arquiteturas trabalhadas")
    st.write("##")
    st.subheader("SaShiMi")
    st.write("##")
    st.write("SaShiMi ?? uma arquitetura criada no ??nicio de 2022 baseada na teoria de controle de estados de espa??o. Ela cria uma nova parametriza????o dessa t??cnica de forma a aplic??-la no contexto de sequ??ncias com longas dep??ndencias, por exemplo para trabalhar com ??udio em formato cru. O c??digo utilizado foi adaptado do reposit??rio: https://github.com/HazyResearch/state-spaces/tree/main/sashimi.")
    st.image("./sashimi.png", caption="Especifica????o da arquitetura SaShiMi. Retirada da publica????o original.")
    st.write("##")
    st.subheader("Jukebox")
    st.write("##")
    st.write("Jukebox ?? uma rede treinada pelo grupo OpenAI que utiliza representa????es reduzidas dos dados de entrada para gerar novas amostras. Essa ideia ?? realizada por estruturas chamadas VQ-VAEs, um tipo espec??fico de variational autoencoder. O c??digo utilizado foi adaptado do reposit??rio: https://github.com/openai/jukebox.")
    st.image("./vae.png", caption="Ilustra????o de um VAE, bloco fundamental da arquitetura Jukebox.")


with st.container():
    st.write("---")
    st.header("??udios gerados")
    st.write("##")
    st.subheader("SaShiMi - base de dados 1")
    st.write("##")
    st.write("A primeira base foi composta por 100 funks muito escutados em 2021, de diversos g??neros e produtoras diferentes. As gera????es realizadas n??o compreenderam corretamente o funk, elas cont??m desde sons n??o ritmados ?? ru??dos. Uma das melhores geradas ?? mostrada abaixo. Todas as m??sicas do SaShiMi tem os 4 primeiros segundos provenientes de uma m??sica real, e os 4 ??ltimos gerados pela rede.")
    st.write("##")
    st.audio(sashimi1, format="audio/wav")
    st.write("##")
    st.write("Um caso peculiar foi a amostra gerada em que a m??sica simplesmente acabou no in??cio da gera????o. Sup??e-se que pode ter sido efeito da falta de filtragem neste primeira base de dados, pois as outras bases de dados passaram por esse processo e esta foi a ??nica amostra gerada assim.")
    st.write("##")
    st.audio(sashimi2, format="audio/wav")
    st.subheader("SaShiMi - base de dados 2")
    st.write("##")
    st.write("A segunda base de dados usada para treinamento cont??m apenas m??sicas da produtora Kondzilla, tentando reduzir a vari??ncia das amostras atrav??s de restringir o estilo de edi????o empregado nas m??sicas. Gerou ??udios como o seguinte: ")
    st.audio(sashimi3, format="audio/wav")
    st.write("##")
    st.write("Ainda existem muitas amostras consideradas meio que ru??dos: ")
    st.audio(sashimi4, format="audio/wav")
    st.write("##")
    st.write("Por??m, com essa base, apesar das melhores m??tricas de treinamento, a rede parece ter percebido a grande presen??a de graves na m??sica funk, e come??ou a acertar mais s?? criando graves sem nenhuma musicalidade: ")
    st.audio(sashimi5, format="audio/wav")
    st.write("##")
    st.subheader("SaShiMi - base de dados 3")
    st.write("##")
    st.write("A terceira base de dados usada para treinamento cont??m apenas m??sicas do subg??nero Mandel??o e tenta melhorar os resultados reduzindo a variabilidade oriunda dos g??neros presentes na base. Os resultados n??o diferem muito da primeira gera????o, provavelmente porque dentro das amostras ainda existe bastante varia????o, j?? que as m??sicas cont??m diferentes produtores. Algumas das m??sicas selecionadas aleatoriamente para a parti????o de teste s??o razoavelmente distintas do resto. Abaixo algumas das amostras geradas:")
    st.audio(sashimi6, format="audio/wav")
    st.audio(sashimi7, format="audio/wav")
    st.write("##")


    st.subheader("Jukebox")
    st.write("##")
    st.write("O modelo aqui utilizado '1b_lyrics' foi treinado pela OpenAI em uma base de 1,2 milh??o de m??sicas de v??rios g??neros e utilizando uma capacidade computacional estimada em mais de 5 milh??es de d??lares. Ele gerou uma das ??nicas amostras condizentes com o g??nero funk utilizando como condicionamento um trecho de 15 segundos da m??sica 'Abusadamente'. Percebe-se um vocal ingl??s, mas o ritmo foi compreendido e continuado de forma natural pela rede.")
    st.write("##")
    st.audio(jukebox1, format="audio/wav")
    st.write("Com a mesma entrada tamb??m foram geradas amostras que falharam em seguir a proposta da m??sica, provavelmente pela base de dados utilizada em seu treinamento, que cont??m outros g??neros e nenhum funk, al??m de 600 mil das 1.2 milh??o de m??sicas serem da l??ngua inglesa.")
    st.audio(jukebox2, format="audio/wav")
    st.write("Em outro teste com uma entrada menos regular, que transiciona de um ritmo para outro, a rede teve resultados piores. Abaixo a amostra foi condicionada em 16 segundos de m??sica.")
    st.audio(jukebox3, format="audio/wav")
    st.audio(jukebox4, format="audio/wav")
    st.write("E mesmo aumentando esse tempo de condicionamento de 16 para 18 segundos, dando mais acesso ao novo ritmo sendo tocado, n??o foi suficiente para melhoras significativas: ")
    st.audio(jukebox5, format="audio/wav")
    st.audio(jukebox6, format="audio/wav")


    with st.container():
        st.write("---")
        st.header("Conclus??es")
        st.write("##")
        st.write("Fica claro que o funk ?? como qualquer outro estilo, tem suas nuances, complexidades, mas tamb??m suas caracter??sticas marcantes que d??o origem ao g??nero. Sua import??ncia cultural n??o deve ser subestimada, e ele pode ser sim objeto de estudos acad??micos. Do ponto de vista t??cnico, ?? uma m??sica ritmada que tem potencial para gerar novos insights na ??rea do Deep learning. Contudo, essa ??rea se mostra computacionalmente muito custosa, requerendo muito investimento em servidores especializados para o treinamento das redes. S?? assim essas arquiteturas podem atingir seu verdadeiro potencial e de fato representar e reproduzir uma parte da arte, da subjetividade do ser humano por meio de um evento matem??tico-antropof??gico.")
