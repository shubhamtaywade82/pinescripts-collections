# Strategy Specification: Supertrend2 Automation Bot (v6)

## 1. Executive Summary
The **Supertrend2 Automation Bot** is a high-probability scalping system designed to capture 1% price movements in the direction of the dominant macro trend. It utilizes a "Bottleneck Filtration" approach, where trades are only executed when four independent market dimensions (Macro Trend, Volume Conviction, Trend Strength, and Timing) align.

### Core Objective
To automate the capture of high-conviction scalps while avoiding the "bag-holding" risks associated with All-Time High (ATH) entries and low-volume market chop.

---

## 2. The Four "Automation Gates" (Entry Edge)

### Gate 1: The HTF Trend (Macro Alignment)
*   **Logic**: The bot pulls the Supertrend direction from a Higher Timeframe (Default: 4H).
*   **Edge**: Eliminates counter-trend "trap" signals. If the 4H trend is bearish, the bot is restricted to Short trades only, regardless of local 15m signals.
*   **Optimization Parameter**: `higherTF`. Use "1D" for extreme safety or "1H" for higher frequency.

### Gate 2: Relative Volume (RVOL)
*   **Logic**: Signals are only valid if current bar volume > SMA(Volume, 20) * Multiplier.
*   **Edge**: Confirms institutional "Smart Money" participation. Avoids "ghost flips" during low-liquidity sessions (e.g., weekend or late NY).
*   **Optimization Parameter**: `volMultiplier`. Range: 1.0 (Loose) to 2.0 (Strict).

### Gate 3: ADX Strength (Trend Intensity)
*   **Logic**: Signals are only valid if ADX > Threshold (Default: 20).
*   **Edge**: Filters out "weak" trend flips. A Supertrend flip is much more likely to hit +1% if there is already trending momentum in the market. This prevents the bot from entering during "flat" sideways ranges.
*   **Optimization Parameter**: `adxThreshold`. Range: 15 (Aggressive) to 30 (Conservative).

### Gate 4: Structural Exclusivity
*   **Logic**: Only allows new entries when the strategy is "Flat" (`position_size == 0`).
*   **Edge**: Prevents "flip-flopping" exits. Once in a trade, the bot ignores all other signals until the target is hit or the safety valve triggers.

---

## 3. Exit Mechanics & Safety Valves

### Primary Exit: The 1% Scalp
*   **Limit Order**: Places a passive limit order at entry + 1%.
*   **Trailing Option**: If `useTrailing` is enabled, the 1% target becomes an activation trigger. The bot then follows the price with a `trailPercent` offset to catch "Moon-shot" trends.

### Safety Valve A: The Time-Based Exit
*   **Logic**: If a trade is stuck for `maxDays`, the bot admits defeat.
*   **Edge**: Protects capital from being locked in a dead trade for months.

### Safety Valve B: The Breakeven Recovery
*   **Logic**: If the Time-Based exit is triggered but `useBreakeven` is enabled, the bot waits for the price to return to entry before closing.
*   **Edge**: Minimizes realized losses on trades that eventually recover to entry but failed to hit the +1% target.

---

## 4. Parameter Optimization Guide (The Search Space)

To find the best "Edge" for specific assets (BTC, ETH, Forex), use the TradingView Strategy Optimizer with these ranges:

| Parameter | Type | Search Range | Purpose |
| :--- | :--- | :--- | :--- |
| **Factor** | Float | 2.0 - 5.0 | Sensitivity of the Supertrend signal. |
| **ATR Length** | Int | 10 - 20 | Smoothing of the Supertrend volatility. |
| **tpPercent** | Float | 0.5% - 2.5% | The "Sweet Spot" for your asset's daily range. |
| **volMultiplier**| Float | 1.0 - 1.5 | Filter strictness for market conviction. |
| **adxThreshold** | Int | 15 - 30 | Minimum trend strength required to enter. |
| **maxDays** | Int | 7 - 45 | Your "Patience Limit" for capital lockup. |

---

## 5. Automation & Execution
*   **Webhook Protocol**: JSON-formatted payloads.
*   **Real-time Calculation**: `calc_on_every_tick=true` ensures the dashboard and alerts are responsive to intra-bar price action.
*   **Dashboard**: Displays real-time Net Profit, Win Rate, and Max Drawdown to monitor the bot's health at a glance.

---

## 6. Dynamic Adjustment Strategy (Market Regimes)

*   **Bull Market**: Increase `tpPercent` to 1.5% and enable `useTrailing`. Set `adxThreshold` to 25.
*   **Bear Market**: Reduce `tpPercent` to 0.8% and use a shorter `higherTF` (e.g., 1H) for faster trend reaction.
*   **Ranging/Sideways**: Increase `adxThreshold` to 30 and `volMultiplier` to 1.5 to avoid getting chopped in the range middle.
