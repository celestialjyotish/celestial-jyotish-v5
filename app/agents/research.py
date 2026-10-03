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

IMPORTANT SOURCE DISCIPLINE:

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

6. A claim may be placed in verified_claims only when the supplied evidence
   directly supports the claim and the source identity is clear.

7. If the evidence is relevant but insufficient, place the claim in
   uncertain_claims.

8. If supplied sources materially disagree, place the affected claim in
   disputed_claims and explain the disagreement in research_notes.

9. If the available evidence does not adequately support a claim, place it
   in blocked_claims rather than inventing support.

10. Do not upgrade a modern website's interpretation into a classical rule
    merely because the website mentions a classical text.

11. Preserve important technical Jyotish terminology.

12. Distinguish source-derived information from interpretation or inference.

13. research_notes must preserve the actual source title and URL for every
    source used.

14. Do not write the final YouTube script.

15. Do not manufacture certainty from the model's prior knowledge.

The final response must conform exactly to the FactPack structure.
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

Do not infer that a source is classical merely because its title, URL,
or passage mentions a classical text.

Prepare a FactPack that clearly separates:
- supported claims
- disputed claims
- uncertain claims
- blocked claims
- important research notes

For each source used in research_notes, preserve its exact title and URL.
"""

    result = await research_agent.run(research_prompt)

    return result.output
