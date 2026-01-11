#!/usr/bin/env python3
"""
Consolidation script for vaccine analysis pipeline.
Reads progress.json and individual analysis JSON files,
and outputs consolidated html/vaccines.json
"""

import json
import os
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROGRESS_FILE = os.path.join(BASE_DIR, "progress.json")
JSON_DIR = os.path.join(BASE_DIR, "json")
OUTPUT_FILE = os.path.join(BASE_DIR, "html", "vaccines.json")


def load_json(filepath):
    """Load a JSON file, return None if not found."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: File not found: {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"Warning: Invalid JSON in {filepath}: {e}")
        return None


def build_vaccines_list(progress):
    """Build the vaccines array from progress.json and individual analysis files."""
    vaccines = []

    for vaccine_id, vaccine_data in progress.get("vaccines", {}).items():
        if not vaccine_data.get("verified", False):
            print(f"Skipping unverified vaccine: {vaccine_id}")
            continue

        vaccine_entry = {
            "id": vaccine_id,
            "name": vaccine_data.get("name", ""),
            "type": vaccine_data.get("type", ""),
            "manufacturer": vaccine_data.get("manufacturer", ""),
            "description": vaccine_data.get("description", ""),
            "sources": vaccine_data.get("sources", []),
        }

        # Load the 4 analysis files
        for analysis_type in ["trial", "safety"]:
            for lang in ["en", "pt"]:
                key = f"{analysis_type}_{lang}"
                filepath = os.path.join(JSON_DIR, analysis_type, f"{vaccine_id}_{analysis_type}_{lang}.json")
                analysis = load_json(filepath)
                if analysis:
                    vaccine_entry[key] = analysis
                else:
                    print(f"Error: Missing {key} for {vaccine_id}")
                    return None

        vaccines.append(vaccine_entry)

    return vaccines


def build_criteria_trial():
    """Build the trial criteria definitions with EN/PT translations."""
    return {
        "placebo_control": {
            "id": "placebo_control",
            "name": "Placebo control group",
            "name_pt": "Grupo controle com placebo",
            "why_it_matters": "Allows identification of which reactions are caused by the vaccine vs. coincidental events",
            "why_it_matters_pt": "Permite identificar quais reações são causadas pela vacina vs. eventos coincidentes",
            "what_is_ideal": "Inert placebo (saline). Using another vaccine as comparator obscures true adverse event rates",
            "what_is_ideal_pt": "Placebo inerte (solução salina). Usar outra vacina como comparador obscurece as taxas reais de eventos adversos"
        },
        "double_blind": {
            "id": "double_blind",
            "name": "Double-blind study",
            "name_pt": "Estudo duplo-cego",
            "why_it_matters": "Prevents bias in observation and symptom reporting",
            "why_it_matters_pt": "Previne viés na observação e relato de sintomas",
            "what_is_ideal": "Neither participants nor researchers know who received vaccine/placebo",
            "what_is_ideal_pt": "Nem participantes nem pesquisadores sabem quem recebeu vacina/placebo"
        },
        "randomization": {
            "id": "randomization",
            "name": "Randomization",
            "name_pt": "Randomização",
            "why_it_matters": "Ensures differences in outcomes are due to the vaccine, not pre-existing characteristics",
            "why_it_matters_pt": "Garante que diferenças nos resultados são devido à vacina, não características pré-existentes",
            "what_is_ideal": "Documented random allocation with allocation concealment",
            "what_is_ideal_pt": "Alocação aleatória documentada com ocultação da alocação"
        },
        "pediatric_sample_size": {
            "id": "pediatric_sample_size",
            "name": "Pediatric sample size",
            "name_pt": "Tamanho da amostra pediátrica",
            "why_it_matters": "Small samples cannot detect rare reactions. Detecting 1:1,000 events requires ~3,000 participants",
            "why_it_matters_pt": "Amostras pequenas não podem detectar reações raras. Detectar eventos 1:1.000 requer ~3.000 participantes",
            "what_is_ideal": ">3,000 children per age group for adequate safety detection",
            "what_is_ideal_pt": ">3.000 crianças por grupo etário para detecção adequada de segurança"
        },
        "follow_up_duration": {
            "id": "follow_up_duration",
            "name": "Follow-up duration",
            "name_pt": "Duração do acompanhamento",
            "why_it_matters": "Autoimmune/neurological reactions may emerge weeks or months later",
            "why_it_matters_pt": "Reações autoimunes/neurológicas podem surgir semanas ou meses depois",
            "what_is_ideal": "Minimum 6-12 months; ideal: several years with scheduled assessments",
            "what_is_ideal_pt": "Mínimo 6-12 meses; ideal: vários anos com avaliações programadas"
        },
        "separate_age_groups": {
            "id": "separate_age_groups",
            "name": "Separate age groups",
            "name_pt": "Grupos etários separados",
            "why_it_matters": "Infants, toddlers, and older children have different immune systems",
            "why_it_matters_pt": "Bebês, crianças pequenas e crianças mais velhas têm sistemas imunológicos diferentes",
            "what_is_ideal": "Separate analysis: 0-1 years, 1-5 years, 6-12 years",
            "what_is_ideal_pt": "Análise separada: 0-1 ano, 1-5 anos, 6-12 anos"
        },
        "inclusion_exclusion_criteria": {
            "id": "inclusion_exclusion_criteria",
            "name": "Inclusion/exclusion criteria",
            "name_pt": "Critérios de inclusão/exclusão",
            "why_it_matters": "Allows understanding of who the results apply to",
            "why_it_matters_pt": "Permite entender a quem os resultados se aplicam",
            "what_is_ideal": "Balanced criteria that include representative population",
            "what_is_ideal_pt": "Critérios equilibrados que incluem população representativa"
        },
        "standardized_adverse_events": {
            "id": "standardized_adverse_events",
            "name": "Standardized definition of adverse events",
            "name_pt": "Definição padronizada de eventos adversos",
            "why_it_matters": "Enables comparison across studies and prevents under/over-reporting",
            "why_it_matters_pt": "Permite comparação entre estudos e previne sub/super-notificação",
            "what_is_ideal": "Brighton Collaboration criteria or MedDRA coding",
            "what_is_ideal_pt": "Critérios Brighton Collaboration ou codificação MedDRA"
        },
        "active_monitoring_serious": {
            "id": "active_monitoring_serious",
            "name": "Active monitoring of serious adverse events",
            "name_pt": "Monitoramento ativo de eventos adversos graves",
            "why_it_matters": "Passive/unsolicited reporting vastly underestimates serious events",
            "why_it_matters_pt": "Notificação passiva/não solicitada subestima muito os eventos graves",
            "what_is_ideal": "Active solicited surveillance for hospitalization, sequelae, deaths",
            "what_is_ideal_pt": "Vigilância ativa solicitada para hospitalização, sequelas, mortes"
        },
        "autoimmune_neurological": {
            "id": "autoimmune_neurological",
            "name": "Assessment of autoimmune/neurological reactions",
            "name_pt": "Avaliação de reações autoimunes/neurológicas",
            "why_it_matters": "Conditions like Guillain-Barré, seizures, myocarditis are rare but serious",
            "why_it_matters_pt": "Condições como Guillain-Barré, convulsões, miocardite são raras mas graves",
            "what_is_ideal": "Specific long-term monitoring with scheduled exams",
            "what_is_ideal_pt": "Monitoramento específico de longo prazo com exames programados"
        },
        "vulnerable_subgroups": {
            "id": "vulnerable_subgroups",
            "name": "Vulnerable subgroups",
            "name_pt": "Subgrupos vulneráveis",
            "why_it_matters": "Premature, immunocompromised children may react differently",
            "why_it_matters_pt": "Crianças prematuras, imunocomprometidas podem reagir diferentemente",
            "what_is_ideal": "Intentional inclusion and separate analysis of these groups",
            "what_is_ideal_pt": "Inclusão intencional e análise separada desses grupos"
        },
        "statistical_analysis": {
            "id": "statistical_analysis",
            "name": "Robust statistical analysis",
            "name_pt": "Análise estatística robusta",
            "why_it_matters": "Most vaccine trials are powered for efficacy, not safety",
            "why_it_matters_pt": "A maioria dos ensaios de vacinas tem poder para eficácia, não segurança",
            "what_is_ideal": "Study powered for safety outcomes; confidence intervals documented",
            "what_is_ideal_pt": "Estudo com poder para desfechos de segurança; intervalos de confiança documentados"
        },
        "data_transparency": {
            "id": "data_transparency",
            "name": "Data transparency",
            "name_pt": "Transparência dos dados",
            "why_it_matters": "Allows independent verification by other researchers",
            "why_it_matters_pt": "Permite verificação independente por outros pesquisadores",
            "what_is_ideal": "Independent DSMB; raw data available; peer-reviewed publication",
            "what_is_ideal_pt": "DSMB independente; dados brutos disponíveis; publicação revisada por pares"
        },
        "post_marketing_surveillance": {
            "id": "post_marketing_surveillance",
            "name": "Post-marketing surveillance",
            "name_pt": "Vigilância pós-comercialização",
            "why_it_matters": "Detects rare reactions that only appear in millions of doses",
            "why_it_matters_pt": "Detecta reações raras que só aparecem em milhões de doses",
            "what_is_ideal": "Active pharmacovigilance system with periodic public reports",
            "what_is_ideal_pt": "Sistema ativo de farmacovigilância com relatórios públicos periódicos"
        },
        "conflict_of_interest": {
            "id": "conflict_of_interest",
            "name": "Conflict of interest / funding source",
            "name_pt": "Conflito de interesse / fonte de financiamento",
            "why_it_matters": "Industry-funded studies are more likely to report favorable outcomes",
            "why_it_matters_pt": "Estudos financiados pela indústria tendem a relatar resultados favoráveis",
            "what_is_ideal": "Independent funding or full disclosure of all financial ties",
            "what_is_ideal_pt": "Financiamento independente ou divulgação completa de todos os vínculos financeiros"
        },
        "all_cause_mortality": {
            "id": "all_cause_mortality",
            "name": "All-cause mortality and morbidity",
            "name_pt": "Mortalidade e morbidade por todas as causas",
            "why_it_matters": "Focusing only on vaccine-related outcomes can miss overall harm",
            "why_it_matters_pt": "Focar apenas em resultados relacionados à vacina pode perder danos gerais",
            "what_is_ideal": "Report total deaths and hospitalizations in all groups",
            "what_is_ideal_pt": "Relatar total de mortes e hospitalizações em todos os grupos"
        }
    }


def build_criteria_safety():
    """Build the safety criteria definitions with EN/PT translations."""
    return {
        "pediatric_sample_size": {
            "id": "pediatric_sample_size",
            "name": "Pediatric sample size",
            "name_pt": "Tamanho da amostra pediátrica",
            "why_it_matters": "Small samples cannot detect rare events (1 in 1,000, 1 in 10,000)",
            "why_it_matters_pt": "Amostras pequenas não podem detectar eventos raros (1 em 1.000, 1 em 10.000)",
            "what_is_ideal": ">3,000 children per age group",
            "what_is_ideal_pt": ">3.000 crianças por grupo etário"
        },
        "follow_up_duration": {
            "id": "follow_up_duration",
            "name": "Follow-up duration",
            "name_pt": "Duração do acompanhamento",
            "why_it_matters": "Autoimmune and neurological problems may take months or years to appear",
            "why_it_matters_pt": "Problemas autoimunes e neurológicos podem levar meses ou anos para aparecer",
            "what_is_ideal": "Minimum 12 months; 2-3+ years to assess long-term effects",
            "what_is_ideal_pt": "Mínimo 12 meses; 2-3+ anos para avaliar efeitos de longo prazo"
        },
        "comparison_group": {
            "id": "comparison_group",
            "name": "Comparison group",
            "name_pt": "Grupo de comparação",
            "why_it_matters": "Need a group that did not receive the vaccine for comparison",
            "why_it_matters_pt": "Precisa de um grupo que não recebeu a vacina para comparação",
            "what_is_ideal": "True placebo (saline solution), with randomization and double-blind",
            "what_is_ideal_pt": "Placebo verdadeiro (solução salina), com randomização e duplo-cego"
        },
        "active_surveillance": {
            "id": "active_surveillance",
            "name": "Active surveillance for serious events",
            "name_pt": "Vigilância ativa para eventos graves",
            "why_it_matters": "Passive reporting vastly underestimates serious events",
            "why_it_matters_pt": "Notificação passiva subestima muito eventos graves",
            "what_is_ideal": "Regular contact with families, review of medical records, causality analysis",
            "what_is_ideal_pt": "Contato regular com famílias, revisão de prontuários, análise de causalidade"
        },
        "neurological_monitoring": {
            "id": "neurological_monitoring",
            "name": "Neurological/developmental monitoring",
            "name_pt": "Monitoramento neurológico/desenvolvimento",
            "why_it_matters": "Check if children developed normally months and years later",
            "why_it_matters_pt": "Verificar se as crianças se desenvolveram normalmente meses e anos depois",
            "what_is_ideal": "Scheduled developmental assessments, follow-up neurological exams",
            "what_is_ideal_pt": "Avaliações de desenvolvimento programadas, exames neurológicos de acompanhamento"
        },
        "vulnerable_subgroups": {
            "id": "vulnerable_subgroups",
            "name": "Vulnerable subgroups",
            "name_pt": "Subgrupos vulneráveis",
            "why_it_matters": "Premature and immunosuppressed children may react differently",
            "why_it_matters_pt": "Crianças prematuras e imunossuprimidas podem reagir diferentemente",
            "what_is_ideal": "These groups intentionally included with results presented separately",
            "what_is_ideal_pt": "Esses grupos intencionalmente incluídos com resultados apresentados separadamente"
        },
        "data_transparency": {
            "id": "data_transparency",
            "name": "Data transparency",
            "name_pt": "Transparência dos dados",
            "why_it_matters": "Is it possible to verify the complete study data?",
            "why_it_matters_pt": "É possível verificar os dados completos do estudo?",
            "what_is_ideal": "Peer-reviewed publication with complete adverse event data",
            "what_is_ideal_pt": "Publicação revisada por pares com dados completos de eventos adversos"
        },
        "post_marketing_surveillance": {
            "id": "post_marketing_surveillance",
            "name": "Post-marketing surveillance",
            "name_pt": "Vigilância pós-comercialização",
            "why_it_matters": "What was discovered after millions of children received it?",
            "why_it_matters_pt": "O que foi descoberto após milhões de crianças receberem?",
            "what_is_ideal": "Active pharmacovigilance system with periodic public reports",
            "what_is_ideal_pt": "Sistema ativo de farmacovigilância com relatórios públicos periódicos"
        }
    }


def main():
    """Main consolidation function."""
    print("Loading progress.json...")
    progress = load_json(PROGRESS_FILE)
    if not progress:
        print("Error: Could not load progress.json")
        return False

    print("Building vaccines list...")
    vaccines = build_vaccines_list(progress)
    if vaccines is None:
        print("Error: Could not build vaccines list")
        return False

    print(f"Found {len(vaccines)} verified vaccines")

    # Build the final output structure
    output = {
        "vaccines": vaccines,
        "criteria_trial": build_criteria_trial(),
        "criteria_safety": build_criteria_safety(),
        "metadata": {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "vaccines_count": len(vaccines),
            "verification_status": "all_verified"
        }
    }

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Write output
    print(f"Writing {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("Consolidation complete!")
    print(f"  - Vaccines: {len(vaccines)}")
    print(f"  - Trial criteria: {len(output['criteria_trial'])}")
    print(f"  - Safety criteria: {len(output['criteria_safety'])}")

    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
