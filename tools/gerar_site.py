#!/usr/bin/env python3
"""Gera index.html e curriculo.html (bilíngues PT/EN) a partir dos dados deste arquivo.

Uso (na raiz do projeto):
    python tools/gerar_site.py

Para atualizar o currículo: edite os dados abaixo (cada texto é um par (português, inglês)),
rode o script, faça commit e push. O GitHub Actions publica o site automaticamente.
"""
import json
from datetime import date
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------- #
# DADOS
# --------------------------------------------------------------------------- #
NOME = "Rodrigo Machado Schuler"
EMAIL = "rmschuler@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/rmschuler/"
LINKEDIN_LABEL = "linkedin.com/in/rmschuler"
TELEFONE = "81 99618-1436"  # celular e WhatsApp
TELEFONE_TEL = "+5581996181436"
WHATSAPP_URL = "https://wa.me/5581996181436"
LOCAL = ("Recife, PE – Brasil", "Recife, PE – Brazil")
PDF = {"pt": "curriculo-rodrigo-schuler-pt.pdf", "en": "curriculo-rodrigo-schuler-en.pdf"}

HEADLINE = (
    "Coordenação de Infraestrutura e Sustentação de TI | ITSM | Liderança Técnica | Scrum | ITIL",
    "IT Infrastructure & Support Coordination | ITSM | Technical Leadership | Scrum | ITIL",
)
TAGLINE = (
    "Líder técnico em infraestrutura, ITSM e dados: transformo desafios técnicos em resultados "
    "estratégicos para operações críticas.",
    "Technical leader in infrastructure, ITSM and data: I turn technical challenges into "
    "strategic results for mission-critical operations.",
)

RESUMO = [
    (
        "Profissional sênior de Tecnologia da Informação com mais de 16 anos de experiência consolidada em gestão de "
        "infraestrutura de servidores, sustentação de ambientes críticos, liderança de equipes e coordenação de "
        "projetos de TI.",
        "Senior Information Technology professional with over 16 years of solid experience in server infrastructure "
        "management, support of critical environments, team leadership and IT project coordination.",
    ),
    (
        "Especialista na governança de TI utilizando metodologias ITIL, garantindo a continuidade operacional, entrega "
        "de soluções de alta disponibilidade e o cumprimento rigoroso de SLAs. Comprovada habilidade na liderança "
        "técnica e gestão de pessoas, aliando visão estratégica de negócio, metodologias ágeis (Scrum) e inteligência "
        "de dados (desenvolvimento de relatórios e dashboards operacionais em Power BI e automações). Reconhecido por "
        "transformar desafios técnicos em resultados estratégicos, para otimização de processos.",
        "Specialist in IT governance using ITIL methodologies, ensuring operational continuity, high-availability "
        "solutions and strict SLA compliance. Proven technical leadership and people management skills, combining "
        "business strategy vision, agile methodologies (Scrum) and data intelligence (operational reports and "
        "dashboards in Power BI, plus automation). Known for turning technical challenges into strategic results and "
        "optimized processes.",
    ),
]

# Texto da seção "Sobre" (somente na página inicial; o currículo usa RESUMO)
SOBRE = [
    (
        "Com mais de 16 anos de trajetória na área de Tecnologia da Informação em grandes multinacionais, construí "
        "minha carreira combinando uma sólida base técnica em infraestrutura de servidores com a liderança "
        "estratégica de equipes e gestão de operações críticas.",
        "With over 16 years in the Information Technology field at large multinational companies, I built my career "
        "combining a solid technical foundation in server infrastructure with strategic team leadership and "
        "management of critical operations.",
    ),
    (
        "Minha jornada evoluiu organicamente da administração prática de sistemas operacionais (Windows Server, "
        "Linux, Mainframe e Virtualização) para a gestão da governança de serviços de TI (ITSM/ITIL). Tenho ampla "
        "experiência na liderança de equipes multidisciplinares de infraestrutura (Servidores, HPC, Suporte N2/N3 e "
        "Field Service), focando no desenvolvimento de pessoas, no acompanhamento rigoroso de SLAs e na otimização "
        "de custos operacionais.",
        "My journey evolved organically from hands-on administration of operating systems (Windows Server, Linux, "
        "Mainframe and Virtualization) to IT service governance management (ITSM/ITIL). I have broad experience "
        "leading multidisciplinary infrastructure teams (Servers, HPC, L2/L3 Support and Field Service), focused on "
        "people development, strict SLA tracking and operational cost optimization.",
    ),
    (
        "Nos últimos anos, expandi minha atuação para a Coordenação de Projetos de TI (com forte apoio de "
        "metodologias ágeis como Scrum e Kanban) e incorporei a Inteligência de Dados ao meu dia a dia de gestão, "
        "desenvolvendo painéis executivos em Power BI e automações com Power Automate para tomada de decisão "
        "baseada em indicadores reais.",
        "In recent years, I expanded my scope to IT Project Coordination (strongly supported by agile "
        "methodologies such as Scrum and Kanban) and brought Data Intelligence into my daily management, building "
        "executive dashboards in Power BI and automations with Power Automate for decision-making based on real "
        "indicators.",
    ),
]

# (valor PT, valor EN, rótulo PT, rótulo EN)
DESTAQUES = [
    ("16+", "16+", "anos de experiência em TI", "years of IT experience"),
    ("5.250", "5,250", "servidores com patching em metade do tempo (4 → 2 semanas)",
     "servers patched in half the time (4 → 2 weeks)"),
    ("98%", "98%", "de conformidade de servidores reportada", "reported server compliance"),
    ("100%", "100%", "de cumprimento de SLA", "SLA compliance"),
    ("−50%", "−50%", "no tempo de fila de chamados", "in ticket queue time"),
    ("< 4 h", "< 4 h", "para disponibilizar dados (antes: meses)", "to deliver data (previously: months)"),
]

COMPETENCIAS = [
    (
        ("Infraestrutura & Operações", "Infrastructure & Operations"),
        [
            ("Gestão de infraestrutura e operações de TI", "IT infrastructure and operations management"),
            ("Administração e sustentação de servidores Windows e Linux",
             "Windows and Linux server administration and support"),
            ("Virtualização: VMware e Hyper-V", "Virtualization: VMware and Hyper-V"),
            ("Ambientes HPC e clusters", "HPC environments and clusters"),
            ("SCCM, OpenShift e Tenable", "SCCM, OpenShift and Tenable"),
        ],
    ),
    (
        ("ITSM & Governança", "ITSM & Governance"),
        [
            ("ITSM / ITIL e ServiceNow", "ITSM / ITIL and ServiceNow"),
            ("Gestão de incidentes, mudanças e problemas", "Incident, change and problem management"),
            ("Gestão de SLA, indicadores e relatórios operacionais", "SLA, KPI and operational reporting management"),
            ("Gestão de vulnerabilidades, patches e conformidade", "Vulnerability, patch and compliance management"),
            ("Documentação técnica e base de conhecimento", "Technical documentation and knowledge base"),
            ("Jira e gestão de ativos", "Jira and asset management"),
        ],
    ),
    (
        ("Dados & Monitoramento", "Data & Monitoring"),
        [
            ("Power BI: dashboards e visualização de indicadores", "Power BI: dashboards and KPI visualization"),
            ("Monitoramento: Zabbix e Grafana", "Monitoring: Zabbix and Grafana"),
        ],
    ),
    (
        ("Liderança & Agilidade", "Leadership & Agility"),
        [
            ("Liderança técnica, desenvolvimento de equipes e feedback",
             "Technical leadership, team development and feedback"),
            ("Coordenação de operação e suporte", "Operations and support coordination"),
            ("Scrum, metodologias ágeis e facilitação de cerimônias",
             "Scrum, agile methodologies and ceremony facilitation"),
        ],
    ),
]

# ini/fim = (ano, mês); fim=None => atual
EXPERIENCIA = [
    dict(
        emp="Atos / Semantix",
        cargo=("Líder Técnico", "Technical Lead"),
        ini=(2025, 11), fim=(2026, 9),
        destaque=("Dados de engenharia digital disponíveis em menos de 4 horas (antes: meses).",
                  "Digital engineering data available in under 4 hours (previously months)."),
        resumo=(
            "Liderança técnica na implantação, evolução e entrega em produção de soluções de Engenharia Digital, "
            "assegurando manutenção, monitoramento e controle para garantir alta confiabilidade operacional.",
            "Technical leadership in the deployment, evolution and production delivery of Digital Engineering "
            "solutions, ensuring maintenance, monitoring and control for high operational reliability.",
        ),
        itens=[
            (("Liderança Técnica", "Technical Leadership"),
             ("Apoio às equipes de infraestrutura, desenvolvimento e gestão na resolução de problemas complexos e na "
              "condução de atividades críticas durante implantações. Participação ativa em reuniões com POs, "
              "contribuindo para definições estratégicas, remoção de impedimentos e atuação como facilitador para o "
              "time de desenvolvimento.",
              "Supported infrastructure, development and management teams in solving complex problems and driving "
              "critical activities during deployments. Active participation in meetings with POs, contributing to "
              "strategic decisions, removing impediments and acting as a facilitator for the development team.")),
            (("Arquitetura e Integrações", "Architecture & Integrations"),
             ("Implementação de integrações entre diferentes plataformas de engenharia digital, estruturando um fluxo "
              "automatizado de extração e envio de dados para o Databricks. Os dados passaram a ser consumidos "
              "diretamente em dashboards interativos, garantindo visibilidade em tempo real. O tempo de "
              "disponibilização foi reduzido de meses para menos de 4 horas.",
              "Implemented integrations between different digital engineering platforms, building an automated flow "
              "to extract and send data to Databricks. The data is consumed directly in interactive dashboards, "
              "providing real-time visibility. Delivery time dropped from months to under 4 hours.")),
            (("Qualidade", "Quality"),
             ("Desenvolvimento de painéis em Power BI para controle e monitoramento das conexões e integrações "
              "sistêmicas, reduzindo a indisponibilidade dos serviços em até 98% e aumentando significativamente a "
              "satisfação dos clientes.",
              "Built Power BI dashboards to control and monitor system connections and integrations, reducing "
              "service downtime by up to 98% and significantly increasing customer satisfaction.")),
            (("Melhoria de Processos", "Process Improvement"),
             ("Evolução dos controles de implantação, substituindo o gerenciamento manual em Excel por soluções "
              "integradas no Power BI e Microsoft SharePoint.",
              "Evolved deployment controls, replacing manual Excel management with integrated solutions in Power BI "
              "and Microsoft SharePoint.")),
        ],
        tech="Power BI, AVEVA Global, AVEVA AIS, AVEVA PROII, AVEVA Marine, Microsoft SharePoint, ServiceNow, Jira, "
             "Databricks",
    ),
    dict(
        emp="Atos Brasil",
        cargo=("Coordenador de Infraestrutura e Sustentação de TI", "IT Infrastructure and Support Coordinator"),
        ini=(2022, 6), fim=(2025, 10),
        destaque=("13 pessoas lideradas, 5.250 servidores, 100% de SLA e patching em metade do tempo.",
                  "Led 13 people, 5,250 servers, 100% SLA and patching in half the time."),
        resumo=(
            "Atuação na liderança direta de equipe multidisciplinar de Infraestrutura, composta por 13 profissionais "
            "das áreas de Servidores e High Performance Computing (HPC), conduzindo o desenvolvimento de "
            "competências, gestão de desempenho e fortalecimento da cultura de feedback contínuo, resultando em "
            "aumento do engajamento da equipe e melhoria dos indicadores de produtividade e qualidade operacional.",
            "Direct leadership of a multidisciplinary Infrastructure team of 13 professionals from the Servers and "
            "High Performance Computing (HPC) areas, driving skills development, performance management and a "
            "culture of continuous feedback, resulting in higher team engagement and improved productivity and "
            "operational quality indicators.",
        ),
        itens=[
            (("Liderança Técnica", "Technical Leadership"),
             ("Orientação técnica de equipes, definição de soluções arquiteturais e contribuição para padrões de "
              "infraestrutura. Gestão de fila de chamados, indicadores de SLA, incidentes, mudanças, problemas e base "
              "de conhecimento.",
              "Technical guidance for teams, definition of architectural solutions and contribution to infrastructure "
              "standards. Management of the ticket queue, SLA indicators, incidents, changes, problems and knowledge "
              "base.")),
            (("Melhoria de Processos", "Process Improvement"),
             ("Criação de painéis em Power BI para acompanhamento de indicadores de conformidade de servidores, "
              "resultando em 98% de conformidade reportada. Estruturação de padrão para aplicação de patches em "
              "servidores e clusters HPC (onshore e offshore), reduzindo o tempo de execução de 4 semanas para 2 "
              "semanas em um parque de 5.250 servidores.",
              "Built Power BI dashboards to track server compliance indicators, resulting in 98% reported "
              "compliance. Defined a standard for patching servers and HPC clusters (onshore and offshore), cutting "
              "execution time from 4 weeks to 2 weeks across a fleet of 5,250 servers.")),
            (("Infraestrutura", "Infrastructure"),
             ("Padronização do fluxo de orquestração de servidores físicos e virtuais. Implementação de pipelines "
              "automatizados com Ansible e Python, acelerando o aprovisionamento e entrega de hosts.",
              "Standardized the orchestration flow for physical and virtual servers. Implemented automated "
              "pipelines with Ansible and Python, speeding up host provisioning and delivery.")),
            (("Qualidade", "Quality"),
             ("Revisão e aprimoramento da documentação técnica, criação de padrões de base de conhecimento e "
              "padronização dos atendimentos. Melhoria na análise e solução de problemas, redução de 50% no tempo de "
              "fila e garantia de 100% de cumprimento do SLA. Reconhecimento formal pelo desempenho nas entregas.",
              "Reviewed and improved technical documentation, created knowledge-base standards and standardized "
              "support handling. Better problem analysis and resolution, 50% reduction in queue time and 100% SLA "
              "compliance. Formally recognized for delivery performance.")),
        ],
        tech="Linux Red Hat, Windows, SCCM, OpenShift, Power BI, Python, PowerShell, VMware, Zabbix, Grafana, "
             "Tenable, ServiceNow, Indigo, Genetec, AVEVA Intelatrac, Ansible",
    ),
    dict(
        emp="Atos Brasil",
        cargo=("Analista de Suporte a Aplicações Sênior", "Senior Application Support Analyst"),
        ini=(2022, 1), fim=(2022, 6),
        destaque=("Nuvem privada, Domino/Notes, Zabbix/Grafana e vulnerabilidades com Tenable.",
                  "Private cloud, Domino/Notes, Zabbix/Grafana and vulnerability management with Tenable."),
        resumo=None,
        itens=[
            (("Administração de ambientes e servidores", "Environment and server administration"),
             ("Responsável pelo aprovisionamento e desprovisionamento em nuvem privada.",
              "Responsible for provisioning and deprovisioning in a private cloud.")),
            (("Suporte a plataformas", "Platform support"),
             ("Sustentação de Lotus Domino/Notes e IBM Connect, com monitoramento contínuo via Zabbix e Grafana.",
              "Support for Lotus Domino/Notes and IBM Connect, with continuous monitoring via Zabbix and Grafana.")),
            (("Segurança e conformidade", "Security and compliance"),
             ("Aplicação de patches, controles de segurança e gestão de vulnerabilidades utilizando Tenable.",
              "Patching, security controls and vulnerability management using Tenable.")),
            (("Gestão de serviços de TI", "IT service management"),
             ("Atuação em incidentes, mudanças e configuração de itens no ServiceNow, garantindo o cumprimento dos "
              "SLAs.",
              "Handled incidents, changes and configuration items in ServiceNow, ensuring SLA compliance.")),
        ],
        tech="Windows Server, Linux, IBM Connect, IBM Lotus Domino/Notes, Zabbix, Grafana, ServiceNow",
    ),
    dict(
        emp="Proxxi Tecnologia",
        cargo=("Analista de Suporte N2", "L2 Support Analyst"),
        ini=(2018, 8), fim=(2021, 12),
        destaque=("Servidores Windows/Linux, TEF e administração da base de conhecimento.",
                  "Windows/Linux servers, TEF and knowledge-base administration."),
        resumo=None,
        itens=[
            (("Suporte técnico e atendimento", "Technical support"),
             ("Triagem de incidentes e requisições, com atuação em suporte de segundo nível (N2), incluindo "
              "instalação e configuração de sistemas de TEF e pagamentos.",
              "Incident and request triage, working in second-level (L2) support, including installation and "
              "configuration of TEF and payment systems.")),
            (("Administração de infraestrutura", "Infrastructure administration"),
             ("Gestão de servidores Windows Server e Linux, além de dispositivos de rede.",
              "Management of Windows Server and Linux servers, as well as network devices.")),
            (("Procedimentos e integrações", "Procedures and integrations"),
             ("Criação de procedimentos, execução de testes e homologações, e apoio em integrações de ferramentas.",
              "Creation of procedures, testing and acceptance, and support for tool integrations.")),
            (("Documentação e conhecimento", "Documentation and knowledge"),
             ("Registro de procedimentos técnicos, problemas e erros conhecidos, além da administração da base de "
              "conhecimento.",
              "Recording of technical procedures, problems and known errors, plus knowledge-base administration.")),
            (("Capacitação", "Training"),
             ("Desenvolvimento e realização de treinamentos presenciais e online.",
              "Development and delivery of in-person and online training.")),
        ],
        tech="ServiceNow, Windows Server, Linux openSUSE, Cisco, TEF, Grafana, Slack",
    ),
    dict(
        emp="Proxxi Tecnologia",
        cargo=("Coordenador Field Service", "Field Service Coordinator"),
        ini=(2016, 1), fim=(2018, 8),
        destaque=("30 técnicos em 5 estados, 95% de satisfação e −40% no tempo médio de atendimento.",
                  "30 technicians across 5 states, 95% satisfaction and −40% average handling time."),
        resumo=(
            "Gestão de equipe de 30 técnicos de campo dedicados ao atendimento de clientes comerciais, com foco em "
            "infraestrutura e servidores. Atuação em liderança direta, desenvolvimento de competências e fornecimento "
            "de feedback contínuo, promovendo engajamento e alta performance. Responsável pela implementação de "
            "melhorias nos processos operacionais, garantindo eficiência, qualidade e satisfação dos clientes.",
            "Managed a team of 30 field technicians serving commercial customers, focused on infrastructure and "
            "servers. Direct leadership, skills development and continuous feedback, promoting engagement and high "
            "performance. Responsible for implementing operational process improvements, ensuring efficiency, "
            "quality and customer satisfaction.",
        ),
        itens=[
            (("Liderança Técnica", "Technical Leadership"),
             ("Coordenou equipes operacionais de campo em 5 estados do Nordeste, garantindo o cumprimento dos "
              "indicadores de SLA e satisfação do cliente. Implementou melhorias nos processos de atendimento, "
              "reduzindo o tempo médio em 40% e otimizando a logística de deslocamento dos técnicos, o que resultou "
              "em maior eficiência e fluidez nos atendimentos.",
              "Coordinated field operations teams in 5 states of Brazil's Northeast, meeting SLA and customer "
              "satisfaction targets. Improved service processes, reducing average handling time by 40% and "
              "optimizing technician travel logistics, resulting in greater efficiency and smoother service.")),
            (("Qualidade e Modernização", "Quality and Modernization"),
             ("Implementação de atualizações constantes nos procedimentos técnicos, eliminando barreiras "
              "operacionais e elevando o padrão de atendimento. O resultado foi um índice de satisfação de 95%, com "
              "reconhecimento recorrente pela excelência dos serviços prestados.",
              "Continuously updated technical procedures, removing operational barriers and raising the service "
              "standard. The result was a 95% satisfaction rate, with recurring recognition for service "
              "excellence.")),
            (("Custo e Eficiência", "Cost and Efficiency"),
             ("Reestruturação estratégica da equipe técnica com distribuição geográfica otimizada, reduzindo "
              "deslocamentos desnecessários. Essa medida garantiu menor consumo de combustível, diminuição "
              "significativa do tempo de viagem e maior disponibilidade dos profissionais para atender às demandas "
              "com agilidade.",
              "Strategic restructuring of the technical team with optimized geographic distribution, reducing "
              "unnecessary travel. This lowered fuel consumption, significantly cut travel time and increased "
              "technician availability to respond quickly.")),
        ],
        tech="ServiceNow, Excel, ITSM, IBM z/OS",
    ),
    dict(
        emp="Capgemini Consulting, Technology Outsourcing",
        cargo=("Analista de Infraestrutura Pleno", "Mid-level Infrastructure Analyst"),
        ini=(2013, 11), fim=(2015, 12),
        destaque=("Windows Server, Active Directory, VMware/Hyper-V e serviços de rede corporativa.",
                  "Windows Server, Active Directory, VMware/Hyper-V and corporate network services."),
        resumo=None,
        itens=[
            (("Administração de servidores e infraestrutura", "Server and infrastructure administration"),
             ("Suporte a ambientes Windows Server, Active Directory, DMZ e serviços de rede corporativa.",
              "Support for Windows Server, Active Directory, DMZ and corporate network services environments.")),
            (("Gerenciamento de serviços de rede", "Network services management"),
             ("Atuação com FTP, DHCP, DNS, WINS, NLB, GPO/GPP, IIS, WSUS, VPN, file server, print server, além de "
              "ferramentas como Lotus Domino Administrator e RSA Authentication Manager.",
              "Worked with FTP, DHCP, DNS, WINS, NLB, GPO/GPP, IIS, WSUS, VPN, file and print servers, plus tools "
              "such as Lotus Domino Administrator and RSA Authentication Manager.")),
            (("Virtualização", "Virtualization"),
             ("Administração de servidores virtuais utilizando VMware vCenter, vSphere Client e Hyper-V.",
              "Administration of virtual servers using VMware vCenter, vSphere Client and Hyper-V.")),
            (("Suporte técnico e manutenção", "Technical support and maintenance"),
             ("Apoio a sistemas corporativos, configuração e manutenção de desktops e notebooks, além da instalação "
              "de equipamentos de rede e telecomunicações.",
              "Support for corporate systems, configuration and maintenance of desktops and laptops, and "
              "installation of network and telecom equipment.")),
        ],
        tech="Windows Server, VMware, RSA, IBM Domino/Notes, ITSM, Office",
    ),
    dict(
        emp="IBM Brasil",
        cargo=("Especialista de Serviços Global Júnior", "Junior Global Services Specialist"),
        ini=(2011, 3), fim=(2013, 11),
        destaque=("Automação bancária Santander e rollout de transição Banco Real → Santander.",
                  "Santander banking automation and Banco Real → Santander transition rollout."),
        resumo=None,
        itens=[
            (("Automação bancária", "Banking automation"),
             ("Atendimento às soluções do Santander, incluindo ATMs e equipamentos de fabricantes como Itautec, "
              "Procomp e Wincor, além de estações de trabalho, impressoras e servidores.",
              "Support for Santander solutions, including ATMs and equipment from manufacturers such as Itautec, "
              "Procomp and Wincor, as well as workstations, printers and servers.")),
            (("Projeto de migração", "Migration project"),
             ("Participação no rollout de transição do sistema do Banco Real para a plataforma Santander.",
              "Took part in the rollout migrating Banco Real's system to the Santander platform.")),
            (("Automação comercial", "Retail automation"),
             ("Suporte a soluções de automação comercial e estações de trabalho Lenovo.",
              "Support for retail automation solutions and Lenovo workstations.")),
        ],
        tech="Windows, TEF, ECF",
    ),
    dict(
        emp="Hospital São Salvador",
        cargo=("Coordenador de Suporte de TI", "IT Support Coordinator"),
        ini=(2010, 11), fim=(2011, 3),
        destaque=("Equipe de 3 profissionais, modernização de servidores e alta disponibilidade.",
                  "Team of 3, server modernization and high availability."),
        resumo=(
            "Liderança direta e desenvolvimento de equipe multidisciplinar de profissionais de infraestrutura e "
            "suporte, com 3 profissionais, realizando gestão de competências e feedback contínuo do time.",
            "Direct leadership and development of a multidisciplinary infrastructure and support team of 3 "
            "professionals, handling skills management and continuous feedback.",
        ),
        itens=[
            (("Liderança Técnica", "Technical Leadership"),
             ("Gestão dos serviços de TI e das operações tecnológicas hospitalares, garantindo alta disponibilidade, "
              "segurança da informação e suporte contínuo às atividades clínicas.",
              "Management of IT services and hospital technology operations, ensuring high availability, "
              "information security and continuous support for clinical activities.")),
            (("Modernização de Sistemas Legados", "Legacy Systems Modernization"),
             ("Atualização das versões de servidores e otimização da infraestrutura, elevando a eficiência "
              "operacional e proporcionando melhor desempenho para os usuários.",
              "Upgraded server versions and optimized infrastructure, raising operational efficiency and improving "
              "performance for users.")),
            (("Qualidade e Melhoria Contínua", "Quality and Continuous Improvement"),
             ("Definição de procedimentos e aprimoramento constante dos processos tecnológicos, reduzindo "
              "indisponibilidades e assegurando maior confiabilidade dos serviços.",
              "Defined procedures and continuously improved technology processes, reducing downtime and ensuring "
              "greater service reliability.")),
        ],
        tech="Windows Server, Oracle Server, Linux, ITSM, Zabbix",
    ),
    dict(
        emp="Vanguard-IT Solution",
        cargo=("Analista de Suporte Júnior – Suporte TSM", "Junior Support Analyst – TSM Support"),
        ini=(2010, 8), fim=(2010, 11),
        destaque=("Suporte com IBM TSM/ITM e servidores físicos e virtuais em VMware.",
                  "Support with IBM TSM/ITM and physical and virtual servers on VMware."),
        resumo=None,
        itens=[
            (("Suporte a Clientes", "Customer support"),
             ("Utilização das ferramentas IBM TSM e ITM para monitoramento, gerenciamento e apoio técnico.",
              "Use of IBM TSM and ITM tools for monitoring, management and technical support.")),
            (("Servidores Windows e Linux", "Windows and Linux servers"),
             ("Instalação e configuração de servidores físicos e virtuais em ambientes VMware.",
              "Installation and configuration of physical and virtual servers in VMware environments.")),
            (("Ferramentas Wiki", "Wiki tools"),
             ("Criação e utilização de plataformas colaborativas para documentação e compartilhamento de "
              "conhecimento.",
              "Creation and use of collaborative platforms for documentation and knowledge sharing.")),
        ],
        tech="IBM Tivoli TSM, ITM, VMware, Wiki, Windows Server, Linux",
    ),
    dict(
        emp="Stefanini IT Solutions",
        cargo=("Técnico de Suporte Nível 2 – Service Desk", "Level 2 Support Technician – Service Desk"),
        ini=(2008, 10), fim=(2010, 9),
        destaque=("Service Desk N2, gestão de incidentes e manutenção de desktops e notebooks.",
                  "Level 2 Service Desk, incident management and desktop/laptop maintenance."),
        resumo=None,
        itens=[
            (("Suporte Técnico e Infraestrutura", "Technical Support and Infrastructure"),
             ("Atendimento a sistemas corporativos, além de manutenção preventiva e corretiva, montagem e "
              "configuração de desktops e notebooks.",
              "Support for corporate systems, plus preventive and corrective maintenance, assembly and "
              "configuration of desktops and laptops.")),
            (("Atendimento e Gestão de Incidentes", "Service and Incident Management"),
             ("Atuação completa em processos de Service Desk e Gerenciamento de Incidentes, focando na resolução "
              "rápida de chamados e suporte aos usuários.",
              "End-to-end work in Service Desk and Incident Management processes, focused on fast ticket "
              "resolution and user support.")),
        ],
        tech="Microsoft SQL Server, BDE Administrator, VNC, Microsoft Office, BrOffice, CRK, CDC",
    ),
]

FORMACAO = [(
    "Bacharelado em Sistemas de Informação – Faculdade Santa Maria, 2009",
    "Bachelor's degree in Information Systems – Faculdade Santa Maria, 2009",
)]

CERTIFICACOES = [
    ("Certified ScrumMaster (CSM) – Scrum Alliance, 2025", "Certified ScrumMaster (CSM) – Scrum Alliance, 2025"),
    ("L2M – License to Manager – Atos Brasil, 2024", "L2M – License to Manager – Atos Brasil, 2024"),
    ("ITIL V2 – IT Service Management Foundation, 2010", "ITIL V2 – IT Service Management Foundation, 2010"),
    ("Microsoft Certified Professional Specialist (MCPS) – Windows Server 2012, 2015",
     "Microsoft Certified Professional Specialist (MCPS) – Windows Server 2012, 2015"),
    ("Interskill – Mainframe Specialist: Linux Operations and Programming, 2020",
     "Interskill – Mainframe Specialist: Linux Operations and Programming, 2020"),
    ("Cloud Service Management and Operations Explorer, 2020", "Cloud Service Management and Operations Explorer, 2020"),
    ("IBM Cloud Private: Foundation Technology; Infrastructure and Architecture; Installation and Configuration; "
     "CI/CD Pipelines, 2020",
     "IBM Cloud Private: Foundation Technology; Infrastructure and Architecture; Installation and Configuration; "
     "CI/CD Pipelines, 2020"),
    ("IBM Cloud Essentials; IBM Cloud Core; Building Cloud-Native and Multicloud Applications, 2020",
     "IBM Cloud Essentials; IBM Cloud Core; Building Cloud-Native and Multicloud Applications, 2020"),
]

CURSOS = [
    ("Microsoft Azure Fundamentals", "Microsoft Azure Fundamentals"),
    ("AWS Security Fundamentals", "AWS Security Fundamentals"),
    ("Trilha IBM Cloud Private: Architecture, Infrastructure, Installation, CI/CD, Kubernetes, Docker e Microservices",
     "IBM Cloud Private track: Architecture, Infrastructure, Installation, CI/CD, Kubernetes, Docker and "
     "Microservices"),
    ("IBM System x Architecture & SAN Storage", "IBM System x Architecture & SAN Storage"),
    ("Administração de Servidores Linux", "Linux Server Administration"),
    ("Administração de Redes Mistas Linux", "Mixed Linux Networks Administration"),
    ("TSM 6.2 Tivoli Storage Manager", "TSM 6.2 Tivoli Storage Manager"),
    ("CHPT – Hardware Professional", "CHPT – Hardware Professional"),
    ("PL/SQL", "PL/SQL"),
    ("Treinamentos técnicos Lenovo", "Lenovo technical training"),
]

IDIOMAS = [
    ("Espanhol: avançado", "Spanish: advanced"),
    ("Inglês: intermediário", "English: intermediate"),
]

# Rótulos da interface
T = dict(
    nav_resultados=("Resultados", "Highlights"),
    nav_sobre=("Sobre", "About"),
    nav_comp=("Competências", "Skills"),
    nav_traj=("Trajetória", "Career"),
    nav_contato=("Contato", "Contact"),
    voltar=("← Início", "← Home"),
    ver_cv=("Ver currículo completo", "View full résumé"),
    baixar=("Baixar PDF", "Download PDF"),
    imprimir=("Imprimir", "Print"),
    sec_resultados=("Resultados em números", "Results in numbers"),
    sec_sobre=("Resumo profissional", "Professional summary"),
    sec_sobre_site=("Sobre", "About"),
    sec_comp=("Competências", "Skills"),
    sec_traj=("Trajetória profissional", "Career path"),
    sec_exp=("Experiência profissional", "Professional experience"),
    sec_form=("Formação acadêmica", "Education"),
    sec_cert=("Certificações e badges", "Certifications & badges"),
    sec_cursos=("Cursos complementares", "Additional courses"),
    sec_idiomas=("Idiomas", "Languages"),
    sec_contato=("Vamos conversar?", "Let's talk?"),
    contato_txt=("Aberto a conversas sobre infraestrutura, ITSM, dados e liderança técnica.",
                 "Open to conversations about infrastructure, ITSM, data and technical leadership."),
    resp=("Principais responsabilidades e resultados", "Key responsibilities and results"),
    tecnologias=("Tecnologias", "Technologies"),
    atual=("atual", "present"),
    ver_mais=("Ver detalhes no currículo completo →", "See details in the full résumé →"),
    rodape=("Feito com HTML, CSS e JavaScript puros · Publicado com GitHub Pages",
            "Built with plain HTML, CSS and JavaScript · Published with GitHub Pages"),
    idioma_aria=("Alternar idioma", "Switch language"),
    tema_aria=("Alternar tema claro/escuro", "Toggle light/dark theme"),
)

MESES = (
    ("jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"),
    ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"),
)

TITULO = (
    f"{NOME} | Infraestrutura, ITSM e Liderança Técnica",
    f"{NOME} | Infrastructure, ITSM & Technical Leadership",
)
DESCRICAO = (
    "Profissional sênior de TI com mais de 16 anos em infraestrutura de servidores, ITSM/ITIL, Power BI e "
    "liderança técnica. Currículo e portfólio profissional."
)

# --------------------------------------------------------------------------- #
# HELPERS
# --------------------------------------------------------------------------- #
LANGS = ("pt", "en")


def dual(tag, fn, cls=""):
    """Gera o mesmo elemento duas vezes (pt e en); o CSS esconde o idioma inativo."""
    c = f' class="{cls}"' if cls else ""
    return "".join(f'<{tag} lang="{lg}"{c}>{fn(i)}</{tag}>' for i, lg in enumerate(LANGS))


def bi(pair):
    return dual("span", lambda i: e(pair[i]))


def periodo(job, i):
    def fmt(ym):
        return f"{MESES[i][ym[1] - 1]}/{ym[0]}" if i == 0 else f"{MESES[i][ym[1] - 1]} {ym[0]}"

    fim = fmt(job["fim"]) if job["fim"] else T["atual"][i]
    return f"{fmt(job['ini'])} – {fim}"


def iso(ym):
    return f"{ym[0]}-{ym[1]:02d}"


HEAD_SCRIPT = """<script>
(function(){try{var d=document.documentElement,q=new URLSearchParams(location.search),
l=q.get('lang')||localStorage.getItem('lang')||((navigator.language||'pt').slice(0,2)==='en'?'en':'pt'),
t=q.get('theme')||localStorage.getItem('theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
l=l==='en'?'en':'pt';d.dataset.lang=l;d.lang=l==='en'?'en':'pt-BR';d.dataset.theme=t==='dark'?'dark':'light';}catch(x){}})();
</script>"""


def json_ld():
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": NOME,
        "jobTitle": "IT Infrastructure & Operations Leader",
        "sameAs": [LINKEDIN],
        "address": {"@type": "PostalAddress", "addressLocality": "Recife", "addressRegion": "PE",
                    "addressCountry": "BR"},
        "knowsAbout": ["ITIL", "ITSM", "ServiceNow", "Power BI", "VMware", "Scrum", "Linux", "Windows Server"],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def head(extra_css=()):
    css = "".join(f'\n<link rel="stylesheet" href="{c}">' for c in ("styles.css", *extra_css))
    return f"""<!doctype html>
<html lang="pt-BR" data-lang="pt" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(TITULO[0])}</title>
<meta name="description" content="{e(DESCRICAO)}">
<meta name="author" content="{e(NOME)}">
<meta name="theme-color" content="#0a6e6e">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(TITULO[0])}">
<meta property="og:description" content="{e(DESCRICAO)}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
{HEAD_SCRIPT}{css}
{json_ld()}
</head>
<body data-title-pt="{e(TITULO[0])}" data-title-en="{e(TITULO[1])}">
<a class="skip" href="#main">{bi(("Ir para o conteúdo", "Skip to content"))}</a>
"""


def toggles():
    return f"""<div class="toggles no-print">
  <button type="button" id="lang-toggle" class="icon-btn" aria-label="{e(T['idioma_aria'][0])} / {e(T['idioma_aria'][1])}">{dual('span', lambda i: 'EN' if i == 0 else 'PT')}</button>
  <button type="button" id="theme-toggle" class="icon-btn" aria-label="{e(T['tema_aria'][0])} / {e(T['tema_aria'][1])}"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.5a6.5 6.5 0 0 1 0 13z" fill="currentColor"/></svg></button>
</div>"""


def pdf_link(cls="btn btn-ghost"):
    return "".join(
        f'<a lang="{lg}" class="{cls}" href="{PDF[lg]}" download>{e(T["baixar"][i])}</a>' for i, lg in enumerate(LANGS)
    )


def footer():
    return f"""<footer class="site-footer">
  <div class="wrap">
    <p>© {date.today().year} {e(NOME)} · {bi(T['rodape'])}</p>
  </div>
</footer>
<script src="app.js" defer></script>
</body>
</html>
"""


def contato_linha():
    return (
        f'<a href="tel:{TELEFONE_TEL}">{TELEFONE}</a> (<a href="{WHATSAPP_URL}" rel="noopener" target="_blank">WhatsApp</a>)'
        f' <span aria-hidden="true">·</span> <a href="mailto:{EMAIL}">{EMAIL}</a>'
        f' <span aria-hidden="true">·</span> <a href="{LINKEDIN}" rel="me noopener" target="_blank">{LINKEDIN_LABEL}</a>'
        f' <span aria-hidden="true">·</span> {bi(LOCAL)}'
    )


# --------------------------------------------------------------------------- #
# INDEX
# --------------------------------------------------------------------------- #
def build_index():
    h = [head()]
    h.append(f"""<header class="site-header no-print">
  <div class="wrap bar">
    <a class="brand" href="#topo" aria-label="{e(NOME)}"><span class="mono">RS</span><span class="brand-name">{e(NOME)}</span></a>
    <nav aria-label="Principal">
      <a href="#resultados">{bi(T['nav_resultados'])}</a>
      <a href="#sobre">{bi(T['nav_sobre'])}</a>
      <a href="#competencias">{bi(T['nav_comp'])}</a>
      <a href="#trajetoria">{bi(T['nav_traj'])}</a>
      <a href="#contato">{bi(T['nav_contato'])}</a>
    </nav>
    {toggles()}
  </div>
</header>
<main id="main">
<section class="hero" id="topo">
  <div class="wrap">
    <p class="eyebrow">{bi(LOCAL)}</p>
    <h1>{e(NOME)}</h1>
    <p class="headline">{bi(HEADLINE)}</p>
    <p class="lead">{bi(TAGLINE)}</p>
    <div class="cta">
      <a class="btn btn-primary" lang="pt" href="curriculo.html">{e(T['ver_cv'][0])}</a>
      <a class="btn btn-primary" lang="en" href="curriculo.html">{e(T['ver_cv'][1])}</a>
      {pdf_link()}
      <a class="btn btn-ghost" href="{LINKEDIN}" rel="me noopener" target="_blank">LinkedIn</a>
    </div>
  </div>
</section>
""")
    # Resultados
    tiles = "".join(
        f'<li class="tile">{dual("span", lambda i, d=d: e(d[i]), "num")}{dual("span", lambda i, d=d: e(d[2 + i]), "lbl")}</li>'
        for d in DESTAQUES
    )
    h.append(f"""<section class="section" id="resultados">
  <div class="wrap">
    <h2>{bi(T['sec_resultados'])}</h2>
    <ul class="tiles">{tiles}</ul>
  </div>
</section>
""")
    # Sobre
    h.append(f"""<section class="section alt" id="sobre">
  <div class="wrap narrow">
    <h2>{bi(T['sec_sobre_site'])}</h2>
    {''.join(dual('p', lambda i, p=p: e(p[i])) for p in SOBRE)}
  </div>
</section>
""")
    # Competências
    cards = ""
    for titulo, itens in COMPETENCIAS:
        lis = "".join(f"<li>{bi(it)}</li>" for it in itens)
        cards += f'<article class="card"><h3>{bi(titulo)}</h3><ul class="checks">{lis}</ul></article>'
    h.append(f"""<section class="section" id="competencias">
  <div class="wrap">
    <h2>{bi(T['sec_comp'])}</h2>
    <div class="cards">{cards}</div>
  </div>
</section>
""")
    # Trajetória
    lis = ""
    for j in EXPERIENCIA:
        lis += dual(
            "li",
            lambda i, j=j: (
                f'<time>{e(periodo(j, i))}</time>'
                f'<h3>{e(j["cargo"][i])} <span class="at">· {e(j["emp"])}</span></h3>'
                f'<p>{e(j["destaque"][i])}</p>'
            ),
        )
    h.append(f"""<section class="section alt" id="trajetoria">
  <div class="wrap narrow">
    <h2>{bi(T['sec_traj'])}</h2>
    <ol class="timeline">{lis}</ol>
    <p class="more"><a lang="pt" href="curriculo.html">{e(T['ver_mais'][0])}</a><a lang="en" href="curriculo.html">{e(T['ver_mais'][1])}</a></p>
  </div>
</section>
""")
    # Certificações (resumo)
    certs = "".join(f"<li>{bi(c)}</li>" for c in CERTIFICACOES[:4])
    h.append(f"""<section class="section" id="certificacoes">
  <div class="wrap narrow">
    <h2>{bi(T['sec_cert'])}</h2>
    <ul class="checks">{certs}</ul>
    <p class="more"><a lang="pt" href="curriculo.html#certificacoes">{e(T['ver_mais'][0])}</a><a lang="en" href="curriculo.html#certificacoes">{e(T['ver_mais'][1])}</a></p>
  </div>
</section>
""")
    # Contato
    h.append(f"""<section class="section contact" id="contato">
  <div class="wrap narrow center">
    <h2>{bi(T['sec_contato'])}</h2>
    <p>{bi(T['contato_txt'])}</p>
    <div class="cta center">
      <a class="btn btn-primary" href="mailto:{EMAIL}">{EMAIL}</a>
      <a class="btn btn-ghost" href="{WHATSAPP_URL}" rel="noopener" target="_blank">WhatsApp · {TELEFONE}</a>
      <a class="btn btn-ghost" href="{LINKEDIN}" rel="me noopener" target="_blank">LinkedIn</a>
    </div>
  </div>
</section>
</main>
""")
    h.append(footer())
    return "".join(h)


# --------------------------------------------------------------------------- #
# CURRÍCULO
# --------------------------------------------------------------------------- #
def build_cv():
    h = [head(("curriculo.css",))]
    h.append(f"""<header class="site-header no-print">
  <div class="wrap bar">
    <a class="brand" href="index.html"><span class="mono">RS</span><span class="brand-name">{bi(T['voltar'])}</span></a>
    <div class="actions">
      {pdf_link("btn btn-ghost btn-sm")}
      <button type="button" class="btn btn-ghost btn-sm js-print">{bi(T['imprimir'])}</button>
    </div>
    {toggles()}
  </div>
</header>
<main id="main" class="cv">
<div class="wrap narrow">
  <header class="cv-head">
    <h1>{e(NOME)}</h1>
    <p class="headline">{bi(HEADLINE)}</p>
    <p class="contact-line">{contato_linha()}</p>
  </header>
""")
    h.append(f'<section class="cv-sec"><h2>{bi(T["sec_sobre"])}</h2>'
             + "".join(dual("p", lambda i, p=p: e(p[i])) for p in RESUMO) + "</section>")

    # competências (compacto)
    grupos = ""
    for titulo, itens in COMPETENCIAS:
        lis = "".join(f"<li>{bi(it)}</li>" for it in itens)
        grupos += f'<div class="skill-group"><h3>{bi(titulo)}</h3><ul>{lis}</ul></div>'
    h.append(f'<section class="cv-sec" id="competencias"><h2>{bi(T["sec_comp"])}</h2><div class="skill-grid">{grupos}</div></section>')

    # experiência
    jobs = ""
    for j in EXPERIENCIA:
        def corpo(i, j=j):
            out = (
                f'<header><h3>{e(j["emp"])} <span class="role">· {e(j["cargo"][i])}</span></h3>'
                f'<time datetime="{iso(j["ini"])}">{e(periodo(j, i))}</time></header>'
            )
            if j["resumo"]:
                out += f'<p class="job-intro">{e(j["resumo"][i])}</p>'
                out += f'<p class="job-sub">{e(T["resp"][i])}</p>'
            out += "<ul>" + "".join(
                f"<li><strong>{e(rot[i])}:</strong> {e(txt[i])}</li>" for rot, txt in j["itens"]
            ) + "</ul>"
            out += f'<p class="tech"><strong>{e(T["tecnologias"][i])}:</strong> {e(j["tech"])}</p>'
            return out

        jobs += dual("article", corpo, "job")
    h.append(f'<section class="cv-sec" id="experiencia"><h2>{bi(T["sec_exp"])}</h2>{jobs}</section>')

    h.append(f'<section class="cv-sec"><h2>{bi(T["sec_form"])}</h2><ul class="plain">'
             + "".join(f"<li>{bi(f)}</li>" for f in FORMACAO) + "</ul></section>")
    h.append(f'<section class="cv-sec" id="certificacoes"><h2>{bi(T["sec_cert"])}</h2><ul class="plain">'
             + "".join(f"<li>{bi(c)}</li>" for c in CERTIFICACOES) + "</ul></section>")
    h.append(f'<section class="cv-sec"><h2>{bi(T["sec_cursos"])}</h2><ul class="inline-list">'
             + "".join(f"<li>{bi(c)}</li>" for c in CURSOS) + "</ul></section>")
    h.append(f'<section class="cv-sec"><h2>{bi(T["sec_idiomas"])}</h2><ul class="inline-list">'
             + "".join(f"<li>{bi(c)}</li>" for c in IDIOMAS) + "</ul></section>")
    h.append("</div>\n</main>\n")
    h.append(footer())
    return "".join(h)


def main():
    (ROOT / "index.html").write_text(build_index(), encoding="utf-8")
    (ROOT / "curriculo.html").write_text(build_cv(), encoding="utf-8")
    print("OK: index.html e curriculo.html gerados em", ROOT)


if __name__ == "__main__":
    main()
