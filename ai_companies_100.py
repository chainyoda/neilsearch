"""Top 100 AI/ML companies and their career pages - US & Remote only."""

AI_COMPANIES_100 = {
    # TIER 1: Leading AI Labs & Research (10 companies)
    "openai": {
        "name": "OpenAI",
        "url": "https://openai.com/careers",
        "api_url": "https://api.ashbyhq.com/posting-api/job-board/openai",
        "type": "ashby",
        "tier": 1
    },
    "anthropic": {
        "name": "Anthropic",
        "url": "https://www.anthropic.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/anthropic/jobs",
        "type": "api",
        "tier": 1
    },
    "deepmind": {
        "name": "Google DeepMind",
        "url": "https://www.deepmind.com/careers",
        "jobs_url": "https://www.deepmind.com/careers/jobs",
        "type": "scrape",
        "tier": 1
    },
    "meta_ai": {
        "name": "Meta AI (FAIR)",
        "url": "https://ai.meta.com/careers",
        "jobs_url": "https://www.metacareers.com/jobs",
        "type": "scrape",
        "tier": 1
    },
    "google_brain": {
        "name": "Google Brain/Research",
        "url": "https://research.google/careers",
        "jobs_url": "https://careers.google.com/jobs/results/?q=machine%20learning",
        "type": "scrape",
        "tier": 1
    },
    "microsoft_research": {
        "name": "Microsoft Research",
        "url": "https://www.microsoft.com/en-us/research/careers",
        "jobs_url": "https://careers.microsoft.com/us/en/search-results?keywords=AI%20Research",
        "type": "scrape",
        "tier": 1
    },
    "nvidia_ai": {
        "name": "NVIDIA AI Research",
        "url": "https://www.nvidia.com/en-us/research",
        "jobs_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite",
        "type": "scrape",
        "tier": 1
    },
    "apple_ml": {
        "name": "Apple Machine Learning",
        "url": "https://machinelearning.apple.com/jobs",
        "jobs_url": "https://jobs.apple.com/en-us/search?team=machine-learning-and-ai-MLAI",
        "type": "scrape",
        "tier": 1
    },
    "amazon_science": {
        "name": "Amazon Science",
        "url": "https://www.amazon.science/careers",
        "jobs_url": "https://www.amazon.jobs/en/search?base_query=machine+learning",
        "type": "scrape",
        "tier": 1
    },
    "ibm_research": {
        "name": "IBM Research AI",
        "url": "https://research.ibm.com/careers",
        "jobs_url": "https://www.ibm.com/careers/search?field_keyword_08[0]=Artificial%20Intelligence",
        "type": "scrape",
        "tier": 1
    },

    # TIER 2: AI-First Unicorns (15 companies)
    "cohere": {
        "name": "Cohere",
        "url": "https://cohere.com/careers",
        "api_url": "https://api.ashbyhq.com/posting-api/job-board/cohere",
        "type": "ashby",
        "tier": 2
    },
    "huggingface": {
        "name": "Hugging Face",
        "url": "https://huggingface.co/careers",
        "jobs_url": "https://apply.workable.com/huggingface",
        "type": "scrape",
        "tier": 2
    },
    "adept": {
        "name": "Adept",
        "url": "https://www.adept.ai/careers",
        "jobs_url": "https://jobs.ashbyhq.com/Adept",
        "type": "scrape",
        "tier": 2
    },
    "inflection": {
        "name": "Inflection AI",
        "url": "https://inflection.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/inflectionai/jobs",
        "type": "api",
        "tier": 2
    },
    "character": {
        "name": "Character.AI",
        "url": "https://character.ai/careers",
        "jobs_url": "https://jobs.ashbyhq.com/character",
        "type": "scrape",
        "tier": 2
    },
    "perplexity": {
        "name": "Perplexity AI",
        "url": "https://www.perplexity.ai/careers",
        "jobs_url": "https://www.perplexity.ai/careers",
        "type": "scrape",
        "tier": 2
    },
    "mistral": {
        "name": "Mistral AI",
        "url": "https://mistral.ai/careers",
        "jobs_url": "https://mistral.ai/careers",
        "type": "scrape",
        "tier": 2
    },
    "together": {
        "name": "Together AI",
        "url": "https://www.together.ai/careers",
        "jobs_url": "https://www.together.ai/careers",
        "type": "scrape",
        "tier": 2
    },
    "fireworks": {
        "name": "Fireworks AI",
        "url": "https://fireworks.ai/careers",
        "jobs_url": "https://fireworks.ai/careers",
        "type": "scrape",
        "tier": 2
    },
    "ai21": {
        "name": "AI21 Labs",
        "url": "https://www.ai21.com/careers",
        "jobs_url": "https://www.ai21.com/careers",
        "type": "scrape",
        "tier": 2
    },
    "contextual": {
        "name": "Contextual AI",
        "url": "https://contextual.ai/careers",
        "jobs_url": "https://contextual.ai/careers",
        "type": "scrape",
        "tier": 2
    },
    "aleph_alpha": {
        "name": "Aleph Alpha",
        "url": "https://www.aleph-alpha.com/careers",
        "jobs_url": "https://www.aleph-alpha.com/careers",
        "type": "scrape",
        "tier": 2
    },
    "reka": {
        "name": "Reka AI",
        "url": "https://www.reka.ai/careers",
        "jobs_url": "https://www.reka.ai/careers",
        "type": "scrape",
        "tier": 2
    },
    "you": {
        "name": "You.com",
        "url": "https://about.you.com/careers",
        "jobs_url": "https://about.you.com/careers",
        "type": "scrape",
        "tier": 2
    },
    "glean": {
        "name": "Glean",
        "url": "https://glean.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/gleanwork/jobs",
        "type": "api",
        "tier": 2
    },

    # TIER 3: AI Infrastructure & Tools (20 companies)
    "scale": {
        "name": "Scale AI",
        "url": "https://scale.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/scaleai/jobs",
        "type": "api",
        "tier": 3
    },
    "databricks": {
        "name": "Databricks",
        "url": "https://www.databricks.com/company/careers",
        "jobs_url": "https://www.databricks.com/company/careers/open-positions",
        "type": "scrape",
        "tier": 3
    },
    "weights_biases": {
        "name": "Weights & Biases",
        "url": "https://wandb.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/wandb/jobs",
        "type": "api",
        "tier": 3
    },
    "anyscale": {
        "name": "Anyscale",
        "url": "https://www.anyscale.com/careers",
        "api_url": "https://api.lever.co/v0/postings/anyscale",
        "type": "api",
        "tier": 3
    },
    "modal": {
        "name": "Modal",
        "url": "https://modal.com/careers",
        "jobs_url": "https://jobs.ashbyhq.com/modal",
        "type": "scrape",
        "tier": 3
    },
    "replicate": {
        "name": "Replicate",
        "url": "https://replicate.com/careers",
        "jobs_url": "https://jobs.ashbyhq.com/replicate",
        "type": "scrape",
        "tier": 3
    },
    "baseten": {
        "name": "Baseten",
        "url": "https://www.baseten.co/careers",
        "jobs_url": "https://www.baseten.co/careers",
        "type": "scrape",
        "tier": 3
    },
    "banana": {
        "name": "Banana",
        "url": "https://www.banana.dev/careers",
        "jobs_url": "https://www.banana.dev/careers",
        "type": "scrape",
        "tier": 3
    },
    "roboflow": {
        "name": "Roboflow",
        "url": "https://roboflow.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/roboflow/jobs",
        "type": "api",
        "tier": 3
    },
    "labelbox": {
        "name": "Labelbox",
        "url": "https://labelbox.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/labelbox/jobs",
        "type": "api",
        "tier": 3
    },
    "snorkel": {
        "name": "Snorkel AI",
        "url": "https://snorkel.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/snorkelai/jobs",
        "type": "api",
        "tier": 3
    },
    "tecton": {
        "name": "Tecton",
        "url": "https://www.tecton.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/tecton/jobs",
        "type": "api",
        "tier": 3
    },
    "pinecone": {
        "name": "Pinecone",
        "url": "https://www.pinecone.io/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/pinecone/jobs",
        "type": "api",
        "tier": 3
    },
    "weaviate": {
        "name": "Weaviate",
        "url": "https://weaviate.io/company/careers",
        "jobs_url": "https://weaviate.io/company/careers",
        "type": "scrape",
        "tier": 3
    },
    "chroma": {
        "name": "Chroma",
        "url": "https://www.trychroma.com/careers",
        "jobs_url": "https://www.trychroma.com/careers",
        "type": "scrape",
        "tier": 3
    },
    "qdrant": {
        "name": "Qdrant",
        "url": "https://qdrant.tech/careers",
        "jobs_url": "https://qdrant.tech/careers",
        "type": "scrape",
        "tier": 3
    },
    "milvus": {
        "name": "Milvus/Zilliz",
        "url": "https://zilliz.com/careers",
        "jobs_url": "https://zilliz.com/careers",
        "type": "scrape",
        "tier": 3
    },
    "mosaic": {
        "name": "MosaicML (Databricks)",
        "url": "https://www.databricks.com/company/careers",
        "jobs_url": "https://www.databricks.com/company/careers/open-positions?search=mosaic",
        "type": "scrape",
        "tier": 3
    },
    "runpod": {
        "name": "RunPod",
        "url": "https://www.runpod.io/careers",
        "jobs_url": "https://www.runpod.io/careers",
        "type": "scrape",
        "tier": 3
    },
    "coreweave": {
        "name": "CoreWeave",
        "url": "https://www.coreweave.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/coreweave/jobs",
        "type": "api",
        "tier": 3
    },

    # TIER 4: AI-Powered Applications (25 companies)
    "notion": {
        "name": "Notion",
        "url": "https://www.notion.so/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/notion/jobs",
        "type": "api",
        "tier": 4
    },
    "cursor": {
        "name": "Cursor",
        "url": "https://cursor.sh/careers",
        "jobs_url": "https://jobs.ashbyhq.com/cursor",
        "type": "scrape",
        "tier": 4
    },
    "replit": {
        "name": "Replit",
        "url": "https://replit.com/careers",
        "api_url": "https://api.lever.co/v0/postings/replit",
        "type": "api",
        "tier": 4
    },
    "codeium": {
        "name": "Codeium",
        "url": "https://codeium.com/careers",
        "jobs_url": "https://codeium.com/careers",
        "type": "scrape",
        "tier": 4
    },
    "tabnine": {
        "name": "Tabnine",
        "url": "https://www.tabnine.com/careers",
        "jobs_url": "https://www.tabnine.com/careers",
        "type": "scrape",
        "tier": 4
    },
    "grammarly": {
        "name": "Grammarly",
        "url": "https://www.grammarly.com/jobs",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/grammarly/jobs",
        "type": "api",
        "tier": 4
    },
    "jasper": {
        "name": "Jasper",
        "url": "https://www.jasper.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/jasperai/jobs",
        "type": "api",
        "tier": 4
    },
    "copy_ai": {
        "name": "Copy.ai",
        "url": "https://www.copy.ai/careers",
        "jobs_url": "https://www.copy.ai/careers",
        "type": "scrape",
        "tier": 4
    },
    "writesonic": {
        "name": "Writesonic",
        "url": "https://writesonic.com/careers",
        "jobs_url": "https://writesonic.com/careers",
        "type": "scrape",
        "tier": 4
    },
    "runway": {
        "name": "Runway",
        "url": "https://runwayml.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/runwayml/jobs",
        "type": "api",
        "tier": 4
    },
    "midjourney": {
        "name": "Midjourney",
        "url": "https://www.midjourney.com/jobs",
        "jobs_url": "https://www.midjourney.com/jobs",
        "type": "scrape",
        "tier": 4
    },
    "stability": {
        "name": "Stability AI",
        "url": "https://stability.ai/careers",
        "jobs_url": "https://stability.ai/careers",
        "type": "scrape",
        "tier": 4
    },
    "leonardo": {
        "name": "Leonardo.ai",
        "url": "https://leonardo.ai/careers",
        "jobs_url": "https://leonardo.ai/careers",
        "type": "scrape",
        "tier": 4
    },
    "adobe_firefly": {
        "name": "Adobe (Firefly)",
        "url": "https://careers.adobe.com",
        "jobs_url": "https://careers.adobe.com/us/en/search-results?keywords=AI",
        "type": "scrape",
        "tier": 4
    },
    "canva": {
        "name": "Canva",
        "url": "https://www.canva.com/careers",
        "jobs_url": "https://www.canva.com/careers/jobs",
        "type": "scrape",
        "tier": 4
    },
    "figma": {
        "name": "Figma",
        "url": "https://www.figma.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/figma/jobs",
        "type": "api",
        "tier": 4
    },
    "synthesia": {
        "name": "Synthesia",
        "url": "https://www.synthesia.io/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/synthesia/jobs",
        "type": "api",
        "tier": 4
    },
    "heygen": {
        "name": "HeyGen",
        "url": "https://www.heygen.com/careers",
        "jobs_url": "https://www.heygen.com/careers",
        "type": "scrape",
        "tier": 4
    },
    "descript": {
        "name": "Descript",
        "url": "https://www.descript.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/descript/jobs",
        "type": "api",
        "tier": 4
    },
    "elevenlabs": {
        "name": "ElevenLabs",
        "url": "https://elevenlabs.io/careers",
        "jobs_url": "https://elevenlabs.io/careers",
        "type": "scrape",
        "tier": 4
    },
    "resemble": {
        "name": "Resemble AI",
        "url": "https://www.resemble.ai/careers",
        "jobs_url": "https://www.resemble.ai/careers",
        "type": "scrape",
        "tier": 4
    },
    "otter": {
        "name": "Otter.ai",
        "url": "https://otter.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/otterai/jobs",
        "type": "api",
        "tier": 4
    },
    "fireflies": {
        "name": "Fireflies.ai",
        "url": "https://fireflies.ai/careers",
        "jobs_url": "https://fireflies.ai/careers",
        "type": "scrape",
        "tier": 4
    },
    "harvey": {
        "name": "Harvey AI",
        "url": "https://www.harvey.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/harvey/jobs",
        "type": "api",
        "tier": 4
    },
    "mem": {
        "name": "Mem",
        "url": "https://get.mem.ai/careers",
        "jobs_url": "https://get.mem.ai/careers",
        "type": "scrape",
        "tier": 4
    },
    "netflix": {
        "name": "Netflix",
        "url": "https://jobs.netflix.com",
        "jobs_url": "https://jobs.netflix.com/search?q=machine%20learning",
        "type": "scrape",
        "tier": 4
    },

    # TIER 5: Robotics & Autonomous Systems (15 companies)
    "tesla_ai": {
        "name": "Tesla AI",
        "url": "https://www.tesla.com/careers",
        "jobs_url": "https://www.tesla.com/careers/search/?query=AI",
        "type": "scrape",
        "tier": 5
    },
    "cruise": {
        "name": "Cruise",
        "url": "https://getcruise.com/careers",
        "jobs_url": "https://getcruise.com/careers/jobs",
        "type": "scrape",
        "tier": 5
    },
    "waymo": {
        "name": "Waymo",
        "url": "https://waymo.com/careers",
        "jobs_url": "https://waymo.com/careers/search",
        "type": "scrape",
        "tier": 5
    },
    "figure_ai": {
        "name": "Figure AI",
        "url": "https://www.figure.ai/careers",
        "api_url": "https://api.lever.co/v0/postings/figureai",
        "type": "api",
        "tier": 5
    },
    "1x_technologies": {
        "name": "1X Technologies",
        "url": "https://www.1x.tech/careers",
        "jobs_url": "https://www.1x.tech/careers",
        "type": "scrape",
        "tier": 5
    },
    "physical_intelligence": {
        "name": "Physical Intelligence",
        "url": "https://www.physicalintelligence.company/careers",
        "jobs_url": "https://www.physicalintelligence.company/careers",
        "type": "scrape",
        "tier": 5
    },
    "covariant": {
        "name": "Covariant",
        "url": "https://covariant.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/covariant/jobs",
        "type": "api",
        "tier": 5
    },
    "intrinsic": {
        "name": "Intrinsic (Alphabet)",
        "url": "https://intrinsic.ai/careers",
        "jobs_url": "https://intrinsic.ai/careers",
        "type": "scrape",
        "tier": 5
    },
    "skydio": {
        "name": "Skydio",
        "url": "https://www.skydio.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/skydio/jobs",
        "type": "api",
        "tier": 5
    },
    "zipline": {
        "name": "Zipline",
        "url": "https://flyzipline.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/zipline/jobs",
        "type": "api",
        "tier": 5
    },
    "zoox": {
        "name": "Zoox",
        "url": "https://zoox.com/careers",
        "jobs_url": "https://zoox.com/careers",
        "type": "scrape",
        "tier": 5
    },
    "aurora": {
        "name": "Aurora",
        "url": "https://aurora.tech/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/aurorainnovation/jobs",
        "type": "api",
        "tier": 5
    },
    "nuro": {
        "name": "Nuro",
        "url": "https://www.nuro.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/nuro/jobs",
        "type": "api",
        "tier": 5
    },
    "kodiak": {
        "name": "Kodiak Robotics",
        "url": "https://kodiak.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/kodiakrobotics/jobs",
        "type": "api",
        "tier": 5
    },
    "gatik": {
        "name": "Gatik",
        "url": "https://gatik.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/gatikaicareers/jobs",
        "type": "api",
        "tier": 5
    },

    # TIER 6: Enterprise AI & Vertical SaaS (15 companies)
    "snowflake": {
        "name": "Snowflake",
        "url": "https://careers.snowflake.com",
        "jobs_url": "https://careers.snowflake.com/us/en/search-results?keywords=machine%20learning",
        "type": "scrape",
        "tier": 6
    },
    "salesforce_einstein": {
        "name": "Salesforce Einstein",
        "url": "https://www.salesforce.com/company/careers",
        "jobs_url": "https://salesforce.wd1.myworkdayjobs.com/External_Career_Site",
        "type": "scrape",
        "tier": 6
    },
    "servicenow": {
        "name": "ServiceNow",
        "url": "https://careers.servicenow.com",
        "jobs_url": "https://careers.servicenow.com/careers/jobs?keywords=AI",
        "type": "scrape",
        "tier": 6
    },
    "c3_ai": {
        "name": "C3.ai",
        "url": "https://c3.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/c3iot/jobs",
        "type": "api",
        "tier": 6
    },
    "datarobot": {
        "name": "DataRobot",
        "url": "https://www.datarobot.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/datarobot/jobs",
        "type": "api",
        "tier": 6
    },
    "h2o": {
        "name": "H2O.ai",
        "url": "https://h2o.ai/company/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/h2oai/jobs",
        "type": "api",
        "tier": 6
    },
    "domino": {
        "name": "Domino Data Lab",
        "url": "https://www.dominodatalab.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/dominodatalab/jobs",
        "type": "api",
        "tier": 6
    },
    "alteryx": {
        "name": "Alteryx",
        "url": "https://www.alteryx.com/about-us/careers",
        "jobs_url": "https://www.alteryx.com/about-us/careers/jobs",
        "type": "scrape",
        "tier": 6
    },
    "dataiku": {
        "name": "Dataiku",
        "url": "https://www.dataiku.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/dataiku/jobs",
        "type": "api",
        "tier": 6
    },
    "palantir": {
        "name": "Palantir",
        "url": "https://www.palantir.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/palantir/jobs",
        "type": "api",
        "tier": 6
    },
    "samsara": {
        "name": "Samsara",
        "url": "https://www.samsara.com/company/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/samsara/jobs",
        "type": "api",
        "tier": 6
    },
    "upstart": {
        "name": "Upstart",
        "url": "https://www.upstart.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/upstart/jobs",
        "type": "api",
        "tier": 6
    },
    "affirm": {
        "name": "Affirm",
        "url": "https://www.affirm.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/affirm/jobs",
        "type": "api",
        "tier": 6
    },
    "stripe": {
        "name": "Stripe",
        "url": "https://stripe.com/jobs",
        "jobs_url": "https://stripe.com/jobs/search?s=machine%20learning",
        "type": "scrape",
        "tier": 6
    },
    "plaid": {
        "name": "Plaid",
        "url": "https://plaid.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/plaid/jobs",
        "type": "api",
        "tier": 6
    },

    # TIER 7: Financial Services - Investment Banks & Hedge Funds (20 companies)
    "goldman_sachs": {
        "name": "Goldman Sachs",
        "url": "https://www.goldmansachs.com/careers",
        "jobs_url": "https://www.goldmansachs.com/careers/find-a-role/search?keywords=machine%20learning",
        "type": "scrape",
        "tier": 7
    },
    "jpmorgan": {
        "name": "JPMorgan Chase",
        "url": "https://careers.jpmorgan.com",
        "jobs_url": "https://careers.jpmorgan.com/us/en/search-results?keywords=machine%20learning",
        "type": "scrape",
        "tier": 7
    },
    "morgan_stanley": {
        "name": "Morgan Stanley",
        "url": "https://www.morganstanley.com/careers",
        "jobs_url": "https://morganstanley.tal.net/vx/lang-en-GB/mobile-0/appcentre-1/brand-2/candidate/jobboard/vacancy/1/adv",
        "type": "scrape",
        "tier": 7
    },
    "citadel": {
        "name": "Citadel",
        "url": "https://www.citadel.com/careers",
        "jobs_url": "https://www.citadel.com/careers/open-opportunities/",
        "type": "scrape",
        "tier": 7
    },
    "citadel_securities": {
        "name": "Citadel Securities",
        "url": "https://www.citadelsecurities.com/careers",
        "jobs_url": "https://www.citadelsecurities.com/careers/open-opportunities/",
        "type": "scrape",
        "tier": 7
    },
    "jane_street": {
        "name": "Jane Street",
        "url": "https://www.janestreet.com/join-jane-street",
        "jobs_url": "https://www.janestreet.com/join-jane-street/open-positions",
        "type": "scrape",
        "tier": 7
    },
    "two_sigma": {
        "name": "Two Sigma",
        "url": "https://www.twosigma.com/careers",
        "jobs_url": "https://careers.twosigma.com/careers/OpenRoles",
        "type": "scrape",
        "tier": 7
    },
    "de_shaw": {
        "name": "D. E. Shaw & Co.",
        "url": "https://www.deshaw.com/careers",
        "jobs_url": "https://www.deshaw.com/careers/choose-your-path",
        "type": "scrape",
        "tier": 7
    },
    "bridgewater": {
        "name": "Bridgewater Associates",
        "url": "https://www.bridgewater.com/careers",
        "jobs_url": "https://boards.greenhouse.io/bridgewater89",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/bridgewater89/jobs",
        "type": "api",
        "tier": 7
    },
    "renaissance": {
        "name": "Renaissance Technologies",
        "url": "https://www.rentec.com/Careers.action",
        "jobs_url": "https://www.rentec.com/Careers.action",
        "type": "scrape",
        "tier": 7
    },
    "point72": {
        "name": "Point72",
        "url": "https://careers.point72.com",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/point72/jobs",
        "type": "api",
        "tier": 7
    },
    "millennium": {
        "name": "Millennium Management",
        "url": "https://www.mlp.com/careers",
        "jobs_url": "https://www.mlp.com/careers/#positions",
        "type": "scrape",
        "tier": 7
    },
    "aqr": {
        "name": "AQR Capital Management",
        "url": "https://www.aqr.com/Careers",
        "jobs_url": "https://careers.aqr.com/jobs",
        "type": "scrape",
        "tier": 7
    },
    "worldquant": {
        "name": "WorldQuant",
        "url": "https://www.worldquant.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/worldquant/jobs",
        "type": "api",
        "tier": 7
    },
    "jump_trading": {
        "name": "Jump Trading",
        "url": "https://www.jumptrading.com/careers",
        "jobs_url": "https://www.jumptrading.com/careers/open-positions",
        "type": "scrape",
        "tier": 7
    },
    "hrt": {
        "name": "Hudson River Trading",
        "url": "https://www.hudsonrivertrading.com/careers",
        "jobs_url": "https://www.hudsonrivertrading.com/careers/job-openings",
        "type": "scrape",
        "tier": 7
    },
    "virtu": {
        "name": "Virtu Financial",
        "url": "https://www.virtu.com/careers",
        "jobs_url": "https://www.virtu.com/careers/#openings",
        "type": "scrape",
        "tier": 7
    },
    "tower_research": {
        "name": "Tower Research Capital",
        "url": "https://www.tower-research.com/careers",
        "jobs_url": "https://www.tower-research.com/open-positions",
        "type": "scrape",
        "tier": 7
    },
    "imc_trading": {
        "name": "IMC Trading",
        "url": "https://www.imc.com/us/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/imc/jobs",
        "type": "api",
        "tier": 7
    },
    "sig": {
        "name": "Susquehanna International Group (SIG)",
        "url": "https://sig.com/careers",
        "jobs_url": "https://careers.sig.com/job-openings",
        "type": "scrape",
        "tier": 7
    },

    # TIER 8: Major Tech Companies (20 companies)
    "oracle": {
        "name": "Oracle",
        "url": "https://www.oracle.com/careers",
        "jobs_url": "https://eeho.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/jobsearch/results?keyword=machine%20learning",
        "type": "scrape",
        "tier": 8
    },
    "cisco": {
        "name": "Cisco",
        "url": "https://jobs.cisco.com",
        "jobs_url": "https://jobs.cisco.com/jobs/SearchJobs/machine%20learning",
        "type": "scrape",
        "tier": 8
    },
    "intel": {
        "name": "Intel",
        "url": "https://jobs.intel.com",
        "jobs_url": "https://jobs.intel.com/en/search-jobs/machine%20learning",
        "type": "scrape",
        "tier": 8
    },
    "amd": {
        "name": "AMD",
        "url": "https://careers.amd.com",
        "jobs_url": "https://careers.amd.com/careers-home/jobs?keywords=machine%20learning",
        "type": "scrape",
        "tier": 8
    },
    "vmware": {
        "name": "VMware",
        "url": "https://careers.vmware.com",
        "jobs_url": "https://careers.vmware.com/main/jobs?keywords=machine%20learning",
        "type": "scrape",
        "tier": 8
    },
    "intuit": {
        "name": "Intuit",
        "url": "https://www.intuit.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/intuit/jobs",
        "type": "api",
        "tier": 8
    },
    "workday": {
        "name": "Workday",
        "url": "https://www.workday.com/en-us/company/careers.html",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/workday/jobs",
        "type": "api",
        "tier": 8
    },
    "square": {
        "name": "Square (Block)",
        "url": "https://careers.squareup.com",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/square/jobs",
        "type": "api",
        "tier": 8
    },
    "paypal": {
        "name": "PayPal",
        "url": "https://www.paypal.com/us/webapps/mpp/jobs",
        "jobs_url": "https://jobsearch.paypal-corp.com/en-US/search?keywords=machine%20learning",
        "type": "scrape",
        "tier": 8
    },
    "uber": {
        "name": "Uber",
        "url": "https://www.uber.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/uber/jobs",
        "type": "api",
        "tier": 8
    },
    "lyft": {
        "name": "Lyft",
        "url": "https://www.lyft.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/lyft/jobs",
        "type": "api",
        "tier": 8
    },
    "airbnb": {
        "name": "Airbnb",
        "url": "https://careers.airbnb.com",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/airbnb/jobs",
        "type": "api",
        "tier": 8
    },
    "doordash": {
        "name": "DoorDash",
        "url": "https://careers.doordash.com",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/doordash/jobs",
        "type": "api",
        "tier": 8
    },
    "instacart": {
        "name": "Instacart",
        "url": "https://careers.instacart.com",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/instacart/jobs",
        "type": "api",
        "tier": 8
    },
    "robinhood": {
        "name": "Robinhood",
        "url": "https://robinhood.com/us/en/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/robinhood/jobs",
        "type": "api",
        "tier": 8
    },
    "roblox": {
        "name": "Roblox",
        "url": "https://corp.roblox.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/roblox/jobs",
        "type": "api",
        "tier": 8
    },
    "discord": {
        "name": "Discord",
        "url": "https://discord.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/discord/jobs",
        "type": "api",
        "tier": 8
    },
    "reddit": {
        "name": "Reddit",
        "url": "https://www.redditinc.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/reddit/jobs",
        "type": "api",
        "tier": 8
    },
    "twitter": {
        "name": "X (Twitter)",
        "url": "https://careers.twitter.com",
        "jobs_url": "https://careers.twitter.com/en/roles.html",
        "type": "scrape",
        "tier": 8
    },

    # TIER 9: Game Developers (15 companies)
    "ea": {
        "name": "Electronic Arts (EA)",
        "url": "https://www.ea.com/careers",
        "jobs_url": "https://ea.gr8people.com/jobs",
        "type": "scrape",
        "tier": 9
    },
    "ubisoft": {
        "name": "Ubisoft",
        "url": "https://www.ubisoft.com/en-us/company/careers",
        "jobs_url": "https://www.ubisoft.com/en-us/company/careers/search",
        "type": "scrape",
        "tier": 9
    },
    "epic_games": {
        "name": "Epic Games",
        "url": "https://www.epicgames.com/site/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/epicgames/jobs",
        "type": "api",
        "tier": 9
    },
    "riot_games": {
        "name": "Riot Games",
        "url": "https://www.riotgames.com/en/work-with-us",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/riotgames/jobs",
        "type": "api",
        "tier": 9
    },
    "valve": {
        "name": "Valve",
        "url": "https://www.valvesoftware.com/en/jobs",
        "jobs_url": "https://www.valvesoftware.com/en/jobs",
        "type": "scrape",
        "tier": 9
    },
    "blizzard": {
        "name": "Blizzard Entertainment",
        "url": "https://careers.blizzard.com",
        "jobs_url": "https://careers.blizzard.com/global/en/search-results",
        "type": "scrape",
        "tier": 9
    },
    "bungie": {
        "name": "Bungie",
        "url": "https://careers.bungie.com",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/bungie/jobs",
        "type": "api",
        "tier": 9
    },
    "rockstar": {
        "name": "Rockstar Games",
        "url": "https://www.rockstargames.com/careers",
        "jobs_url": "https://www.rockstargames.com/careers/openings",
        "type": "scrape",
        "tier": 9
    },
    "take_two": {
        "name": "Take-Two Interactive",
        "url": "https://www.take2games.com/careers",
        "jobs_url": "https://www.take2games.com/careers/#openings",
        "type": "scrape",
        "tier": 9
    },
    "unity": {
        "name": "Unity Technologies",
        "url": "https://unity.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/unity/jobs",
        "type": "api",
        "tier": 9
    },
    "activision": {
        "name": "Activision",
        "url": "https://www.activision.com/careers",
        "jobs_url": "https://www.activision.com/careers/jobs",
        "type": "scrape",
        "tier": 9
    },
    "playstation": {
        "name": "PlayStation Studios",
        "url": "https://www.playstation.com/en-us/corporate/playstation-careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/sonyinteractiveentertainmentplaystation/jobs",
        "type": "api",
        "tier": 9
    },
    "nintendo": {
        "name": "Nintendo of America",
        "url": "https://careers.nintendo.com",
        "jobs_url": "https://careers.nintendo.com/job-openings",
        "type": "scrape",
        "tier": 9
    },
    "king": {
        "name": "King (Candy Crush)",
        "url": "https://www.king.com/careers",
        "jobs_url": "https://www.king.com/careers/jobs",
        "type": "scrape",
        "tier": 9
    },
    "zynga": {
        "name": "Zynga (Take-Two)",
        "url": "https://www.zynga.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/zynga/jobs",
        "type": "api",
        "tier": 9
    },

    # TIER 10: Healthcare & Biotech (10 companies)
    "tempus": {
        "name": "Tempus AI",
        "url": "https://www.tempus.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/tempus/jobs",
        "type": "api",
        "tier": 10
    },
    "recursion": {
        "name": "Recursion Pharmaceuticals",
        "url": "https://www.recursion.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/recursionpharmaceuticals/jobs",
        "type": "api",
        "tier": 10
    },
    "insitro": {
        "name": "Insitro",
        "url": "https://insitro.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/insitro/jobs",
        "type": "api",
        "tier": 10
    },
    "flatiron": {
        "name": "Flatiron Health",
        "url": "https://flatiron.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/flatironhealth/jobs",
        "type": "api",
        "tier": 10
    },
    "color": {
        "name": "Color Health",
        "url": "https://www.color.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/color/jobs",
        "type": "api",
        "tier": 10
    },
    "veracyte": {
        "name": "Veracyte",
        "url": "https://www.veracyte.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/veracyte/jobs",
        "type": "api",
        "tier": 10
    },
    "grail": {
        "name": "GRAIL",
        "url": "https://grail.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/graboratory/jobs",
        "type": "api",
        "tier": 10
    },
    "freenome": {
        "name": "Freenome",
        "url": "https://www.freenome.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/freenome/jobs",
        "type": "api",
        "tier": 10
    },
    "atomwise": {
        "name": "Atomwise",
        "url": "https://www.atomwise.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/atomwise/jobs",
        "type": "api",
        "tier": 10
    },
    "benchling": {
        "name": "Benchling",
        "url": "https://www.benchling.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/benchling/jobs",
        "type": "api",
        "tier": 10
    },

    # TIER 11: Defense & Aerospace (10 companies)
    "anduril": {
        "name": "Anduril Industries",
        "url": "https://www.anduril.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/andurilindustries/jobs",
        "type": "api",
        "tier": 11
    },
    "spacex": {
        "name": "SpaceX",
        "url": "https://www.spacex.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/spacex/jobs",
        "type": "api",
        "tier": 11
    },
    "relativity": {
        "name": "Relativity Space",
        "url": "https://www.relativityspace.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/relataboratories/jobs",
        "type": "api",
        "tier": 11
    },
    "shield_ai": {
        "name": "Shield AI",
        "url": "https://shield.ai/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/shieldai/jobs",
        "type": "api",
        "tier": 11
    },
    "saronic": {
        "name": "Saronic Technologies",
        "url": "https://www.saronic.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/saronic/jobs",
        "type": "api",
        "tier": 11
    },
    "hadrian": {
        "name": "Hadrian",
        "url": "https://www.hadrian.co/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/hadrian/jobs",
        "type": "api",
        "tier": 11
    },
    "epirus": {
        "name": "Epirus",
        "url": "https://www.epirusinc.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/epirus/jobs",
        "type": "api",
        "tier": 11
    },
    "hermeus": {
        "name": "Hermeus",
        "url": "https://www.hermeus.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/hermeus/jobs",
        "type": "api",
        "tier": 11
    },
    "rocket_lab": {
        "name": "Rocket Lab",
        "url": "https://www.rocketlabusa.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/rocketlab/jobs",
        "type": "api",
        "tier": 11
    },
    "astra": {
        "name": "Astra",
        "url": "https://astra.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/aaboratories/jobs",
        "type": "api",
        "tier": 11
    },

    # TIER 12: E-commerce & Supply Chain (10 companies)
    "shopify": {
        "name": "Shopify",
        "url": "https://www.shopify.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/shopify/jobs",
        "type": "api",
        "tier": 12
    },
    "flexport": {
        "name": "Flexport",
        "url": "https://www.flexport.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/flexport/jobs",
        "type": "api",
        "tier": 12
    },
    "etsy": {
        "name": "Etsy",
        "url": "https://careers.etsy.com",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/etsy/jobs",
        "type": "api",
        "tier": 12
    },
    "wayfair": {
        "name": "Wayfair",
        "url": "https://www.wayfair.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/wayfair/jobs",
        "type": "api",
        "tier": 12
    },
    "chewy": {
        "name": "Chewy",
        "url": "https://careers.chewy.com",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/chewycom/jobs",
        "type": "api",
        "tier": 12
    },
    "convoy": {
        "name": "Convoy",
        "url": "https://convoy.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/convoy/jobs",
        "type": "api",
        "tier": 12
    },
    "project44": {
        "name": "project44",
        "url": "https://www.project44.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/project44/jobs",
        "type": "api",
        "tier": 12
    },
    "faire": {
        "name": "Faire",
        "url": "https://www.faire.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/faire/jobs",
        "type": "api",
        "tier": 12
    },
    "bolt": {
        "name": "Bolt",
        "url": "https://www.bolt.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/bolt/jobs",
        "type": "api",
        "tier": 12
    },
    "wish": {
        "name": "Wish",
        "url": "https://www.wish.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/wish/jobs",
        "type": "api",
        "tier": 12
    },

    # TIER 13: EdTech & Learning (10 companies)
    "duolingo": {
        "name": "Duolingo",
        "url": "https://careers.duolingo.com",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/duolingo/jobs",
        "type": "api",
        "tier": 13
    },
    "coursera": {
        "name": "Coursera",
        "url": "https://about.coursera.org/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/coursera/jobs",
        "type": "api",
        "tier": 13
    },
    "khan_academy": {
        "name": "Khan Academy",
        "url": "https://www.khanacademy.org/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/khanacademy/jobs",
        "type": "api",
        "tier": 13
    },
    "chegg": {
        "name": "Chegg",
        "url": "https://www.chegg.com/jobs",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/chegg/jobs",
        "type": "api",
        "tier": 13
    },
    "quizlet": {
        "name": "Quizlet",
        "url": "https://quizlet.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/quizlet/jobs",
        "type": "api",
        "tier": 13
    },
    "masterclass": {
        "name": "MasterClass",
        "url": "https://www.masterclass.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/masterclass/jobs",
        "type": "api",
        "tier": 13
    },
    "udemy": {
        "name": "Udemy",
        "url": "https://about.udemy.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/udemy/jobs",
        "type": "api",
        "tier": 13
    },
    "brilliant": {
        "name": "Brilliant",
        "url": "https://brilliant.org/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/brilliant/jobs",
        "type": "api",
        "tier": 13
    },
    "guild": {
        "name": "Guild Education",
        "url": "https://www.guild.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/guild/jobs",
        "type": "api",
        "tier": 13
    },
    "outschool": {
        "name": "Outschool",
        "url": "https://outschool.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/outschool/jobs",
        "type": "api",
        "tier": 13
    },

    # TIER 14: Crypto & Web3 (ML/AI focused roles only) - 10 companies
    "coinbase": {
        "name": "Coinbase",
        "url": "https://www.coinbase.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/coinbase/jobs",
        "type": "api",
        "tier": 14
    },
    "a16z_crypto": {
        "name": "a16z Crypto",
        "url": "https://a16zcrypto.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/a16zcrypto/jobs",
        "type": "api",
        "tier": 14
    },
    "chainalysis": {
        "name": "Chainalysis",
        "url": "https://www.chainalysis.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/chainalysis/jobs",
        "type": "api",
        "tier": 14
    },
    "alchemy": {
        "name": "Alchemy",
        "url": "https://www.alchemy.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/alchemy/jobs",
        "type": "api",
        "tier": 14
    },
    "fireblocks": {
        "name": "Fireblocks",
        "url": "https://www.fireblocks.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/fireblocks/jobs",
        "type": "api",
        "tier": 14
    },
    "anchorage": {
        "name": "Anchorage Digital",
        "url": "https://www.anchorage.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/anchorage/jobs",
        "type": "api",
        "tier": 14
    },
    "paradigm": {
        "name": "Paradigm",
        "url": "https://www.paradigm.xyz/opportunities",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/paradigm/jobs",
        "type": "api",
        "tier": 14
    },
    "consensys": {
        "name": "Consensys",
        "url": "https://consensys.io/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/consensys/jobs",
        "type": "api",
        "tier": 14
    },
    "circle": {
        "name": "Circle",
        "url": "https://www.circle.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/circle/jobs",
        "type": "api",
        "tier": 14
    },
    "dune": {
        "name": "Dune Analytics",
        "url": "https://dune.com/careers",
        "api_url": "https://boards-api.greenhouse.io/v1/boards/duneanalytics/jobs",
        "type": "api",
        "tier": 14
    },
}

# Location filters for US-only jobs
US_LOCATIONS = [
    # Major Tech Hubs
    "san francisco", "sf", "bay area", "silicon valley",
    "palo alto", "mountain view", "sunnyvale", "santa clara",
    "menlo park", "redwood city", "cupertino", "san jose",

    # California
    "los angeles", "la", "san diego", "irvine", "santa monica",
    "berkeley", "oakland", "san mateo",

    # Seattle/Pacific Northwest
    "seattle", "bellevue", "redmond", "portland",

    # New York/East Coast
    "new york", "nyc", "manhattan", "brooklyn",
    "boston", "cambridge", "somerville",
    "washington", "dc", "arlington", "virginia",

    # Other Major Cities
    "austin", "denver", "chicago", "atlanta",
    "miami", "philadelphia", "pittsburgh",

    # States
    "california", "ca", "washington", "wa",
    "new york", "ny", "massachusetts", "ma",
    "texas", "tx", "colorado", "co",

    # Remote
    "remote", "us remote", "usa remote", "anywhere",
    "work from home", "wfh", "distributed",

    # US Generic
    "united states", "usa", "us", "u.s."
]

# Locations to EXCLUDE (international)
EXCLUDED_LOCATIONS = [
    "london", "uk", "united kingdom", "england",
    "berlin", "germany", "munich", "hamburg",
    "paris", "france",
    "amsterdam", "netherlands",
    "toronto", "canada", "vancouver", "montreal",
    "sydney", "australia", "melbourne",
    "singapore",
    "tel aviv", "israel",
    "zurich", "switzerland",
    "dublin", "ireland",
    "barcelona", "spain", "madrid",
    "stockholm", "sweden",
    "copenhagen", "denmark",
    "oslo", "norway",
    "helsinki", "finland",
    "warsaw", "poland",
    "prague", "czech",
    "bangalore", "india", "mumbai", "delhi",
    "tokyo", "japan",
    "seoul", "korea",
    "beijing", "china", "shanghai",
    "hong kong",
    "emea", "apac", "europe", "asia"
]

def is_us_location(location: str) -> bool:
    """Check if location is US-based or remote."""
    if not location:
        return True  # Assume US if not specified

    location_lower = location.lower()

    # First check if it's explicitly excluded (international)
    for excluded in EXCLUDED_LOCATIONS:
        if excluded in location_lower:
            return False

    # Then check if it matches US locations or is remote
    for us_loc in US_LOCATIONS:
        if us_loc in location_lower:
            return True

    # If location specified but doesn't match US or excluded, be conservative
    # Check for generic US indicators
    if any(indicator in location_lower for indicator in ["usa", "u.s.", "united states"]):
        return True

    # If we can't determine, exclude to be safe
    return False

def get_sector_for_tier(tier: int) -> str:
    """Get sector name for a given tier."""
    sector_map = {
        1: "AI/ML",
        2: "AI/ML",
        3: "AI/ML",
        4: "AI/ML",
        5: "AI/ML",
        6: "AI/ML",
        7: "Financial Services",
        8: "Tech",
        9: "Gaming",
        10: "Healthcare/Biotech",
        11: "Defense/Aerospace",
        12: "E-commerce/Supply Chain",
        13: "EdTech",
        14: "Crypto/Web3"
    }
    return sector_map.get(tier, "Other")

def get_company_sector(company_key: str) -> str:
    """Get sector for a specific company."""
    company = AI_COMPANIES_100.get(company_key, {})
    tier = company.get("tier", 0)
    return get_sector_for_tier(tier)

def get_companies_by_tier(tier: int = None):
    """Get companies by tier (1-9)."""
    if tier:
        return {k: v for k, v in AI_COMPANIES_100.items() if v.get("tier") == tier}
    return AI_COMPANIES_100

def get_companies_by_sector(sector: str):
    """Get companies by sector (AI/ML, Financial Services, Tech, Gaming)."""
    return {k: v for k, v in AI_COMPANIES_100.items() if get_company_sector(k) == sector}

def get_api_companies():
    """Get companies that have public APIs."""
    return {k: v for k, v in AI_COMPANIES_100.items() if v.get("type") == "api"}

def get_greenhouse_companies():
    """Get companies using Greenhouse ATS."""
    return {k: v for k, v in AI_COMPANIES_100.items()
            if "greenhouse" in v.get("api_url", "")}

def get_lever_companies():
    """Get companies using Lever ATS."""
    return {k: v for k, v in AI_COMPANIES_100.items()
            if "lever" in v.get("api_url", "")}

def get_ashby_companies():
    """Get companies using Ashby ATS."""
    return {k: v for k, v in AI_COMPANIES_100.items()
            if v.get("type") == "ashby"}

def get_all_companies_count():
    """Get total count of companies."""
    return len(AI_COMPANIES_100)

def get_api_companies_count():
    """Get count of companies with APIs."""
    return len(get_api_companies())
