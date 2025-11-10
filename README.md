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

> **Formato preferido**: Markdown (`.md`). Evite PDFs quando precisar que o ChatGPT “leia” o conteúdo.

---

## Como usar com o ChatGPT
1. **Repositório público**: cole o link do arquivo (ex.: `prompts/civil/contestacao_consumidor.md`) e peça “leia e adapte para o caso X”.
2. **Repositório privado**: conecte o GitHub ao ChatGPT e cite o caminho do arquivo.  
3. Ao pedir geração/edição, informe: **(a) contexto fático**, **(b) objetivo da peça**, **(c) tribunal/rito**, **(d) limites** (tamanho, tom, citações), **(e) variáveis** a preencher.

---

## Convenções
- **Tags no topo**: `tags: civil, consumidor, contestação`.
- **Cabeçalho do prompt/modelo**:
  - **Objetivo**: o que o modelo deve produzir.
  - **Entradas**: lista de `{{variaveis}}`.
  - **Formato de saída**: ex. “Markdown com títulos e sumário”.
  - **Verificações**: checagem de requisitos (cabimento, competência, prazos).
- **Placeholders**: use `{{parte_autora}}`, `{{processo_numero}}`, etc.
- **Comentários**: utilize blocos `> Nota:` para orientações editoriais.

---

## Áreas e escopo

### Processo Civil
**Escopo**: petições iniciais, contestações, réplicas, agravos, apelações, embargos, incidentes, cumprimento de sentença, tutela provisória.  
**Campos padrão (modelos)**:
- **Síntese fática** (com checklist de provas)
- **Preliminares** (pressupostos processuais/condições da ação)
- **Mérito** (tese principal + subsidiárias)
- **Jurisprudência** (citada com fonte)
- **Pedidos** (claros e cumulados)
- **Valor da causa** e **honorários**
**Exemplo de prompt**:
> “Com base em `modelos/civil/contestações/contestacao_consumidor.md`, gere contestação para {{processo_numero}} (foro {{foro}}), cliente {{reu}}, com fatos: {{fatos}}, documentos: {{documentos}}, tese central: {{tese}}. Saída em Markdown, com pedidos numerados e jurisprudência atual.”

---

### Processo Penal
**Escopo**: defesa prévia, resposta à acusação, memoriais, habeas corpus, recursos (RESE, apelação, agravo), incidentes, medidas cautelares.  
**Campos padrão (modelos)**:
- **Síntese do fato e tipificação**
- **Legalidade da prova** (cadeia de custódia, nulidades)
- **Teses** (atipicidade, excludentes, ausência de dolo/culpa, etc.)
- **Prisão cautelar** (requisitos do art. 312, medidas alternativas)
- **Pedidos** (absolvição, desclassificação, liberdade, acesso a provas)
**Exemplo de prompt**:
> “Usando `modelos/penal/pecas/defesa_previa.md`, elabore defesa prévia para {{processo_numero}}, réu {{nome}}, fatos {{fatos}}. Avalie nulidades e proponha medidas cautelares alternativas. Estruture conforme o modelo e cite precedentes pertinentes.”

---

### Processo Trabalhista
**Escopo**: petição inicial, contestação, reconvenção, impugnação ao valor da causa, embargos, recursos (RO, AI, RR), liquidação e cumprimento.  
**Campos padrão (modelos)**:
- **Relato do contrato** (função, salário, jornada)
- **Pedidos** (salariais, verbas rescisórias, adicionais, multas)
- **Prescrição** e **competência**
- **Base de cálculo** e **reflexos**
- **Provas** (documental, testemunhal)
**Exemplo de prompt**:
> “Com `modelos/trabalhista/peticoes/contestacao.md` como base, gere contestação para {{reclamacao_numero}}. Empregador {{empresa}}, empregado {{reclamante}}. Aponte prescrição parcial/total conforme datas, rebata jornada e adicionais, proponha cálculos sintéticos.”

---

## Qualidade, segurança e limites
- **Sem dados sensíveis**: substitua por `{{DADO_CONFIDENCIAL}}`.
- **Checagem humana obrigatória**: o conteúdo gerado é apoio, não consultoria definitiva.
- **Jurisprudência**: cite tribunal, número/processo, data e link quando possível.
- **Atualização**: revise periodicamente modelos à luz de novas leis/precedentes.

---

## Roadmap
- [ ] Índice navegável de prompts por tags.
- [ ] Scripts para extrair sumário dos modelos.
- [ ] Templates de PR/Issue com checklist jurídico.

## Licença
Defina conforme a necessidade (ex.: privado).

---
## Estrutura de pastas
# ChatGPT

Central de prompts, modelos e materiais para trabalhar com o ChatGPT.

## Objetivos
- Organizar **prompts reutilizáveis** (por área/tema).
- Manter **modelos de peças/textos** e referências.
- Documentar **fluxos** (como usar, padrões de saída, limites, aviso de confidencialidade).
