# Founder Weekly Operating Review Agent

Generate a founder-ready weekly operating review from startup metrics and company context.

<!-- FOUNDER_OS_STANDARD_README -->

## The founder problem

Weekly reviews become slow when metrics, risks, product issues, GTM movement, and team asks are assembled manually. Founders need one operating packet that shows what changed, what matters, and what decisions need attention.

## What this repo does

- reads weekly metrics and company context
- identifies changes, risks, priorities, and asks
- generates a CEO-ready weekly review memo
- creates an investor-safe narrative when needed

## What a founder gets in 10 minutes

- weekly operating review memo
- risk and priority list
- next-week execution plan
- investor-safe update language

## Before and after

Before:

- manual weekly reporting
- unclear decision points
- scattered metrics
- no reusable cadence

After:

- one weekly operating packet
- clear risks and priorities
- repeatable cadence
- founder-ready narrative

## Who this is for

- early-stage founders
- Founder's Office teams
- BizOps operators
- startup generalists
- board and investor reporting owners

## Quick start

- Run `python -m pip install -e .`.
- Run `PYTHONPATH=src python3 -m founder_weekly_review --metrics examples/weekly_metrics.csv --context examples/company_context.md --out outputs/demo`.
- Open `outputs/demo/weekly_operating_review.md` first.

## How to fork and use this for your company

1. Click Fork.
2. Rename the repo if needed.
3. Replace `examples/weekly_metrics.csv` with your weekly metrics.
4. Replace `examples/company_context.md` with company context.
5. Run the weekly review command.
6. Move decisions into Linear, Asana, ClickUp, Notion, or your internal ops tracker.

### Non-technical path

- Replace one CSV: `examples/weekly_metrics.csv`.
- Edit one context file: `examples/company_context.md`.
- Run one command.
- Read one output first: `outputs/demo/weekly_operating_review.md`.

## Input format

- weekly metrics CSV with growth, retention, activation, pipeline, runway, support, product, and operating notes where relevant
- company context describing stage, strategy, team, and constraints

The default sample data and examples are synthetic, anonymized, or template-only unless the repo explicitly documents a public source. Keep private customer, prospect, employee, investor, borrower, merchant, payment, or company data out of public forks.

## Output files

- `outputs/demo/weekly_operating_review.md`: founder weekly review memo generated from the CLI

## Example founder workflow

- Monday: update metrics.
- Tuesday: run the weekly review.
- Wednesday: review risks and owners.
- Thursday: close decisions.
- Friday: roll decisions into next week and investor-safe notes.

## Customization guide

Customize these before using the repo for a real company:

- metric columns
- risk thresholds
- company context
- review sections
- decision owners

## Where this fits in the Founder OS

Use this as the weekly cadence layer. It can absorb signals from `founder-os-revenue-engine`, `startup-metrics-playbook`, `founder-ai-workflow-roi-os`, and `board-pack-investor-update-agent`.

## Why this matters

This is not a dashboard. It is the weekly operating review that turns metrics into decisions and next actions.

## Roadmap

- Google Sheets import
- Notion export
- Slack decision alerts
- board pack handoff
- AI-assisted narrative review

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) if present. Practical improvements are welcome when they make the workflow easier to fork, run, or adapt.

## License

MIT License. See [LICENSE](LICENSE).

## Built by

Built by Shubham Singh, a founder-facing operator focused on RevOps, GTM systems, startup metrics, AI workflows, and operating systems for early-stage teams.

## Use this in your company

Fork it, replace the sample inputs with your company context, and run the workflow. Start with the main output listed in the Quick Start section. Keep private data out of public forks.

## If you are a Founder's Office candidate

Use this repo to understand how a founder-facing operator turns messy inputs into decisions, cadence, and execution artifacts. Fork it, adapt it to a real company example, and write a short case note explaining what changed.

---

## Detailed implementation notes

The founder-facing guide above is the fastest path. The original repo-specific notes are preserved below for deeper implementation context.

## Problem This Solves

Founders lose time turning scattered weekly metrics into a clear operating narrative. The problem is not knowing the numbers; it is deciding what changed, what is risky, what needs action, and what can be safely shared with investors.

## How It Helps

- Converts a weekly metrics CSV and company context into a CEO-ready operating review.
- Produces risks, priorities, team asks, an investor-safe update, and a next-week execution plan.
- Gives founders and founder's office operators a forkable cadence for weekly business reviews before they have a full BizOps, RevOps, or FP&A function.

## When To Fork This

- Fork this if your weekly review is still built manually from spreadsheets, Slack notes, and founder memory.
- Fork it when leadership needs one operating packet that connects growth, churn, activation, pipeline, runway, support load, and product issues.
- Replace the sample metrics, thresholds, and output format with your company's operating cadence.

## Use This In Your Company

This repo is designed to be forked into an internal company workflow. Fork it, replace the sample inputs with your company context, and keep only the parts that match your operating cadence. No permission request or sales call is needed before using it; the repo is the handoff. Check the license if you plan to redistribute your version.

- Use it as a weekly operating review generator for founders and Founder Office teams.
- Keep the output set: CEO review, investor-safe update, risks, team asks, next-week plan, and JSON analysis.
- Replace only the weekly metrics CSV and company context to start.

## Minimum Edits To Make It Yours

Change these first:

| Edit | Where | Why |
|---|---|---|
| Replace weekly metrics. | `examples/weekly_metrics.csv` | This is the core input for risks, priorities, wins, blockers, and follow-ups. |
| Rewrite company context. | `examples/company_context.md` | Makes the review read like your business, not a generic demo. |
| Tune risk and priority logic. | `src/founder_weekly_review/analysis.py` | Adjusts what the system escalates to the founder. |
| Review the generated operating review. | output Markdown/report | Keeps judgment with the founder or operator before sharing. |

You can leave the reporting format, CLI, and sample output structure alone on the first fork. Run it with your metrics once before changing the analysis code.

## What It Produces

```text
weekly_operating_review.md  CEO-ready weekly review
investor_safe_update.md   External-safe investor narrative
team_asks.md         Clear asks by function
next_week_plan.md      Focus areas and execution plan
analysis.json        Structured metric deltas, risks, and priorities
```

## AI leverage input

[Founder AI Workflow ROI OS](https://github.com/shubham1502-hue/founder-ai-workflow-roi-os) can feed the weekly operating review with automation priorities, AI pilots, owner assignments, risk flags, and estimated savings.

## Quickstart

```bash
git clone https://github.com/shubham1502-hue/founder-weekly-operating-review-agent.git
cd founder-weekly-operating-review-agent

python3 -m founder_weekly_review \
 --metrics examples/weekly_metrics.csv \
 --context examples/company_context.md \
 --out outputs/demo
```

Then open:

- `outputs/demo/weekly_operating_review.md`
- `outputs/demo/investor_safe_update.md`
- `outputs/demo/team_asks.md`
- `outputs/demo/next_week_plan.md`
- `outputs/demo/analysis.json`

## Demo Output Preview

See [docs/sample_weekly_operating_review.md](docs/sample_weekly_operating_review.md) for a generated example.

## Project Structure

```text
founder-weekly-operating-review-agent/
|-- examples/
|  |-- company_context.md
|  `-- weekly_metrics.csv
|-- src/founder_weekly_review/
|  |-- analysis.py
|  |-- cli.py
|  |-- metrics.py
|  `-- reporting.py
|-- tests/
|  `-- test_analysis.py
`-- README.md
```

## Metrics Expected

The sample CSV includes:

- MRR, new MRR, expansion MRR, churn MRR
- Active customers, new customers, churned customers
- Activation rate
- Pipeline value
- Cash balance, burn, runway
- Open support tickets
- NPS
- Open product issues

## Why This Matters

This repo is built for the founder's office job to be done: absorb messy operating signal, identify what deserves leadership attention, and convert it into a weekly cadence that makes decisions faster.

## License

MIT
