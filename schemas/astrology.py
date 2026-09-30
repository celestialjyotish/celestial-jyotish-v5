from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ClaimType(str, Enum):
    CLASSICAL_RULE = "classical_rule"
    INTERPRETATION = "interpretation"
    MODERN_CONTEXT = "modern_context"
    INFERENCE = "inference"


class VerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    DISPUTED = "disputed"
    UNCERTAIN = "uncertain"
    BLOCKED = "blocked"


class SourceType(str, Enum):
    CLASSICAL_TEXT = "classical_text"
    BOOK = "book"
    SCHOLAR = "scholar"
    JOURNAL = "journal"
    REPUTABLE_MODERN_SOURCE = "reputable_modern_source"
    MODEL_INFERENCE = "model_inference"


class AstrologyClaim(BaseModel):
    """
    A single astrological claim used by the Celestial Jyotish V5 pipeline.

    The model deliberately separates:
    - what the claim says,
    - what kind of claim it is,
    - where it came from,
    - and whether it has been verified.
    """

    claim_id: str = Field(
        ...,
        description="Stable identifier for this claim."
    )

    claim_text: str = Field(
        ...,
        description="The exact substantive astrological claim."
    )

    claim_type: ClaimType = Field(
        ...,
        description="Whether this is a classical rule, interpretation, modern context, or inference."
    )

    category: str = Field(
        ...,
        description="Broad Jyotish category, such as planet, house, sign, nakshatra, yoga, or divisional chart."
    )

    technical_terms: list[str] = Field(
        default_factory=list,
        description="Relevant technical Jyotish terminology."
    )

    source_title: Optional[str] = Field(
        default=None,
        description="Title of the source supporting the claim."
    )

    source_type: Optional[SourceType] = Field(
        default=None,
        description="Type of source supporting the claim."
    )

    source_reference: Optional[str] = Field(
        default=None,
        description="Specific citation, page, chapter, verse, or other traceable reference."
    )

    verification_status: VerificationStatus = Field(
        default=VerificationStatus.UNVERIFIED,
        description="Current verification state of the claim."
    )

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence in the claim after evaluation."
    )

    interpretation_notes: Optional[str] = Field(
        default=None,
        description="Context explaining how an interpretation differs from the source rule."
    )

    uncertainty_notes: Optional[str] = Field(
        default=None,
        description="Known ambiguity, disagreement, or limitation."
    )
