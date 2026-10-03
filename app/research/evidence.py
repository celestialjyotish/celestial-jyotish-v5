from dataclasses import dataclass
from enum import StrEnum


class EvidenceKind(StrEnum):
    """Type of evidence retrieved for an astrology research claim."""

    PRIMARY_TEXT = "primary_text"
    BOOK = "book"
    SCHOLAR = "scholar"
    JOURNAL = "journal"
    MODERN_REFERENCE = "modern_reference"
    WEB_SOURCE = "web_source"


@dataclass(frozen=True)
class EvidenceSource:
    """
    Identifies the external source from which evidence was retrieved.

    This object records source identity and location only. It does not
    decide whether the evidence verifies a claim.
    """

    source_id: str
    title: str
    source_type: str
    reference: str
    url: str = ""
    author: str = ""
    publisher: str = ""
    publication_year: str = ""


@dataclass(frozen=True)
class EvidenceItem:
    """
    A specific piece of retrieved evidence supporting or challenging a claim.

    Evidence must contain identifiable source information and a precise
    evidence location whenever the source provides one.
    """

    evidence_id: str
    claim_id: str
    source: EvidenceSource
    evidence_kind: EvidenceKind
    evidence_text: str
    evidence_location: str = ""
    retrieval_method: str = ""
    retrieved_at: str = ""
    notes: str = ""


@dataclass(frozen=True)
class EvidenceRetrievalRequest:
    """
    Request for evidence supporting a specific astrology research claim.

    The retrieval layer should search for actual source evidence rather than
    asking a language model to invent or reconstruct citations.
    """

    claim_id: str
    claim_text: str
    preferred_source_ids: tuple[str, ...] = ()
    required_source_types: tuple[str, ...] = ()
    search_terms: tuple[str, ...] = ()
    max_results: int = 5


@dataclass(frozen=True)
class EvidenceRetrievalResult:
    """
    Result returned by the evidence-retrieval layer.

    Retrieved evidence is kept separate from verification. A downstream
    verification function decides whether the evidence is sufficient.
    """

    claim_id: str
    items: tuple[EvidenceItem, ...]
    retrieval_notes: tuple[str, ...] = ()
    retrieval_successful: bool = False


def validate_evidence_item(item: EvidenceItem) -> tuple[str, ...]:
    """
    Perform deterministic completeness checks on one evidence item.

    This function does not determine whether the evidence proves the claim.
    It only checks whether the evidence record contains the minimum
    information required for downstream evaluation.
    """

    errors: list[str] = []

    if not item.evidence_id.strip():
        errors.append("Evidence ID is required.")

    if not item.claim_id.strip():
        errors.append("Claim ID is required.")

    if not item.source.source_id.strip():
        errors.append("Source ID is required.")

    if not item.source.title.strip():
        errors.append("Source title is required.")

    if not item.source.reference.strip():
        errors.append("Source reference is required.")

    if not item.evidence_text.strip():
        errors.append("Evidence text is required.")

    return tuple(errors)


def validate_retrieval_request(
    request: EvidenceRetrievalRequest,
) -> tuple[str, ...]:
    """
    Perform deterministic validation on an evidence retrieval request.
    """

    errors: list[str] = []

    if not request.claim_id.strip():
        errors.append("Claim ID is required.")

    if not request.claim_text.strip():
        errors.append("Claim text is required.")

    if request.max_results < 1:
        errors.append("max_results must be at least 1.")

    return tuple(errors)


def build_retrieval_result(
    claim_id: str,
    items: tuple[EvidenceItem, ...],
    *,
    retrieval_notes: tuple[str, ...] = (),
) -> EvidenceRetrievalResult:
    """
    Construct a retrieval result after validating the supplied evidence.

    Invalid evidence records are rejected rather than silently passed
    downstream.
    """

    if not claim_id.strip():
        raise ValueError("claim_id is required.")

    validation_errors: list[str] = []

    for item in items:
        validation_errors.extend(validate_evidence_item(item))

    if validation_errors:
        raise ValueError(
            "Invalid evidence records: "
            + " | ".join(validation_errors)
        )

    return EvidenceRetrievalResult(
        claim_id=claim_id,
        items=items,
        retrieval_notes=retrieval_notes,
        retrieval_successful=bool(items),
    )
