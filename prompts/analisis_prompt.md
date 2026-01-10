# Prompt: Avaliação de Estudos de Segurança de Vacinas para Crianças

## ARQUIVOS DE ENTRADA E SAÍDA

**ENTRADA:** O arquivo PDF a ser analisado está na pasta `sources/`
- Pode ser uma **bula/package insert** de vacina
- Pode ser um **artigo científico** descrevendo clinical trials

**SAÍDA:** Você DEVE salvar o resultado em um arquivo Markdown na pasta `analisys/`

⚠️ **IMPORTANTE:** Este prompt requer que você SALVE o resultado em arquivo. NÃO apenas exiba na tela.

---

## Instrução

Analise o documento anexado (localizado em `sources/`) — seja uma bula/package insert ou um artigo de clinical trial — e avalie os estudos de segurança com foco na aplicação pediátrica (crianças de 0 a 12 anos).

---

## ESCALA DE AVALIAÇÃO

Use esta escala para classificar cada critério:

| Nível               | Descrição                                                            |
| ------------------- | -------------------------------------------------------------------- |
| ⭐ **Exemplar**      | Supera o padrão esperado para a época e tipo de estudo               |
| ✅ **Adequado**      | Atende ao que seria esperado em um estudo de segurança robusto       |
| ⚠️  **Parcial**     | Presente, mas com falhas ou limitações significativas                |
| 🔴 **Insuficiente** | Mencionado na bula, mas de forma inadequada ou muito abaixo do ideal |
| ❓ **Ausente**       | Não realizado ou não documentado na bula                             |

---

## OUTPUT ESPERADO

### TABELA 1: AVALIAÇÃO DA VACINA

Crie uma tabela com 3 colunas:
- **Coluna 1**: Critério ideal para estudo de segurança
- **Coluna 2**: O que a bula informa sobre esse critério
- **Coluna 3**: Nível de atendimento ao critério (use a escala acima)

Avalie os seguintes critérios:

1. Grupo controle com placebo
2. Estudo duplo-cego
3. Randomização
4. Tamanho da amostra pediátrica
5. Duração do acompanhamento
6. Faixas etárias separadas
7. Critérios de inclusão/exclusão
8. Definição padronizada de eventos adversos
9. Monitoramento ativo de eventos graves
10. Avaliação de reações autoimunes/neurológicas
11. Subgrupos vulneráveis (prematuros, imunossuprimidos)
12. Análise estatística robusta
13. Transparência dos dados
14. Vigilância pós-comercialização

---

### AVALIAÇÃO GERAL

Escreva APENAS um parágrafo com um resumo honesto sobre quão bem esse estudo comprova a segurança dessa vacina em crianças. Inclua uma nota final com emoji.

---

## REGRAS DE AVALIAÇÃO

- Baseie-se **exclusivamente** no que está documentado no documento anexado (bula ou artigo)
- Se algo não está mencionado, classifique como ❓ Ausente (não assuma que foi feito)
- Considere o contexto histórico apenas para o nível "Exemplar" (superou o padrão da época)
- Seja específico na coluna 2: cite números, durações e metodologias quando disponíveis
- Na dúvida entre dois níveis, escolha o mais conservador

---

## AÇÃO OBRIGATÓRIA: SALVAR RESULTADO

🔴 **VOCÊ DEVE USAR A FERRAMENTA Write PARA CRIAR O ARQUIVO DE SAÍDA**

1. Identifique o nome do PDF analisado em `sources/`
2. Crie o nome do arquivo de saída baseado no PDF
3. Use a ferramenta Write para salvar em `analisys/`

**Formato do nome:** Baseie-se no nome do arquivo de entrada, substituindo a extensão por `_avaliacao.md`

**Exemplos:**
- `sources/dtap_infanrix_package-insert.pdf` → `analisys/dtap_infanrix_avaliacao.md`
- `sources/mmr_clinical-trial-2015.pdf` → `analisys/mmr_clinical-trial-2015_avaliacao.md`
- `sources/hpv_gardasil_study.pdf` → `analisys/hpv_gardasil_study_avaliacao.md`

⚠️ **NÃO termine sem salvar o arquivo. A análise só está completa quando o arquivo estiver salvo.**
