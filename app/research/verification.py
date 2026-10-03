from dataclasses import dataclass

from schemas.astrology import (
    AstrologyClaim,
    SourceType,
    VerificationStatus,
)

from .source_registry import SourcePriority, get_source


@dataclass(frozen=True)
class EvidenceRecord:
    """Evidence retrieved from an identifiable research source."""

    source_id: str
    source_reference: str
    evidence_text: str
    evidence_location: str = ""


@dataclass(frozen=True)
class VerificationResult:
    """Deterministic result of evaluating evidence for an astrology claim."""

    claim_id: str
    status: VerificationStatus
    confidence: float
    source_id: str | None
    reason: str


def verify_claim(
    claim: AstrologyClaim,
    evidence: EvidenceRecord | None = None,
) -> VerificationResult:
    """
    Evaluate whether a claim has sufficient source evidence.

    This function does not perform web or book retrieval itself.
    It only evaluates evidence that has actually been supplied to it.

    A model-generated claim without evidence is never treated as verified.
    """

    if evidence is None:
        return VerificationResult(
            claim_id=claim.claim_id,
            status=VerificationStatus.UNVERIFIED,
            confidence=0.0,
            source_id=None,
            reason=(
                "No source evidence was supplied. "
                "The claim must not be treated as verified."
            ),
        )

    source = get_source(evidence.source_id)

    if source is None:
        return VerificationResult(
            claim_id=claim.claim_id,
            status=VerificationStatus.BLOCKED,
            confidence=0.0,
            source_id=evidence.source_id,
            reason=(
                "The supplied source is not registered in the "
                "Celestial Jyotish source registry."
            ),
        )

    if not evidence.source_reference.strip():
        return VerificationResult(
            claim_id=claim.claim_id,
            status=VerificationStatus.BLOCKED,
            confidence=0.0,
            source_id=source.source_id,
            reason=(
                "The source was identified, but no source reference "
                "was supplied."
            ),
        )

    if not evidence.evidence_text.strip():
        return VerificationResult(
            claim_id=claim.claim_id,
            status=VerificationStatus.BLOCKED,
            confidence=0.0,
            source_id=source.source_id,
            reason=(
                "The source was identified, but no supporting evidence "
                "text was supplied."
            ),
        )

    if source.source_type == SourceType.MODEL_INFERENCE:
        return VerificationResult(
            claim_id=claim.claim_id,
            status=VerificationStatus.BLOCKED,
            confidence=0.0,
            source_id=source.source_id,
            reason=(
                "Model inference cannot independently verify an "
                "astrology claim."
            ),
        )

    confidence = _confidence_for_source(source.priority)

    return VerificationResult(
        claim_id=claim.claim_id,
        status=VerificationStatus.VERIFIED,
        confidence=confidence,
        source_id=source.source_id,
        reason=(
            f"Supporting evidence was supplied from the registered "
            f"source '{source.title}'."
        ),
    )


def _confidence_for_source(priority: SourcePriority) -> float:
    """Return the maximum evidence confidence allowed by source tier."""

    confidence_by_priority = {
        SourcePriority.PRIMARY_CLASSICAL: 0.95,
        SourcePriority.AUTHORITATIVE_BOOK: 0.90,
        SourcePriority.SCHOLAR: 0.80,
        SourcePriority.JOURNAL: 0.75,
        SourcePriority.REPUTABLE_MODERN: 0.65,
        SourcePriority.MODEL_INFERENCE: 0.0,
    }

    return confidence_by_priority[priority]