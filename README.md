# ChatGPT

Central de prompts, modelos e materiais para trabalhar com o ChatGPT.

## Objetivos
- Organizar **prompts reutilizáveis** (por área/tema).
- Manter **modelos de peças/textos** e referências.
- Documentar **fluxos** (como usar, padrões de saída, limites, aviso de confidencialidade).

## Estrutura de pastas
# ChatGPT
ChatGPT

## Como usar com o ChatGPT
1. Repositório **público**: cole a URL do arquivo no ChatGPT e peça “leia e resuma / adapte”.
2. Repositório **privado**: conecte o GitHub ao ChatGPT (Settings → Connected apps → GitHub), conceda acesso a este repo e depois cite o caminho do arquivo (ex.: `prompts/civel/contestacao.md`).

> Dica: Prefira **Markdown (.md)** ou **TXT/CSV** para facilitar a análise.

## Convenções de escrita
- **Cabeçalho do prompt**: objetivo, persona, dados de entrada, formato de saída.
- **Modelos jurídicos**: sumário com tese, fundamentos, jurisprudência e campos `{{variaveis}}`.
- Use tags no topo (ex.: `tags: cível, contestação, consumidor`).

## Qualidade e segurança
- Sem dados sensíveis de clientes.
- Coloque trechos de fatos em arquivos `.env.local` (não versionar) ou marque como `{{DADO_CONFIDENCIAL}}`.
- Revise saídas do modelo (não é consultoria jurídica).

## Roadmap
- [ ] Índice navegável dos prompts.
- [ ] Scripts para gerar sumários automáticos.
- [ ] templates de PR/Issue.

## Licença
Defina a licença conforme necessidade (ex.: Private/All rights reserved).
# ChatGPT – Base de Prompts & Modelos (Civil, Penal e Trabalhista)

Repositório para organizar **prompts reutilizáveis**, **modelos de peças** e **referências** para uso com o ChatGPT nas áreas de **Processo Civil**, **Processo Penal** e **Processo Trabalhista**.

---

## Objetivos
- Manter uma biblioteca versionada de **prompts** por área/assunto.
- Armazenar **modelos de peças** com placeholders `{{variavel}}`.
- Padronizar **formato de saída** e **fluxos de uso** no ChatGPT.
- Centralizar **jurisprudência** e **referências**.

---

## Estrutura de pastas

