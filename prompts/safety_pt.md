# Avaliação de Segurança de Vacinas Pediátricas

## ARQUIVOS DE ENTRADA E SAÍDA

**ENTRADA:** O arquivo PDF a ser analisado está na pasta `sources/`
- Pode ser uma **bula/package insert** de vacina
- Pode ser um **artigo científico** descrevendo clinical trials

**SAÍDA:** Você DEVE salvar o resultado em um arquivo Markdown na pasta `analysis/safety/`

⚠️ **IMPORTANTE:** Este prompt requer que você SALVE o resultado em arquivo. NÃO apenas exiba na tela.

---

## Objetivo

Avaliar as evidências de segurança para crianças (0-12 anos) no documento anexado, respondendo à pergunta central:

> **"Esse documento me dá confiança de que essa vacina é segura para meu filho — agora e no futuro?"**

---

## Critérios de Avaliação

### 1. Tamanho da amostra pediátrica

Quantas crianças foram estudadas? Amostras pequenas não conseguem detectar eventos raros (1 em 1.000, 1 em 10.000).
**Ideal:** >3.000 crianças por faixa etária.

### 2. Duração do acompanhamento

Por quanto tempo as crianças foram monitoradas após a vacinação? Problemas autoimunes e neurológicos podem levar meses ou anos para aparecer.
**Ideal:** Mínimo 12 meses; 2-3+ anos para avaliar efeitos de longo prazo.

### 3. Grupo de comparação

Como sabemos que um evento foi causado pela vacina e não é coincidência? Precisa haver um grupo que não recebeu a vacina para comparar.
**Ideal:** Placebo verdadeiro (solução salina), com alocação aleatória (randomização) e duplo-cego (nem pais nem médicos sabiam quem recebeu o quê).

### 4. Busca ativa por eventos graves

Os pesquisadores procuraram ativamente por problemas sérios ou apenas esperaram alguém relatar?
**Ideal:** Contato regular com famílias, revisão de prontuários médicos, investigação de qualquer hospitalização/morte/sequela com análise de causalidade.

### 5. Monitoramento neurológico/desenvolvimento

Verificaram se as crianças se desenvolveram normalmente meses e anos depois? Avaliaram convulsões, atrasos, condições autoimunes?
**Ideal:** Avaliações de desenvolvimento programadas, exames neurológicos de acompanhamento, busca ativa por condições como Guillain-Barré, convulsões, regressão de habilidades.

### 6. Subgrupos vulneráveis

Testaram em crianças com condições especiais? Prematuros e imunossuprimidos podem reagir de forma diferente.
**Ideal:** Esses grupos foram incluídos intencionalmente e seus resultados são apresentados separadamente.

### 7. Transparência dos dados

É possível verificar os dados completos do estudo, ou apenas um resumo está disponível?
**Ideal:** Publicação em periódico revisado por pares com dados completos de todos os eventos adversos, ou dados brutos disponíveis para análise independente.

### 8. Vigilância pós-comercialização

O que foi descoberto depois que milhões de crianças tomaram? Existe monitoramento contínuo?
**Ideal:** Sistema de farmacovigilância ativo mencionado, com relatórios públicos periódicos e sinais de segurança novos identificados.

---

## Escala de Avaliação

| Símbolo | Nível          | Significado                                         |
|---------|----------------|-----------------------------------------------------|
| ⭐      | Excelente      | Evidência forte e tranquilizadora sobre este ponto  |
| ✅      | Adequado       | Abordado de forma razoável                          |
| ⚠️      | Parcial        | Mencionado, mas com falhas ou informação incompleta |
| 🔴      | Insuficiente   | Mencionado, mas muito limitado para dar confiança   |
| ❓      | Sem informação | Não fornece informação sobre este ponto             |

---

## Regras de Avaliação

1. Baseie-se **apenas** no documento anexado — não assuma que algo foi feito se não está escrito
2. Se não está mencionado, classifique como ❓
3. Na dúvida entre dois níveis, escolha o mais conservador
4. Seja específico: cite números e durações quando disponíveis

---

## Formato de Saída

### TABELA

| Critério                                  | Avaliação |
|-------------------------------------------|-----------|
| Tamanho da amostra pediátrica             |           |
| Duração do acompanhamento                 |           |
| Grupo de comparação                       |           |
| Busca ativa por eventos graves            |           |
| Monitoramento neurológico/desenvolvimento |           |
| Subgrupos vulneráveis                     |           |
| Transparência dos dados                   |           |
| Vigilância pós-comercialização            |           |

**Formato da coluna "Avaliação":** Emoji + nível + explicação breve.

Exemplo:

> ⚠️ **Parcial** — Apenas 6 meses de follow-up; insuficiente para detectar efeitos de longo prazo.

### RESUMO

Um único parágrafo iniciando com **emoji + nota geral**, seguido de avaliação honesta e direta sobre o que esse documento comprova (ou não) sobre a segurança dessa vacina em crianças.

---

## AÇÃO OBRIGATÓRIA: SALVAR RESULTADO

🔴 **VOCÊ DEVE USAR A FERRAMENTA Write PARA CRIAR O ARQUIVO DE SAÍDA**

1. Identifique o nome do PDF analisado em `sources/`
2. Crie o nome do arquivo de saída baseado no PDF
3. Use a ferramenta Write para salvar em `analysis/safety/`

**Formato do nome:** Baseie-se no nome do arquivo de entrada, substituindo a extensão por `_seguranca.md`

**Exemplos:**
- `sources/dtap_infanrix_insert.pdf` → `analysis/safety/dtap_infanrix_seguranca.md`
- `sources/mmr_mmrii_clinical.pdf` → `analysis/safety/mmr_mmrii_seguranca.md`
- `sources/hpv_gardasil9_clinical.pdf` → `analysis/safety/hpv_gardasil9_seguranca.md`

⚠️ **NÃO termine sem salvar o arquivo. A análise só está completa quando o arquivo estiver salvo.**
