from pydantic import BaseModel, Field

from astrology import AstrologyClaim


class FactPack(BaseModel):
    """
    Verified research package for one Celestial Jyotish topic.

    A FactPack is the controlled handoff between research
    and the story/script stages.
    """

    topic: str = Field(
        ...,
        description="The astrology topic being researched."
    )

    topic_id: str = Field(
        ...,
        description="Stable identifier for the topic."
    )

    claims: list[AstrologyClaim] = Field(
        default_factory=list,
        description="Astrological claims collected during research."
    )

    verified_claims: list[str] = Field(
        default_factory=list,
        description="claim_id values that have passed verification."
    )

    disputed_claims: list[str] = Field(
        default_factory=list,
        description="claim_id values with meaningful source disagreement."
    )

    uncertain_claims: list[str] = Field(
        default_factory=list,
        description="claim_id values requiring additional research."
    )

    blocked_claims: list[str] = Field(
        default_factory=list,
        description="claim_id values that must not enter the script."
    )

    research_notes: list[str] = Field(
        default_factory=list,
        description="Important research observations and limitations."
    )
