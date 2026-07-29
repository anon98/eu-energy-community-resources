<div align="center">

# ⚡ EU Energy Community Resources

### Research • Regulation • Flexibility • Grid Integration

A curated knowledge hub for building, modelling, and operating energy communities in Europe.

[![EU Focus](https://img.shields.io/badge/Scope-European_Union-003399?style=flat-square&logo=europeanunion&logoColor=white)](https://energy.ec.europa.eu/topics/markets-and-consumers/energy-consumers-and-prosumers/energy-communities_en)
[![Resources](https://img.shields.io/badge/Resources-Curated-14854F?style=flat-square)](#explore-the-hub)
[![Research](https://img.shields.io/badge/Focus-EC–DSO_Coordination-6F42C1?style=flat-square)](#grid-constraints-flexibility-and-operating-envelopes)
[![Updated](https://img.shields.io/badge/Updated-July_2026-0969DA?style=flat-square)](#)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-EF9421?style=flat-square)](LICENSE)

[Explore resources](#explore-the-hub) · [Start reading](#start-here) · [Publications](#selected-scientific-publications) · [Contribute](CONTRIBUTING.md)

</div>

---

<a id="explore-the-hub"></a>
## Explore the hub

| | Area | Go directly to |
|---:|---|---|
| ⚖️ | **Law & policy** | [EU directives, regulations, and implementation tracking](#eu-legal-and-policy-framework) |
| 📚 | **Research** | [Selected peer-reviewed publications](#selected-scientific-publications) |
| 🧰 | **Tools** | [Grid, optimization, control, and co-simulation software](#open-source-software) |
| 📊 | **Data** | [European datasets, load profiles, and test networks](#open-data-and-test-systems) |
| 🔌 | **Standards** | [Interoperability and communication standards](#interoperability-and-technical-standards) |
| 🇪🇺 | **Projects** | [European projects, networks, and knowledge platforms](#european-projects-and-networks) |

### Choose your pathway

<table>
<tr>
<td width="33%" valign="top">

#### 🎓 New to the topic

1. Read the [six essential resources](#start-here)
2. Understand [REC versus CEC](#rec-and-cec-are-not-interchangeable)
3. Scan the [foundational reviews](#foundations-definitions-and-governance)

</td>
<td width="33%" valign="top">

#### 🧪 Building a study

1. Select [software](#open-source-software)
2. Select [data and test grids](#open-data-and-test-systems)
3. Use the [evaluation dimensions](#recommended-evaluation-dimensions)

</td>
<td width="33%" valign="top">

#### ⚡ Working on EC–DSO coordination

1. Read [grid and DOE papers](#grid-constraints-flexibility-and-operating-envelopes)
2. Review [interoperability standards](#interoperability-and-technical-standards)
3. Select [grid and optimization tools](#open-source-software)

</td>
</tr>
</table>

---

### Scope

This hub collects European Union legislation, policy guidance, scientific publications, open-source tools, datasets, standards, and projects relevant to **energy communities**.

The collection is especially focused on:

- renewable energy communities (RECs) and citizen energy communities (CECs);
- community energy management, scheduling, and model predictive control;
- energy-community–distribution-system-operator (DSO) coordination;
- network-safe operating envelopes and dynamic operating envelopes (DOEs);
- flexibility declaration, aggregation, and market participation;
- hosting capacity, distribution-grid constraints, and fairness;
- local electricity markets, collective self-consumption, and benefit allocation.

> [!NOTE]
> This is a living resource. Links and descriptions were last checked on **29 July 2026**. Inclusion does not imply endorsement.

> [!IMPORTANT]
> Legal material is provided for research orientation, not legal advice. Always check the current consolidated EU text and national transposition.

<a id="start-here"></a>
## 🚀 Start here

For a compact introduction, read these resources in order:

1. [European Commission: Energy communities](https://energy.ec.europa.eu/topics/markets-and-consumers/energy-consumers-and-prosumers/energy-communities_en) — official overview and links to EU support material.
2. [Directive (EU) 2018/2001, consolidated text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02018L2001-20240716) — definitions and rights of renewable energy communities, especially Articles 2(16) and 22.
3. [Directive (EU) 2019/944, consolidated text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02019L0944-20240716) — citizen energy communities and electricity-market participation, especially Articles 2(11) and 16.
4. [Caramizaru and Uihlein (2020)](https://publications.jrc.ec.europa.eu/repository/handle/JRC119433) — accessible JRC overview of European energy-community models and cases.
5. [Gjorgievski et al. (2021)](https://doi.org/10.1016/j.renene.2021.01.078) — review of social arrangements, technical designs, and impacts.
6. [Barabino et al. (2023)](https://doi.org/10.1016/j.segan.2023.101187) — review of modelling choices, business models, and optimization objectives.

<a id="eu-legal-and-policy-framework"></a>
## ⚖️ EU legal and policy framework

### Core legislation

| Instrument | Why it matters |
|---|---|
| [Renewable Energy Directive: Directive (EU) 2018/2001](https://eur-lex.europa.eu/eli/dir/2018/2001/oj) | Introduces the EU concept of the **renewable energy community** and establishes enabling-framework requirements. Use the [consolidated text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02018L2001-20240716) for amendments. |
| [Electricity Directive: Directive (EU) 2019/944](https://eur-lex.europa.eu/eli/dir/2019/944/oj) | Defines the **citizen energy community** and its electricity-market rights and responsibilities. Use the [consolidated text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02019L0944-20240716). |
| [Directive (EU) 2024/1711](https://eur-lex.europa.eu/eli/dir/2024/1711/oj) | Part of the 2024 electricity-market-design reform; strengthens consumer protection and establishes a framework for energy sharing. |
| [Electricity Regulation: Regulation (EU) 2019/943](https://eur-lex.europa.eu/eli/reg/2019/943/oj) | Sets wholesale-market, balancing, congestion-management, aggregation, and system-operation principles. |
| [Regulation (EU) 2024/1747](https://eur-lex.europa.eu/eli/reg/2024/1747/oj) | Amends the electricity-market regulation as part of the 2024 market-design reform. |
| [Energy Efficiency Directive: Directive (EU) 2023/1791](https://eur-lex.europa.eu/eli/dir/2023/1791/oj) | Relevant to energy poverty, vulnerable customers, local planning, demand response, and efficiency-first community actions. |
| [Energy Performance of Buildings Directive: Directive (EU) 2024/1275](https://eur-lex.europa.eu/eli/dir/2024/1275/oj) | Relevant to building renovation, solar deployment, smart readiness, charging infrastructure, and building-level collective action. |
| [General Data Protection Regulation: Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Governs personal-data processing, including granular metering and household flexibility data. |
| [Data Act: Regulation (EU) 2023/2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj) | Relevant to access, portability, and use of data from connected products and related services. |

<a id="rec-and-cec-are-not-interchangeable"></a>
### REC and CEC are not interchangeable

The two EU concepts overlap but have different legal scopes. A REC is tied to renewable energy, proximity, and specific control criteria under the Renewable Energy Directive. A CEC is an electricity-market concept under the Electricity Directive and may undertake a broader set of electricity activities. National transposition determines the operational details, including legal forms, proximity rules, metering, settlement, network charges, and licensing.

<details>
<summary><strong>Quick comparison: REC versus CEC</strong></summary>

| Dimension | Renewable energy community | Citizen energy community |
|---|---|---|
| Main EU basis | Directive (EU) 2018/2001 | Directive (EU) 2019/944 |
| Energy scope | Renewable energy | Electricity |
| Proximity | Embedded in the EU definition | No equivalent EU-level proximity criterion |
| Effective control | Limited to qualifying nearby members/shareholders | Member State may restrict effective control to specified participant classes |
| Primary purpose | Environmental, economic, or social community benefits | Environmental, economic, or social community benefits |

This table is an orientation aid, not a substitute for the directives or national law.

</details>

### Policy and implementation tracking

- [European Commission: Setting up an energy community](https://energy.ec.europa.eu/setting-energy-community_en)
- [European Commission energy-community policy page](https://energy.ec.europa.eu/topics/markets-and-consumers/energy-consumers-and-prosumers/energy-communities_en)
- [Florence School of Regulation: mapping policies and regulations](https://fsr.eui.eu/mapping-policies-and-regulations-for-energy-communities-across-europe/)
- [REScoop.eu policy and transposition resources](https://www.rescoop.eu/toolbox)
- [Council of European Energy Regulators](https://www.ceer.eu/) — regulatory reports on active customers, flexibility, DSOs, and consumer protection.
- [ACER](https://www.acer.europa.eu/) — EU electricity-market monitoring, framework guidelines, and regulatory decisions.

<a id="implementation-and-practitioner-resources"></a>
## 🏗️ Implementation and practitioner resources

| Resource | Use |
|---|---|
| [European Commission setup guidance](https://energy.ec.europa.eu/setting-energy-community_en) | Entry point for governance, finance, technical assistance, and archived Energy Communities Repository material. |
| [REScoop.eu toolbox](https://www.rescoop.eu/toolbox) | Cooperative governance, financing, legal models, citizen participation, and policy guidance. |
| [Energy Community Platform: digital-tools guide](https://energycommunityplatform.eu/resources/digital-tools-for-energy-communities-a-short-guide/) | Practical overview of digital tools for monitoring, forecasting, demand response, mobility, and community management. |
| [COMPILE knowledge base](https://www.compile-project.eu/) | Experiences and methods for local energy-community development and operation. |
| [Clean Energy for EU Islands](https://clean-energy-islands.ec.europa.eu/) | Transition agendas, project support, and island-community cases. |
| [EU Covenant of Mayors](https://eu-mayors.ec.europa.eu/) | Local-energy and climate planning resources for municipalities. |

<a id="selected-scientific-publications"></a>
## 📚 Selected scientific publications

The list prioritizes foundational work, systematic reviews, methods relevant to network-aware community operation, and studies with reusable research concepts.

<a id="foundations-definitions-and-governance"></a>
### Foundations, definitions, and governance

| Publication | Relevance |
|---|---|
| Koirala et al. (2016), [*Energetic communities for community energy*](https://doi.org/10.1016/j.rser.2015.11.080) | Foundational review of integrated community-energy systems. |
| Lowitzsch, Hoicka, and van Tulder (2020), [*Renewable energy communities under the 2019 European Clean Energy Package*](https://doi.org/10.1016/j.rser.2019.109489) | Governance interpretation of the EU legal framework. |
| Caramizaru and Uihlein (2020), [*Energy communities: an overview of energy and social innovation*](https://publications.jrc.ec.europa.eu/repository/handle/JRC119433) | JRC report with European cases, activities, organizational forms, and policy implications. |
| Gjorgievski, Cundeva, and Georghiou (2021), [*Social arrangements, technical designs and impacts of energy communities: A review*](https://doi.org/10.1016/j.renene.2021.01.078) | Integrates social, organizational, and engineering dimensions. |
| Frieden et al. (2021), [*Are we on the right track? Collective self-consumption and energy communities in the European Union*](https://doi.org/10.1016/j.scs.2021.103273) | Comparison of emerging national implementation approaches. |
| Tarpani et al. (2022), [*Energy Communities Implementation in the European Union*](https://doi.org/10.3390/su141912528) | Cross-country assessment of implementation status and barriers. |

### Business models, markets, and allocation

| Publication | Relevance |
|---|---|
| Reis et al. (2021), [*Business models for energy communities: A review of key issues and trends*](https://doi.org/10.1016/j.rser.2021.111013) | Business-model archetypes, value propositions, and revenue logic. |
| Tushar et al. (2021), [*Peer-to-peer energy systems for connected communities*](https://doi.org/10.1016/j.apenergy.2020.116131) | Technical and market review of peer-to-peer community systems. |
| Capper et al. (2022), [*Peer-to-peer, community self-consumption, and transactive energy*](https://doi.org/10.1016/j.rser.2022.112403) | Systematic review and terminology across local-market models. |
| Gržanić et al. (2021), [*Electricity cost-sharing in energy communities under dynamic pricing and uncertainty*](https://doi.org/10.1109/ACCESS.2021.3059476) | Cost allocation and uncertainty-aware community scheduling. |
| Lüth, Weibezahn, and Zepter (2020), [*On distributional effects in local electricity market designs*](https://doi.org/10.3390/en13081993) | Fairness and distributional effects in a German case study. |
| Kubli and Puranik (2023), [*A typology of business models for energy communities*](https://doi.org/10.1016/j.rser.2023.113588) | Structured business-model typology for research and practice. |

### Modelling, optimization, and control

| Publication | Relevance |
|---|---|
| Barabino et al. (2023), [*Energy Communities: A review on trends, energy system modelling, business models, and optimisation objectives*](https://doi.org/10.1016/j.segan.2023.101187) | Direct guide to model boundaries, objectives, and evaluation choices. |
| Schwarz et al. (2021), [*pycity_scheduling—A Python framework for the development and assessment of optimisation-based power scheduling algorithms*](https://doi.org/10.1016/j.softx.2021.100839) | Reproducible scheduling framework for local multi-energy systems. |
| Orozco et al. (2022), [*Intra-day scheduling of a local energy community coordinated with day-ahead multistage decisions*](https://doi.org/10.1016/j.segan.2021.100573) | Links day-ahead decisions with intraday recourse. |
| Secchi et al. (2021), [*Multi-objective battery sizing optimisation for renewable energy communities with distribution-level constraints*](https://doi.org/10.1016/j.apenergy.2021.117171) | Couples community investment decisions to grid constraints. |
| Tomar et al. (2021), [*An integrated flexibility optimizer for economic gains of local energy communities*](https://doi.org/10.1016/j.segan.2021.100518) | Community flexibility optimization and economic assessment. |

<a id="grid-constraints-flexibility-and-operating-envelopes"></a>
### Grid constraints, flexibility, and operating envelopes

| Publication | Relevance |
|---|---|
| Hadush and Meeus (2018), [*DSO–TSO cooperation issues and solutions for distribution grid congestion management*](https://doi.org/10.1016/j.enpol.2018.05.065) | Coordination principles for accessing distributed flexibility. |
| Silva et al. (2018), [*Estimating the active and reactive power flexibility area at the TSO–DSO interface*](https://doi.org/10.1109/TPWRS.2018.2805765) | P–Q flexibility aggregation and network-feasible regions. |
| Petrou et al. (2021), [*Ensuring distribution network integrity using dynamic operating limits for prosumers*](https://doi.org/10.1109/TSG.2021.3081371) | Core reference for time-varying import/export limits derived from network constraints. |
| Dynge et al. (2021), [*Impact of local electricity markets and peer-to-peer trading on low-voltage grid operations*](https://doi.org/10.1016/j.apenergy.2021.117404) | Shows why market clearing must be evaluated against LV-network constraints. |
| Guerrero et al. (2020), [*Towards a transactive energy system for integration of distributed energy resources*](https://doi.org/10.1016/j.rser.2020.109756) | Connects home energy management, distributed OPF, and peer-to-peer trading. |
| Wickramasinghe et al. (2025), [*A Review of Dynamic Operating Envelopes: Computation, Allocation and Control*](https://doi.org/10.3390/electricity6020029) | DOE taxonomy and open research questions. |
| AEMO Project EDGE (2023), [*Fairness in Dynamic Operating Envelope Objective Functions*](https://www.aemo.com.au/-/media/files/initiatives/der/2023/the-fairness-in-dynamic-operating-envelope-objectives-report.pdf) | Practical comparison of fairness objectives for network-capacity allocation. |

<a id="recommended-evaluation-dimensions"></a>
### Recommended evaluation dimensions

A technically credible energy-community study should report more than cost savings or self-consumption. Depending on scope, evaluate:

- **grid:** voltage violations, thermal overloads, losses, transformer loading, hosting capacity, curtailment;
- **community:** self-consumption, self-sufficiency, peak demand, flexibility activation, battery degradation;
- **economics:** total cost, member bills, community revenue, network costs, risk exposure;
- **fairness:** benefit distribution, curtailment allocation, participation constraints, energy-poverty effects;
- **control:** constraint violations, tracking error, forecast sensitivity, solve time, communication burden;
- **robustness:** forecast error, missing data, device unavailability, topology errors, and adversarial conditions;
- **replicability:** open inputs, documented assumptions, fixed random seeds, and machine-readable outputs.

<a id="open-source-software"></a>
## 🧰 Open-source software

### Distribution-grid analysis

| Tool | Best suited to |
|---|---|
| [pandapower](https://www.pandapower.org/) | Python-based power flow, optimal power flow, state estimation, short circuit, and time-series analysis. |
| [OpenDSS](https://opendss.epri.com/) / [DSS-Extensions](https://dss-extensions.org/) | Detailed unbalanced distribution-system and DER studies with strong time-series support. |
| [GridCal](https://github.com/SanPen/GridCal) | Power flow, OPF, contingency analysis, and graphical network modelling. |
| [PowerModelsDistribution.jl](https://github.com/lanl-ansi/PowerModelsDistribution.jl) | Optimization of unbalanced distribution networks in Julia. |
| [OpenModelica](https://openmodelica.org/) | Dynamic and multi-domain physical modelling, including electrical and thermal systems. |

### Community scheduling and energy-system optimization

| Tool | Best suited to |
|---|---|
| [pycity_scheduling](https://github.com/ElsevierSoftwareX/SOFTX-D-20-00087) | Optimization-based scheduling of buildings and local multi-energy systems. |
| [PyPSA](https://pypsa.org/) | Power-system and sector-coupled planning, dispatch, and investment optimization. |
| [oemof.solph](https://oemof-solph.readthedocs.io/) | Flexible graph-based energy-system optimization using Pyomo. |
| [Calliope](https://calliope.readthedocs.io/) | Spatially and temporally explicit multi-energy planning. |
| [FlexMeasures](https://flexmeasures.io/) | Forecast-driven energy scheduling and flexibility-oriented energy management. |
| [Pyomo](https://www.pyomo.org/) | Algebraic optimization modelling in Python. |
| [CVXPY](https://www.cvxpy.org/) | Convex optimization, useful for MPC, flexibility sets, and distributed algorithms. |
| [JuMP](https://jump.dev/) | High-performance mathematical optimization in Julia. |

### Co-simulation and communication

| Tool | Best suited to |
|---|---|
| [mosaik](https://mosaik.offis.de/) | Smart-grid co-simulation across heterogeneous simulators. |
| [HELICS](https://helics.org/) | Scalable co-simulation for cyber-physical energy systems. |
| [OpenEMS](https://openems.io/) | Modular open-source energy-management systems and field integration. |
| [Eclipse VOLTTRON](https://volttron.org/) | Distributed control, building-grid integration, and transactive applications. |

<a id="open-data-and-test-systems"></a>
## 📊 Open data and test systems

### Energy and weather data

- [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/) — generation, load, transmission, balancing, and market data.
- [ENTSO-E RESTful API documentation](https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html) — machine access to Transparency Platform data.
- [Open Power System Data](https://open-power-system-data.org/) — processed European time series, power-plant, and weather-related datasets.
- [Eurostat energy database](https://ec.europa.eu/eurostat/web/energy/database) — official EU energy statistics.
- [JRC PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) — solar resource and PV-generation estimates.
- [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/) — ERA5 and other climate and weather products.
- [Renewables.ninja](https://www.renewables.ninja/) — weather-derived wind and PV capacity-factor time series.
- [Zenodo](https://zenodo.org/) — citable research datasets and software releases; verify the provenance and license of each record.

### Distribution networks and load profiles

- [pandapower networks](https://pandapower.readthedocs.io/en/latest/networks.html) — standard and benchmark networks accessible directly in Python.
- [IEEE PES test feeders](https://cmte.ieee.org/pes-testfeeders/resources/) — distribution-system benchmarks.
- [CIGRE benchmark systems](https://www.e-cigre.org/publications/detail/575-benchmark-systems-for-network-integration-of-renewable-and-distributed-energy-resources.html) — LV, MV, and HV reference networks; check access and reuse terms.
- [SimBench](https://simbench.de/) — German benchmark grids and scenario data.
- [Low Voltage Network Solutions data](https://www.enwl.co.uk/go-net-zero/innovation/smaller-projects/low-voltage-network-solutions/) — UK LV monitoring and network-study material.
- [London SmartMeter Energy Consumption Data](https://data.london.gov.uk/dataset/smartmeter-energy-use-data-in-london-households) — household smart-meter data; review its sampling and representativeness before use.

<a id="interoperability-and-technical-standards"></a>
## 🔌 Interoperability and technical standards

Standards are often paywalled. The links below point to official landing pages or open specifications where available.

| Standard/specification | Relevance |
|---|---|
| [IEC 61850](https://www.iec.ch/61850) | Power-utility automation, information models, and communication services. |
| [IEC 61968 / Common Information Model](https://www.iec.ch/dyn/www/f?p=103:7:0::::FSP_ORG_ID:1273) | Distribution-management information exchange and semantic interoperability. |
| [IEC 62325](https://www.iec.ch/dyn/www/f?p=103:7:0::::FSP_ORG_ID:1273) | Electricity-market communications based on CIM. |
| [IEC 62746-10-1 / OpenADR 2.0](https://www.openadr.org/) | Automated demand-response signalling. |
| [IEEE 2030.5](https://standards.ieee.org/ieee/2030.5/5897/) | DER communication; widely used in Australian smart-inverter and DOE implementations. |
| [SunSpec Modbus](https://sunspec.org/sunspec-modbus-specifications/) | Open DER and inverter monitoring/control models. |
| [EEBUS](https://www.eebus.org/) | European device-level energy-management communication, including buildings, heat pumps, and EV charging. |
| [S2 interoperability specification](https://s2standard.org/) | Device flexibility communication between customer energy managers and flexible devices. |
| [Open Charge Point Protocol](https://openchargealliance.org/protocols/open-charge-point-protocol/) | Charging-station to management-system communication. |
| [ISO 15118](https://www.iso.org/standard/77845.html) | EV–charging-station communication, including smart charging and bidirectional-power-transfer work. |

For implementation, distinguish carefully between:

1. **semantic models** — what an asset, measurement, forecast, schedule, or constraint means;
2. **transport and APIs** — how messages are exchanged;
3. **market processes** — who may request, validate, activate, and settle flexibility;
4. **grid-safety processes** — how network constraints are calculated and enforced;
5. **cybersecurity and privacy** — identity, authorization, integrity, availability, and data minimization.

<a id="european-projects-and-networks"></a>
## 🇪🇺 European projects and networks

### Networks and knowledge platforms

- [REScoop.eu](https://www.rescoop.eu/) — European federation of citizen-energy cooperatives.
- [Energy Cities](https://energy-cities.eu/) — network of local authorities working on energy transition.
- [FEDARENE](https://fedarene.org/) — regional and local energy agencies.
- [Open Energy Modelling Initiative](https://openmod-initiative.org/) — open models, data, and research practices.
- [BRIDGE](https://bridge-smart-grid-storage-systems-digital-projects.ec.europa.eu/) — cooperation platform for EU smart-grid, storage, island, and digitalization projects.

### Research and innovation projects

| Project | Focus |
|---|---|
| [COMPILE](https://www.compile-project.eu/) | Local energy islands and community deployment. |
| [NEWCOMERS](https://www.newcomersh2020.eu/) | New clean-energy-community business and governance models. |
| [COME RES](https://come-res.eu/) | Enabling frameworks and transfer of renewable-energy-community practices. |
| [DECIDE](https://energy-cities.eu/project/decide/) | Consumer and citizen engagement in energy communities. |
| [BECoop](https://www.becoop-project.eu/) | Community bioenergy and business support. |
| [IElectrix](https://ielectrix-h2020.eu/) | DSO innovation and local energy communities in distribution grids. |
| [InterConnect](https://interconnectproject.eu/) | Interoperable smart homes, buildings, and grids. |
| [OneNet](https://onenet-project.eu/) | Coordinated European electricity-market architecture and flexibility services. |
| [CoordiNet](https://coordinet-project.eu/) | TSO–DSO–consumer coordination and flexibility demonstrations. |
| [INTERRFACE](http://www.interrface.eu/) | TSO–DSO coordination and flexibility-service platforms. |

## 🤝 How to contribute

Contributions are welcome through pull requests. Please read [CONTRIBUTING.md](CONTRIBUTING.md).

A suggested resource should have:

- a stable publisher, DOI, official page, or maintained repository;
- a clear connection to European energy communities or the technical methods used to study them;
- a one-sentence explanation of why it is useful;
- transparent access and licensing information where relevant;
- no predatory journals, link farms, or unverifiable claims.

## Citation and reuse

This repository is a curated index, not a systematic literature review. Cite the original publications, legislation, datasets, and software rather than this list when making substantive claims.

The repository text is licensed under [CC BY 4.0](LICENSE). Linked resources retain their own copyright and license terms.
