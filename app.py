import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Marketing Performance Analytics",
    layout="wide"
)

def moeda(valor):
    return f"R$ {valor/1_000_000:.2f} Mi"

def numero(valor):
    return f"{valor:,.0f}".replace(",", ".")

def percentual(valor):
    return f"{valor * 100:.2f}%"

def roas(valor):
    return f"{valor:.2f}x"

@st.cache_data
def carregar_dados():
    df = pd.read_csv("dados/bruto/global_ads_performance_dataset.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

def gerar_analise(df, dimensao):
    analise = (
        df.groupby(dimensao)
        .agg(
            investimento=("ad_spend", "sum"),
            receita=("revenue", "sum"),
            conversoes=("conversions", "sum"),
            impressoes=("impressions", "sum"),
            cliques=("clicks", "sum")
        )
        .reset_index()
    )

    analise["ROAS"] = analise["receita"] / analise["investimento"]
    analise["CPA"] = analise["investimento"] / analise["conversoes"]
    analise["CTR"] = analise["cliques"] / analise["impressoes"]

    return analise.sort_values("ROAS", ascending=False)

def tabela_formatada(analise, dimensao):
    tabela = analise.copy()
    tabela["investimento"] = tabela["investimento"].apply(moeda)
    tabela["receita"] = tabela["receita"].apply(moeda)
    tabela["conversoes"] = tabela["conversoes"].apply(numero)
    tabela["ROAS"] = tabela["ROAS"].apply(roas)
    tabela["CPA"] = tabela["CPA"].apply(lambda x: f"R$ {x:.2f}")
    tabela["CTR"] = tabela["CTR"].apply(percentual)

    return tabela[[dimensao, "investimento", "receita", "conversoes", "ROAS", "CPA", "CTR"]]

def bloco_analise(df, dimensao, titulo, pergunta):
    st.subheader(titulo)
    st.caption(pergunta)

    analise = gerar_analise(df, dimensao)

    melhor = analise.iloc[0]
    pior = analise.iloc[-1]

    col_grafico, col_insight = st.columns([2, 1])

    with col_grafico:
        fig = px.bar(
            analise,
            x=dimensao,
            y="ROAS",
            text=analise["ROAS"].round(2),
            title=f"ROAS por {titulo}"
        )

        fig.update_traces(textposition="outside")
        fig.update_layout(
            xaxis_title=titulo,
            yaxis_title="ROAS",
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    with col_insight:
        st.info(
            f"""
            **Insight principal**

            Melhor desempenho: **{melhor[dimensao]}**  
            ROAS: **{melhor["ROAS"]:.2f}x**  
            CPA: **R$ {melhor["CPA"]:.2f}**

            Menor desempenho: **{pior[dimensao]}**  
            ROAS: **{pior["ROAS"]:.2f}x**  
            CPA: **R$ {pior["CPA"]:.2f}**
            """
        )

    st.dataframe(
        tabela_formatada(analise, dimensao),
        use_container_width=True,
        hide_index=True
    )

    return analise

df = carregar_dados()

investimento_total = df["ad_spend"].sum()
receita_total = df["revenue"].sum()
conversoes_total = df["conversions"].sum()
impressoes_total = df["impressions"].sum()
cliques_total = df["clicks"].sum()

roas_global = receita_total / investimento_total
ctr_global = cliques_total / impressoes_total
cpa_global = investimento_total / conversoes_total

st.sidebar.title("Marketing Analytics")
st.sidebar.caption("App analítico de campanhas digitais")

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Visão Executiva",
        "Plataformas",
        "Tipos de Campanha",
        "Indústrias",
        "Países",
        "Storytelling",
        "Dicionário de Métricas"
    ]
)

if pagina == "Visão Executiva":

    st.title("Marketing Performance Analytics")
    st.caption("Análise executiva de campanhas digitais com foco em investimento, receita, conversões e retorno.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Investimento Total", moeda(investimento_total))
    col2.metric("Receita Total", moeda(receita_total))
    col3.metric("Conversões", numero(conversoes_total))
    col4.metric("ROAS Global", roas(roas_global))

    st.info(
        f"""
        **Resumo operacional**

        CTR Global: **{percentual(ctr_global)}**  
        CPA Global: **R$ {cpa_global:.2f}**  
        Cliques Totais: **{numero(cliques_total)}**
        """
    )

    st.divider()

    st.subheader("Resumo do Projeto")

    st.write(
        """
        Este app simula uma análise de performance de mídia paga em uma operação de marketing digital.

        A proposta é responder perguntas de negócio como:

        - Qual plataforma gera mais retorno?
        - Qual tipo de campanha é mais eficiente?
        - Qual indústria performa melhor?
        - Qual país apresenta melhor retorno sobre investimento?
        - Onde faria sentido aumentar ou revisar orçamento?
        """
    )

    st.divider()

    analise_plataforma = gerar_analise(df, "platform")

    fig = px.bar(
        analise_plataforma,
        x="platform",
        y="ROAS",
        text=analise_plataforma["ROAS"].round(2),
        title="Comparativo Geral de ROAS por Plataforma"
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(
        xaxis_title="Plataforma",
        yaxis_title="ROAS",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

elif pagina == "Plataformas":

    st.title("Análise por Plataforma")

    bloco_analise(
        df,
        "platform",
        "Plataforma",
        "Pergunta de negócio: qual canal de mídia paga gera melhor retorno?"
    )

elif pagina == "Tipos de Campanha":

    st.title("Análise por Tipo de Campanha")

    bloco_analise(
        df,
        "campaign_type",
        "Tipo de Campanha",
        "Pergunta de negócio: qual estratégia de campanha gera melhor retorno?"
    )

elif pagina == "Indústrias":

    st.title("Análise por Indústria")

    bloco_analise(
        df,
        "industry",
        "Indústria",
        "Pergunta de negócio: qual segmento de mercado apresenta melhor desempenho?"
    )

elif pagina == "Países":

    st.title("Análise por País")

    bloco_analise(
        df,
        "country",
        "País",
        "Pergunta de negócio: em qual país as campanhas performam melhor?"
    )

elif pagina == "Storytelling":

    st.title("Storytelling Executivo")
    st.caption("Tradução dos dados em linguagem simples para tomada de decisão.")

    analise_plataforma = gerar_analise(df, "platform")
    analise_campanha = gerar_analise(df, "campaign_type")
    analise_industria = gerar_analise(df, "industry")
    analise_pais = gerar_analise(df, "country")

    melhor_plataforma = analise_plataforma.iloc[0]
    melhor_campanha = analise_campanha.iloc[0]
    melhor_industria = analise_industria.iloc[0]
    melhor_pais = analise_pais.iloc[0]

    st.header("1. Cenário Geral")

    st.write(
        f"""
        Foram analisadas campanhas digitais com investimento total de **{moeda(investimento_total)}**.

        Esse investimento gerou **{moeda(receita_total)}** em receita e **{numero(conversoes_total)} conversões**.

        O retorno geral foi de **{roas_global:.2f}x**.
        """
    )

    st.header("2. Principais Descobertas")

    st.success(
        f"""
        **Melhor plataforma:** {melhor_plataforma["platform"]}  
        ROAS: {melhor_plataforma["ROAS"]:.2f}x

        **Melhor tipo de campanha:** {melhor_campanha["campaign_type"]}  
        ROAS: {melhor_campanha["ROAS"]:.2f}x

        **Melhor indústria:** {melhor_industria["industry"]}  
        ROAS: {melhor_industria["ROAS"]:.2f}x

        **Melhor país:** {melhor_pais["country"]}  
        ROAS: {melhor_pais["ROAS"]:.2f}x
        """
    )

    st.header("3. Recomendação Estratégica")

    st.info(
        f"""
        Com base nos dados, a estratégia mais eficiente seria priorizar campanhas na plataforma
        **{melhor_plataforma["platform"]}**, especialmente em campanhas do tipo
        **{melhor_campanha["campaign_type"]}**.

        Também existe oportunidade de aprofundar a análise nos segmentos de
        **{melhor_industria["industry"]}** e no país **{melhor_pais["country"]}**.

        A recomendação não é cortar automaticamente os canais com menor ROAS, mas revisar orçamento,
        segmentação, criativos e estratégia antes de aumentar investimento.
        """
    )

elif pagina == "Dicionário de Métricas":

    st.title("Dicionário de Métricas")
    st.caption("Explicação simples dos principais termos usados no dashboard.")

    st.markdown(
        """
        ### Investimento
        Valor gasto nas campanhas de anúncios.

        ### Receita
        Valor financeiro gerado pelas campanhas.

        ### Conversões
        Ações desejadas realizadas pelos usuários. Exemplos: compra, cadastro, orçamento, lead ou download.

        ### ROAS
        Retorno sobre investimento em anúncios.  
        Exemplo: ROAS de 5x significa que cada R$ 1 investido gerou R$ 5 de receita.

        ### CTR
        Taxa de clique.  
        Exemplo: CTR de 4% significa que, a cada 100 pessoas que viram o anúncio, 4 clicaram.

        ### CPA
        Custo por aquisição.  
        Exemplo: CPA de R$ 25 significa que cada conversão custou R$ 25.

        ### Impressões
        Quantidade de vezes que o anúncio foi exibido.

        ### Cliques
        Quantidade de vezes que usuários clicaram no anúncio.
        """
    )