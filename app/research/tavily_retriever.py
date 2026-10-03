import os
import re

from tavily import TavilyClient

from .evidence import (
    EvidenceItem,
    EvidenceKind,
    EvidenceSource,
)


class TavilyRetriever:
    """Simple Tavily source and evidence retriever for Celestial Jyotish V5."""

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("TAVILY_API_KEY")

        if not self.api_key:
            raise RuntimeError(
                "TAVILY_API_KEY is not configured."
            )

        self.client = TavilyClient(api_key=self.api_key)

    def search(
        self,
        query: str,
        *,
        max_results: int = 5,
        include_raw_content: bool = False,
    ) -> list[dict[str, str]]:
        """Search the web and return source information."""

        response = self.client.search(
            query=query,
            search_depth="basic",
            max_results=max_results,
            include_raw_content=include_raw_content,
        )

        results: list[dict[str, str]] = []

        for result in response.get("results", []):
            results.append(
                {
                    "title": str(result.get("title", "")),
                    "url": str(result.get("url", "")),
                    "content": str(result.get("content", "")),
                    "raw_content": str(
                        result.get("raw_content", "")
                    ),
                }
            )

        return results

    def extract_relevant_passage(
        self,
        text: str,
        query: str,
        *,
        max_chars: int = 2500,
    ) -> str:
        """
        Extract a compact passage from source text that is relevant
        to the supplied search query.

        This is a deterministic text-selection step. It does not claim
        that the selected passage proves the research claim.
        """

        if not text.strip():
            return ""

        if len(text) <= max_chars:
            return text.strip()

        query_terms = self._query_terms(query)

        if not query_terms:
            return text[:max_chars].strip()

        sentences = self._split_into_sentences(text)

        if not sentences:
            return text[:max_chars].strip()

        scored_sentences: list[tuple[int, int, str]] = []

        for index, sentence in enumerate(sentences):
            normalized_sentence = sentence.lower()

            score = sum(
                1
                for term in query_terms
                if term in normalized_sentence
            )

            if score > 0:
                scored_sentences.append(
                    (score, index, sentence.strip())
                )

        if not scored_sentences:
            return text[:max_chars].strip()

        scored_sentences.sort(
            key=lambda item: (-item[0], item[1])
        )

        best_index = scored_sentences[0][1]

        selected: list[str] = []

        for index in range(
            max(0, best_index - 1),
            min(len(sentences), best_index + 2),
        ):
            sentence = sentences[index].strip()

            if sentence:
                selected.append(sentence)

        passage = " ".join(selected).strip()

        if len(passage) <= max_chars:
            return passage

        return passage[:max_chars].rsplit(" ", 1)[0].strip()

    def search_evidence(
        self,
        claim_id: str,
        query: str,
        *,
        source_id: str = "REPUTABLE_MODERN",
        max_results: int = 5,
        include_raw_content: bool = True,
        extract_passages: bool = True,
        passage_max_chars: int = 2500,
    ) -> list[EvidenceItem]:
        """
        Search for sources and convert the returned material into
        source-backed EvidenceItem records.

        When extract_passages is enabled, evidence_text contains a
        compact passage selected from the retrieved source material
        rather than the entire page or document.
        """

        results = self.search(
            query,
            max_results=max_results,
            include_raw_content=include_raw_content,
        )

        evidence_items: list[EvidenceItem] = []

        for index, result in enumerate(results, start=1):
            title = result["title"].strip()
            url = result["url"].strip()

            content = (
                result["raw_content"].strip()
                or result["content"].strip()
            )

            if not title or not url or not content:
                continue

            evidence_text = content

            if extract_passages:
                evidence_text = self.extract_relevant_passage(
                    content,
                    query,
                    max_chars=passage_max_chars,
                )

            source = EvidenceSource(
                source_id=source_id,
                title=title,
                source_type="web_source",
                reference=url,
                url=url,
            )

            evidence_items.append(
                EvidenceItem(
                    evidence_id=f"{claim_id}_TAVILY_{index:03d}",
                    claim_id=claim_id,
                    source=source,
                    evidence_kind=EvidenceKind.WEB_SOURCE,
                    evidence_text=evidence_text,
                    evidence_location="Relevant passage selected from retrieved source",
                    retrieval_method="Tavily Search",
                )
            )

        return evidence_items

    @staticmethod
    def _query_terms(query: str) -> tuple[str, ...]:
        """Return useful search terms from a query."""

        stop_words = {
            "the",
            "and",
            "for",
            "with",
            "from",
            "about",
            "this",
            "that",
            "first",
            "house",
            "vedic",
            "astrology",
        }

        words = re.findall(r"[a-zA-Z0-9]+", query.lower())

        terms = [
            word
            for word in words
            if len(word) >= 4 and word not in stop_words
        ]

        return tuple(dict.fromkeys(terms))

    @staticmethod
    def _split_into_sentences(text: str) -> list[str]:
        """Split retrieved source text into manageable sentences."""

        cleaned = re.sub(r"\s+", " ", text).strip()

        if not cleaned:
            return []

        return re.split(r"(?<=[.!?])\s+", cleaned)
