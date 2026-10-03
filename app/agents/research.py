from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from app.research.tavily_retriever import TavilyRetriever
from schemas.fact_pack import FactPack


MODEL_NAME = "gemini-3.5-flash-lite"


RESEARCH_SYSTEM_PROMPT = """
You are the Research Agent for the Celestial Jyotish V5 pipeline.

Your job is to transform a research topic together with retrieved source
material into a structured FactPack for downstream story and script
generation.

SOURCE DISCIPLINE:

1. Retrieved web material is source material, not automatic proof.

2. Always identify a source by its actual title and URL supplied in the
   research material.

3. Never assume that a web page is BPHS, Phaladeepika, Saravali, or another
   classical text merely because the search query mentions that text.

4. Never invent a source, URL, quotation, book reference, scholar,
   citation, or evidence.

5. Never claim that you personally verified a classical text unless the
   supplied source material actually contains identifiable evidence from
   that text.

CLAIM HANDLING:

6. verified_claims MUST contain the actual factual claim as a concise,
   human-readable sentence. Do NOT put claim IDs in this field.

7. A claim may be placed in verified_claims only when the supplied evidence
   directly supports the statement.

8. uncertain_claims MUST contain the actual claim or proposition that has
   insufficient supporting evidence. Do NOT put claim IDs there.

9. disputed_claims MUST contain the actual claim or proposition when
   supplied sources materially disagree.

10. blocked_claims MUST contain the actual claim or proposition that should
    not be used because the available evidence does not adequately support
    it.

11. Do not upgrade a modern website's interpretation into a classical rule
    merely because the website mentions a classical text.

12. Do not use the model's prior knowledge to fill evidence gaps.

13. Preserve important technical Jyotish terminology.

14. Distinguish source-derived information from interpretation or inference.

RESEARCH NOTES:

15. research_notes must explain important source limitations,
    terminology, disagreements, and research dependencies.

16. research_notes must preserve the actual title and URL for every source
    used.

17. If a source appears to reproduce or summarize a classical text rather
    than being the classical text itself, make that distinction clear.

OUTPUT:

18. Do not write the final YouTube script.

19. The FactPack is a research handoff for downstream agents.

20. The final response must conform exactly to the FactPack structure.

Most important rule:

The FactPack claim lists contain REAL CLAIM SENTENCES, not labels,
identifiers, or internal IDs.
"""


def create_research_agent() -> Agent:
    """Create the structured Celestial Jyotish V5 research agent."""

    provider = GoogleProvider()

    model = GoogleModel(
        MODEL_NAME,
        provider=provider,
    )

    return Agent(
        model=model,
        output_type=FactPack,
        system_prompt=RESEARCH_SYSTEM_PROMPT,
    )


research_agent = create_research_agent()


def _format_evidence_for_agent(
    evidence_items: list,
) -> str:
    """Format retrieved source evidence for the research agent."""

    if not evidence_items:
        return (
            "NO SOURCE EVIDENCE WAS RETRIEVED.\n"
            "Do not treat model knowledge as verified evidence."
        )

    sections: list[str] = []

    for index, item in enumerate(evidence_items, start=1):
        sections.append(
            "\n".join(
                [
                    f"SOURCE {index}",
                    f"Title: {item.source.title}",
                    f"URL: {item.source.url}",
                    "Source type: Retrieved web source",
                    f"Evidence passage: {item.evidence_text}",
                ]
            )
        )

    return "\n\n".join(sections)


async def research_topic(
    topic: str,
    *,
    search_query: str | None = None,
    max_sources: int = 5,
) -> FactPack:
    """
    Retrieve source material for a topic and produce a source-grounded
    FactPack.

    The retrieval step happens before the Research Agent is called.
    """

    query = search_query or topic

    retriever = TavilyRetriever()

    evidence_items = retriever.search_evidence(
        claim_id="RESEARCH_TOPIC",
        query=query,
        max_results=max_sources,
        include_raw_content=True,
        extract_passages=True,
        passage_max_chars=2500,
        source_id="WEB_SOURCE",
    )

    evidence_text = _format_evidence_for_agent(
        evidence_items
    )

    research_prompt = f"""
Research topic:

{topic}

Search query used:

{query}

Retrieved source material:

{evidence_text}

Use only the supplied source material as external evidence.

Create a FactPack for downstream story development.

CRITICAL OUTPUT REQUIREMENT:

Every entry in verified_claims, disputed_claims, uncertain_claims, and
blocked_claims must be an actual human-readable claim or proposition.

For example:

GOOD:
"The first house is associated with the body, personality, and overall
orientation of the native."

BAD:
"claim_lagna_significations"

Do not create internal claim IDs.

For every source used in research_notes, preserve its exact title and URL.

If the retrieved evidence is insufficient to support a classical rule,
say so rather than filling the gap from prior model knowledge.
"""

    result = await research_agent.run(research_prompt)

    return result.output
