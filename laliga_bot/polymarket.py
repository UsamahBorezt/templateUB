from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EdgeDecision:
    side: str
    model_prob: float
    market_prob: float
    edge: float
    take: bool


def implied_prob_from_price(price: float) -> float:
    if price < 0 or price > 1:
        raise ValueError("Price harus di antara 0.0 dan 1.0")
    return float(price)


def build_edge_decision(side: str, model_prob: float, market_prob: float, min_edge: float = 0.05) -> EdgeDecision:
    if not 0 <= model_prob <= 1:
        raise ValueError("model_prob harus di antara 0.0 dan 1.0")
    if not 0 <= market_prob <= 1:
        raise ValueError("market_prob harus di antara 0.0 dan 1.0")

    edge = model_prob - market_prob
    return EdgeDecision(
        side=side,
        model_prob=model_prob,
        market_prob=market_prob,
        edge=edge,
        take=edge >= min_edge,
    )
