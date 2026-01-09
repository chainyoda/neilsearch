"""Top 100 AI/ML companies and their career pages - US & Remote only."""

AI_COMPANIES_100 = {
    # TIER 1: Leading AI Labs & Research (10 companies)
    "openai": {
        "name": "OpenAI",
        "url": "https://openai.com/careers",
        "api_url": "https://api.lever.co/v0/postings/openai",
        "type": "api",
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
        "api_url": "https://api.lever.co/v0/postings/cohere",
        "type": "api",
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
        "api_url": "https://api.lever.co/v0/postings/inflection-ai",
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
        "api_url": "https://boards-api.greenhouse.io/v1/boards/glean/jobs",
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

def get_companies_by_tier(tier: int = None):
    """Get companies by tier (1-6)."""
    if tier:
        return {k: v for k, v in AI_COMPANIES_100.items() if v.get("tier") == tier}
    return AI_COMPANIES_100

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

def get_all_companies_count():
    """Get total count of companies."""
    return len(AI_COMPANIES_100)

def get_api_companies_count():
    """Get count of companies with APIs."""
    return len(get_api_companies())
