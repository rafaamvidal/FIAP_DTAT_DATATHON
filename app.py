import streamlit as st
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler

# Configurando o menu lateral
menu = st.sidebar.radio("Menu", ["Home", "Introdução", "Proposta analítica", "Proposta preditiva", "Dashboard", "Conclusão"])

# Exibe conteúdo com base na opção selecionada
if menu == "Home":

    # Título da aplicação
    st.title("O Impacto da ONG Passos Mágicos no Desempenho Educacional")

    # Adiciona uma imagem a partir de uma URL
    st.image(
        "https://niverdobem.com.br/wp-content/uploads/2020/10/18A3D82B-2FDB-4355-A9D1-FBAA99E56F41.jpeg",
        use_container_width=True,
    )
    st.subheader("Projeto: Pós Tech Alura/Fiap - Datathon Fase 5")
    st.write("Data: Fev/2025")
    st.markdown('<h2 style="color:#e61859;">Integrantes do Projeto</h2>', unsafe_allow_html=True)
    st.write("**Rafael Morais Vidal RM 354846**")
    st.write("**Rafael Lopes Tanaka RM 356096**")
    st.write("**Rodrigo Kenji Rossetti Inonhe RM 354906**")
    st.write("**Lucas Morikawa Giovanini RM 355007**")

    st.markdown('<h2 style="color:#e61859;">O Desafio</h2>', unsafe_allow_html=True)
    st.write(
        """O grande objetivo do Datathon é você como cientista de dados criar uma
            proposta preditiva, ou como analista de dados realizar uma proposta analítica
            para demonstrar o impacto que a ONG “Passos Mágicos” tem realizado sobre a
            comunidade que atende. """

        """ A associação busca instrumentalizar o uso da educação como ferramenta
              para a mudança das condições de vida das crianças e jovens em vulnerabilidade
              social. Com base no dataset de pesquisa extensiva do desenvolvimento
              educacional no período de 2020, 2021 e 2022.
              """
    )
    st.markdown('<h2 style="color:#e61859;">O Objetivo</h2>', unsafe_allow_html=True)
    st.write("""• Proposta analítica""")
    st.write(
        """  A ideia é demonstrar os impactos que a ONG “Passos
              Mágicos” realizou sobre o desempenho de estudantes e levantar indicadores de
              performance. Sendo assim, deve-se criar um dashboard e storytelling
              contando uma história com os dados para auxiliar a Passos Mágicos a tomar as
              melhores decisões com base nos indicadores e conhecer o perfil dos estudantes.
              """
    )
    st.write(
        """• Proposta preditiva"""
    )
    st.write(
        """Criar um modelo preditivo para prever o
            comportamento do estudante com base em algumas variáveis que podem ser
            cruciais para a identificação de seu desenvolvimento. Na proposta preditiva,
            você pode utilizar a criatividade para propor uma solução de algoritmo
            supervisionado ou não supervisionado. A ideia é utilizar um dos conhecimentos
            aprendidos no curso como solução (machine learning, deep learning ou
            processamento de linguagem natural).
            """
    )

elif menu == "Introdução":
  

  # Título da aplicação
  st.markdown('<h2 style="color:#e61859;">Introdução</h2>', unsafe_allow_html=True)

  # Adiciona uma imagem a partir de uma URL
  st.image("https://passosmagicos.org.br/wp-content/uploads/2020/11/abraco-meninos.jpg",use_container_width=True,)
  
  st.write("""A educação é um dos pilares fundamentais para o desenvolvimento social e individual, e a ONG Passos Mágicos tem desempenhado um papel 
            essencial na transformação da realidade de centenas de estudantes. Este estudo busca analisar, por meio de uma abordagem baseada em dados, 
            os impactos do trabalho da ONG no desempenho acadêmico dos alunos atendidos ao longo dos anos de 2020, 2021 e 2022.""")

  st.write("""Utilizando indicadores educacionais estruturados e métricas estatísticas, esta análise explora a evolução dos estudantes em três principais dimensões:""")

  st.write("""**Indicador de Autoavaliação Acadêmica (IAA):** Mede a percepção do próprio aluno sobre seu desempenho e progresso.""")
  
  st.write("""**Índice de Desenvolvimento Educacional (INDE):** Avalia o desenvolvimento global dos estudantes com base em um conjunto de critérios pedagógicos.""")
  
  st.write("""**Índice de Desempenho Acadêmico (IDA):** Mensura objetivamente a evolução das notas dos estudantes ao longo dos anos.""")
   
  st.write("""Além disso, a análise se aprofunda na correlação entre diferentes variáveis educacionais, permitindo identificar padrões de avanço, 
            estabilidade ou retrocesso dentro da jornada educacional dos alunos. Comparações entre os anos de 2020, 2021 e 2022 são feitas 
            para compreender a progressão e destacar como a intervenção da Passos Mágicos tem impactado positivamente os estudantes.""")
  
  st.write("""Os resultados desta investigação fornecem uma visão quantitativa do papel da ONG na redução da defasagem escolar, 
            melhoria do engajamento estudantil e aumento da performance acadêmica. Ao longo deste estudo, os dados são apresentados 
            de forma clara e visual, utilizando análises estatísticas e gráficos para ilustrar os efeitos tangíveis do suporte pedagógico oferecido.""")

  st.write("""Por fim, espera-se que esta análise contribua para uma compreensão mais ampla do impacto social da educação e forneça subsídios para a 
              expansão e aprimoramento das ações desenvolvidas pela Passos Mágicos, garantindo que ainda mais estudantes tenham acesso a oportunidades 
              de aprendizado e crescimento acadêmico.""")


  # Título da aplicação
  st.markdown('<h2 style="color:#e61859;">A Importância dos Dados para a Análise do Impacto da ONG Passos Mágicos</h2>', unsafe_allow_html=True)

  # Adiciona uma imagem a partir de uma URL
  st.image("https://www.sponte.com.br/hubfs/Imported_Blog_Media/importancia-da-coleta-e-analise-de-dados-educacionais-4.jpg",use_container_width=True,)

  st.write("""A utilização de dados na avaliação de projetos sociais, como o desenvolvido pela ONG Passos Mágicos, é fundamental para transformar percepções
             subjetivas em evidências concretas, garantindo credibilidade e clareza na mensuração do impacto. No contexto educacional, onde as transformações são 
             graduais e multifacetadas, os dados atuam como uma lente de precisão, revelando padrões, progressos e desafios que, de outra forma, poderiam permanecer ocultos.""")  

  st.write("""No caso específico deste estudo, os dados coletados entre 2020 e 2022 — período marcado por desafios sem precedentes devido à pandemia — permitem não apenas quantificar
             o impacto da ONG, mas também contextualizá-lo frente a um cenário de crise educacional global. A análise estruturada em três indicadores (IAA, INDE e IDA) oferece uma 
             abordagem holística, combinando dimensões subjetivas (como a autoavaliação dos alunos) e objetivas (como notas e critérios pedagógicos). 
             Essa triangulação metodológica é essencial para evitar viéses e capturar nuances do desenvolvimento educacional que métricas isoladas não revelariam.""")  

  st.write("""Os dados conferem rigor acadêmico à análise, transformando histórias individuais em tendências coletivas. Por exemplo, o Índice de Desempenho Acadêmico (IDA) 
            permite verificar se as intervenções pedagógicas da ONG resultaram em melhorias mensuráveis nas notas dos alunos, enquanto o Indicador de Autoavaliação Acadêmica (IAA) 
            revela como os estudantes percebem seu próprio crescimento, um fator crítico para motivação e engajamento. Já o INDE integra múltiplas variáveis, como participação em 
            atividades extracurriculares e domínio de competências socioemocionais, oferecendo uma visão sistêmica do desenvolvimento educacional.""")              

  st.write("""Em um cenário onde projetos sociais frequentemente enfrentam ceticismo quanto a seu impacto real, a análise baseada em dados posiciona a ONG Passos Mágicos 
            como um modelo de excelência e transparência. Os indicadores IAA, INDE e IDA, aliados à correlação estatística e à análise temporal, não apenas validam o trabalho já realizado, 
            mas também iluminam caminhos para otimizá-lo. Assim, os dados transcendem sua função técnica: tornam-se instrumentos de transformação social, capazes de amplificar vozes, guiar 
            decisões e, acima de tudo, garantir que cada "passo mágico" dos alunos seja um avanço mensurável em direção a um futuro educacional mais justo e inclusivo.""")    



elif menu == "Proposta analítica":
  # Título da aplicação

  st.markdown('<h2 style="color:#e61859;">Análise exploratória de dados</h2>', unsafe_allow_html=True)

  st.image("https://media.licdn.com/dms/image/D4D12AQFIpZ5f8JSSUQ/article-cover_image-shrink_720_1280/0/1687819271214?e=2147483647&v=beta&t=VkFfe3IHtb2TBzxE6iAN5erYau7vy27yxfGzshSW4sQ",use_container_width=True,) 


  st.markdown('<h3 style="color:#e61859;">Análise da Evolução do INDE ao Longo dos Anos (2020-2022)</h3>', unsafe_allow_html=True)

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "evo_media_inde.png"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)

  st.write("""Com base nos dados apresentados no gráfico, podemos realizar uma análise mais aprofundada da evolução do INDE (Índice de Desenvolvimento Educacional) ao longo dos anos de 2020 a 2022, buscando identificar possíveis causas para as variações observadas.""")    

  st.write("""**2020:** O INDE inicia o período com uma média de 5.12, indicando um nível de desenvolvimento educacional considerado razoável, porém com espaço para melhorias. A pandemia de COVID-19, pode ter afetado o desempenho dos alunos em 2020, impactando os resultados observados.""")    

  st.write("""**2021:** Há um salto significativo para 6.89, sugerindo um avanço notável no desenvolvimento educacional dos alunos.""")    

  st.write("""**2022:** O INDE atinge o ápice com 7.65, evidenciando uma melhora contínua e consistente ao longo do período analisado.""")  

#############################################################################################################################################################################################

  st.markdown('<h3 style="color:#e61859;">Análise do Gráfico: Distribuição de Alunos por Nível de Desenvolvimento (Pedra)</h3>', unsafe_allow_html=True)

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "qtd_alunos_pedras.png"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)


  st.write("""O gráfico apresentado revela a distribuição do número total de alunos (2020-2022) em cada nível de desenvolvimento, classificados como "pedras" com base em seus resultados no INDE (Índice de Desenvolvimento Educacional). Vamos analisar cada categoria:""")    

  st.write("""**1. Ametista:**""")
  st.write("""**Total de Alunos: 979**""")      
  st.write("""A Ametista representa o grupo com o maior número de alunos, indicando um forte desempenho no INDE, já que esta categoria
           engloba os alunos com pontuação entre 6,868 e 8,230. Este resultado sugere que uma parcela significativa dos alunos demonstra um desenvolvimento educacional sólido, próximo ao nível mais alto.""")    

  st.write("""**2. Ágata:**""")
  st.write("""**Total de Alunos: 599**""")      
  st.write("""O grupo Ágata, com 599 alunos, representa o segundo maior grupo. Agata corresponde aos alunos com pontuação INDE entre 5,506 e 6,868, o que ainda indica um desempenho educacional positivo, porém com margem para melhorias em relação ao grupo""")    

  st.write("""**3. Quartzo:**""")
  st.write("""**Total de Alunos: 372**""")      
  st.write("""O Quartzo, com 372 alunos, aponta para um grupo com um desempenho intermediário no INDE (2,405 a 5,506). Este grupo pode necessitar de maior atenção e investimento para alcançar os níveis de desenvolvimento mais elevados.""")    

  st.write("""**4. Topázio:**""")
  st.write("""**Total de Alunos: 323**""")      
  st.write("""O Topázio, com 323 alunos, representa o grupo com menor número de alunos. Esta categoria corresponde aos alunos com pontuação INDE entre 8,230 e 9,294, o que sugere que este grupo atingiu o nível de desenvolvimento mais alto.""")    

  st.markdown('<h5 style="color:#e61859;">Considerações Adicionais</h5>', unsafe_allow_html=True)    
  st.write("""**Fatores Socioeconômicos:** É crucial considerar que o desempenho no INDE pode ser influenciado por fatores socioeconômicos e familiares.""")      
  st.write("""**Ações da Instituição:** As ações e projetos desenvolvidos pela instituição podem ter um impacto significativo na progressão dos alunos entre os níveis de desenvolvimento.""")      
  st.write("""**Necessidade de Acompanhamento:** Os grupos Quartzo e Ágata, por representarem a maioria dos alunos, necessitam de acompanhamento pedagógico e ações direcionadas para que progridam para os níveis Ametista e Topázio.""")      


#############################################################################################################################################################################################

  st.markdown('<h3 style="color:#e61859;">Média das Notas por Matéria Escolar (2022)</h3>', unsafe_allow_html=True)

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "media_notas_2022.png"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)

  st.write("""O gráfico apresenta a média das notas dos alunos em três matérias escolares: Português, Inglês e Matemática, no ano de 2022. Através da análise do gráfico, podemos extrair os seguintes insights:""")    

  st.markdown('<h5 style="color:#e61859;">Desempenho em Matemática</h5>', unsafe_allow_html=True)     
  st.write("""A média da turma em Matemática é de 6.3, a mais alta entre as três matérias.""")    
  st.write("""Este resultado sugere um bom desempenho geral da turma em Matemática, indicando que a maioria dos alunos obteve notas acima da média nesta disciplina.""")    
  st.write("""É importante investigar os métodos de ensino e recursos utilizados em Matemática que podem ter contribuído para este bom desempenho.""")    

  st.markdown('<h5 style="color:#e61859;">Desempenho em Português e Inglês</h5>', unsafe_allow_html=True)      
  st.write("""As médias em Português e Inglês são ambas de 5.6,consideravelmente inferiores à média em Matemática.""")    
  st.write("""Este resultado sugere que a turma pode ter tido mais dificuldades em Português e Inglês em comparação com Matemática.""")    

  st.markdown('<h5 style="color:#e61859;">Comparação entre as matérias</h5>', unsafe_allow_html=True)      
  st.write("""A diferença de 0.7 pontos na média entre Matemática e as demais matérias pode parecer pequena, mas em termos de desempenho escolar, representa uma diferença considerável.""")    
  st.write("""É importante que a escola investigue as possíveis causas dessa diferença e implemente medidas para melhorar o desempenho dos alunos em Português e Inglês, buscando equiparar o nível de aprendizado em todas as matérias.""")  

  st.markdown('<h5 style="color:#e61859;">Insights e Recomendações</h5>', unsafe_allow_html=True)      
  st.write("""**Investigar as causas do bom desempenho em Matemática:** É importante identificar os fatores que contribuíram para o bom desempenho da turma em Matemática para replicar as estratégias em outras matérias.""")    
  st.write("""**Implementar medidas para melhorar o desempenho em Português e Inglês:** É fundamental que a escola adote medidas para melhorar o desempenho dos alunos em Português e Inglês, como:""")  
  st.write("""• Revisão dos métodos de ensino.""")  
  st.write("""• Criação de atividades de reforço.""")  
  st.write("""• Oferecimento de apoio individualizado aos alunos com mais dificuldades.""")  
  st.write("""• Investimento em recursos didáticos.""")  
  st.write("""• Maior acompanhamento do aprendizado dos alunos.""")  

  st.write("""**Considerar os fatores externos:** É importante levar em consideração os fatores externos que podem estar afetando o desempenho dos alunos e buscar formas de minimizar o impacto negativo desses fatores.""")  

#############################################################################################################################################################################################


  st.markdown('<h3 style="color:#e61859;">Análise de impacto do nível de defasagem nos indicadores de aprendizado (IDA) e desenvolvimento educacional (INDE)</h3>', unsafe_allow_html=True)

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "correlacao_defasagem.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)

  st.write("""A análise realizada buscou entender a relação entre o nível de defasagem dos alunos e seus indicadores de desempenho. 
              Os gráficos de dispersão mostram a distribuição dos alunos em relação ao nível de defasagem e seus respectivos indicadores educacionais.""")    

  st.markdown('<h5 style="color:#e61859;">Correlação entre Defasagem e INDE</h5>', unsafe_allow_html=True)     
  st.write("""O gráfico sugere uma correlação positiva fraca a moderada (coeficiente ≈ 0.33).""")    
  st.write("""Isso significa que, conforme a defasagem aumenta, o INDE tende a ser menor.""")    
  st.write("""No entanto, os pontos estão bastante dispersos, indicando que outros fatores podem estar influenciando o desempenho.""")    

  st.markdown('<h5 style="color:#e61859;">Correlação entre Defasagem e IDA</h5>', unsafe_allow_html=True)     
  st.write("""A correlação entre Defasagem e IDA também é positiva, mas mais fraca (≈ 0.18).""")    
  st.write("""Isso indica que a defasagem tem um impacto pequeno sobre o aprendizado medido pelo IDA.""")    
  st.write("""A dispersão dos dados mostra que há alunos com diferentes níveis de defasagem que ainda conseguem manter um IDA alto.""")    

  st.markdown('<h5 style="color:#e61859;">Correlação entre INDE e IDA</h5>', unsafe_allow_html=True)     
  st.write("""A correlação entre INDE e IDA é forte e positiva (0.85).""")    
  st.write("""Isso significa que os alunos com melhores índices de aprendizado (IDA) também apresentam maiores níveis de desenvolvimento educacional (INDE).""")    
  st.write("""Esse resultado faz sentido, pois um aluno que aprende mais tende a se desenvolver melhor ao longo do tempo.""")    


  st.write("""A defasagem tem um impacto moderado no desenvolvimento educacional (INDE), mas um impacto mais fraco no aprendizado (IDA).""")    
  st.write("""Os alunos com maior defasagem tendem a apresentar um desempenho menor, mas há muita variabilidade nos dados.""")    
  st.write("""O forte vínculo entre INDE e IDA sugere que estratégias para melhorar o aprendizado podem ajudar no desenvolvimento geral do aluno, independentemente da defasagem inicial.""")    



#############################################################################################################################################################################################

  st.markdown('<h3 style="color:#e61859;">Análise de Comparação do INDE e IDA entre Diferentes Níveis de Defasagem</h3>', unsafe_allow_html=True)

  st.write("""Aqui os gráficos fornecem uma visão da evolução do Indicador de Aprendizado (IDA) e do Índice de Desenvolvimento Educacional (INDE) 
            ao longo dos anos (2020-2022), segmentados por diferentes níveis de defasagem educacional (Baixa, Média e Alta).""")    

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "evolucao_ida_defasagem.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)

  st.markdown('<h5 style="color:#e61859;">Evolução do IDA por Nível de Defasagem</h5>', unsafe_allow_html=True)     
  st.write("""O IDA apresenta uma queda significativa entre 2020 e 2021 para todos os níveis de defasagem.""")    
  st.write("""Os alunos com defasagem baixa tiveram o maior impacto negativo, com uma queda mais acentuada no IDA.""")    
  st.write("""Em 2022, há uma recuperação no IDA, indicando uma possível melhora no aprendizado dos alunos.""")    
  st.write("""Mesmo com a recuperação, alunos com defasagem baixa ainda têm o menor IDA, enquanto os com defasagem alta mantêm o melhor desempenho.""")    

  st.write("""A queda no IDA em 2021 pode estar associada a impactos externos, como dificuldades na aprendizagem durante a pandemia.""")    
  st.write("""A recuperação em 2022 sugere medidas de intervenção bem-sucedidas, mas alunos com menor defasagem (teoricamente com melhor base educacional) foram mais impactados negativamente.""")    
  st.write("""Estratégias de reforço devem ser mais focadas nos alunos com menor defasagem, garantindo que a recuperação do aprendizado seja equilibrada entre todos os grupos.""")    


  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "evolucao_inde_defasagem.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)

  st.markdown('<h5 style="color:#e61859;">Evolução do INDE por Nível de Defasagem</h5>', unsafe_allow_html=True)     
  st.write("""O INDE cai drasticamente para todos os níveis de defasagem entre 2020 e 2021.""")    
  st.write("""Em 2021, o INDE atinge praticamente zero para todos os níveis de defasagem.""")    
  st.write("""Em 2022, há uma forte recuperação do INDE, mas o grupo com baixa defasagem teve o crescimento mais expressivo.""")    

  st.write("""A queda extrema do INDE em 2021 pode estar relacionada aos desafios educacionais enfrentados nesse ano, como mudanças no ensino remoto ou falta de acesso adequado a recursos educacionais.""")    
  st.write("""A forte recuperação do INDE em 2022 sugere ações eficazes da ONG para reverter os impactos negativos.""")    
  st.write("""O grupo de baixa defasagem teve o maior crescimento do INDE, o que pode indicar que oportunidades e reforços educacionais foram mais bem aproveitados por alunos com melhor base de conhecimento.""")    
  st.write("""Para manter um crescimento sustentável, a ONG pode considerar ações mais específicas para alunos com maior defasagem, garantindo que eles também tenham um avanço expressivo.""")    

  st.write("""Os gráficos mostram que 2021 foi um ano crítico para o aprendizado e o desenvolvimento educacional dos alunos, independentemente do nível de defasagem. 
            No entanto, as ações implementadas pela ONG "Passos Mágicos" parecem ter sido eficazes para promover uma recuperação em 2022.""")    



#############################################################################################################################################################################################

  st.markdown('<h3 style="color:#e61859;">Análise da Relação entre Recomendações das Equipes de Avaliação e Desempenho dos Alunos</h3>', unsafe_allow_html=True)

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "ida_qtd_recomendacoes.png"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  st.markdown('<h5 style="color:#e61859;">Gráfico IDA por Quantidade de Recomendações (2021)</h5>', unsafe_allow_html=True)    

  # Exibir a imagem no Streamlit
  st.image(imagem)

  st.write("""O gráfico sugere que alunos com 4 recomendações têm um IDA mais alto (próximo de 4), enquanto aqueles com 0 recomendações apresentam desempenho mais baixo.""")    
  st.write("""Há um aumento gradual no IDA conforme o número de recomendações aumenta, indicando uma possível correlação positiva entre recomendações e desempenho.""")    

  st.write("""Alunos que recebem mais recomendações (provavelmente orientações ou intervenções pedagógicas) tendem a ter um melhor aprendizado, refletido no IDA. 
          Isso pode indicar que as recomendações são eficazes para aprimorar o desempenho acadêmico.""")    


  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "inde_qtd_recomendacoes.png"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  st.markdown('<h5 style="color:#e61859;">Gráfico INDE por Quantidade de Recomendações (2021)</h5>', unsafe_allow_html=True)   

  # Exibir a imagem no Streamlit
  st.image(imagem)

  st.write("""Os dados estão altamente dispersos, com valores de INDE variando drasticamente para cada quantidade de recomendações. Por exemplo, alunos com 0 recomendações podem ter INDE entre 0 e 156.""")    
  st.write("""Não há uma tendência clara de aumento ou diminuição do INDE conforme as recomendações aumentam.""")

  st.write("""A relação entre recomendações e INDE é menos evidente do que no IDA. Isso pode indicar que:""")   
  st.write("""O INDE é influenciado por fatores além das recomendações (como contexto socioeconômico ou infraestrutura escolar).""")   
  st.write("""As recomendações podem impactar aspectos específicos do aprendizado (medidos pelo IDA), mas não o desenvolvimento educacional geral (medido pelo INDE).""")   


  st.markdown('<h5 style="color:#e61859;">Conclusões e interpretação</h5>', unsafe_allow_html=True)   

  st.write("""Correlação Positiva no IDA: Alunos com mais recomendações apresentam melhoria no aprendizado, sugerindo que as orientações das equipes de avaliação são eficazes.""")   
  st.write("""Dispersão no INDE: A falta de padrão no INDE indica que outros fatores (como políticas públicas ou recursos escolares) podem ser mais relevantes para o desenvolvimento educacional global.""")   
  st.write("""Limitações dos Dados: A amostra pequena (apenas 0, 2, 4 recomendações no IDA) e a dispersão no INDE exigem cautela nas conclusões.""")   

  st.write("""As recomendações parecem ter um impacto positivo no aprendizado específico (IDA), mas seu efeito no desenvolvimento educacional amplo (INDE) é menos claro. Recomenda-se ampliar o acompanhamento pedagógico e investigar fatores externos para melhorar o INDE.""")   

#############################################################################################################################################################################################


elif menu == "Proposta preditiva":

  st.markdown('<h2 style="color:#e61859;">Proposta preditiva</h2>', unsafe_allow_html=True)

  st.image("https://7793103.fs1.hubspotusercontent-na1.net/hubfs/7793103/Imported_Blog_Media/machine-redimensionado.jpg",use_container_width=True,) 

  st.markdown('<h3 style="color:#e61859;">Modelo para prever a indicação de bolsas com base nos avaliadores de desempenho</h3>', unsafe_allow_html=True)

  # Código usado para leitura e exibição da tabela
  codigo = """
  df_2022_desempenho = df_2022_limpo[['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN', 'INDICADO_BOLSA']]
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  df_2022_desempenho.head()
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "df_head_preditivo.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)


  # Código usado para leitura e exibição da tabela
  codigo = """
  #Alterando o valor indicado_bolsa para um valor binario

  df_2022_desempenho['INDICADO_BOLSA'] = df_2022_desempenho['INDICADO_BOLSA'].map({'Sim': 1, 'Não': 0}) 
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  #Avaliando a quantidade de valores de indicado_bolsa para ver o balanço de valores

  print(df_2022_desempenho['INDICADO_BOLSA'].value_counts())
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "indicados_bolsa_qtd.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)



  # Código usado para leitura e exibição da tabela
  codigo = """
  #Avaliando a correlação

  correlation_matrix = df_2022_desempenho.corr().round(2)

  fig, ax = plt.subplots(figsize=(15,10))
  sns.heatmap(data=correlation_matrix, annot=True, linewidths=.5, ax=ax)
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "grafico_correlacao.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)



  # Código usado para leitura e exibição da tabela
  codigo = """
  df_2022_desempenho = shuffle(df_2022_desempenho, random_state=9)
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  set(df_2022_desempenho["INDICADO_BOLSA"])
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  # Código usado para leitura e exibição da tabela
  codigo = """
  colunas = df_2022_desempenho.columns.difference(['INDICADO_BOLSA'])
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  #Avaliando os valores máximo e min de cada coluna
  max_vlr = df_2022_desempenho[colunas].max()
  min_vlr = df_2022_desempenho[colunas].min()

  # Display the results
  print("Valor Max:")
  print(max_vlr)

  print("\Valor Min:")
  print(min_vlr)
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  # Código usado para leitura e exibição da tabela
  codigo = """
  Valor Max:
  IAA     10.000020
  IAN     10.000000
  IDA      9.916667
  IEG     10.000000
  INDE     9.441522
  IPP      9.218750
  IPS     10.000000
  IPV     10.000010
  dtype: float64
  \Valor Min:
  IAA     0.000000
  IAN     2.500000
  IDA     0.000000
  IEG     0.000000
  INDE    3.031806
  IPP     0.000000
  IPS     2.500000
  IPV     2.500010
  dtype: float64
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  df_2022_desempenho_indicado = df_2022_desempenho[df_2022_desempenho["INDICADO_BOLSA"] == 1]
  df_2022_desempenho_nao_indicado = df_2022_desempenho[df_2022_desempenho["INDICADO_BOLSA"] == 0]
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  df_2022_desempenho_indicado
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "df_desempenho_indicado.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)


  # Código usado para leitura e exibição da tabela
  codigo = """
  df_2022_desempenho_indicado.mean()
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "df_desempenho_mean.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)


  # Código usado para leitura e exibição da tabela
  codigo = """
  df_2022_desempenho_nao_indicado
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "df_desempenho_nao_indicado.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)




  # Código usado para leitura e exibição da tabela
  codigo = """
  df_2022_desempenho_nao_indicado.mean()
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "df_desempenho_nao_indicado_mean.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)
  


  # Código usado para leitura e exibição da tabela
  codigo = """
  #Avaliando a quantidade de valores de indicado_bolsa para ver o balanço de valores

  print(df_2022_desempenho['INDICADO_BOLSA'].value_counts())
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  # Código usado para leitura e exibição da tabela
  codigo = """
  INDICADO_BOLSA
  0    730
  1    132
  Name: count, dtype: int64
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  minority_class = df_2022_desempenho[df_2022_desempenho['INDICADO_BOLSA'] == 1]
  majority_class = df_2022_desempenho[df_2022_desempenho['INDICADO_BOLSA'] == 0]
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  st.markdown('<h3 style="color:#e61859;">Treinamento do modelo usando resample dos dados</h3>', unsafe_allow_html=True)

  # Código usado para leitura e exibição da tabela
  codigo = """
  from imblearn.over_sampling import SMOTE

  # Separate features and target
  X = df_2022_desempenho[['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']]
  y = df_2022_desempenho['INDICADO_BOLSA']


  smote = SMOTE(sampling_strategy={1: 500}, random_state=42)
  X_resampled, y_resampled = smote.fit_resample(X, y)

  # Convert the resampled data to a DataFrame
  synthetic_data = pd.DataFrame(X_resampled, columns=['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN'])
  synthetic_data['INDICADO_BOLSA'] = y_resampled

  # Combine with the original dataset
  df_balanced = pd.concat([minority_class, synthetic_data], ignore_index=True)

  print(df_balanced)
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "inicio_treino_modelo.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)



  # Código usado para leitura e exibição da tabela
  codigo = """
  print(df_balanced['INDICADO_BOLSA'].value_counts())
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  # Código usado para leitura e exibição da tabela
  codigo = """
  INDICADO_BOLSA
  0    730
  1    632
  Name: count, dtype: int64
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  # Código usado para leitura e exibição da tabela
  codigo = """
  df_balanced = shuffle(df_balanced, random_state=55)
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  # Código usado para leitura e exibição da tabela
  codigo = """
  df_balanced.tail()
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "df_balanced_tail.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)


  # Código usado para leitura e exibição da tabela
  codigo = """
  X = df_balanced[['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']]
  y = df_balanced['INDICADO_BOLSA']

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  scaler = StandardScaler()
  X_train = scaler.fit_transform(X_train)
  X_test = scaler.fit_transform(X_test)
  y_train = np.asarray(y_train).reshape((-1, 1))
  y_test = np.asarray(y_test).reshape((-1, 1))
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),  # Input layer
    Dense(8, activation='relu'),  # Hidden layer
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # Output layer (binary classification)
  ])
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  model.summary()
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "model_sumary.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)




  # Código usado para leitura e exibição da tabela
  codigo = """
  epoch=150

  history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    shuffle=True,
    epochs=epoch,
    batch_size=16,
    verbose=1
  )
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')



  # Código usado para leitura e exibição da tabela
  codigo = """
  acc = '{:.2%}'.format(history.history['accuracy'][-1])
  print(f"O modelo possui uma acurácia de {acc} com {epoch} epochs de processamento")
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  # Código usado para leitura e exibição da tabela
  codigo = """
  O modelo possui uma acurácia de 86.78% com 150 epochs de processamento
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  # Código usado para leitura e exibição da tabela
  codigo = """
  # Visualizando os resultados de treino
  acc = history.history['accuracy']
  val_acc = history.history['val_accuracy']

  loss = history.history['loss']
  val_loss = history.history['val_loss']

  epochs_range = range(epoch)

  # Plot Acurácia
  plt.figure(figsize=(20, 8))
  plt.subplot(1, 2, 1)
  plt.plot(epochs_range, acc, label='Acurácia de Treinamento')
  plt.plot(epochs_range, val_acc, label='Acurácia de Validação')
  plt.legend(loc='lower right')
  plt.title('Acurácia de treino e teste')

  # Plot Erro de treinamento
  plt.subplot(1, 2, 2)
  plt.plot(epochs_range, loss, label='Erro de treinamento')
  plt.plot(epochs_range, val_loss, label='Erro de Validação')
  plt.legend(loc='upper right')
  plt.title('Erro de treinamento vs validação')
  plt.show()
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "graficos_modelo.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)



  # Código usado para leitura e exibição da tabela
  codigo = """
  from sklearn.metrics import classification_report
  # Predictions
  y_pred = model.predict(X_test)
  y_pred_class = [round(x[0]) for x in y_pred]
  y_test_class = y_test

  # classification report
  class_names = ['Não', 'Sim']

  print(classification_report(y_test_class, y_pred_class, target_names=class_names))
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')

  from PIL import Image

  # Caminho da imagem no computador
  caminho_imagem = "metrics.jpg"  # Substitua pelo nome ou caminho completo da imagem

  # Abrir a imagem com o Pillow
  imagem = Image.open(caminho_imagem)

  # Exibir a imagem no Streamlit
  st.image(imagem)


  # Código usado para leitura e exibição da tabela
  codigo = """
  model.save("modelo_desempenho_2022.keras")

  joblib.dump(scaler, 'scaler.pkl')
  """

  # Exibe o código na aplicação
  st.code(codigo, language='python')


  st.markdown('<h3 style="color:#e61859;">Conclusão do modelo</h3>', unsafe_allow_html=True)

  st.write("""O modelo desenvolvido para prever a indicação de bolsas (indicado_bolsa) com base nos avaliadores de desempenho apresentou uma acurácia de 86,78%, 
              demonstrando eficácia significativa na identificação de padrões associados à variável target.""")

  st.markdown('<h4 style="color:#e61859;">Desempenho Estável e Generalização Adequada</h4>', unsafe_allow_html=True)

  st.write("""A curva de acurácia de treino e teste converge para valores elevados (próximos a 86-90%), indicando que o modelo não sofre de overfitting e generaliza bem para dados não vistos.""")

  st.write("""O erro de treinamento e validação diminui consistentemente ao longo das iterações, estabilizando-se em níveis baixos (próximo a 0,3-0,4), o que reforça a robustez do modelo.""")

  st.markdown('<h4 style="color:#e61859;">Relevância dos Avaliadores de Desempenho</h4>', unsafe_allow_html=True)

  st.write("""A alta acurácia sugere que as variáveis relacionadas aos avaliadores de desempenho (como recomendações, notas ou métricas pedagógicas) 
            são fatores críticos para prever a indicação de bolsas. Isso ressalta a importância de políticas de acompanhamento contínuo e avaliação criteriosa.""")


  st.markdown('<h4 style="color:#e61859;">Implicações Práticas</h4>', unsafe_allow_html=True)

  st.write("""Os resultados indicam que o modelo pode ser utilizado como ferramenta de apoio à decisão para otimizar a distribuição de bolsas, 
              priorizando alunos cujos indicadores de desempenho alinham-se aos critérios de elegibilidade. Além disso, reforça a 
              necessidade de integrar avaliações pedagógicas sistemáticas aos processos de seleção.""")

  st.markdown('<h4 style="color:#e61859;">Resumo Final</h4>', unsafe_allow_html=True)

  st.write("""O modelo demonstra alta eficácia (86,78% de acurácia) na previsão de indicações de bolsa, com estabilidade e generalização adequadas. 
            Isso evidencia a relevância dos avaliadores de desempenho no processo, destacando seu potencial para embasar decisões estratégicas em políticas educacionais.""")

#################################################################################################################################################

elif menu == "Dashboard":

  # Título da aplicação
  st.markdown('<h2 style="color:#e61859;">Dashboard</h2>', unsafe_allow_html=True)
  
  # URL do relatório do Power BI (substitua pelo link do seu relatório)
  power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNmY1NTA5YjEtNDA5Ny00NWMwLTliZmUtY2E1NDZkNTNhMTViIiwidCI6ImVmYTU1OWEyLTJmOTctNGRkNi1hMmFlLThhYjAyZDliMzMyOSJ9"

  # Incorporando o Power BI com iframe
  st.components.v1.iframe(power_bi_url, width=1000, height=1000)

  st.write("Se o painel carregar de forma desproporcional, clique no ícone de ajustar à página, ou expanda para tela inteira.")

  st.write("Para acessar o dashboard em uma nova página, clique abaixo")
  st.markdown(
      """
      <a href="https://app.powerbi.com/view?r=eyJrIjoiNmY1NTA5YjEtNDA5Ny00NWMwLTliZmUtY2E1NDZkNTNhMTViIiwidCI6ImVmYTU1OWEyLTJmOTctNGRkNi1hMmFlLThhYjAyZDliMzMyOSJ9" target="_blank" style="text-decoration:none; color:#e61859; font-size:18px;">
      DASHBOARD</a>
      """,
      unsafe_allow_html=True)    

elif menu == "Conclusão":

  # Título da aplicação
  st.markdown('<h2 style="color:#e61859;">Conclusão do Projeto de Análise e Previsão do Impacto da ONG Passos Mágicos</h2>', unsafe_allow_html=True)

  st.write("""O estudo realizado sobre a atuação da ONG Passos Mágicos trouxe à tona evidências concretas do impacto da educação na transformação da 
            vida de crianças e jovens em situação de vulnerabilidade. Por meio de análises exploratórias e modelagem preditiva, investigamos padrões 
            de desempenho acadêmico, a evolução dos estudantes ao longo dos anos e os principais fatores que impulsionam o sucesso educacional dentro do programa.""")

  st.markdown('<h3 style="color:#e61859;">Respostas às Perguntas do Estudo</h3>', unsafe_allow_html=True)

  st.write("""1. **Qual o impacto da ONG no desenvolvimento educacional dos alunos?**""")
  st.write("""A evolução dos **indicadores educacionais (IAA, INDE e IDA)** mostrou que os alunos atendidos pela ONG tiveram um crescimento significativo ao longo dos anos. 
            O **INDE subiu de 5.12 em 2020 para 7.65 em 2022**, indicando que a intervenção educacional teve um impacto positivo e consistente, especialmente após os desafios impostos pela pandemia.""")

  st.write("""2. **Quais grupos de alunos mais se beneficiaram do programa?**""")
  st.write("""A análise da distribuição dos estudantes revelou que a maior parte dos alunos está nas categorias **Ametista e Ágata**, que representam níveis de desenvolvimento intermediário e avançado. 
            No entanto, **os grupos Quartzo e Ágata merecem atenção**, pois ainda possuem margem para crescimento. Estratégias pedagógicas focadas podem ajudar esses estudantes a alcançarem níveis mais elevados de desempenho.""")


  st.write("""3. **Quais fatores influenciam o aprendizado e a evolução dos estudantes?**""")
  st.write("""Os dados indicam uma **correlação forte (0.85) entre aprendizado (IDA) e desenvolvimento educacional (INDE)**, reforçando que o progresso acadêmico está diretamente ligado ao desenvolvimento global do aluno. 
            Por outro lado, a relação entre **defasagem escolar e aprendizado é mais fraca (0.18)**, o que sugere que, apesar de dificuldades passadas, os alunos ainda podem alcançar bons resultados com o suporte adequado.""")


  st.write("""4. **Como a pandemia impactou o desempenho dos alunos?**  """)
  st.write("""O ano de **2021 apresentou uma queda acentuada nos indicadores educacionais**, reflexo dos desafios do ensino remoto e das dificuldades impostas pelo período. 
            No entanto, a **recuperação observada em 2022** indica que as estratégias da ONG foram eficazes para mitigar os impactos negativos da pandemia e retomar a trajetória de aprendizado.""")


  st.markdown('<h3 style="color:#e61859;">Modelo Preditivo para Indicação de Bolsas  </h3>', unsafe_allow_html=True)
  st.write("""Além da análise exploratória, foi desenvolvido um **modelo de Machine Learning baseado em redes neurais** para prever a indicação de bolsas de estudo. Com uma **acurácia de 86,78%**, o modelo demonstrou 
            grande eficiência em identificar padrões associados ao desempenho acadêmico dos alunos. Isso reforça a relevância da análise de dados para otimizar a distribuição de bolsas e garantir que os recursos sejam direcionados de forma estratégica.""")


  st.markdown('<h3 style="color:#e61859;">Implicações e Recomendações</h3>', unsafe_allow_html=True)
  st.write("""1. **Apoio Focado para Alunos em Defasagem:** O grupo **Quartzo** e parte do **Ágata** necessitam de suporte adicional para atingir níveis mais altos de desempenho.""")
  st.write("""2. **Melhoria no Ensino de Português e Inglês:** As médias nessas disciplinas ficaram abaixo da de Matemática, indicando a necessidade de adaptação de métodos pedagógicos.""")
  st.write("""3. **Aprimoramento das Recomendações Pedagógicas:** A análise indicou que **alunos que receberam mais recomendações apresentaram melhor desempenho no IDA**, reforçando a importância de um monitoramento estruturado.""")
  st.write("""4. **Uso do Modelo Preditivo para Distribuição de Bolsas:** O modelo pode ser integrado ao processo de avaliação da ONG para priorizar alunos que possuem indicadores compatíveis com os critérios de elegibilidade.""")



  st.markdown('<h3 style="color:#e61859;">Conclusão Final: Transformando Dados em Oportunidades  </h3>', unsafe_allow_html=True)
  st.write("""O estudo reafirma a importância do **uso de dados para embasar decisões educacionais** e garantir que intervenções pedagógicas sejam eficazes. A ONG **Passos Mágicos** 
            não apenas gerou um impacto positivo no desempenho acadêmico dos estudantes, mas também demonstrou como um programa educacional estruturado pode reduzir desigualdades e criar oportunidades reais.""")

  st.write("""A ciência de dados, quando aplicada à educação, **vai além da análise numérica — ela se torna um instrumento para transformar vidas**. Os insights gerados por este projeto podem orientar a ONG na 
            tomada de decisões estratégicas, garantindo que o crescimento dos alunos seja sustentado e que ainda mais estudantes possam trilhar um caminho de aprendizado e desenvolvimento pessoal.""")

