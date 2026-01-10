# Prompt: Avaliação de Estudos de Segurança de Vacinas para Crianças

## ARQUIVOS DE ENTRADA E SAÍDA

**ENTRADA:** O arquivo PDF a ser analisado está na pasta `sources/`
- Pode ser uma **bula/package insert** de vacina
- Pode ser um **artigo científico** descrevendo clinical trials

**SAÍDA:** Você DEVE salvar o resultado em um arquivo Markdown na pasta `analysis/trial/`

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

Avalie os seguintes critérios usando este guia de referência:

| Critério | Por que importa | O que é ideal |
|----------|-----------------|---------------|
| **1. Grupo controle com placebo** | Permite identificar quais reações são causadas pela vacina vs. eventos coincidentes | Placebo inerte (solução salina). Usar outra vacina como comparador obscurece as taxas reais de eventos adversos |
| **2. Estudo duplo-cego** | Previne viés na observação e relato de sintomas | Nem participantes nem pesquisadores sabem quem recebeu vacina/placebo |
| **3. Randomização** | Garante que diferenças nos resultados são devido à vacina, não características pré-existentes | Alocação aleatória documentada com ocultação da alocação (pesquisadores não podem prever a próxima atribuição) |
| **4. Tamanho da amostra pediátrica** | Amostras pequenas não detectam reações raras. Detectar eventos 1:1.000 requer ~3.000 participantes | >3.000 crianças por faixa etária para detecção adequada de segurança; >1.000 é o mínimo e ainda perde eventos mais raros |
| **5. Duração do acompanhamento** | Reações autoimunes/neurológicas podem surgir semanas ou meses depois. 30-42 dias (comum em trials) é grosseiramente inadequado | Mínimo 6-12 meses; ideal: vários anos com avaliações programadas |
| **6. Faixas etárias separadas** | Bebês, crianças pequenas e crianças mais velhas têm sistemas imunológicos diferentes | Análise separada: 0-1 anos, 1-5 anos, 6-12 anos |
| **7. Critérios de inclusão/exclusão** | Permite entender a quem os resultados se aplicam. Critérios muito restritivos (excluindo crianças com qualquer condição de saúde) limitam a aplicabilidade no mundo real | Critérios equilibrados que incluem população representativa; discussão explícita das limitações de generalização |
| **8. Definição padronizada de eventos adversos** | Permite comparação entre estudos e previne sub/super-notificação | Critérios Brighton Collaboration ou codificação MedDRA; limiares objetivos (ex: febre >38°C) em vez de avaliações subjetivas |
| **9. Monitoramento ativo de eventos graves** | Relato passivo/não solicitado subestima vastamente eventos graves | Vigilância ativa solicitada para hospitalização, sequelas, mortes com investigação causal; distinção clara entre eventos solicitados e não solicitados |
| **10. Avaliação de reações autoimunes/neurológicas** | Condições como Guillain-Barré, convulsões, miocardite, encefalite e doenças autoimunes são raras mas graves | Monitoramento específico de longo prazo com exames/consultas programadas; lista predefinida de condições a observar |
| **11. Subgrupos vulneráveis** | Prematuros, imunossuprimidos, crianças com alergias, condições crônicas ou em medicações concomitantes podem reagir diferentemente | Inclusão intencional e análise separada desses grupos; não excluídos dos trials |
| **12. Análise estatística robusta** | A maioria dos trials de vacinas tem poder para eficácia, não segurança — uma limitação fundamental. Sem poder adequado, sinais de segurança são perdidos | Estudo com poder para desfechos de segurança; intervalos de confiança, valores-p, cálculo de poder documentados; análise intention-to-treat |
| **13. Transparência dos dados** | Permite verificação independente por outros pesquisadores | Comitê Independente de Monitoramento de Segurança de Dados (DSMB); dados brutos e dados individuais de participantes (IPD) disponíveis; publicação peer-reviewed |
| **14. Vigilância pós-comercialização** | Detecta reações raras que só aparecem em milhões de doses. Sistemas passivos (VAERS, Yellow Card) dependem de relato voluntário e subestimam vastamente as taxas reais | Sistema de farmacovigilância ativo com relatórios públicos periódicos; não depende apenas de relato passivo |
| **15. Conflito de interesse / fonte de financiamento** | Estudos financiados pela indústria têm mais probabilidade de relatar resultados favoráveis; vínculos financeiros podem enviesar a interpretação | Financiamento independente ou divulgação completa de todos os vínculos financeiros; pesquisadores sem conflitos conduzem a análise |
| **16. Mortalidade e morbidade por todas as causas** | Focar apenas em desfechos "relacionados à vacina" pode perder danos gerais; determinação de causalidade é subjetiva | Relatar total de mortes e hospitalizações em todos os grupos, não apenas aquelas julgadas "relacionadas" à vacina |

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
3. Use a ferramenta Write para salvar em `analysis/trial/`

**Formato do nome:** Baseie-se no nome do arquivo de entrada, substituindo a extensão por `_avaliacao.md`

**Exemplos:**
- `sources/dtap_infanrix_package-insert.pdf` → `analysis/trial/dtap_infanrix_avaliacao.md`
- `sources/mmr_clinical-trial-2015.pdf` → `analysis/trial/mmr_clinical-trial-2015_avaliacao.md`
- `sources/hpv_gardasil_study.pdf` → `analysis/trial/hpv_gardasil_study_avaliacao.md`

⚠️ **NÃO termine sem salvar o arquivo. A análise só está completa quando o arquivo estiver salvo.**
